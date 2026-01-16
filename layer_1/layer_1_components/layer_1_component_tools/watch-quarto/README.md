# Quarto Watcher Helper

Use `watch-quarto.ps1` to automatically render a Quarto document and capture the output whenever the source (or any watched dependency) changes. Each Quarto file gets its own subfolder of tall PNG screenshots by default—ideal for AI review—and you can optionally export PDFs alongside them.

## Prerequisites

- Quarto CLI installed and available on the `PATH`.
- Microsoft Edge or Google Chrome installed with headless support (the script auto-discovers typical install paths; override with `-BrowserPath` if needed).
- PowerShell 5.1+ (ships with Windows 10/11).

## Quick Start

```powershell
# From the repo root
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\dev\Degree\Data Science Programming\forked_brother_palmers_version\DS250-Course-Draft\Templates\unit1_task2_template.qmd" `
  -RenderOnStart
```

What happens:
- Renders the Quarto file immediately.
- Creates (if needed) `quarto_shots/<file-stem>/` next to the source and drops a tall PNG (`preview_YYYYMMDD_HHMMSS.png`, viewport `1400 x 6000`) inside it.
- Keeps watching the file for further changes until you press Enter in that PowerShell window. Expect the browser to print messages like `xxxxx bytes written…`—they come from Edge/Chrome and can be ignored.

## Watching Additional Inputs

```powershell
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\path\to\report.qmd" `
  -WatchExtras ".\data", ".\images\charts" `
  -RenderOnStart
```

Every save inside the listed directories triggers a render.

## Controlling Capture Output

- `-CaptureMode png|pdf|both` – choose screenshot (default), PDF export, or both.
- `-ViewportWidth` / `-ViewportHeight` – set the browser viewport before capturing; raise the height (default 6000 px) if the page is still longer than the screenshot.
- `-ScreenshotDir` – root folder for captures; the script creates a subdirectory named after the `.qmd` within this path.
- `-BrowserPath` – point explicitly at `msedge.exe` or `chrome.exe` if auto-detect fails.

Examples:

```powershell
# PNG only with a taller viewport for very long pages
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\path\to\report.qmd" `
  -ViewportHeight 8000 `
  -RenderOnStart
```

```powershell
# Full-page PDF only (stored under the same per-file subfolder)
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\path\to\report.qmd" `
  -CaptureMode pdf `
  -RenderOnStart
```

```powershell
# Produce both the tall PNG for AI review and a PDF for archiving
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\path\to\report.qmd" `
  -CaptureMode both `
  -RenderOnStart
```

## Other Options

- `-QuartoExe` – supply the full path to `quarto.exe` if it isn’t on `PATH`.
- `-CooldownMs` – debounce repeated change events (default 3000 ms).

## Stopping the Watcher

Focus the PowerShell window running the watcher and press Enter. All filesystem watchers are disposed cleanly.

## Troubleshooting Tips

- "Unable to locate a headless-capable browser": pass `-BrowserPath` pointing to Edge or Chrome.
- No screenshot/PDF produced: check the Quarto render output for errors, and confirm Edge/Chrome supports headless mode on your build.
- Only part of the page captured: raise `-ViewportHeight` or switch to `-CaptureMode pdf` to grab a full-page PDF.
- Excess files: tweak `-CooldownMs` and your editor’s auto-save behavior.
