---
resource_id: "64a8639c-b493-4d3e-9d0c-08d0396e55f3"
resource_type: "readme_document"
resource_name: "README"
---
# Quarto Watcher Helper

Use `watch-quarto.ps1` to automatically render a Quarto document and capture the output whenever the source (or any watched dependency) changes. Each Quarto file gets its own subfolder of tall PNG screenshots by default�ideal for AI review�and you can optionally export PDFs alongside them.

<!-- section_id: "35d36d43-b813-4d72-b427-87ead49ab799" -->
## Prerequisites

- Quarto CLI installed and available on the `PATH`.
- Microsoft Edge or Google Chrome installed with headless support (the script auto-discovers typical install paths; override with `-BrowserPath` if needed).
- PowerShell 5.1+ (ships with Windows 10/11).

<!-- section_id: "849add9f-4f6c-4001-9c61-dd168f60c9b8" -->
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
- Keeps watching the file for further changes until you press Enter in that PowerShell window. Expect the browser to print messages like `xxxxx bytes written�`�they come from Edge/Chrome and can be ignored.

<!-- section_id: "987396f3-8035-4cca-9098-52a5b028f4f2" -->
## Watching Additional Inputs

```powershell
powershell -ExecutionPolicy Bypass -File tools/watch-quarto/watch-quarto.ps1 `
  -QuartoFile "C:\path\to\report.qmd" `
  -WatchExtras ".\data", ".\images\charts" `
  -RenderOnStart
```

Every save inside the listed directories triggers a render.

<!-- section_id: "cda2d008-638e-4be6-af9d-eba70ca119ec" -->
## Controlling Capture Output

- `-CaptureMode png|pdf|both` � choose screenshot (default), PDF export, or both.
- `-ViewportWidth` / `-ViewportHeight` � set the browser viewport before capturing; raise the height (default 6000 px) if the page is still longer than the screenshot.
- `-ScreenshotDir` � root folder for captures; the script creates a subdirectory named after the `.qmd` within this path.
- `-BrowserPath` � point explicitly at `msedge.exe` or `chrome.exe` if auto-detect fails.

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

<!-- section_id: "beb2271a-bbaa-4c25-830b-51f5baf9b0b1" -->
## Other Options

- `-QuartoExe` � supply the full path to `quarto.exe` if it isn�t on `PATH`.
- `-CooldownMs` � debounce repeated change events (default 3000 ms).

<!-- section_id: "49e189ea-6869-44e7-95e9-ddc0702a461e" -->
## Stopping the Watcher

Focus the PowerShell window running the watcher and press Enter. All filesystem watchers are disposed cleanly.

<!-- section_id: "3e99e88d-3859-4b74-823e-5174ce97253a" -->
## Troubleshooting Tips

- "Unable to locate a headless-capable browser": pass `-BrowserPath` pointing to Edge or Chrome.
- No screenshot/PDF produced: check the Quarto render output for errors, and confirm Edge/Chrome supports headless mode on your build.
- Only part of the page captured: raise `-ViewportHeight` or switch to `-CaptureMode pdf` to grab a full-page PDF.
- Excess files: tweak `-CooldownMs` and your editor�s auto-save behavior.
