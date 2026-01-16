param(
    [Parameter(Mandatory = $true)]
    [string]$QuartoFile,

    [string[]]$WatchExtras = @(),

    [string]$ScreenshotDir,

    [string]$BrowserPath,

    [string]$QuartoExe = 'quarto',

    [int]$CooldownMs = 3000,

    [ValidateSet('png', 'pdf', 'both')]
    [string]$CaptureMode = 'png',

    [int]$ViewportWidth = 1400,

    [int]$ViewportHeight = 6000,

    [switch]$RenderOnStart
)

$ErrorActionPreference = 'Stop'

$resolvedQuarto = (Resolve-Path -LiteralPath $QuartoFile -ErrorAction Stop).ProviderPath
$quartoFileInfo = Get-Item -LiteralPath $resolvedQuarto
if ($quartoFileInfo.PSIsContainer) {
    throw "QuartoFile must point to a file, not a directory: $resolvedQuarto"
}

$baseScreenshotDir = $null
if ($ScreenshotDir) {
    $resolvedBase = Resolve-Path -LiteralPath $ScreenshotDir -ErrorAction SilentlyContinue
    if ($resolvedBase) {
        $baseScreenshotDir = $resolvedBase.ProviderPath
    } else {
        $base = New-Item -ItemType Directory -Path $ScreenshotDir -Force
        $baseScreenshotDir = $base.FullName
    }
} else {
    $baseScreenshotDir = Join-Path $quartoFileInfo.Directory.FullName 'quarto_shots'
    if (-not (Test-Path -LiteralPath $baseScreenshotDir)) {
        New-Item -ItemType Directory -Path $baseScreenshotDir | Out-Null
    }
}

$subDirName = [System.IO.Path]::GetFileNameWithoutExtension($quartoFileInfo.Name)
$ScreenshotDir = Join-Path $baseScreenshotDir $subDirName
if (-not (Test-Path -LiteralPath $ScreenshotDir)) {
    New-Item -ItemType Directory -Path $ScreenshotDir | Out-Null
}

if (-not $BrowserPath) {
    $candidates = @(
        (Join-Path $env:ProgramFiles 'Microsoft\Edge\Application\msedge.exe'),
        (Join-Path $env:ProgramFiles 'Google\Chrome\Application\chrome.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'Microsoft\Edge\Application\msedge.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe')
    )

    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) {
            $BrowserPath = $candidate
            break
        }
    }

    if (-not $BrowserPath) {
        $cmd = Get-Command -Name msedge -ErrorAction SilentlyContinue
        if ($cmd) {
            $BrowserPath = $cmd.Source
        }
    }

    if (-not $BrowserPath) {
        $cmd = Get-Command -Name chrome -ErrorAction SilentlyContinue
        if ($cmd) {
            $BrowserPath = $cmd.Source
        }
    }
}

if (-not $BrowserPath -or -not (Test-Path -LiteralPath $BrowserPath)) {
    throw 'Unable to locate a headless-capable browser (Edge or Chrome). Specify -BrowserPath explicitly.'
}

function New-Watcher {
    param(
        [Parameter(Mandatory = $true)] [string]$Path,
        [Parameter(Mandatory = $true)] [string]$Filter,
        [bool]$IncludeSubdirectories = $false
    )

    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = $Path
    $watcher.Filter = $Filter
    $watcher.IncludeSubdirectories = $IncludeSubdirectories
    $watcher.NotifyFilter = [System.IO.NotifyFilters]'FileName, LastWrite, CreationTime, Size'
    $watcher.EnableRaisingEvents = $true
    return $watcher
}

$watchers = @()
$mainWatcher = New-Watcher -Path $quartoFileInfo.Directory.FullName -Filter $quartoFileInfo.Name
$watchers += $mainWatcher

foreach ($extra in $WatchExtras) {
    $resolvedExtras = Resolve-Path -LiteralPath $extra -ErrorAction Stop
    foreach ($pathInfo in $resolvedExtras) {
        $providerPath = $pathInfo.ProviderPath
        $item = Get-Item -LiteralPath $providerPath
        if ($item.PSIsContainer) {
            $watchers += New-Watcher -Path $item.FullName -Filter '*.*' -IncludeSubdirectories $true
        } else {
            $watchers += New-Watcher -Path $item.Directory.FullName -Filter $item.Name
        }
    }
}

$htmlOutput = [System.IO.Path]::ChangeExtension($quartoFileInfo.FullName, '.html')

function Invoke-Render {
    param(
        [string]$QuartoExe,
        [string]$QuartoPath
    )

    Write-Host "[$(Get-Date -Format T)] Rendering $QuartoPath"
    $renderResult = & $QuartoExe render $QuartoPath --quiet 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Quarto render failed with exit code $LASTEXITCODE"
        if ($renderResult) {
            Write-Warning $renderResult
        }
        return $false
    }
    return $true
}

function Invoke-Screenshot {
    param(
        [string]$Browser,
        [string]$HtmlPath,
        [string]$ScreenshotDir,
        [int]$Width,
        [int]$Height
    )

    if (-not (Test-Path -LiteralPath $HtmlPath)) {
        Write-Warning "Rendered HTML not found: $HtmlPath"
        return $null
    }

    $timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $shotPath = Join-Path $ScreenshotDir "preview_$timestamp.png"
    $uri = (New-Object System.Uri $HtmlPath).AbsoluteUri

    $args = @('--headless=new', '--disable-gpu', "--window-size=$Width,$Height", "--screenshot=$shotPath", $uri)
    & $Browser $args | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Browser screenshot command failed with exit code $LASTEXITCODE"
        return $null
    }

    Write-Host "[$(Get-Date -Format T)] Saved screenshot to $shotPath"
    return $shotPath
}

function Invoke-Pdf {
    param(
        [string]$Browser,
        [string]$HtmlPath,
        [string]$ScreenshotDir
    )

    if (-not (Test-Path -LiteralPath $HtmlPath)) {
        Write-Warning "Rendered HTML not found: $HtmlPath"
        return $null
    }

    $timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $pdfPath = Join-Path $ScreenshotDir "preview_$timestamp.pdf"
    $uri = (New-Object System.Uri $HtmlPath).AbsoluteUri

    $args = @('--headless=new', '--disable-gpu', "--print-to-pdf=$pdfPath", $uri)
    & $Browser $args | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Browser PDF export failed with exit code $LASTEXITCODE"
        return $null
    }

    Write-Host "[$(Get-Date -Format T)] Saved PDF to $pdfPath"
    return $pdfPath
}

$script:lastRun = [DateTime]::MinValue
$script:cooldown = [TimeSpan]::FromMilliseconds($CooldownMs)

$action = {
    param($Sender, $EventArgs)
    $now = Get-Date
    if ($now - $script:lastRun -lt $script:cooldown) {
        return
    }
    $script:lastRun = $now

    Write-Host "[$($now.ToString('T'))] Change detected: $($EventArgs.FullPath)"
    if (Invoke-Render -QuartoExe $using:QuartoExe -QuartoPath $using:resolvedQuarto) {
        Start-Sleep -Milliseconds 500

        switch ($using:CaptureMode) {
            'png' {
                Invoke-Screenshot -Browser $using:BrowserPath -HtmlPath $using:htmlOutput -ScreenshotDir $using:ScreenshotDir -Width $using:ViewportWidth -Height $using:ViewportHeight | Out-Null
            }
            'pdf' {
                Invoke-Pdf -Browser $using:BrowserPath -HtmlPath $using:htmlOutput -ScreenshotDir $using:ScreenshotDir | Out-Null
            }
            'both' {
                Invoke-Screenshot -Browser $using:BrowserPath -HtmlPath $using:htmlOutput -ScreenshotDir $using:ScreenshotDir -Width $using:ViewportWidth -Height $using:ViewportHeight | Out-Null
                Invoke-Pdf -Browser $using:BrowserPath -HtmlPath $using:htmlOutput -ScreenshotDir $using:ScreenshotDir | Out-Null
            }
        }
    }
}

$registrations = @()
foreach ($watcher in $watchers) {
    $registrations += Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action
    $registrations += Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action
    $registrations += Register-ObjectEvent -InputObject $watcher -EventName Renamed -Action $action
}

Write-Host "Watching for changes. Press Enter to stop."

if ($RenderOnStart) {
    if (Invoke-Render -QuartoExe $QuartoExe -QuartoPath $resolvedQuarto) {
        Start-Sleep -Milliseconds 500
        switch ($CaptureMode) {
            'png' {
                Invoke-Screenshot -Browser $BrowserPath -HtmlPath $htmlOutput -ScreenshotDir $ScreenshotDir -Width $ViewportWidth -Height $ViewportHeight | Out-Null
            }
            'pdf' {
                Invoke-Pdf -Browser $BrowserPath -HtmlPath $htmlOutput -ScreenshotDir $ScreenshotDir | Out-Null
            }
            'both' {
                Invoke-Screenshot -Browser $BrowserPath -HtmlPath $htmlOutput -ScreenshotDir $ScreenshotDir -Width $ViewportWidth -Height $ViewportHeight | Out-Null
                Invoke-Pdf -Browser $BrowserPath -HtmlPath $htmlOutput -ScreenshotDir $ScreenshotDir | Out-Null
            }
        }
    }
}

[Console]::ReadLine() | Out-Null

foreach ($registration in $registrations) {
    Unregister-Event -SubscriptionId $registration.Id -ErrorAction SilentlyContinue
}
foreach ($watcher in $watchers) {
    $watcher.Dispose()
}

Write-Host 'Stopped.'
