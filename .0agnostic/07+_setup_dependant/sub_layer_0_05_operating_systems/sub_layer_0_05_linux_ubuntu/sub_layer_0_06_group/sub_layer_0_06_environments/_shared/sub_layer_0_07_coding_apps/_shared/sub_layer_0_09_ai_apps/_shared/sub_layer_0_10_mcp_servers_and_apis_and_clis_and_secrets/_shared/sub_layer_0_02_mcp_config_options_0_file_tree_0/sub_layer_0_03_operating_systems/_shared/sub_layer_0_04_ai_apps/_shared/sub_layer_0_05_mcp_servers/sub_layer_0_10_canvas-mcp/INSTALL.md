---
resource_id: "362621dc-772f-437b-b9cc-31df1cda86f3"
resource_type: "document"
resource_name: "INSTALL"
---
# Canvas MCP Server Installation Guide

<!-- section_id: "8f5c5e7f-fba6-404c-b3a9-edb6e1a8150a" -->
## Overview
The Canvas MCP Server enables Canvas LMS integration for AI agents, providing read access to courses, assignments, announcements, grades, and more for students using BYU-Idaho's Canvas LMS.

**Recommended Server**: [Shigakuresama/canvas-mcp-developer](https://github.com/Shigakuresama/canvas-mcp-developer)
- ~15 tools focused on read-only student operations
- Safer for students (no accidental writes)
- FERPA-aware design

**Alternative Servers**:
- [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) - 54 tools, full-featured read/write
- [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) - ~25 tools, Python, FERPA-aware
- [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) - ~20 tools

---

<!-- section_id: "71c240bc-4c4e-42ab-88ab-06bf83b1eaff" -->
## Prerequisites

<!-- section_id: "75b60789-d71d-4d34-abdc-9f403da5d01f" -->
### 1. Get Your Canvas API Key
1. Log into your Canvas account at your institution's Canvas URL (e.g., `https://byui.instructure.com`)
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations** section
4. Click **+ New Access Token**
5. Enter a purpose (e.g., "Claude Code MCP")
6. Click **Generate Token**
7. **IMPORTANT**: Copy the token immediately - you won't be able to see it again!

<!-- section_id: "d295b00d-e442-490a-bb2d-6facf0890f21" -->
### 2. Identify Your Canvas Base URL
- BYU-Idaho: `https://byui.instructure.com`
- Other institutions: Check your Canvas login URL

---

<!-- section_id: "8cd222a7-f546-4c15-99b1-4dcd17544e33" -->
## Installation by OS & Tool

<!-- section_id: "f823d1cc-8141-413c-9be4-fc95f3984357" -->
### For Claude Code CLI (Linux/Ubuntu)

**Method 1: Using claude mcp add (Recommended)**
```bash
claude mcp add canvas-lms -s user -- npx -y @anthropic/mcp-canvas-lms \
  --canvas-url "https://byui.instructure.com" \
  --api-token "YOUR_CANVAS_API_TOKEN"
```

**Method 2: Manual Configuration**
Add to `~/.claude.json`:
```json
{
  "mcpServers": {
    "canvas": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-canvas-lms"],
      "env": {
        "CANVAS_BASE_URL": "https://byui.instructure.com",
        "CANVAS_API_TOKEN": "YOUR_CANVAS_API_TOKEN"
      }
    }
  }
}
```

<!-- section_id: "ac068a74-f5e8-4c0e-831e-ec13f3afb86d" -->
### Alternative: Shigakuresama Canvas MCP Developer (Student-Focused)

Clone and build:
```bash
git clone https://github.com/Shigakuresama/canvas-mcp-developer.git
cd canvas-mcp-developer
npm install
npm run build
```

Add to configuration:
```json
{
  "mcpServers": {
    "canvas": {
      "command": "node",
      "args": ["/path/to/canvas-mcp-developer/build/index.js"],
      "env": {
        "CANVAS_BASE_URL": "https://byui.instructure.com",
        "CANVAS_API_TOKEN": "YOUR_CANVAS_API_TOKEN"
      }
    }
  }
}
```

---

<!-- section_id: "eec839cc-bdbb-41c6-82ae-92b2e62d18af" -->
## Canvas API Capabilities for Students

<!-- section_id: "ac238b16-7dda-483b-9ef2-a7e6b6c40e63" -->
### What You CAN Do via API:
- **Courses**: List, view details, get syllabus
- **Assignments**: List, view details, submit text/files
- **Announcements**: Read course announcements
- **Discussions**: View and post to discussions
- **Grades**: View your grades
- **Files**: List and download course files
- **Calendar**: View events and assignments
- **Modules**: View course modules and items

<!-- section_id: "568da8f7-f22e-4f96-9e18-c3d2f8bfabc3" -->
### Quiz Workflow (Special Case):
The Canvas API supports quiz interaction in a specific workflow:
1. **Start Quiz**: `POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`
2. **Get Questions**: After starting, questions become visible
3. **Save Answers (Draft)**: `POST /api/v1/quiz_submissions/:quiz_submission_id/questions`
   ```json
   {
     "attempt": 1,
     "validation_token": "YOUR_VALIDATION_TOKEN",
     "quiz_questions": [
       {"id": "1", "answer": "5"},        // Multiple choice - answer ID
       {"id": "2", "answer": ["3", "6"]}, // Multiple answers
       {"id": "3", "answer": "Essay text"} // Essay
     ]
   }
   ```
4. **Final Submit**: Must be done via web UI (API cannot complete final submission)

<!-- section_id: "eef35bb0-370e-4303-8bfc-ccf86aac8f9c" -->
### What You CANNOT Do:
- Submit quizzes (final submission requires web UI)
- View quiz questions before starting
- Access other students' data
- Modify course content (you're a student)

---

<!-- section_id: "b8f605d2-802b-47ee-bbed-97665d2c956a" -->
## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `CANVAS_BASE_URL` | Your institution's Canvas URL | `https://byui.instructure.com` |
| `CANVAS_API_TOKEN` | Your personal API access token | `7~abc123...` |

---

<!-- section_id: "77539876-f56f-4803-ab08-2a4635212a2d" -->
## Verification

Test your setup:
```bash
# Check MCP server is running
claude mcp list

# Should show canvas server connected
```

---

<!-- section_id: "cfa9d693-0887-45d3-9cb5-d935d3d6283b" -->
## Security Notes

- **Never commit your API token** to version control
- Store tokens in environment variables or secure credential storage
- API tokens have the same access as your Canvas account
- Revoke tokens immediately if compromised (Account > Settings > Approved Integrations)

---

<!-- section_id: "ab59cae1-87df-4ea4-8bde-a33c7a672f58" -->
## Troubleshooting

<!-- section_id: "82affbc0-12c9-42aa-a989-8d1301f87319" -->
### "401 Unauthorized" Error
- Verify your API token is correct
- Check the token hasn't expired or been revoked
- Ensure you're using the correct Canvas base URL

<!-- section_id: "48342155-f2d6-4c47-ba82-43eaca06a1ad" -->
### "Cannot find courses"
- Verify you're enrolled in active courses
- Check semester dates - courses may not be published yet

<!-- section_id: "15f4386d-2db0-4b81-93f5-3d1a148de05b" -->
### Server Won't Start
- Ensure Node.js is installed (`node --version`)
- Check environment variables are set correctly
- Verify network connectivity to Canvas

---

<!-- section_id: "ee30d9bc-ed53-4eb5-9c17-053ff2916cf8" -->
## Related Documentation

- [Canvas REST API Docs](https://canvas.instructure.com/doc/api/)
- [Quiz Submission API](https://canvas.instructure.com/doc/api/quiz_submission_questions.html)
