# Claude Code Agent Teams - Research Report

> **Layer**: -1 (Research) | **Stage**: 02 (Research)
> **Date**: 2026-02-07
> **Subject**: Verification of claims about Claude Code Agent Teams feature

---

## Executive Summary

Claude Code Agent Teams is an **experimental feature** released alongside Opus 4.6 in February 2026. It enables multiple Claude Code instances to work in parallel, coordinated by a lead session through a shared task list and peer-to-peer messaging system. The feature is disabled by default and must be enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

Below are findings for each claim under investigation, with source citations.

---

## 1. Are agents terminated when the team is deleted? Or do they persist?

**Finding: Agents must be shut down BEFORE the team can be cleaned up. They do not persist after cleanup.**

The lifecycle is explicit:

- The lead sends a **shutdown request** to each teammate. The teammate can **approve** (exit gracefully) or **reject** with an explanation.
- Teammates finish their current request or tool call before actually shutting down (this can be slow).
- When the lead runs **cleanup**, it checks for active teammates and **fails if any are still running**. You must shut them all down first.
- Cleanup then **removes the shared team resources** (config at `~/.claude/teams/{team-name}/config.json` and tasks at `~/.claude/tasks/{team-name}/`).

Teammates are separate Claude Code processes. Once shut down and cleaned up, they do not persist. There is no mechanism for teammates to survive independently after team cleanup.

**Edge case**: Orphaned tmux sessions may persist after cleanup if not fully cleaned up. These must be killed manually with `tmux kill-session -t <session-name>`.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Clean up the team" and "Shut down teammates" sections
- [ClaudeFast Guide](https://claudefa.st/blog/guide/agents/agent-teams) -- "Step 5: Clean Up"

---

## 2. Can users "enter" any running agent and interact with it?

**Finding: Yes. Users can interact directly with any running teammate, independent of the lead.**

This is a key differentiator from subagents. Two display modes support this:

- **In-process mode**: Use `Shift+Up/Down` to select a teammate, then type to send them a message. Press `Enter` to view a teammate's session. Press `Escape` to interrupt their current turn. Press `Ctrl+T` to toggle the task list.
- **Split-pane mode** (requires tmux or iTerm2): Click into a teammate's pane to interact with their session directly. Each teammate has a full view of their own terminal.

The official docs state: "Each teammate is a full, independent Claude Code session. You can message any teammate directly to give additional instructions, ask follow-up questions, or redirect their approach."

This direct interaction is one of the main advantages over subagents, which can only report results back to the main agent.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Talk to teammates directly" section
- [SerenityAI Setup Guide](https://serenitiesai.com/articles/claude-code-agent-teams-documentation)

---

## 3. Is agent context reusable across team sessions?

**Finding: No. Agent context is NOT reusable across sessions. This is a known limitation.**

Key facts:

- `/resume` and `/rewind` **do not restore in-process teammates**. After resuming a session, the lead may attempt to message teammates that no longer exist.
- The workaround is to **spawn fresh teammates** after resuming.
- Each teammate's conversation history is independent and not transferred between sessions.
- Team configuration files persist locally at `~/.claude/teams/{team-name}/config.json` and `~/.claude/tasks/{team-name}/`, but these are metadata/coordination files, not conversation context.
- There is no built-in mechanism to resume a teammate with its prior conversation history intact.

However, **project context** (CLAUDE.md, MCP servers, skills) is loaded fresh for each teammate when spawned, so project-level instructions are always available.

For long-running work, some practitioners use a `claude-progress.txt` file in the repository to maintain cross-session state manually -- each agent reads and updates it as a handoff mechanism.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Limitations" section
- [Anthropic Engineering: Building C Compiler](https://www.anthropic.com/engineering/building-c-compiler)

---

## 4. How are teams created -- from layer structure or ad-hoc?

**Finding: Teams are created ad-hoc via natural language prompts. There is no layer/structure-based creation mechanism.**

Two ways teams get started:

1. **You request a team**: Give Claude a task that benefits from parallel work and explicitly ask for an agent team. Claude creates one based on your instructions.
2. **Claude proposes a team**: If Claude determines your task would benefit from parallel work, it may suggest creating a team. You confirm before it proceeds.

In both cases, you describe the team structure in natural language. Examples from the docs:

```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
```

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

There is no declarative team definition file, no YAML/JSON team specification, and no automatic team creation from directory structure or layer systems. The creation is entirely conversational and ad-hoc.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "How Claude starts agent teams" section
- [NxCode Guide](https://www.nxcode.io/resources/news/claude-agent-teams-parallel-ai-development-guide-2026)

---

## 5. What is the actual lifecycle: create team -> spawn agents -> work -> shutdown?

**Finding: The lifecycle is as documented below.**

### Full Lifecycle

1. **Enable**: Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings or environment.
2. **Create team**: User describes the task and team structure in natural language. Claude creates the team, which generates a config at `~/.claude/teams/{team-name}/config.json`.
3. **Spawn teammates**: The lead spawns separate Claude Code instances. Each gets:
   - Its own full context window
   - Project context (CLAUDE.md, MCP servers, skills)
   - A spawn prompt from the lead describing their role
   - The lead's permission settings
   - The lead's conversation history does NOT carry over.
4. **Task creation and assignment**: The lead creates a shared task list at `~/.claude/tasks/{team-name}/`. Tasks have three states: pending, in progress, completed. Tasks can have dependencies.
5. **Work execution**: Teammates claim tasks (self-claim or lead-assigned). File locking prevents race conditions. Teammates communicate via direct messages or broadcasts.
6. **Monitoring**: User checks progress via `Shift+Up/Down` or tmux panes. Lead synthesizes findings. User can redirect approaches.
7. **Shutdown**: Lead sends shutdown requests to each teammate. Teammates approve or reject. They finish current work before exiting.
8. **Cleanup**: Lead removes shared team resources. Fails if any teammates are still active.

### Key Coordination Mechanisms

- **Shared task list** with automatic dependency unblocking
- **Peer-to-peer messaging** (direct messages and broadcasts)
- **Idle notifications** (teammates auto-notify lead when finished)
- **Plan approval** (optional: teammates plan in read-only mode until lead approves)
- **Delegate mode** (`Shift+Tab`): restricts lead to coordination-only tools

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- full page
- [Paddo.dev: Hidden Swarm](https://paddo.dev/blog/claude-code-hidden-swarm/)

---

## 6. Can agents be spawned with custom CLAUDE.md paths or context?

**Finding: No custom CLAUDE.md paths. All teammates load the standard project CLAUDE.md. Context is customized via spawn prompts.**

Per the official docs: "When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills. It also receives the spawn prompt from the lead."

There is no documented mechanism to:
- Specify a different CLAUDE.md file per teammate
- Override MCP server configurations per teammate
- Pass custom context file paths at spawn time

**What you CAN do**:

- Provide detailed, role-specific instructions in the **spawn prompt**. This is the primary mechanism for giving teammates different context.
- Example from docs:
  ```
  Spawn a security reviewer teammate with the prompt: "Review the authentication
  module at src/auth/ for security vulnerabilities. Focus on token handling, session
  management, and input validation. The app uses JWT tokens stored in httpOnly
  cookies. Report any issues with severity ratings."
  ```
- Teammates read CLAUDE.md from their working directory, so if you use different working directories, they could theoretically pick up different CLAUDE.md files. But this is not a documented or supported pattern for agent teams.

The docs also note: "CLAUDE.md works normally: teammates read CLAUDE.md files from their working directory."

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Context and communication" section and Limitations tip
- [Addy Osmani Blog](https://addyosmani.com/blog/claude-code-agent-teams/)

---

## 7. What tools do teammates have access to?

**Finding: Teammates have the same tools as any regular Claude Code session, inheriting the lead's permission settings.**

Teammates get access to:

- **Core tools**: Read, Edit, Write, Bash, Glob, Grep (same as any Claude Code session)
- **MCP servers**: All configured MCP servers from the project
- **Skills**: All skills defined in `.claude/skills/`
- **Team-specific tools**: SendMessage (direct messages, broadcasts, shutdown responses, plan approval responses), TaskUpdate

### Permission Inheritance

- Teammates start with the **lead's permission settings**
- If the lead uses `--dangerously-skip-permissions`, all teammates do too
- After spawning, you can change individual teammate modes
- You CANNOT set per-teammate permission modes at spawn time
- Permission tiers: read-only operations (Read, Grep) need no approval; file modifications and Bash commands may need approval based on settings

### Lead in Delegate Mode

When the lead enters delegate mode (`Shift+Tab`), it is restricted to **coordination-only tools**:
- Spawning teammates
- Sending messages
- Shutting down teammates
- Managing tasks

The lead CANNOT touch code directly in delegate mode.

### Hooks

Two hooks are specific to agent teams:
- **TeammateIdle**: Runs when a teammate is about to go idle. Exit code 2 sends feedback and keeps the teammate working.
- **TaskCompleted**: Runs when a task is being marked complete. Exit code 2 prevents completion and sends feedback.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Permissions" and "Enforce quality gates with hooks" sections
- [Official Docs: Permissions](https://code.claude.com/docs/en/permissions)
- [ClaudeFast Guide](https://claudefa.st/blog/guide/agents/agent-teams) -- "Quality Gates with Hooks"

---

## 8. How does the team lead coordinate -- is it customizable?

**Finding: The lead coordinates via natural language instructions, shared task lists, and messaging. Coordination behavior is customizable through prompts and modes.**

### Default Lead Behavior

The lead is your main Claude Code session. It:
- Creates the team and spawns teammates
- Decomposes work into tasks
- Assigns tasks or lets teammates self-claim
- Receives automatic notifications when teammates go idle or send messages
- Synthesizes results from teammates
- Manages shutdown and cleanup

### Customization Points

1. **Natural language instructions**: The lead's coordination behavior is shaped by your prompts. You can tell it:
   - "Wait for your teammates to complete their tasks before proceeding"
   - "Only approve plans that include test coverage"
   - "Reject plans that modify the database schema"

2. **Delegate mode** (`Shift+Tab`): Forces the lead to coordinate only, preventing it from implementing tasks itself.

3. **Plan approval**: Require teammates to plan before implementing. The lead reviews and approves/rejects plans autonomously based on criteria you set.

4. **Task dependencies**: You can describe task ordering and the lead creates appropriate dependencies in the shared task list.

5. **Model selection**: You can specify which model each teammate uses (e.g., Opus for the lead, Sonnet for teammates), balancing cost vs. capability.

6. **Hooks**: `TeammateIdle` and `TaskCompleted` hooks let you enforce automated quality gates.

### What is NOT Customizable

- The lead is **fixed** to the session that creates the team. No promotion or transfer.
- The lead cannot be replaced mid-session.
- You cannot define a custom coordination protocol or override the built-in TeammateTool operations.
- No nested teams: teammates cannot spawn their own teams.

**Sources**:
- [Official Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams) -- "Control your agent team" and "How agent teams work" sections
- [Paddo.dev: The Switch Got Flipped](https://paddo.dev/blog/agent-teams-the-switch-got-flipped/)
- [Gist: Multi-Agent Orchestration](https://gist.github.com/kieranklaassen/d2b35569be2c7f1412c64861a219d51f)

---

## Additional Findings

### Known Limitations (Official)

| Limitation | Detail |
|---|---|
| No session resumption | `/resume` and `/rewind` do not restore teammates |
| One team per session | Must clean up before starting a new one |
| No nested teams | Teammates cannot spawn their own teams |
| Fixed lead | Cannot promote a teammate or transfer leadership |
| Permissions set at spawn | Inherited from lead; can change after but not at spawn time |
| Split panes need tmux/iTerm2 | Not supported in VS Code terminal, Windows Terminal, or Ghostty |
| Shutdown can be slow | Teammates finish current work before exiting |
| Task status can lag | Teammates sometimes forget to mark tasks complete |

### Storage Locations

```
~/.claude/
  teams/{team-name}/
    config.json          # Team metadata + members array
  tasks/{team-name}/     # Shared task list files
```

### Environment Variables (from binary analysis)

| Variable | Purpose |
|---|---|
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Enable the feature |
| `CLAUDE_CODE_TEAM_NAME` | Current team context |
| `CLAUDE_CODE_AGENT_ID` | Agent identifier |
| `CLAUDE_CODE_AGENT_NAME` | Agent display name |
| `CLAUDE_CODE_AGENT_TYPE` | Agent role/type |
| `CLAUDE_CODE_PLAN_MODE_REQUIRED` | Whether plan approval is needed |

### Cost Considerations

Agent teams use significantly more tokens than single sessions. Each teammate has its own full context window. A 3-teammate team running for 30 minutes uses roughly 3-4x the tokens of a single session. The C compiler project (16 agents, ~2000 sessions) cost approximately $20,000 in API calls.

---

## Sources

- [Official Documentation: Agent Teams](https://code.claude.com/docs/en/agent-teams)
- [Official Documentation: Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Official Documentation: Permissions](https://code.claude.com/docs/en/permissions)
- [Anthropic Engineering: Building a C Compiler](https://www.anthropic.com/engineering/building-c-compiler)
- [Anthropic Engineering: Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Addy Osmani: Claude Code Agent Teams](https://addyosmani.com/blog/claude-code-agent-teams/)
- [ClaudeFast: Agent Teams Guide](https://claudefa.st/blog/guide/agents/agent-teams)
- [Paddo.dev: Claude Code's Hidden Multi-Agent System](https://paddo.dev/blog/claude-code-hidden-swarm/)
- [Paddo.dev: Agent Teams - The Switch Got Flipped](https://paddo.dev/blog/agent-teams-the-switch-got-flipped/)
- [NxCode: Claude Agent Teams Guide](https://www.nxcode.io/resources/news/claude-agent-teams-parallel-ai-development-guide-2026)
- [SerenityAI: Agent Teams Setup Guide](https://serenitiesai.com/articles/claude-code-agent-teams-documentation)
- [Kieran Klaassen Gist: Multi-Agent Orchestration](https://gist.github.com/kieranklaassen/d2b35569be2c7f1412c64861a219d51f)
- [TechCrunch: Anthropic Releases Opus 4.6](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/)
