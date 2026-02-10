## Safety, Permissions, and Governance

This document defines security boundaries, permission models, and governance policies for the AI manager hierarchy system.

It ensures:
- **Safety**: Agents cannot perform unauthorized or destructive actions
- **Compliance**: Meets organizational and regulatory requirements
- **Auditability**: All actions are traceable and reviewable
- **Control**: Humans maintain oversight of critical decisions

---

## 1. Permission Model

### 1.1 Permission Levels

Agents operate under a hierarchical permission system:

**Level 0: Read-Only**
- Can read files and handoffs
- Can query APIs (read-only)
- Cannot modify filesystem
- Cannot execute commands
- **Use Case**: Research agents, code review agents

**Level 1: Sandboxed Write**
- Can create/modify files in designated directories
- Can run safe commands (linting, testing)
- Cannot access network
- Cannot modify system files
- **Use Case**: Implementation workers (L3/L4)

**Level 2: Standard Agent**
- Can create/modify project files
- Can install dependencies (with approval)
- Can make API calls (with rate limits)
- Cannot modify configuration files without approval
- **Use Case**: Feature managers (L2), component workers (L3)

**Level 3: Project Manager**
- Can modify configuration files
- Can create/delete directories
- Can manage dependencies
- Cannot modify security-critical files
- **Use Case**: Project managers (L1)

**Level 4: System Manager**
- Full filesystem access (within workspace)
- Can execute arbitrary commands
- Can modify all configuration
- Requires human approval for destructive actions
- **Use Case**: Universal managers (L0), administrators

### 1.2 Permission Assignment

```yaml
# permissions.yaml
permissions:
  layers:
    L0:
      default_level: 4  # System Manager
      require_approval:
        - delete_directory
        - modify_security_policy
        - change_budget_limits

    L1:
      default_level: 3  # Project Manager
      require_approval:
        - install_dependency
        - modify_ci_cd_config
        - change_git_hooks

    L2:
      default_level: 2  # Standard Agent
      require_approval:
        - create_api_endpoint
        - modify_database_schema

    L3:
      default_level: 1  # Sandboxed Write
      allowed_directories:
        - src/components/
        - tests/
      allowed_commands:
        - npm test
        - npm run lint
        - npm run type-check

    L4:
      default_level: 1  # Sandboxed Write
      allowed_directories:
        - src/components/**/subcomponents/
      allowed_commands:
        - npm test -- --testPathPattern=

  tools:
    claude-code:
      max_permission_level: 3
      dangerous_tools_disabled: []

    codex:
      max_permission_level: 2
      dangerous_tools_disabled:
        - delete_file
        - execute_shell

    gemini:
      max_permission_level: 2
      dangerous_tools_disabled:
        - write_file  # Research only
```

---

## 2. Security Boundaries

### 2.1 Filesystem Isolation

**Workspace Boundaries:**
```python
class WorkspaceIsolation:
    """Enforce filesystem boundaries for agents."""

    def __init__(self, workspace_root, layer, stage):
        self.workspace_root = Path(workspace_root).resolve()
        self.layer = layer
        self.stage = stage
        self.allowed_paths = self.compute_allowed_paths()

    def compute_allowed_paths(self):
        """Determine which paths this agent can access."""
        base_paths = [
            self.workspace_root / f"layer_{self.layer}",
            self.workspace_root / "shared",
        ]

        # L3/L4 agents restricted to their component directories
        if self.layer >= 3:
            component_dir = get_component_directory(self.stage)
            base_paths = [self.workspace_root / component_dir]

        return base_paths

    def validate_path(self, requested_path):
        """Check if path is within allowed boundaries."""
        resolved = Path(requested_path).resolve()

        # Must be within workspace
        if not str(resolved).startswith(str(self.workspace_root)):
            raise PermissionError(f"Path outside workspace: {requested_path}")

        # Must be in allowed paths
        if not any(str(resolved).startswith(str(p)) for p in self.allowed_paths):
            raise PermissionError(f"Path not allowed for layer {self.layer}: {requested_path}")

        # Blacklist critical files
        if self.is_critical_file(resolved):
            raise PermissionError(f"Cannot modify critical file: {requested_path}")

        return resolved

    def is_critical_file(self, path):
        """Check if file is security-critical."""
        critical_patterns = [
            ".git/config",
            ".env",
            "*.pem",
            "*.key",
            "**/credentials/**",
            ".ssh/**",
            "permissions.yaml"
        ]

        return any(path.match(pattern) for pattern in critical_patterns)
```

### 2.2 Command Execution Sandboxing

```python
class CommandSandbox:
    """Restrict command execution based on permission level."""

    # Command whitelist by permission level
    ALLOWED_COMMANDS = {
        1: [  # Sandboxed Write
            "npm test",
            "npm run lint",
            "npm run type-check",
            "pytest",
            "eslint",
            "tsc --noEmit"
        ],
        2: [  # Standard Agent
            "npm install",
            "npm run build",
            "git status",
            "git diff",
            "git add",
            "git commit"
        ],
        3: [  # Project Manager
            "npm run deploy:staging",
            "docker build",
            "git push",
            "gh pr create"
        ],
        4: [  # System Manager - all commands allowed
            "*"
        ]
    }

    DANGEROUS_COMMANDS = [
        "rm -rf",
        "sudo",
        "chmod 777",
        "curl | sh",
        "wget | sh",
        "> /dev/sd*"  # Writing to disk
    ]

    def __init__(self, permission_level):
        self.permission_level = permission_level

    def validate_command(self, command):
        """Check if command is allowed."""

        # Check for dangerous patterns
        if any(danger in command for danger in self.DANGEROUS_COMMANDS):
            raise PermissionError(f"Dangerous command blocked: {command}")

        # Level 4 can run anything (except dangerous)
        if self.permission_level >= 4:
            return True

        # Check whitelist
        allowed = self.ALLOWED_COMMANDS.get(self.permission_level, [])
        if allowed == ["*"]:
            return True

        # Command must match whitelist
        if not any(cmd in command for cmd in allowed):
            raise PermissionError(
                f"Command not allowed at level {self.permission_level}: {command}"
            )

        return True

    def execute_safe(self, command, cwd):
        """Execute command with safety checks."""
        self.validate_command(command)

        # Additional safety: timeout, resource limits
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            timeout=300,  # 5 min max
            env=self.get_safe_env()
        )

        return result

    def get_safe_env(self):
        """Get environment variables with secrets removed."""
        env = os.environ.copy()

        # Remove sensitive vars
        sensitive_keys = [k for k in env if any(
            pattern in k.upper() for pattern in
            ["SECRET", "KEY", "TOKEN", "PASSWORD", "CREDENTIAL"]
        )]

        for key in sensitive_keys:
            del env[key]

        return env
```

### 2.3 Network Access Control

```python
class NetworkPolicy:
    """Control network access for agents."""

    def __init__(self, layer, stage):
        self.layer = layer
        self.stage = stage

    def is_allowed(self, url, method="GET"):
        """Check if network request is allowed."""

        # Parse URL
        parsed = urllib.parse.urlparse(url)

        # Blacklist internal/sensitive endpoints
        if self.is_internal_network(parsed.hostname):
            raise PermissionError(f"Access to internal network blocked: {url}")

        # Check against whitelist
        if not self.matches_whitelist(parsed):
            raise PermissionError(f"URL not in whitelist: {url}")

        # Restrict methods
        if method not in ["GET", "POST"] and self.layer >= 3:
            raise PermissionError(f"HTTP method {method} not allowed for layer {self.layer}")

        return True

    def is_internal_network(self, hostname):
        """Check if hostname is internal/private."""
        if not hostname:
            return False

        # Private IP ranges
        private_patterns = [
            r"^localhost$",
            r"^127\.",
            r"^10\.",
            r"^172\.(1[6-9]|2[0-9]|3[0-1])\.",
            r"^192\.168\.",
            r"\.local$"
        ]

        return any(re.match(pattern, hostname) for pattern in private_patterns)

    def matches_whitelist(self, parsed_url):
        """Check if URL matches allowed patterns."""
        # Example whitelist
        whitelisted_domains = [
            "github.com",
            "api.github.com",
            "registry.npmjs.org",
            "pypi.org",
            "*.googleapis.com",
            "docs.anthropic.com"
        ]

        hostname = parsed_url.hostname
        return any(
            fnmatch.fnmatch(hostname, pattern)
            for pattern in whitelisted_domains
        )
```

---

## 3. Human-in-the-Loop Approvals

### 3.1 Approval Requirements

Certain actions require human approval before execution:

```python
class ApprovalGate:
    """Require human approval for sensitive operations."""

    REQUIRES_APPROVAL = {
        "delete_file": lambda path: path.count('/') < 3,  # Top-level files
        "delete_directory": lambda path: True,  # Always
        "install_dependency": lambda pkg: pkg not in KNOWN_SAFE_PACKAGES,
        "modify_security_config": lambda _: True,
        "git_push": lambda branch: branch in ["main", "master", "production"],
        "deploy": lambda env: env in ["production", "staging"],
        "api_call_external": lambda url: "payment" in url or "user-data" in url,
        "budget_increase": lambda amount: amount > 100.00
    }

    def __init__(self, notification_channel="slack"):
        self.channel = notification_channel
        self.pending_approvals = {}

    def request_approval(self, action, context, agent_id):
        """Request human approval for an action."""

        approval_id = generate_uuid()
        self.pending_approvals[approval_id] = {
            "action": action,
            "context": context,
            "agent_id": agent_id,
            "requested_at": datetime.utcnow(),
            "status": "pending"
        }

        # Notify humans
        self.send_notification(
            f"Approval Required: {action}\n"
            f"Agent: {agent_id}\n"
            f"Context: {json.dumps(context, indent=2)}\n"
            f"Approve: /approve {approval_id}\n"
            f"Deny: /deny {approval_id}"
        )

        # Wait for approval (with timeout)
        return self.wait_for_approval(approval_id, timeout=3600)  # 1 hour

    def wait_for_approval(self, approval_id, timeout):
        """Block until approval granted or denied."""
        start = time.time()

        while time.time() - start < timeout:
            approval = self.pending_approvals.get(approval_id)

            if approval["status"] == "approved":
                log_audit("approval_granted", approval)
                return True

            if approval["status"] == "denied":
                log_audit("approval_denied", approval)
                return False

            time.sleep(5)  # Poll every 5 seconds

        # Timeout - default deny
        log_audit("approval_timeout", approval)
        return False

    def approve(self, approval_id, approver):
        """Approve a pending request."""
        if approval_id in self.pending_approvals:
            self.pending_approvals[approval_id]["status"] = "approved"
            self.pending_approvals[approval_id]["approver"] = approver
            self.pending_approvals[approval_id]["approved_at"] = datetime.utcnow()

    def deny(self, approval_id, approver, reason=None):
        """Deny a pending request."""
        if approval_id in self.pending_approvals:
            self.pending_approvals[approval_id]["status"] = "denied"
            self.pending_approvals[approval_id]["approver"] = approver
            self.pending_approvals[approval_id]["reason"] = reason
```

### 3.2 Approval UI (Slack Bot Example)

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackApprovalBot:
    """Slack bot for approvals."""

    def __init__(self, token):
        self.client = WebClient(token=token)
        self.approval_gate = ApprovalGate(notification_channel="slack")

    def send_approval_request(self, action, context, agent_id):
        """Send approval request to Slack."""

        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"🚨 Approval Required: {action}"
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Agent:*\n{agent_id}"},
                    {"type": "mrkdwn", "text": f"*Layer:*\n{context.get('layer')}"}
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```\n{json.dumps(context, indent=2)}\n```"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Approve"},
                        "style": "primary",
                        "action_id": f"approve_{approval_id}"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Deny"},
                        "style": "danger",
                        "action_id": f"deny_{approval_id}"
                    }
                ]
            }
        ]

        try:
            response = self.client.chat_postMessage(
                channel="#ai-approvals",
                blocks=blocks
            )
        except SlackApiError as e:
            print(f"Error sending message: {e}")

    def handle_approval_action(self, payload):
        """Handle button click from Slack."""
        action_id = payload["actions"][0]["action_id"]
        user = payload["user"]["username"]

        if action_id.startswith("approve_"):
            approval_id = action_id.replace("approve_", "")
            self.approval_gate.approve(approval_id, approver=user)

        elif action_id.startswith("deny_"):
            approval_id = action_id.replace("deny_", "")
            self.approval_gate.deny(approval_id, approver=user)
```

---

## 4. Budget and Resource Governance

### 4.1 Budget Controls

```python
class BudgetGovernor:
    """Enforce budget limits and controls."""

    def __init__(self, config_path):
        self.config = load_yaml(config_path)
        self.spending_tracker = SpendingTracker()

    def check_budget(self, layer, stage, estimated_cost):
        """Check if task is within budget."""

        # Check daily limit
        daily_spent = self.spending_tracker.get_daily_total()
        daily_limit = self.config["budgets"]["daily_total"]

        if daily_spent + estimated_cost > daily_limit:
            return self.request_budget_increase("daily", estimated_cost)

        # Check layer-specific limit
        layer_spent = self.spending_tracker.get_layer_total(layer, period="daily")
        layer_limit = self.config["budgets"].get(f"L{layer}", {}).get("daily_limit", float('inf'))

        if layer_spent + estimated_cost > layer_limit:
            return self.request_budget_increase(f"layer_{layer}", estimated_cost)

        # Check stage-specific limit
        stage_limit = self.config["budgets"].get(f"L{layer}", {}).get("task_limits", {}).get(stage, float('inf'))

        if estimated_cost > stage_limit:
            return self.request_budget_increase(f"L{layer}_{stage}", estimated_cost)

        return True

    def request_budget_increase(self, budget_type, amount):
        """Request approval to exceed budget."""
        approval_gate = ApprovalGate()

        approved = approval_gate.request_approval(
            "budget_increase",
            {
                "budget_type": budget_type,
                "requested_amount": amount,
                "current_usage": self.spending_tracker.get_usage_summary()
            },
            agent_id="budget_governor"
        )

        if approved:
            # Temporarily increase limit
            self.config["budgets"][budget_type] *= 1.5
            save_yaml(self.config_path, self.config)

        return approved
```

### 4.2 Resource Quotas

```python
class ResourceQuota:
    """Enforce resource limits per agent."""

    DEFAULT_QUOTAS = {
        "max_parallel_tasks": 4,
        "max_task_duration_seconds": 600,
        "max_memory_mb": 4096,
        "max_file_size_mb": 10,
        "max_api_calls_per_minute": 60
    }

    def __init__(self, layer, stage):
        self.layer = layer
        self.quotas = self.get_quotas_for_layer(layer)
        self.usage = defaultdict(int)

    def get_quotas_for_layer(self, layer):
        """Get quota configuration for layer."""
        quotas = self.DEFAULT_QUOTAS.copy()

        # L0-L2 get higher limits
        if layer <= 2:
            quotas["max_parallel_tasks"] = 10
            quotas["max_task_duration_seconds"] = 1800

        # L3-L4 get tighter limits
        else:
            quotas["max_parallel_tasks"] = 2
            quotas["max_task_duration_seconds"] = 300

        return quotas

    def check_quota(self, resource_type, amount=1):
        """Check if resource usage is within quota."""
        current = self.usage[resource_type]
        limit = self.quotas.get(f"max_{resource_type}", float('inf'))

        if current + amount > limit:
            raise QuotaExceeded(
                f"{resource_type} quota exceeded: {current + amount} > {limit}"
            )

        return True

    def acquire(self, resource_type, amount=1):
        """Acquire resource, blocking if quota exceeded."""
        self.check_quota(resource_type, amount)
        self.usage[resource_type] += amount

    def release(self, resource_type, amount=1):
        """Release acquired resource."""
        self.usage[resource_type] = max(0, self.usage[resource_type] - amount)
```

---

## 5. Audit and Compliance

### 5.1 Compliance Requirements

```yaml
compliance:
  # Regulatory requirements
  regulations:
    - GDPR:
        personal_data_handling:
          - no_model_training_on_user_data
          - explicit_consent_required
          - right_to_deletion
        retention:
          max_days: 90
          audit_trail_permanent: true

    - SOC2:
        access_control:
          - role_based_permissions
          - approval_gates_for_sensitive_ops
          - audit_all_actions
        encryption:
          - data_at_rest
          - data_in_transit

    - HIPAA:  # If applicable
        phi_handling:
          - no_phi_in_logs
          - encrypted_storage
          - access_logging

  # Internal policies
  internal:
    code_review:
      - all_l0_l1_changes_require_human_review
      - security_critical_requires_specialist_review

    deployment:
      - production_deploys_require_approval
      - staging_deploys_automated_with_tests

    data_handling:
      - no_secrets_in_code
      - no_api_keys_in_logs
      - pii_redaction_enabled
```

### 5.2 Audit Trail Requirements

All actions must be logged with:
- Timestamp
- Agent ID and layer/stage
- Action type (read/write/execute/api_call)
- Resource accessed (file path, API endpoint, command)
- Outcome (success/failure)
- Approver (if approval required)

See `observability_and_logging.md` for implementation details.

---

## 6. Summary

Effective governance requires:

1. **Layered Permissions**: Restrictive by default, escalate as needed
2. **Filesystem & Network Isolation**: Prevent unauthorized access
3. **Human Approvals**: Critical decisions require human oversight
4. **Budget Controls**: Prevent runaway costs
5. **Resource Quotas**: Prevent resource exhaustion
6. **Comprehensive Auditing**: Full traceability of all actions
7. **Compliance Alignment**: Meet regulatory and organizational requirements

These controls ensure the system is safe, compliant, and trustworthy in production.
