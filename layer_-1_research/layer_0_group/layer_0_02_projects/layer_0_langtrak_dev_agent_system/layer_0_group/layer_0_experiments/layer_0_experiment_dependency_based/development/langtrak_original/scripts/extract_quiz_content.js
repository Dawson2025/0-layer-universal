// resource_id: "f8593d74-4997-42cc-b69e-3658dcd3e5d5"
// resource_type: "document"
// resource_name: "extract_quiz_content"
import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const AUTH_FILE = path.resolve(__dirname, 'canvas_auth.json');
const MODULES_FILE = path.resolve(__dirname, '../data/applied_programming_modules.json');
const SCREENSHOT_DIR = path.resolve(__dirname, '../screenshots');
const OUTPUT_FILE = path.resolve(__dirname, '../data/quiz_details.md');

if (!fs.existsSync(SCREENSHOT_DIR)) {
    fs.mkdirSync(SCREENSHOT_DIR);
}

// Assignments to look for
const TARGET_KEYWORDS = ['Plan', 'Report'];

async function run() {
    if (!fs.existsSync(AUTH_FILE)) {
        console.error(`Auth file not found at ${AUTH_FILE}. Run setup first.`);
        process.exit(1);
    }

    const modulesData = JSON.parse(fs.readFileSync(MODULES_FILE, 'utf8'));
    let assignments = [];

    // Filter assignments
    modulesData.forEach(module => {
        module.items.forEach(item => {
            if (item.title && TARGET_KEYWORDS.some(k => item.title.includes(k))) {
                assignments.push(item);
            }
        });
    });

    // Check existing progress
    let existingOutput = "";
    if (fs.existsSync(OUTPUT_FILE)) {
        existingOutput = fs.readFileSync(OUTPUT_FILE, 'utf8');
    }
    
    // Filter out already processed assignments
    const remainingAssignments = assignments.filter(a => !existingOutput.includes(`## ${a.title}`));

    console.log(`Found ${assignments.length} total. ${remainingAssignments.length} remaining to process.`);

    if (remainingAssignments.length === 0) {
        console.log("All assignments processed.");
        return;
    }

    // Launch browser OUTSIDE the loop, but use new contexts or pages?
    // If the browser itself crashes, we need to restart the browser.
    // Let's try restarting the browser every time for maximum stability since we saw crashes.
    
    for (const assignment of remainingAssignments) {
        console.log(`Processing: ${assignment.title}...`);
        
        let browser;
        try {
            browser = await chromium.launch({ headless: true });
            const context = await browser.newContext({ storageState: AUTH_FILE });
            const page = await context.newPage();

            await page.goto(assignment.link, { waitUntil: 'networkidle', timeout: 60000 });
            
            const takeButton = await page.$('#take_quiz_link, .take_quiz_button, a[href*="/take"]');
            
            if (takeButton) {
                console.log("  Clicking 'Take/Resume Quiz'...");
                await takeButton.click();
                await page.waitForLoadState('networkidle');
                await page.waitForTimeout(3000); 
            }

            const safeTitle = assignment.title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
            const screenshotPath = path.join(SCREENSHOT_DIR, `${safeTitle}.png`);
            const processedPath = path.join(SCREENSHOT_DIR, `${safeTitle}_processed.png`);
            const ocrPrefix = path.join(SCREENSHOT_DIR, `${safeTitle}_ocr`);

            await page.screenshot({ path: screenshotPath, fullPage: true });
            console.log(`  Screenshot saved: ${screenshotPath}`);

            console.log("  Running OCR...");
            try {
                execSync(`convert "${screenshotPath}" -grayscale Rec709Luma -threshold 60% "${processedPath}"`);
            } catch (e) {
                console.warn("  ImageMagick conversion failed, using raw screenshot.");
                fs.copyFileSync(screenshotPath, processedPath);
            }

            let ocrText = "";
            try {
                execSync(`tesseract "${processedPath}" "${ocrPrefix}" -l eng --psm 3`);
                ocrText = fs.readFileSync(`${ocrPrefix}.txt`, 'utf8');
            } catch (e) {
                console.error("  OCR failed:", e.message);
                ocrText = "(OCR Failed)";
            }

            // Append to file immediately
            let entry = `## ${assignment.title}\n`;
            entry += `**Due:** ${assignment.due || 'N/A'}\n`;
            entry += `**Link:** ${assignment.link}\n\n`;
            entry += "### OCR Content\n\n";
            entry += "```text\n";
            entry += ocrText.trim();
            entry += "\n```\n\n---\n\n";

            fs.appendFileSync(OUTPUT_FILE, entry);
            console.log(`  Saved to ${OUTPUT_FILE}`);

        } catch (err) {
            console.error(`  Error processing ${assignment.title}:`, err);
            // Don't write failure to file, so we can retry later or manual fix
        } finally {
            if (browser) await browser.close();
        }
    }
}

run();