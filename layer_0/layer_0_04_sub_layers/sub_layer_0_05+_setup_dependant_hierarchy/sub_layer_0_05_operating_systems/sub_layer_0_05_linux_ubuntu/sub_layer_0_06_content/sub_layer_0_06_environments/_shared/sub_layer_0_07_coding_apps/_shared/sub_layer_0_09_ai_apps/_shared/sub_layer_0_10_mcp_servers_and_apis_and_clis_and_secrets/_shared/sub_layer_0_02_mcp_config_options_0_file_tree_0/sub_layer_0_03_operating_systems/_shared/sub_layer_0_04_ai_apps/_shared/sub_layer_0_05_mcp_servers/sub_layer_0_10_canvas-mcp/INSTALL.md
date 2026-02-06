# Canvas MCP Server Installation Guide

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

## Prerequisites

### 1. Get Your Canvas API Key
1. Log into your Canvas account at your institution's Canvas URL (e.g., `https://byui.instructure.com`)
2. Go to **Account** > **Settings**
3. Scroll to **Approved Integrations** section
4. Click **+ New Access Token**
5. Enter a purpose (e.g., "Claude Code MCP")
6. Click **Generate Token**
7. **IMPORTANT**: Copy the token immediately - you won't be able to see it again!

### 2. Identify Your Canvas Base URL
- BYU-Idaho: `https://byui.instructure.com`
- Other institutions: Check your Canvas login URL

---

## Installation by OS & Tool

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

## Canvas API Capabilities for Students

### What You CAN Do via API:
- **Courses**: List, view details, get syllabus
- **Assignments**: List, view details, submit text/files
- **Announcements**: Read course announcements
- **Discussions**: View and post to discussions
- **Grades**: View your grades
- **Files**: List and download course files
- **Calendar**: View events and assignments
- **Modules**: View course modules and items

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

### What You CANNOT Do:
- Submit quizzes (final submission requires web UI)
- View quiz questions before starting
- Access other students' data
- Modify course content (you're a student)

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `CANVAS_BASE_URL` | Your institution's Canvas URL | `https://byui.instructure.com` |
| `CANVAS_API_TOKEN` | Your personal API access token | `7~abc123...` |

---

## Verification

Test your setup:
```bash
# Check MCP server is running
claude mcp list

# Should show canvas server connected
```

---

## Security Notes

- **Never commit your API token** to version control
- Store tokens in environment variables or secure credential storage
- API tokens have the same access as your Canvas account
- Revoke tokens immediately if compromised (Account > Settings > Approved Integrations)

---

## Troubleshooting

### "401 Unauthorized" Error
- Verify your API token is correct
- Check the token hasn't expired or been revoked
- Ensure you're using the correct Canvas base URL

### "Cannot find courses"
- Verify you're enrolled in active courses
- Check semester dates - courses may not be published yet

### Server Won't Start
- Ensure Node.js is installed (`node --version`)
- Check environment variables are set correctly
- Verify network connectivity to Canvas

---

## Related Documentation

- [Canvas REST API Docs](https://canvas.instructure.com/doc/api/)
- [Quiz Submission API](https://canvas.instructure.com/doc/api/quiz_submission_questions.html)
