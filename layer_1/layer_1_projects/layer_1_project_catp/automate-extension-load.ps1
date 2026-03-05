# resource_id: "4024e8b4-3bee-44ba-8429-27a103e1dd42"
# resource_type: "document"
# resource_name: "automate-extension-load"
# PowerShell script to load the Chrome extension
# Run this in PowerShell as Administrator

$extensionPath = "\\wsl.localhost\Ubuntu-24.04\home\dawson\code\catp\task-timer-frontend"
$canvasUrl = "https://byui.instructure.com/courses/285534/assignments"

Write-Host "🚀 Loading Canvas Assignment Timer Extension..." -ForegroundColor Cyan
Write-Host ""

# Close existing Chrome instances
Write-Host "📋 Step 1: Closing Chrome instances..." -ForegroundColor Yellow
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2

# Launch Chrome with extension and remote debugging
Write-Host "🌐 Step 2: Launching Chrome with extension..." -ForegroundColor Yellow
$chromeArgs = @(
    "--load-extension=`"$extensionPath`"",
    "--remote-debugging-port=9222",
    "--new-window",
    "`"$canvasUrl`""
)

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (Test-Path $chromePath) {
    Start-Process $chromePath -ArgumentList $chromeArgs
    Write-Host "✅ Chrome launched successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Chrome not found at default location" -ForegroundColor Red
    Write-Host "Please update the path in the script" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎯 What should happen:" -ForegroundColor Cyan
Write-Host "  1. Chrome opens with extension loaded" -ForegroundColor White
Write-Host "  2. Navigates to Canvas assignments" -ForegroundColor White
Write-Host "  3. Click any assignment to see the sidebar!" -ForegroundColor White
Write-Host ""
Write-Host "📊 Extension features:" -ForegroundColor Cyan
Write-Host "  ✓ Purple sidebar on the right" -ForegroundColor White
Write-Host "  ✓ Mean/Median/Mode statistics" -ForegroundColor White
Write-Host "  ✓ Timer that counts up" -ForegroundColor White
Write-Host "  ✓ Bell curve visualization" -ForegroundColor White
Write-Host "  ✓ Time submission form" -ForegroundColor White




