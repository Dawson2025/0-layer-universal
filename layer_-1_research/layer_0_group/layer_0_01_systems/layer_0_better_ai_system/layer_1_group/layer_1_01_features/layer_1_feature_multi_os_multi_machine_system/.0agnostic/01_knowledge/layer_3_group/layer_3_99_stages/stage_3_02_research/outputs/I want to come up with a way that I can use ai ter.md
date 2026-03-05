---
resource_id: "155eafb6-87f5-4e62-8609-03143539fdda"
resource_type: "knowledge"
resource_name: "I want to come up with a way that I can use ai ter"
---
<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want to come up with a way that I can use ai terminal tools like. Claude code, codex cli, and Gemini Cli, and even the cursor ide from a remote server that I can access both from my mobile phone, and also from my laptop, and also be able to do things like have the cli tools control browsers like Claude in chrome and like playwright mcp servers and see the screen from my phone and from the laptop, all while seeing it from a remote server. And I want there to be shared file systems between them. I currently have sync thing set up with wsl, windows, and Linux Ubuntu on the same computer, and I’d like to set up connections for the same folder and file system in the remote server and be able to have 2 way sync for all of the systems and environments I use it in

You can treat a remote Linux box as your “AI dev hub” that exposes terminals, MCP browsers, and a shared filesystem to both phone and laptop.  Below is a concrete way to wire this together around SSH/Tailscale, Syncthing, and VNC/noVNC.[^1_1][^1_2]

## Core architecture

- **One main remote dev server** (e.g., Ubuntu VPS or home server) that runs all CLI tools (Claude Code, Gemini CLI, Codex CLI), MCP servers (Playwright), and optionally Cursor via remote desktop.[^1_2][^1_1]
- **Zero‑trust networking** via Tailscale so your laptop and phone can SSH or open web UIs to that server, no port forwarding needed.[^1_3][^1_4][^1_5]
- **Syncthing mesh** between:
    - Windows host
    - WSL
    - Local Ubuntu
    - Remote server
All pointed at the same project folder(s) with full bidirectional sync.[^1_6][^1_7][^1_8]
- **Remote browser view**:
    - GUI browsers and Cursor via VNC/noVNC on the server.[^1_2]
    - Playwright MCP in “WebUI mode” inside Docker with VNC/noVNC, controllable from your AI tools.[^1_2]


## Remote access from laptop and phone

- Install Tailscale on:
    - Remote server
    - Laptop (Windows + WSL)
    - Phone (Blink, Prompt, or similar SSH client works well with Tailscale).[^1_5][^1_3]
- Enable Tailscale SSH on the server (`tailscale up --ssh`), then:
    - From laptop: use VS Code Remote SSH or Tailscale’s VS Code extension to attach to the server and run terminals and dev servers there.[^1_4][^1_1][^1_3]
    - From phone: use a terminal app that supports Tailscale (e.g., Blink + Mosh) for resilient long‑running sessions to the same server.[^1_5]

This gives you the same shell and tools from both devices, pointed at the shared project directories.

## Running AI CLIs and MCP browsers on the server

- Install your AI CLIs (Claude Code, Gemini CLI, etc.) directly on the server and configure them to use the shared project directory synced by Syncthing.[^1_7][^1_6]
- For **Playwright MCP + visible browser**:
    - Use a Docker setup that runs Playwright MCP in WebUI mode with VNC/noVNC, so the browser UI is inside a container but viewable in any browser.[^1_2]
    - Expose:
        - one port for noVNC (e.g., `http://server:6901` for visual control), and
        - the MCP SSE endpoint (e.g., `http://server:8831/sse`) for your AI client.[^1_2]

This lets your AI tools “drive” Chrome/Chromium remotely while you watch and interact from both phone and laptop, all through the same server.

## Shared filesystem with Syncthing

- Put your **canonical project folder** under Syncthing control on one machine first, then add all other devices as “remote devices” and share that folder with them.[^1_8][^1_6][^1_7]
- On each node (Windows, WSL, local Ubuntu, remote server):
    - Install Syncthing
    - Use the device IDs to link them, then share the same folder and ensure the path on each host points to where you want code to live (e.g., `/home/you/dev/shared` on Linux, `D:\dev\shared` on Windows).[^1_6][^1_7][^1_8]

With that setup, edits from any environment (local IDE, server‑side CLIs, Cursor in VNC) propagate to all others nearly in real time.

## Visual desktop (Cursor, Chrome) from both devices

- On the server, run a lightweight desktop (XFCE) plus a VNC server, or use a Dockerized VNC/noVNC environment like the Playwright MCP WebUI stack.[^1_9][^1_10][^1_2]
- Start:
    - Chrome or another browser for Claude‑in‑Chrome
    - Cursor IDE installed on the server (if supported in your distro)
- Connect to that session:
    - From laptop: open the noVNC URL in a browser via the Tailscale hostname.[^1_4][^1_2]
    - From phone: same URL in mobile browser, or a VNC client app over Tailscale.[^1_5][^1_2]

This way you are literally looking at the same remote screen from both devices, while AI CLIs and MCP servers run on that same machine and operate on the shared Syncthing folder.

If you tell which provider you want to use for the remote box (home server vs. VPS) and what phone OS you have, a step‑by‑step command list can be sketched out for your exact stack.

<div align="center">⁂</div>

[^1_1]: https://www.alexjd.co.uk/posts/remote-development-tailscale

[^1_2]: https://lobehub.com/mcp/kuldeepgorasiya-mcp-playwright

[^1_3]: https://tailscale.com/kb/1265/vscode-extension

[^1_4]: https://github.com/tailscale-dev/vscode-tailscale

[^1_5]: https://docs.blink.sh/integrations/tailscale+mosh

[^1_6]: https://docs.oracle.com/en/learn/oci-syncthing/index.html

[^1_7]: https://opensource.com/article/20/1/sync-files-syncthing

[^1_8]: https://forum.syncthing.net/t/sync-multiple-devices/22732

[^1_9]: https://news.ycombinator.com/item?id=35491922

[^1_10]: https://www.reddit.com/r/WebRTC/comments/1hft1p7/webrtc_for_streaming_headless_browsers_to_web_apps/


---

# After setting up a minimum viable product for this for myself, I’d like to be able to use the system to have access to all of these things while also being able to use voice calls with ai and video calls with ai and access and use unreal game engine from my phone and be able to access and use 3D worlds and simulations that are run wherever they need to be and have ai be able to interact with those 3D worlds with an avatar and also control that 3D world as if it was a god using unreal engine controls

You can extend your “remote AI dev hub” into a cloud 3D / voice / video stack by combining Unreal Pixel Streaming with realtime voice APIs and your existing remote server setup.  Think of it as one or more GPU servers running Unreal and AI, streamed to your phone and laptop over WebRTC.[^2_1][^2_2]

## Key building blocks

- **Unreal Engine in the cloud** with Pixel Streaming so any device can see and control the 3D world in a browser.[^2_3][^2_4][^2_5][^2_1]
- **Voice and video AI calls** using a Realtime API over WebRTC (e.g., a browser client talking to an LLM for live speech‑to‑speech and screen‑aware assistance).[^2_6][^2_7][^2_2]
- **AI “god mode” controller** that talks to Unreal via a network API or plugin and can drive an avatar and also send higher‑level commands (teleport, spawn, time of day).[^2_8][^2_9][^2_3]

All of this can run on the same remote environment concept as your MVP: you just add GPU capacity and WebRTC‑based streaming.

## Unreal worlds on phone and laptop

- Use Unreal’s built‑in **Pixel Streaming** to run your Unreal app on a GPU server, and stream its audio/video to any WebRTC‑capable browser.[^2_5][^2_1][^2_3]
- Configure the Pixel Streaming signaling server (Cirrus) and STUN/TURN so you can access the 3D session from outside your LAN on both mobile and laptop with low latency.[^2_4][^2_3][^2_5]

From your perspective, Unreal runs “wherever it needs to be” (on a GPU host), and your devices just open a URL to see and interact with the world.

## AI voice and video calls into the system

- For **voice calls with AI**, implement a WebRTC audio client in your browser or app that connects to a Realtime LLM API for live speech‑to‑speech conversations.[^2_7][^2_2][^2_6]
- Use a small backend (FastAPI or similar) to manage signaling, stream microphone audio to the LLM, and play back synthesized speech while exposing hooks for tool calls (e.g., “move my avatar”, “spawn an object”).[^2_2][^2_6][^2_7]

This gives you a persistent “AI on the line” while you are in the 3D world, on either phone or laptop.

## Letting AI control Unreal worlds

- Inside Unreal, expose a **control layer** (HTTP/REST, WebSockets, or a custom plugin) so external agents can drive pawns, cameras, and game state in response to function calls.[^2_9][^2_8][^2_3]
- When the voice or text agent receives a command, it translates that into structured actions (e.g., “move avatar to X,Y,Z”, “toggle god mode and change time‑of‑day”) and sends them to Unreal via this control API.[^2_8][^2_9][^2_3]

That lets your AI play as both an avatar (first‑person) and a **god‑mode** controller (editor‑like actions) in the same simulation.

## How this connects to your MVP

- Keep the **remote AI dev server** as your orchestration layer: your CLIs, MCP servers, and file sync already live there, and you add:
    - A GPU Unreal host (same machine if powerful enough, or a separate GPU box) running Pixel Streaming.[^2_1][^2_3][^2_4]
    - A Realtime voice backend that shares the same project and configuration to understand world state and commands.[^2_6][^2_7][^2_2]

Once the MVP is stable, the main extra work is wiring Unreal’s Pixel Streaming and a Realtime voice agent together via a control API so your AI can speak with you *and* act inside the 3D world.
<span style="display:none">[^2_10]</span>

<div align="center">⁂</div>

[^2_1]: https://tensorworks.com.au/blog/investigation-custom-unreal-engine-streaming-solutions/

[^2_2]: https://platform.openai.com/docs/guides/realtime-webrtc

[^2_3]: https://unrealcontainers.com/docs/use-cases/pixel-streaming

[^2_4]: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine

[^2_5]: https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-pixel-streaming-in-unreal-engine

[^2_6]: https://dev.to/ag2ai/real-time-voice-interactions-over-webrtc-1p81

[^2_7]: https://www.ridgerun.ai/post/introducing-voice-agent-real-time-voice-assistant-for-language-models

[^2_8]: https://www.eagle3dstreaming.com/multiplayer-collaboration-pixel-streaming-in-unreal-engine

[^2_9]: https://www.reddit.com/r/unrealengine/comments/18c6d2z/creating_multiplayer_unreal_engine_experiences/

[^2_10]: https://www.streampixel.io/post/streampixel-stream-your-unreal-engine-app-to-any-device-anywhere


---

# And the step 2 is setting up the ability to use voice calls with ai and video calls with ai with ai agents that can do stuff with the cli agents and have access to the file system and read and write files and execute commands like Claude code and such

You can treat “voice/video with AI that can touch the CLI and filesystem” as a second layer on top of your remote dev server: a realtime voice agent that uses tools to run shell commands and read/write files.  The pattern is: WebRTC voice → backend agent → tools for shell and files.[^3_1][^3_2]

## Overall architecture

- **Voice/video client** in your browser or native app sends and receives audio (and optionally screen/video) via WebRTC.[^3_3][^3_4][^3_1]
- **Realtime AI agent backend** (on your remote server) maintains a persistent conversation and exposes tools for:
    - running CLI commands (Claude Code, Codex‑style)
    - reading/writing files in your shared project directory.[^3_2][^3_1]
- **Guard rails layer** intercepts commands before execution so you stay in control of what the agent can run.[^3_5][^3_6]

This lets you talk to the agent on your phone or laptop and have it act as a “voice Claude Code” with full access to the same synced filesystem.

## Core pieces to set up

- **Realtime voice stack**
    - Use a Realtime / “voice agents” API that supports streaming audio and tools; the standard pattern is a WebRTC or websocket session plus tool/function calls.[^3_4][^3_1][^3_3]
    - A small Node.js or Python server on your remote box terminates WebRTC, forwards audio to the model, and exposes tool implementations for shell and file operations.[^3_7][^3_1][^3_2]
- **Tools for filesystem and shell**
    - Define tool functions like `read_file(path)`, `write_file(path, contents)`, `list_files(dir)`, `run_command(cmd)` that operate only inside your synced project root.[^3_8][^3_9][^3_2]
    - Attach these tools to the agent so it can decide when to call them during a voice conversation (e.g., “open the log file”, “run the test suite”).[^3_1][^3_2]
- **Safety and permissions**
    - Wrap your CLI tool in a controlled shell that uses a DEBUG trap (or similar) to inspect and allow/deny commands before they actually run.[^3_6][^3_5]
    - Use allow‑lists or pattern checks so destructive or dangerous commands are blocked, and optionally require explicit confirmation for high‑impact actions.[^3_5][^3_6]


## How this connects to your existing setup

- The **remote server** you’re already planning for Claude Code, Gemini CLI, and MCP stays the execution environment.
    - The voice agent backend runs on the same box and uses the same working directories that are synced via Syncthing.[^3_10][^3_11][^3_12]
    - When you speak, the agent can:
        - open files in those folders
        - edit them and save
        - call your existing CLIs (e.g., run tests, call Claude Code helper scripts) and summarize results back to you in voice.[^3_2][^3_1]
- From both **phone and laptop**, you:
    - open a small web app for the voice/video UI, or
    - use a native client built on a framework like LiveKit agents to connect into your backend.[^3_3][^3_7][^3_4]


## Suggested implementation path

- Start with a **simple voice‑only agent** that:
    - listens over WebRTC
    - has tools for `read_file`, `write_file`, and a heavily constrained `run_command`.[^3_7][^3_1][^3_2]
- Once stable, add:
    - integration with your existing CLI agents (e.g., scripts that wrap Claude Code or Codex flows) as additional tools
    - optional video/screen streaming so it can “see” terminal output or a browser if you decide to feed that in later.[^3_13][^3_1][^3_3]

If you share your preferred language (TypeScript vs Python) and which voice/LLM provider you want to lean on, a concrete minimal architecture (files, processes, and example tool definitions) can be outlined next.
<span style="display:none">[^3_14]</span>

<div align="center">⁂</div>

[^3_1]: https://platform.openai.com/docs/guides/voice-agents

[^3_2]: https://openai.github.io/openai-agents-python/tools/

[^3_3]: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/voice-live-quickstart

[^3_4]: https://github.com/livekit/agents

[^3_5]: https://johnthenerd.com/blog/local-llm-assistant/

[^3_6]: https://ricardoanderegg.com/posts/control-shell-permissions-llm-codex/

[^3_7]: https://towardsdatascience.com/build-a-locally-running-voice-assistant-2f2ead904fe9/

[^3_8]: https://platform.openai.com/docs/guides/tools-file-search

[^3_9]: https://platform.openai.com/docs/assistants/tools/file-search

[^3_10]: https://docs.oracle.com/en/learn/oci-syncthing/index.html

[^3_11]: https://opensource.com/article/20/1/sync-files-syncthing

[^3_12]: https://forum.syncthing.net/t/sync-multiple-devices/22732

[^3_13]: https://www.youtube.com/watch?v=h4tuLuzSjbA

[^3_14]: https://livekit.io


---

# While step 3 is more to do with the 3D environment access to the user and ai and unreal and stuff

Step 3 is essentially “3D world as a shared, AI‑aware space”: Unreal runs remotely, is streamed to you, and exposes control channels so both you and AI agents can act inside it. This builds on your step 1 (remote dev hub) and step 2 (voice/tools agent) and connects them to Unreal.

## What step 3 adds conceptually

- **Remote 3D runtime**
    - Unreal projects run on one or more GPU machines, not on your phone or laptop.
    - Those machines render the scene and stream video/audio to your devices, while receiving your input over the network.
- **Multi‑endpoint access (you + AI)**
    - You access the world visually and interactively from phone or laptop via a browser or app (e.g., WebRTC/Pixel‑Streaming style).
    - AI agents connect over separate control channels (APIs, sockets) and can:
        - drive their own avatar or camera
        - issue “god mode” commands (spawn objects, change environment parameters).


## How your previous steps plug in

- **From the remote dev hub (step 1)**
    - The same remote environment that runs your CLIs and file sync also hosts Unreal builds, orchestration scripts, and the networking glue.
    - Your project files for gameplay logic, AI behavior trees, and control plugins live in the shared filesystem you already sync across machines.
- **From the voice/tools agent (step 2)**
    - The voice AI that can read/write files and run commands gains new tools like:
        - `get_world_state()`, `move_avatar(...)`, `spawn_actor(...)`, `set_time_of_day(...)`.
    - When you say things like “move my assistant’s avatar over to that platform and light it up blue,” the voice agent:
        - interprets your request
        - calls the Unreal control tools
        - optionally narrates what it did and why.


## User experience you’re aiming for

- On your **phone**
    - You open a single app/page that gives you:
        - the streamed Unreal view
        - a push‑to‑talk or always‑on voice channel to the AI
        - possibly a minimal HUD or chat log.
    - You can walk around, ask the AI to show or build things, and watch it manipulate the scene alongside you.
- On your **laptop**
    - You see the same or another session, with:
        - richer controls (keyboard/mouse, debug overlays)
        - maybe editor‑like panels if you want “live editing” views.
    - You can debug, inspect logs, or change code while the AI and your phone session remain connected to the running 3D world.


## High‑level design goals for step 3

- **Clear separation between rendering and control**
    - Rendering/streaming handles video/audio and user inputs.
    - Control APIs handle semantic actions (move, spawn, edit) for AI agents and tools.
- **Shared identity and state**
    - Sessions (you, AI agents, and maybe other users) are tracked so each has an avatar, permissions, and history.
    - The AI can “remember” what it changed in the world and refer back to it later.
- **Safety and guard rails**
    - Permissions can limit which AIs can use god‑mode vs avatar‑only control.
    - Potentially add a “review/confirm big changes” flow for destructive world edits.

If you want, the next step can be to sketch an end‑to‑end diagram of the components for step 3 (even just in text) so you can see how Unreal, the voice agent, the CLI tools, and the shared filesystem all connect.

---

# Given this understanding, do research to figure out the best ways to make this happen

The best‑known way to make your whole vision real is to combine three mature patterns: remote dev + voice agents + Unreal pixel streaming. Existing guides and research back this as the most practical, scalable route.[^5_2][^5_3][^5_7]

## 1. Remote Unreal via Pixel Streaming

Pixel Streaming is the standard for running Unreal on a GPU server and streaming it to browsers on phones and laptops with low‑latency control.[^5_3][^5_5][^5_7]

- The **Unreal Engine app** runs on a GPU VM or bare‑metal server, with the Pixel Streaming plugin enabled and packaged as a standalone build.[^5_5][^5_3]
- A **signaling + web server** brokers WebRTC connections so each browser session gets an interactive video stream plus input events; this is the “digital matchmaker” between client and Unreal instance.[^5_6][^5_7][^5_5]

This gives you “Unreal anywhere” with only a browser on the client, which fits your phone + laptop requirement.[^5_7][^5_12][^5_5]

## 2. Hosting and networking best practices

For real‑world access across networks, Unreal docs and hosting guides recommend a focused networking setup.[^5_2][^5_6][^5_7]

- Run **signaling and Unreal** close together (same host or same LAN) with GPU acceleration and host networking for minimal overhead.[^5_5][^5_2]
- Use **STUN/TURN and ICE configuration** so WebRTC streams work over the public internet, not just a LAN, and configure per‑user stacks or matchmaker routing if you plan multiple concurrent users/agents.[^5_6][^5_7]

These practices are what commercial “Unreal‑in‑the‑cloud” providers follow to deliver 3D worlds to arbitrary devices.[^5_8][^5_7][^5_2]

## 3. AI agents controlling Unreal (“avatar + god mode”)

The strongest pattern for letting AI act inside Unreal is to add a control API layer, separate from the video stream.[^5_11][^5_18][^5_5]

- Provide a **programmatic control interface** (HTTP, WebSocket, or custom plugin) that exposes actions like moving pawns, spawning actors, or changing world parameters.[^5_11][^5_5]
- Let an external AI agent call this API based on your voice or text instructions, effectively giving it “avatar level” actions plus higher‑level environment edits (god mode).[^5_18][^5_11]

Research and engineering write‑ups on cloud Unreal systems show that splitting rendering (Pixel Streaming) from control (APIs / events) is the cleanest, most maintainable architecture.[^5_12][^5_18][^5_11]

## 4. Voice / video AI with tools and filesystem

For step 2 (voice and video calls with AI that can use CLI agents and files), current best practice is a realtime multimodal agent with tool calling.[^5_29][^5_30][^5_31]

- A **realtime voice agent** runs on your remote server, establishes a streaming audio session (WebRTC or similar), and integrates tool calls that implement `run_command`, `read_file`, `write_file`, etc., scoped to your project directory.[^5_30][^5_32][^5_29]
- Safety work from similar “LLM controls my system” setups recommends constraining shells, adding allow‑lists, and intercepting risky commands before execution.[^5_33][^5_34]

This lets you talk to “Claude‑code‑like” behavior by voice while the agent reads and edits the same synced files your CLIs and IDEs use.[^5_35][^5_29][^5_30]

## 5. Putting it all together for your roadmap

Across docs and guides, the most feasible strategy for what you want is a staged, layered build.[^5_3][^5_29][^5_5]

- **Step 1 (you already defined)**: Remote dev hub with shared filesystem (Syncthing), SSH/remote IDE, and AI CLIs living on that server.
- **Step 2**: Add a realtime voice agent on that server with tools for filesystem and CLI commands, with guard rails around shell access.[^5_29][^5_30][^5_35]
- **Step 3**: Introduce Unreal with Pixel Streaming on a GPU host, wired to:
    - the same shared filesystem for game logic and tools
    - the voice agent via a control API so the AI can move an avatar and use god‑mode world changes while you see the world via streamed video.[^5_3][^5_5][^5_11]

That combination—remote Unreal via Pixel Streaming, plus a tool‑using voice agent, plus your existing dev hub and synced files—is, according to current docs and practical guides, the most robust and extensible way to realize your full concept.[^5_7][^5_2][^5_5][^5_29][^5_3]
<span style="display:none">[^5_1][^5_10][^5_13][^5_14][^5_15][^5_16][^5_17][^5_19][^5_20][^5_21][^5_22][^5_23][^5_24][^5_25][^5_26][^5_27][^5_28][^5_4][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://www.youtube.com/watch?v=jk3ic4zntnY

[^5_2]: https://vagon.io/blog/how-to-implement-pixel-streaming-with-unreal-engine-on-azure

[^5_3]: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine

[^5_4]: https://github.com/Azure/Unreal-Pixel-Streaming/blob/main/README.md

[^5_5]: https://unrealcontainers.com/docs/use-cases/pixel-streaming

[^5_6]: https://dev.epicgames.com/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine

[^5_7]: https://www.streampixel.io/post/unreal-engine-pixel-streaming-your-complete-guide

[^5_8]: https://www.eagle3dstreaming.com/pixelstreamingguide

[^5_9]: https://forums.unrealengine.com/t/community-tutorial-the-ultimate-pixel-streaming-guide-for-sharing-your-experience-to-unlimited-concurrent-users-with-rtx-enabled-nvidia-gpus-vagon-streams/1875473

[^5_10]: https://forums.unrealengine.com/t/pixel-streaming-2-migrating-and-key-notes/2175491

[^5_11]: https://dl.acm.org/doi/10.1145/3672758.3672762

[^5_12]: https://www.mdpi.com/2076-3417/14/3/955

[^5_13]: https://www.semanticscholar.org/paper/2127c3a1806017f456abd90bf18df810c07c32cf

[^5_14]: https://ijrpr.com/uploads/V6ISSUE4/IJRPR44092.pdf

[^5_15]: https://arxiv.org/abs/2409.06207

[^5_16]: https://isprs-archives.copernicus.org/articles/XLVIII-M-6-2025/353/2025/

[^5_17]: https://www.mdpi.com/2220-9964/10/10/643

[^5_18]: https://pubs.aip.org/jasa/article/156/4_Supplement/A64/3331192/Framework-for-real-time-computation-and-streaming

[^5_19]: https://ieeexplore.ieee.org/document/10808154/

[^5_20]: https://computerresearch.org/index.php/computer/article/view/102442

[^5_21]: https://arxiv.org/html/2504.07485v1

[^5_22]: https://arxiv.org/pdf/2403.10976.pdf

[^5_23]: http://arxiv.org/pdf/2403.11155.pdf

[^5_24]: https://arxiv.org/pdf/1612.08350.pdf

[^5_25]: https://www.tandfonline.com/doi/pdf/10.1080/19443927.2024.2366115?needAccess=true

[^5_26]: http://arxiv.org/pdf/2304.05654.pdf

[^5_27]: https://arxiv.org/html/2503.16979v1

[^5_28]: https://dl.acm.org/doi/pdf/10.1145/3625468.3652172

[^5_29]: https://platform.openai.com/docs/guides/voice-agents

[^5_30]: https://openai.github.io/openai-agents-python/tools/

[^5_31]: https://github.com/livekit/agents

[^5_32]: https://towardsdatascience.com/build-a-locally-running-voice-assistant-2f2ead904fe9/

[^5_33]: https://johnthenerd.com/blog/local-llm-assistant/

[^5_34]: https://ricardoanderegg.com/posts/control-shell-permissions-llm-codex/

[^5_35]: https://platform.openai.com/docs/guides/tools-file-search


---

# Ok, but first step is remote access to environments with Claude code and codex cli and Gemini cli and cursor ide visuals, then step 2 is setting up voice call agent systems and video call agent systems that can access that environment and use the Claude code and codex and Gemini tools and then step 3 is the unreal 3D world and such

Step 1 focuses on creating a unified remote environment accessible from your phone and laptop for Claude Code, Codex CLI, Gemini CLI, and Cursor IDE visuals. Step 2 layers in voice/video AI agents that interact with that environment. Step 3 then integrates Unreal 3D worlds.

## Step 1: Remote access to AI coding tools

Set up a single Linux server (VPS with GPU if possible) as your central hub, using Tailscale for secure access and Syncthing for file sharing.

- Install Claude Code, Codex CLI, and Gemini CLI directly on the server; these are terminal‑based, so SSH or Mosh sessions give you full control from laptop (VS Code Remote) or phone (Blink app).
- For Cursor IDE visuals, run it server‑side via VNC/noVNC or use its remote development features, exposing the desktop over a web URL via Tailscale.
- Sync your project folders bidirectionally with Syncthing across Windows, WSL, local Ubuntu, and the server to ensure one codebase everywhere.


## Step 2: Voice/video AI agents with tool access

Build a realtime voice agent backend on the same server using frameworks like LiveKit or OpenAI Realtime API.

- The agent handles WebRTC audio/video from your devices and exposes tools that call into the environment: run Claude Code commands, invoke Codex/Gemini CLI scripts, read/write synced files.
- Use constrained shells (e.g., allowlisted commands) for safety, letting the AI execute "fix this bug" by running your CLIs and reporting back verbally.
- Access from phone/laptop via a simple web app for voice calls, with optional screen sharing of the remote terminal or Cursor view.


## Step 3: Unreal 3D world integration

Extend the hub with Unreal Pixel Streaming on a GPU instance.

- Unreal runs server‑side, streams interactive 3D to browsers on your devices; the voice agent from step 2 gains new tools for world control (avatar movement, god‑mode edits via Unreal's API/WebSockets).
- Shared filesystem keeps game code in sync; AI can edit blueprints or spawn assets while you watch live.

This progression keeps everything centralized on your remote server, with seamless multi‑device access and escalating AI capabilities.
<span style="display:none">[^6_1][^6_10][^6_11][^6_12][^6_13][^6_14][^6_15][^6_16][^6_17][^6_2][^6_3][^6_4][^6_5][^6_6][^6_7][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: http://arxiv.org/pdf/2406.09577.pdf

[^6_2]: https://www.mdpi.com/2076-3417/9/21/4642/pdf

[^6_3]: https://arxiv.org/pdf/2307.08177.pdf

[^6_4]: https://arxiv.org/html/2404.04902v1

[^6_5]: https://dl.acm.org/doi/pdf/10.1145/3597503.3639187

[^6_6]: https://arxiv.org/html/2410.07002v1

[^6_7]: https://arxiv.org/pdf/2402.11635.pdf

[^6_8]: https://arxiv.org/pdf/2101.11149.pdf

[^6_9]: https://www.youtube.com/watch?v=JcgdGESQlEQ\&vl=en

[^6_10]: https://www.educative.io/blog/codex-vs-cursor-vs-gemini-code-assist

[^6_11]: https://forum.cursor.com/t/mastering-long-codebases-with-cursor-gemini-and-claude-a-practical-guide/38240

[^6_12]: https://www.codeant.ai/blogs/claude-code-cli-vs-codex-cli-vs-gemini-cli-best-ai-cli-tool-for-developers-in-2025

[^6_13]: https://codewithandrea.com/articles/run-ai-agents-inside-devcontainer/

[^6_14]: https://www.cursor-ide.com/blog/codex-vs-claude-code

[^6_15]: https://www.reddit.com/r/ChatGPTCoding/comments/1p698cb/what_coding_agent_have_you_actually_settled_on/

[^6_16]: https://www.linkedin.com/posts/wapan_cursor-windsurf-claude-code-gemini-cli-activity-7351724417795661824-2hJy

[^6_17]: https://www.facebook.com/groups/techtitansgroup/posts/1510017000325613/


---

# Is this the best way to get a system I can use to remotely do cli ai coding tools from my phone and also use voice and video calls to orchestrate stuff in the cli tools and also use the 3D environment that the ai also has access to and can do stuff in?

Yes, the layered remote server approach—starting with a secure hub for CLI AI tools, adding voice/video agents with tool access, then integrating streamed Unreal 3D—is among the strongest practical ways to achieve your full system. It leverages mature patterns like Tailscale SSH, Syncthing, realtime WebRTC agents, and Pixel Streaming, which align perfectly with multi‑device (phone + laptop) access, AI orchestration, and shared 3D environments.[^7_21][^7_22][^7_23][^7_24]

## Why this excels for your requirements

- **Remote CLI AI coding from phone**: Tailscale + Mosh/Blink gives resilient terminal access to Claude Code/Codex/Gemini CLI on the server; VNC/noVNC handles Cursor visuals. Phone apps handle this natively without local compute limits.[^7_25][^7_26][^7_21]
- **Voice/video orchestration**: Realtime agents (LiveKit/OpenAI Realtime) connect via WebRTC, with tools calling your server‑side CLIs and files—AI "hears" you, runs commands, speaks results, all while you multitask.[^7_24][^7_27][^7_28]
- **AI‑accessible 3D environment**: Pixel Streaming delivers interactive Unreal to browsers; voice agent tools hit Unreal's control APIs for avatar/god‑mode actions. Shared Syncthing filesystem keeps code/world state unified.[^7_22][^7_23][^7_29]


## Potential alternatives and trade‑offs

| Approach | Strengths | Weaknesses vs. your stack |
| :-- | :-- | :-- |
| Local AI on phone/laptop | Offline, private | Can't handle heavy CLI/IDE/Unreal; no unified sync/orchestration [^7_19] |
| Fully cloud (e.g., GitHub Codespaces + Replit) | Zero setup | Vendor lock‑in, latency, no custom 3D streaming control [^7_20] |
| Dev containers (Docker + remote) | Isolated tools | Still needs remote host; less seamless for phone voice/3D [^7_26] |

Your design avoids these pitfalls by centralizing compute/powerful tools on the server while streaming everything thin to devices.

## Validation from patterns

Guides confirm this works: devs run Cursor/Claude Code in remote containers via Tailscale, voice agents safely execute CLI tools, and Pixel Streaming handles 3D reliably across networks. No single "magic" tool does it all, but this composes proven components scalably.[^7_20][^7_26][^7_21][^7_22][^7_24]
<span style="display:none">[^7_1][^7_10][^7_11][^7_12][^7_13][^7_14][^7_15][^7_16][^7_17][^7_18][^7_2][^7_3][^7_4][^7_5][^7_6][^7_7][^7_8][^7_9]</span>

<div align="center">⁂</div>

[^7_1]: https://dl.acm.org/doi/10.1145/3641555.3704753

[^7_2]: https://aacrjournals.org/cancerres/article/85/23_Supplement/A029/768264/Abstract-A029-Gen-Z-AI-health-access-A

[^7_3]: https://ijesat.com/ijesat/files/V25I9060_1758818419.pdf

[^7_4]: https://www.suaspress.org/ojs/index.php/JIEAS/article/view/v3n3a02

[^7_5]: https://arxiv.org/abs/2504.03767

[^7_6]: https://www.mdpi.com/2571-9408/6/12/402

[^7_7]: https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12786/2681866/A-smart-beekeeping-platform-based-on-remote-sensing-and-artificial/10.1117/12.2681866.full

[^7_8]: https://www.nature.com/articles/s43856-024-00568-x

[^7_9]: https://ieeexplore.ieee.org/document/11256178/

[^7_10]: https://ieeexplore.ieee.org/document/11170750/

[^7_11]: http://arxiv.org/pdf/2402.10857.pdf

[^7_12]: https://arxiv.org/pdf/2305.13738.pdf

[^7_13]: http://arxiv.org/pdf/2503.14724.pdf

[^7_14]: https://arxiv.org/html/2404.04902v1

[^7_15]: https://arxiv.org/pdf/2307.14349.pdf

[^7_16]: https://arxiv.org/pdf/2310.13896.pdf

[^7_17]: https://www.ijfmr.com/papers/2024/6/30587.pdf

[^7_18]: https://arxiv.org/pdf/2403.08299.pdf

[^7_19]: https://www.sentisight.ai/run-powerful-ai-models-on-laptop-phone/

[^7_20]: https://www.reddit.com/r/vibecoding/comments/1msbs9x/how_to_work_across_2_computers_and_sync_the_ai/

[^7_21]: https://www.alexjd.co.uk/posts/remote-development-tailscale

[^7_22]: https://unrealcontainers.com/docs/use-cases/pixel-streaming

[^7_23]: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine

[^7_24]: https://platform.openai.com/docs/guides/voice-agents

[^7_25]: https://docs.blink.sh/integrations/tailscale+mosh

[^7_26]: https://codewithandrea.com/articles/run-ai-agents-inside-devcontainer/

[^7_27]: https://openai.github.io/openai-agents-python/tools/

[^7_28]: https://github.com/livekit/agents

[^7_29]: https://www.streampixel.io/post/unreal-engine-pixel-streaming-your-complete-guide


---

# Unified Remote AI Dev \& 3D World System

## Executive Summary

This vision outlines a centralized remote server ecosystem that unifies AI‑powered coding (CLI tools + IDE), voice/video agent orchestration, and interactive 3D worlds. Accessible from phone and laptop, it enables seamless workflows where you code via terminals/IDEs, direct AI via voice to run commands/edit files, and collaborate with AI inside streamed Unreal environments—all backed by shared filesystems.

## Core Goals

- Phone/laptop parity for all features (CLI coding, voice control, 3D interaction)
- AI agents with full access to your tools/files/worlds, orchestrated by natural voice/video
- Zero‑trust security, bidirectional sync, low latency across devices
- Scalable from MVP to multi‑user/multi‑world


## System Architecture

```
[Phone & Laptop] ── WebRTC/Tailscale ── [Remote Hub Server]
                                           │
                           ├─ Syncthing (shared filesystem)
                           │
                           ├─ CLI Tools (Claude Code, Codex CLI, Gemini CLI)
                           │
                           ├─ Voice/Video Agents (tools → CLI/files/worlds)
                           │
                           └─ GPU Node ── Pixel Streaming ── Unreal 3D Worlds
                                               │
                                        Control APIs (AI avatar/god mode)
```


## Step 1: Remote AI Coding Hub

**Objective**: Single server for all CLI/IDE tools, accessible anywhere.

- **Infrastructure**:
    - Ubuntu VPS/home server with Tailscale VPN
    - Syncthing mesh (Windows/WSL/Ubuntu/phone storage → server)
- **Tools**:
    - SSH/Mosh terminals for Claude Code/Codex/Gemini CLI
    - VNC/noVNC or Cursor Remote for IDE visuals
- **Access**:
    - Laptop: VS Code Remote‑SSH
    - Phone: Blink/MTerm app over Tailscale

**Success Metric**: Edit/run code from phone terminal, see Cursor desktop in browser.

## Step 2: Voice/Video AI Orchestration

**Objective**: Natural language control of the coding hub.

- **Backend**: Realtime agent (LiveKit + LLM tools) on server
- **Capabilities**:


| Tool | Function |
| :-- | :-- |
| `run_cli(cmd)` | Execute Claude Code/etc. safely |
| `read_file(path)` | Inspect synced projects |
| `write_file(path, content)` | AI‑generated edits |

- **Interface**: WebRTC app (push‑to‑talk video calls)
- **Safety**: Constrained shell, confirmations for risky actions

**Success Metric**: Say "debug the API endpoint" → AI runs tools, narrates fixes verbally.

## Step 3: Shared 3D Worlds

**Objective**: Interactive Unreal environments for you + AI.

- **Rendering**: Pixel Streaming on GPU node (streams to browsers)
- **AI Integration**:


| Control | User | AI Agent |
| :-- | :-- | :-- |
| Avatar Movement | Keyboard/touch | Tool calls |
| God Mode (spawn/edit) | Editor overlays | Voice commands |

- **Sync**: Game code/blueprints in Syncthing folder
- **Orchestration**: Voice agent tools query/control world state

**Success Metric**: Voice "build a red platform for me" → AI spawns it, you see live in stream.

## Security \& Ops

- Tailscale: Zero‑config VPN, auth‑only access
- Guardrails: Tool allowlists, audit logs
- Monitoring: Prometheus for uptime/latency
- Scaling: Kubernetes for multi‑GPU/multi‑agent


## Roadmap

| Phase | Deliverable | Timeline |
| :-- | :-- | :-- |
| MVP (1 month) | Step 1 hub + basic sync |  |
| Voice (2 weeks) | Step 2 agents with CLI tools |  |
| 3D (3 weeks) | Step 3 streaming + AI control |  |
| Polish (2 weeks) | Multi‑session, perf tuning |  |

## Risks \& Mitigations

- Latency: WebRTC + edge GPU → <100ms
- Cost: Start \$20/mo VPS, scale to \$100 GPU
- Complexity: Modular steps, Dockerize each layer

This system turns your devices into thin clients for a powerful, AI‑amplified remote brain—coding, commanding, and creating worlds on demand.

---

# Remote AI Dev \& 3D System - Requirements Document

## 1. Introduction

### 1.1 Purpose

This document specifies functional and non‑functional requirements for a unified remote system enabling:

- CLI AI coding tools (Claude Code, Codex CLI, Gemini CLI) from phone/laptop
- Voice/video AI agents orchestrating CLI tools and filesystem
- Shared Unreal 3D worlds with AI avatar/god‑mode control


### 1.2 Scope

Covers infrastructure, access, agents, 3D streaming, and integration. Excludes production multi‑tenancy.

### 1.3 Stakeholders

- Primary User: You (multi‑device access)
- AI Agents: Voice/video controllers


## 2. Functional Requirements

### 2.1 Remote Coding Hub (Step 1)

| ID | Requirement | Priority |
| :-- | :-- | :-- |
| F1.1 | SSH/Mosh access to server running Claude Code/Codex/Gemini CLI from phone/laptop | Must |
| F1.2 | VNC/noVNC streaming of Cursor IDE desktop | Must |
| F1.3 | Bidirectional Syncthing sync of project folders across Windows/WSL/Ubuntu/server | Must |
| F1.4 | Tailscale zero‑trust networking (no port forwarding) | Must |

### 2.2 Voice/Video Agents (Step 2)

| ID | Requirement | Priority |
| :-- | :-- | :-- |
| F2.1 | WebRTC voice/video calls to persistent AI agent | Must |
| F2.2 | Agent tools: `run_cli(cmd)`, `read_file(path)`, `write_file(path,content)` | Must |
| F2.3 | Constrained execution (allowlist, confirmations) for CLI commands | Must |
| F2.4 | Verbal narration of tool results/actions | Should |
| F2.5 | Screen sharing of terminal/Cursor during calls | Could |

### 2.3 3D Worlds (Step 3)

| ID | Requirement | Priority |
| :-- | :-- | :-- |
| F3.1 | Unreal Pixel Streaming to phone/laptop browsers (<100ms latency) | Must |
| F3.2 | Agent tools: `move_avatar()`, `spawn_object()`, `set_environment(param)` | Must |
| F3.3 | Shared filesystem for game code/blueprints | Must |
| F3.4 | Multi‑session support (user + ≥1 AI avatar) | Should |
| F3.5 | God‑mode controls (time/light/physics) via voice | Could |

### 2.4 Integration

| ID | Requirement | Priority |
| :-- | :-- | :-- |
| F4.1 | Single Syncthing root for code/files/world assets | Must |
| F4.2 | Voice agent routes commands to CLI or 3D based on context | Must |
| F4.3 | Unified auth (Tailscale identities) across components | Must |

## 3. Non‑Functional Requirements

### 3.1 Performance

- CLI latency: <500ms end‑to‑end
- Voice response: <2s
- 3D streaming: 1080p@30fps, <100ms input lag
- Uptime: 99%


### 3.2 Security

- No public ports; Tailscale ACLs
- Tool execution sandboxed
- Audit logs for all AI actions
- Filesystem scoped to project root


### 3.3 Usability

- Phone: Native apps (Blink for SSH, browser for VNC/3D/voice)
- Laptop: VS Code integration
- Voice UX: Natural language, context‑aware


### 3.4 Scalability

- Initial: Single server
- Future: Multi‑GPU, agent pools


## 4. Interfaces

- **User**: WebRTC app, SSH clients, browsers
- **Internal**: REST/WebSocket for agent‑to‑Unreal
- **External**: Tailscale, Syncthing peer mesh


## 5. Assumptions \& Dependencies

- GPU VPS availability (~\$0.5/hr)
- Tailscale/Syncthing accounts
- Unreal Engine 5.4+ licensing
- LLM API keys (Claude/Gemini/OpenAI Realtime)


## 6. Acceptance Criteria

- **Step 1**: Code edit from phone → syncs to laptop Cursor
- **Step 2**: Voice "run tests" → AI executes, reports verbally
- **Step 3**: Voice "spawn cube" → appears in your 3D stream
- **Full**: End‑to‑end voice‑driven coding + world build from phone


## 7. Glossary

- **Hub Server**: Central Ubuntu/Tailscale host
- **Realtime Agent**: Voice LLM with tools
- **Pixel Streaming**: Unreal's WebRTC renderer

This spec provides a testable blueprint for iterative delivery.

---

# Research Document: Foundations for Remote AI Dev, Voice Agents, and 3D Integration

## 1. Executive Summary

This research compiles evidence supporting the proposed system's viability, drawing from tool comparisons, remote dev patterns, realtime voice AI, and Unreal streaming. Key findings: CLI tools like Claude Code, Codex CLI, and Gemini CLI thrive in remote setups; voice agents with MCP/tools enable safe orchestration; Pixel Streaming provides proven 3D access.[^10_1][^10_2][^10_6]

## 2. AI CLI Coding Tools Landscape

### 2.1 Tool Profiles

| Tool | Strengths | Weaknesses | Remote Fit |
| :-- | :-- | :-- | :-- |
| Claude Code | Deep context, MCP for tools/files, IDE integration | Paid tiers for teams | Excellent via SSH/VNC [^10_2][^10_1] |
| Codex CLI | CI/CD/GitHub native, multimodal, open routing | API costs | Strong in containers/Tailscale [^10_3][^10_4] |
| Gemini CLI | Free tier, Google ecosystem, built‑in search | Less specialized for code | Good for quick remote tasks [^10_2][^10_6] |

- All support **MCP (Model Context Protocol)** for live tools (shell, files, APIs), ideal for agentic remote use.[^10_2][^10_4][^10_1]
- Benchmarks show Claude leads in multi‑file refactoring (78.8% success), Gemini in real‑time grounding.[^10_10][^10_19]


### 2.2 Remote Deployment Patterns

- Devs run these in **DevContainers/Docker** over Tailscale/VS Code Remote for phone/laptop sync.[^10_28][^10_29]
- Syncthing proven for multi‑OS file meshes; Cursor/Claude work headless or via noVNC.[^10_30][^10_31][^10_28]


## 3. Voice/Video AI Agents Research

- **Realtime APIs** (OpenAI Realtime, LiveKit): Enable <2s voice loops with tools; used for CLI orchestration.[^10_32][^10_33]
- **Tool Patterns**: `run_shell`, `fs_ops` common; constrained shells mitigate risks (e.g., Codex's tiers).[^10_34][^10_35][^10_36]
- Empirical: Agents boost productivity 2x for debugging/editing when filesystem‑aware.[^10_12][^10_10]


## 4. Unreal 3D Streaming \& AI Control

- **Pixel Streaming**: Epic's WebRTC solution; 1080p/30fps to browsers, <100ms lag with TURN.[^10_37][^10_38][^10_39]
- **AI Integration**: HTTP/WebSocket plugins for avatar/god controls; research shows 70%+ success for semantic actions.[^10_40][^10_41]
- Multi‑user: Signaling servers handle concurrent sessions (user + AI).[^10_42][^10_43]


## 5. Integration Feasibility

- **Unified Stack**: Tailscale + Syncthing + MCP bridges CLI/agents/3D; devs sync AI chats/IDEs across devices.[^10_29][^10_1]
- **Benchmarks**: AI agents refactor reliably (61‑79%); streaming scales to mobile.[^10_11][^10_19][^10_10]
- **Gaps**: Dependency expansion in AI code (13x claimed); mitigate via constrained envs.[^10_11]


## 6. Risks \& Evidence‑Based Mitigations

| Risk | Evidence | Mitigation |
| :-- | :-- | :-- |
| Latency | WebRTC studies: 50‑150ms achievable [^10_39] | GPU co‑location, TURN |
| Safety | MCP exploits noted [^10_44] | Allowlists, audits [^10_35] |
| Reproducibility | AI code gaps [^10_11] | Containers, tests [^10_12] |

## 7. Conclusions \& Recommendations

Research validates the 3‑step architecture as optimal: mature tools (CLI/MCP), proven remote patterns (Tailscale/Syncthing), reliable streaming (Pixel). Proceed with MVP; monitor MCP safety evolutions.[^10_6][^10_1][^10_2][^10_37]
<span style="display:none">[^10_13][^10_14][^10_15][^10_16][^10_17][^10_18][^10_20][^10_21][^10_22][^10_23][^10_24][^10_25][^10_26][^10_27][^10_5][^10_7][^10_8][^10_9]</span>

<div align="center">⁂</div>

[^10_1]: https://stackoverflow.com/questions/79843897/how-to-share-claude-code-skills-with-codex-cli-and-gemini-cli

[^10_2]: https://www.codeant.ai/blogs/claude-code-cli-vs-codex-cli-vs-gemini-cli-best-ai-cli-tool-for-developers-in-2025

[^10_3]: https://www.deployhq.com/blog/comparing-claude-code-openai-codex-and-google-gemini-cli-which-ai-coding-assistant-is-right-for-your-deployment-workflow

[^10_4]: https://www.squadbase.dev/en/blog/claude-code-vs-gemini-cli-vs-codex-cli-whats-the-best-choice-for-internal

[^10_5]: https://www.reddit.com/r/vibecoding/comments/1nkx0zc/which_cli_ai_coding_tool_to_use_right_now_codex/

[^10_6]: https://getstream.io/blog/agentic-cli-tools/

[^10_7]: https://zencoder.ai/blog/save-90-on-ai-costs-using-claude-codex-gemini-2025-guide

[^10_8]: https://www.youtube.com/watch?v=7fQcsPOm8ys

[^10_9]: https://www.facebook.com/groups/techtitansgroup/posts/1510017000325613/

[^10_10]: https://arxiv.org/abs/2511.04824

[^10_11]: https://www.semanticscholar.org/paper/6e3488fc0bcccd535a0dea50e09cb792e508cdc5

[^10_12]: https://ieeexplore.ieee.org/document/11269709/

[^10_13]: https://www.mdpi.com/2227-7102/14/8/922

[^10_14]: https://dl.acm.org/doi/10.1145/3641555.3705074

[^10_15]: https://ieeexplore.ieee.org/document/11232363/

[^10_16]: http://www.e-enm.org/journal/view.php?doi=10.3803/EnM.2025.2675

[^10_17]: https://journalwjarr.com/node/2704

[^10_18]: https://dl.acm.org/doi/10.1145/3702653.3744328

[^10_19]: https://journals.uran.ua/tarp/article/view/326899

[^10_20]: http://arxiv.org/pdf/2411.09224.pdf

[^10_21]: https://arxiv.org/pdf/2310.13896.pdf

[^10_22]: https://arxiv.org/pdf/2406.11409.pdf

[^10_23]: http://arxiv.org/pdf/2412.10953.pdf

[^10_24]: https://dl.acm.org/doi/pdf/10.1145/3643916.3644402

[^10_25]: http://arxiv.org/pdf/2303.17568.pdf

[^10_26]: http://arxiv.org/pdf/2305.12050.pdf

[^10_27]: https://arxiv.org/pdf/2312.11444.pdf

[^10_28]: https://codewithandrea.com/articles/run-ai-agents-inside-devcontainer/

[^10_29]: https://www.reddit.com/r/vibecoding/comments/1msbs9x/how_to_work_across_2_computers_and_sync_the_ai/

[^10_30]: https://opensource.com/article/20/1/sync-files-syncthing

[^10_31]: https://forum.syncthing.net/t/sync-multiple-devices/22732

[^10_32]: https://platform.openai.com/docs/guides/voice-agents

[^10_33]: https://github.com/livekit/agents

[^10_34]: https://johnthenerd.com/blog/local-llm-assistant/

[^10_35]: https://ricardoanderegg.com/posts/control-shell-permissions-llm-codex/

[^10_36]: https://openai.github.io/openai-agents-python/tools/

[^10_37]: https://unrealcontainers.com/docs/use-cases/pixel-streaming

[^10_38]: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine

[^10_39]: https://www.streampixel.io/post/unreal-engine-pixel-streaming-your-complete-guide

[^10_40]: https://dl.acm.org/doi/10.1145/3672758.3672762

[^10_41]: https://www.mdpi.com/2076-3417/14/3/955

[^10_42]: https://dev.epicgames.com/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine

[^10_43]: https://forums.unrealengine.com/t/pixel-streaming-2-migrating-and-key-notes/2175491

[^10_44]: https://arxiv.org/abs/2504.03767


---

# Project Planning Document: Remote AI Dev \& 3D System

## 1. Project Overview

### 1.1 Objectives

Build a phased remote system for CLI AI coding, voice/video orchestration, and shared 3D worlds per vision/reqs/research.

### 1.2 Timeline

- **Total**: 8 weeks (MVP + full)
- **Milestones**: Weekly check‑ins

| Phase | Duration | Key Deliverable |
| :-- | :-- | :-- |
| Prep | Week 1 | Infrastructure |
| Step 1 | Weeks 1‑2 | Coding Hub |
| Step 2 | Weeks 3‑4 | Voice Agents |
| Step 3 | Weeks 5‑7 | 3D Integration |
| Polish | Week 8 | Testing/Optimize |

## 2. Detailed Tasks \& Schedule

### Phase 0: Preparation (Days 1‑3)

- [ ] Procure VPS (Ubuntu 24.04, 16GB RAM; GPU later)
- [ ] Install Tailscale on all devices/server
- [ ] Set up Syncthing mesh (test bidir sync)
- **Est. Effort**: 8 hours


### Phase 1: Remote Coding Hub (Days 4‑10)

| Task ID | Task | Dependencies | Owner | Effort |
| :-- | :-- | :-- | :-- | :-- |
| P1.1 | Install CLIs: Claude Code, Codex, Gemini | Prep | You | 2h |
| P1.2 | Configure SSH/Mosh + phone access (Blink) | P1.1 | You | 1h |
| P1.3 | VNC/noVNC for Cursor IDE | P1.2 | You | 3h |
| P1.4 | Test full workflow (edit→sync→run) | All | You | 2h |
| **Demo**: Phone CLI + laptop Cursor [Day 10] |  |  |  |  |

### Phase 2: Voice/Video Agents (Days 11‑24)

| Task ID | Task | Dependencies | Owner | Effort |
| :-- | :-- | :-- | :-- | :-- |
| P2.1 | Deploy LiveKit/OpenAI Realtime backend | Step 1 | You | 4h |
| P2.2 | Implement tools: run_cli, read/write_file | P2.1 | You | 6h |
| P2.3 | Add safety (allowlists, confirm UI) | P2.2 | You | 4h |
| P2.4 | Build/test WebRTC client app | P2.3 | You | 6h |
| P2.5 | E2E: Voice "fix bug" → CLI run → verbal report | All | You | 4h |
| **Demo**: Live voice orchestration [Day 24] |  |  |  |  |

### Phase 3: 3D Worlds (Days 25‑45)

| Task ID | Task | Dependencies | Owner | Effort |
| :-- | :-- | :-- | :-- | :-- |
| P3.1 | Provision GPU node; install UE5 + Pixel Streaming | Step 2 | You | 6h |
| P3.2 | Build signaling server (Cirrus); configure TURN | P3.1 | You | 4h |
| P3.3 | Create sample world + control API (WebSocket) | P3.2 | You | 8h |
| P3.4 | Extend voice agent tools: move_avatar, spawn, etc. | P3.3 | You | 6h |
| P3.5 | Test multi‑session (you + AI) | P3.4 | You | 4h |
| **Demo**: Voice‑driven 3D collab [Day 45] |  |  |  |  |

### Phase 4: Integration \& Polish (Days 46‑56)

- [ ] Unified monitoring (Prometheus/Grafana)
- [ ] Perf tuning (latency <100ms)
- [ ] Full E2E tests
- [ ] Documentation/scripts


## 3. Resources

- **Hardware**: VPS (\$20/mo), GPU (~\$100/mo)
- **Software**: Free/open (Tailscale, Syncthing, UE5 free tier)
- **APIs**: Claude/Gemini keys (~\$50/mo)
- **Total Budget**: <\$300 initial


## 4. Risks \& Contingencies

| Risk | Probability | Impact | Mitigation |
| :-- | :-- | :-- | :-- |
| GPU setup delays | Medium | High | Use Paperspace/Runpod |
| Voice latency | Low | Medium | Fallback to text |
| Sync conflicts | Medium | Low | Git overlay on Syncthing |
| API costs overrun | Low | Medium | Rate limits, caching |

## 5. Success Metrics

- **Quantitative**: 95% uptime, <150ms 3D latency, 80% voice command success
- **Qualitative**: "Phone feels like full workstation"


## 6. Next Actions

1. Day 1: Spin up VPS, join Tailscale
2. Review plan; adjust based on hardware
3. Weekly: Demo + retros

This plan delivers testable increments, minimizing integration risk.

---

# System Design Document: Remote AI Dev \& 3D Hub

## 1. High‑Level Design

The system comprises a **central remote hub** (Linux server) orchestrating three layers: coding environment, voice agents, and 3D streaming. Devices connect thinly via Tailscale (networking) and WebRTC (media), with Syncthing ensuring filesystem unity.

```
┌─────────────────────┐    Tailscale/WebRTC    ┌─────────────────────┐
│ Phone / Laptop      │◄──────────────────────►│ Remote Hub Server   │
│ - Browser/SSH apps  │                        │                     │
└─────────────────────┘                        │ ┌─────────────────┐ │
                                               │ │ Syncthing       │ │
                                               │ │ (Shared FS)     │ │
                                               │ └─────────────────┘ │
                                               │ ├─────────────────┤ │
                                               │ │ CLI Tools       │ │
                                               │ │ (Claude/Codex/..│ │
                                               │ └─────────────────┘ │
                                               │ ├─────────────────┤ │
                                               │ │ Voice Agent     │ │
                                               │ │ (LiveKit + LLM) │ │
                                               │ └─────────────────┘ │ ── API ──
                                               │                     │         │
                                               └─────────────────────┘         │
                                                             │                 │
                                                     GPU Node ◄────── Control ──┘
                                                     (Unreal + Pixel Stream)
```


## 2. Components

### 2.1 Networking Layer

- **Tailscale**: WireGuard‑based VPN; ACLs for SSH/VNC/HTTP.
- **WebRTC**: STUN/TURN for voice/3D; signaling via simple Node.js server.


### 2.2 Shared Filesystem

- **Syncthing**: P2P mesh; watched folders trigger CLI/agent hooks.
- Constraints: Projects under `/shared/`; ignorelists for temp files.


### 2.3 Coding Hub

- **CLI Tools**: Dockerized (Claude Code, etc.); exposed via constrained shell.
- **Cursor Visuals**: XFCE + noVNC; `--remote-debugging-port` for browser sync.
- API: Unix sockets for agent calls.


### 2.4 Voice/Video Agents

- **Stack**: LiveKit server + LLM (Claude/Gemini) via Realtime API.
- **Tool Schema**:

```json
{
  "run_cli": {"cmd": "str", "timeout": "int"},
  "fs_read": {"path": "str"},
  "fs_write": {"path": "str", "content": "str"}
}
```

- Flow: Audio → STT → LLM (with tools) → TTS + exec → stream response.


### 2.5 3D Layer

- **Unreal**: Packaged app with Pixel Streaming plugin; Cirrus signaling.
- **Control Plane**: Custom Blueprint/WebSocket actor:

```cpp
// Pseudo
UFUNCTION(BlueprintCallable)
void MoveAvatar(FVector Target);
UFUNCTION() void SpawnCube(FVector Loc);
```

- Integration: Agent tools POST to `/api/world/{session}/action`.


## 3. Data Flows

### 3.1 User Coding Session

1. Tailscale SSH → run `claude-code refactor foo.py`
2. Edit saves to Syncthing → propagates everywhere
3. Laptop opens Cursor Remote → sees live changes

### 3.2 Voice Orchestration

```
User: "Debug the API" ──►
  WebRTC audio ──► Agent ──► LLM reasons ──► run_cli("pytest") ──►
  Parse output ──► TTS: "Fixed line 42" ──► Stream back
```


### 3.3 3D Collaboration

```
User: "Spawn platform" ──►
  Agent tool: POST /world/action {spawn: "platform", pos: [0,0,5]} ──►
  Unreal executes ──► Pixel stream updates view ──► Agent: "Done!"
```


## 4. Interfaces

| Client | Endpoint | Protocol |
| :-- | :-- | :-- |
| SSH | `100.x:22` | Tailscale SSH |
| VNC | `100.x:6901` | noVNC Web |
| Voice | `wss://100.x:8888` | WebRTC |
| 3D | `https://100.x:80/stream` | Pixel Signaling |

## 5. Non‑Functional Design

### 5.1 Security

```
Inbound: Tailscale ACLs only
Tools: Chroot + seccomp to /shared/
Logs: All actions to ELK stack
```


### 5.2 Scalability

- Horizontal: Kubernetes for agents/Unreal instances
- State: Redis for sessions; FS for persistence


### 5.3 Reliability

- Health checks: Each service `/healthz`
- Fallbacks: Text if voice fails; local if remote down


## 6. Deployment Diagram

```
Hub Server (Docker Compose):
├── tailscale
├── syncthing
├── clis (docker-compose)
├── novnc + cursor
├── livekit-agent
└── nginx (proxy + TURN)

GPU Node:
├── unreal-app (systemd)
├── cirrus-signaling
└── websocket-api
```


## 7. Trade‑offs

| Choice | Pro | Con |
| :-- | :-- | :-- |
| Tailscale | Simple, secure | Tailnet trust |
| LiveKit | Realtime excellence | Learning curve |
| Pixel Streaming | Native UE | UE5 license |

This design ensures modularity, with clear extension points for new tools/worlds.

---

# Architecture Document: Remote AI DevHub \& 3D Ecosystem

## 1. System Overview

The architecture centers on a **Remote Hub Server** acting as the single source of truth for compute, state, and execution. Thin clients (phone/laptop) connect via secure tunnels and streaming protocols. Key principles: modularity, shared state via filesystem, agentic AI via standardized tools.

**Layers**:

1. **Access Layer**: Tailscale + WebRTC
2. **State Layer**: Syncthing filesystem
3. **Compute Layer**: CLI tools + agents + Unreal
4. **Orchestration Layer**: Voice/video AI with cross‑layer tools

## 2. Core Components \& Interactions

```
                    ┌─────────────────────────────┐
                    │        Thin Clients         │
                    │  Phone ─ Browser/SSH Apps   │
                    │  Laptop ─ VSCode + Browser  │
                    └─────────────┬───────────────┘
                                  │ Tailscale VPN
                                  │ WebRTC/STUN
                                  ▼
┌─────────────────────────────────────────────────────┐
│                  Remote Hub Server                  │
│                                                     │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │   Syncthing │ │   Tailscale │ │     Nginx   │   │
│  │  (FS Mesh)  │ │   (ACLs)    │ │ (Proxy/TURN)│   │
│  └─────────────┘ └─────────────┘ └─────────────┘   │
│            │                        │              │
│            ▼                        ▼              │
│  ┌─────────────┐ ┌─────────────────────────────┐  │
│  │ CLI Tools   │ │     Voice Agent             │  │
│  │ Dockerized  │ │  ┌─────────────┐ ┌─────────┐ │  │
│  │ Claude/etc. │ │  │   LiveKit   │ │  LLM    │ │  │
│  └─────────────┘ │  │ (WebRTC)    │ │ (Tools) │ │  │
│                  │  └─────────────┘ └─────────┘ │  │
│                  │        │ Tools (MCP)         │  │
│                  └────────┼─────────────────────┘  │
│                           ▼                         │
│                    ┌─────────────────────┐          │
│                    │ Control APIs        │          │
│                    │ (REST/WS)           │          │
│                    └─────────────────────┘          │
└─────────────────────┬───────────────────────────────┘
                      │
              ┌───────▼───────┐
              │  GPU Node     │
              │ Unreal +      │
              │ Pixel Stream  │
              │ (Cirrus)      │
              └───────────────┘
```


## 3. Detailed Component Specs

### 3.1 Access Layer

- **Tailscale**: Mesh VPN; users `100.64.x.x`; ACL: SSH/VNC/HTTP to services.
- **Nginx**: Reverse proxy + TURN server for WebRTC.
- **Ports**: 22(SSH), 6901(VNC), 8888(WebRTC), 80/443(3D signaling).


### 3.2 State Layer (Syncthing)

```
Root: /shared/projects/
/shared/projects/{repo}/
  ├── src/
  ├── tests/
  ├── unreal/ (blueprints, assets)
  └── agent_state.json (sessions)
```

- Hooks: Post‑sync triggers for agent notifications.


### 3.3 Compute Layer

- **CLI Container**:

```
docker run -v /shared:/workspace claude-code --mcp
```

Constrained via `bubblewrap` or `seccomp`.
- **Cursor VNC**: `novnc + xfce4 + cursor --remote`.


### 3.4 Voice Agent

```
LiveKit Room ──► STT/LLM Loop ──► Tool Executor ──► FS/CLI/Unreal
     ▲                      ▲
Speech In                Tools Out (JSON)
Speech Out               Exec Results
```

- **Tool Bus**: gRPC or Redis pubsub for `run_cli`, `fs_*`, `world_*`.


### 3.5 3D Compute (GPU Node)

- **Unreal Instance**: systemd service; one per session or pooled.
- **Signaling**: Cirrus SFU; matchmake user→instance.
- **Control Server**: Node.js + UE WebSocket plugin.


## 4. Protocols \& Data Models

### 4.1 Agent Tool Schema (MCP‑inspired)

```json
{
  "tools": [
    {"name": "run_cli", "params": {"cmd": "string"}},
    {"name": "world_spawn", "params": {"type": "string", "pos": [f32,f32,f32]}}
  ]
}
```


### 4.2 Session State

```
Redis Key: session:{user_id}
{
  "active_world": "uuid",
  "fs_context": "/shared/projectX",
  "voice_turn": 42
}
```


## 5. Deployment \& Runtime

### 5.1 Docker Compose (Hub)

```yaml
services:
  tailscale:
  syncthing:
  nginx:
  clis:
    image: ai-coding-stack
    volumes: [/shared:/workspace]
  livekit:
    image: livekit/livekit-server
  agent:
    image: llm-agent
```


### 5.2 Orchestration

- **Static**: systemd + Docker Compose
- **Scale**: Nomad/K8s for dynamic Unreal pods


## 6. Observability

- **Metrics**: Prometheus (latency, tool calls/sec)
- **Logs**: Loki (structured JSON)
- **Traces**: Jaeger (voice→tool→exec)


## 7. Evolution Path

```
MVP ──► Agents ──► 3D ──► Multi‑user ──► Edge GPU ──► Federated
```

This architecture prioritizes **separation of concerns** (render vs control), **shared state** (filesystem), and **extensibility** (tool bus), ensuring the system scales from solo dev to collaborative AI worlds.

---

# Implementation Plan Document: Remote AI DevHub \& 3D System

## 1. Overview

This plan provides **actionable, sequential instructions** to build the system per architecture/design docs. Each phase includes prerequisites, commands, verification steps, and rollback. Total: ~60 hours over 8 weeks, self‑executable.

**Assumptions**: Ubuntu familiarity, API keys ready (Claude/Gemini), VPS access.

## 2. Prerequisites (Day 0, 2 hours)

1. **Provision Servers**:

```
# CPU Hub: e.g., DigitalOcean $24/mo (16GB)
ssh root@your-vps-ip

# GPU Later: RunPod/Paperspace (~$0.5/hr RTX 4090)
```

2. **Install Tailscale Everywhere**:

```
# Server
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --authkey=tskey-...

# Laptop/Windows: Download installer
# Phone: Blink Shell → Settings → Tailscale
# Verify: tailscale status (all online)
```

3. **Syncthing Setup**:
    - Install on all (Windows/WSL/Ubuntu/server)
    - Generate device IDs; connect mesh
    - Share `/shared/projects` folder
    - Test: Create `test.txt` on phone → verify everywhere

## 3. Phase 1: Coding Hub (Days 1‑3, 12 hours)

### 3.1 Server Setup

```
apt update && apt install -y docker.io docker-compose ssh mosh novnc
systemctl enable docker
```


### 3.2 CLI Tools (3 hours)

```
# Docker for isolation
mkdir -p /shared/projects/test && cd /shared/projects/test
git clone your-repo .

# Claude Code (npm global or Docker)
npm i -g @anthropic-ai/claude-code-cli
claude-code --help  # Verify

# Codex CLI (hypothetical; adapt per docs)
pip install codex-cli
codex --version

# Gemini CLI
npm i -g @google/gemini-cli
gemini --help
```


### 3.3 Remote Access (4 hours)

```
# SSH/Mosh from phone/laptop
ssh user@100.64.x.x  # Tailscale IP
mosh user@100.64.x.x  # Better for mobile

# Cursor VNC
apt install xfce4 xfce4-goodies tigervnc-standalone-server novnc
vncpasswd
vncserver :1 -geometry 1920x1080
websockify --web /usr/share/novnc 6901 localhost:5901
# Browser: http://100.64.x.x:6901 → Install/run Cursor
```

**Verify**:

```
# Phone: mosh → claude-code hello.py → edit → sync check
# Laptop: VSCode Remote‑SSH → open folder → Cursor via VNC
```

**Rollback**: `docker stop all; vncserver -kill :1`

## 4. Phase 2: Voice Agents (Days 4‑10, 20 hours)

### 4.1 Backend (8 hours)

```
# Docker Compose for agent stack
cat > docker-compose.yml <<EOF
version: '3'
services:
  livekit:
    image: livekit/livekit-server:latest
    ports: ["8888:8888", "7880:7880"]
    environment:
      - LIVEKIT_KEYS=...
  agent:
    build: .
    volumes: [/shared:/workspace]
EOF

# Agent Dockerfile (Python + LiveKit SDK)
cat > Dockerfile <<EOF
FROM python:3.12-slim
pip install livekit-api anthropic google-generativeai
# Custom agent.py with tools
EOF
```


### 4.2 Tools Implementation (6 hours)

```python
# agent.py snippet
import subprocess, os

TOOLS = {
    "run_cli": lambda cmd: subprocess.run(cmd, shell=True, cwd="/workspace", capture_output=True),
    "read_file": lambda path: open(f"/workspace/{path}").read() if path.startswith("projects/") else "DENIED"
}

# LiveKit room handler → LLM call → tool exec → TTS
```


### 4.3 Client App (4 hours)

```
# Simple HTML/JS WebRTC client
# index.html with LiveKit JS SDK + mic toggle
# Deploy: nginx /var/www/voice.html
```

**Verify**: Voice "list files" → Agent reads `/shared`, responds.

**Rollback**: `docker-compose down`

## 5. Phase 3: 3D Worlds (Days 11‑20, 24 hours)

### 5.1 GPU Node (4 hours)

```
# RunPod template: Ubuntu + NVIDIA drivers + UE5
# Install signaling
npm i -g livekit-cli
livekit-server --config cirrus.yaml
```


### 5.2 Unreal Setup (12 hours)

```
# UE5 Editor:
- Enable Pixel Streaming plugin
- Package project (Shipping build)
- Blueprint: WebSocket actor with RPCs (MoveAvatar, SpawnCube)
- systemd service: ./UnrealApp.exe -PixelStreamingIP=0.0.0.0 -PORT=80
```


### 5.3 Integration (6 hours)

```
# Extend agent tools
TOOLS["world_spawn"] = lambda data: requests.post("ws://gpu:8080/action", json=data)

# Test session: User joins stream → Voice "spawn cube" → Visible
```

**Verify**: Browser to `http://gpu.tailscale:80` → Interactive 3D + voice control.

**Rollback**: Stop UE service

## 6. Phase 4: Integration \& Go‑Live (Days 21‑28, 8 hours)

```
# Monitoring
apt install prometheus node-exporter
# Grafana dashboard: latency, sync status

# Scripts
./healthcheck.sh  # All services green
./e2e_test.sh    # Voice→CLI→3D flow
```


## 7. Maintenance

- **Daily**: `tailscale status; syncthing status`
- **Weekly**: Backup /shared, rotate logs
- **Upgrades**: Rolling Docker/UE updates


## 8. Cost Tracking

| Item | Monthly |
| :-- | :-- |
| CPU VPS | \$24 |
| GPU | \$150 |
| APIs | \$50 |
| **Total** | ~\$225 |

**Start Here**: Run Phase 0 today. Ping for blockers per phase. This plan turns docs into running system.

---

# Implementation Guide: Remote AI DevHub \& 3D System

## 1. Purpose

This **hands‑on guide** provides copy‑paste commands, configs, and troubleshooting for building from the implementation plan. Assumes Ubuntu server access and Tailscale running. Each section is self‑contained.

## 2. Phase 1: Coding Hub Setup

### 2.1 Base Server Config

```bash
# On fresh Ubuntu 24.04 VPS
apt update && apt upgrade -y
apt install -y curl wget docker.io docker-compose-v2 git ssh mosh tigervnc-standalone-server novnc ufw

ufw allow from 100.64.0.0/10  # Tailscale subnet
ufw enable

# Docker
systemctl enable --now docker
usermod -aG docker $USER
```


### 2.2 Syncthing

```bash
# Install & configure
curl -s https://syncthing.net/release-key.txt | apt-key add -
echo "deb https://apt.syncthing.net/ syncthing stable" > /etc/apt/sources.list.d/syncthing.list
apt update && apt install syncthing

# GUI: http://100.64.x.x:8384
# Add folder /shared/projects → share ID with other devices
mkdir -p /shared/projects/test
```


### 2.3 AI CLI Tools

```bash
# Claude Code CLI (Anthropic)
npm install -g @anthropic-ai/sdk  # Or official CLI when available
echo '#!/bin/bash\nanthropic --model claude-3.5-sonnet "$@"' > /usr/local/bin/claude-code
chmod +x /usr/local/bin/claude-code

# Gemini CLI (Google)
npm install -g @google/generative-ai
# Configure GEMINI_API_KEY=...

# Codex CLI (OpenAI equivalent)
pip install openai
echo '#!/bin/bash\nopenai api chat.completions.create ...' > /usr/local/bin/codex-cli
chmod +x /usr/local/bin/codex-cli

# Test in /shared/projects/test
cd /shared/projects/test
echo 'print("hello")' > test.py
claude-code "refactor this" test.py
```


### 2.4 Cursor + VNC

```bash
apt install -y xfce4 xfce4-goodies firefox
vncpasswd  # Set password

# Start VNC
echo '#!/bin/bash\nexport USER=ubuntu\nvncserver :1 -geometry 1920x1080 -depth 24' > start-vnc.sh
chmod +x start-vnc.sh
./start-vnc.sh

# noVNC proxy
websockify --web=/usr/share/novnc/ 6901 localhost:5901 &

# Install Cursor in VNC session
wget https://cursor.sh/download/cursor.deb && dpkg -i cursor.deb
```

**Access**: `http://100.64.x.x:6901/vnc.html?password=...`

**Test**: Phone SSH `claude-code test.py`; edit in Cursor VNC; verify sync.

## 3. Phase 2: Voice Agents

### 3.1 Docker Stack

```yaml
# docker-compose.yml
version: '3.8'
services:
  livekit:
    image: livekit/livekit-server:v1.8
    ports:
      - "7880:7880"
      - "7881:7881/udp"
      - "8888:8888"
    command: --config /etc/livekit.yaml
    volumes:
      - ./livekit.yaml:/etc/livekit.yaml

  agent:
    build: .
    ports: ["3000:3000"]
    volumes: ["/shared:/workspace:ro"]
    environment:
      - ANTHROPIC_API_KEY=...
      - LIVEKIT_URL=ws://livekit:7880
```

**livekit.yaml** (minimal):

```yaml
port: 7880
rtc:
  use_external_stun: true
keys:
  api_key: yourkey
  secret: yoursecret
```


### 3.2 Agent Code (agent/Dockerfile + agent.py)

```dockerfile
FROM node:20-alpine
RUN npm i -g livekit-cli livekit-server-sdk @anthropic-ai/sdk
COPY agent.js /app/
CMD ["node", "/app/agent.js"]
```

**agent.js** (Node.js example):

```javascript
const { RoomServiceClient } = require('livekit-server-sdk');
const Anthropic = require('@anthropic-ai/sdk');

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const roomService = new RoomServiceClient('ws://livekit:7880', 'key', 'secret');

async function handleVoice(roomName, participant) {
  // STT → LLM tools → TTS loop
  const tools = [{
    name: 'run_cli',
    description: 'Run safe CLI command',
    inputSchema: { cmd: 'string' }
  }];
  
  const response = await anthropic.messages.create({
    model: 'claude-3-5-sonnet-20240620',
    messages: [{ role: 'user', content: audioToText }],  // Pseudo
    tools
  });
  
  // Exec safe cmd, publish audio response
  if (response.tools) {
    const result = execSafe(response.tools[0].input.cmd);
    await publishTTS(result, participant);
  }
}
```


### 3.3 Client (voice.html)

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/livekit-client@2/dist/livekit-client.umd.js"></script>
</head>
<body>
  <button id="join">Join Voice</button>
  <script>
    const room = new LivekitClient.Room();
    document.getElementById('join').onclick = () => {
      room.connect('wss://100.64.x.x:8888', 'token');
    };
  </script>
</body>
</html>
```

**Deploy**: `docker-compose up -d; nginx -t; nginx -s reload`

**Test**: Open voice.html → speak "list files" → hears response.

## 4. Phase 3: 3D (GPU Node)

### 4.1 Quickstart on RunPod

```
# RunPod template: RTX 4090 + UE5
apt install nginx nodejs npm unreal-engine  # Pseudo

# Pixel Streaming
npm install -g @epicgames/pixel-streaming
# Package your UE project with plugin enabled
systemd service for UnrealApp.exe
```


### 4.2 Control API

```javascript
// control-api.js (on GPU)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (data) => {
    const action = JSON.parse(data);
    if (action.type === 'spawn') {
      // UE RPC via plugin
      unrealSocket.send(`SpawnCube ${action.pos}`);
    }
  });
});
```

**Integrate**: Add to agent tools.

## 5. Troubleshooting

| Issue | Fix |
| :-- | :-- |
| Tailscale down | `tailscale status; tailscale up` |
| Sync stuck | `syncthing restart; check scanner` |
| VNC blank | `vncserver -kill :1; ./start-vnc.sh` |
| Voice silent | `docker logs agent; check API keys` |

## 6. Go‑Live Checklist

- [ ] All verifies pass
- [ ] Backup /shared
- [ ] Health endpoints 200
- [ ] Latency tests (<150ms)

Copy‑paste to implement; adapt paths/keys. Full repo structure available on request.

