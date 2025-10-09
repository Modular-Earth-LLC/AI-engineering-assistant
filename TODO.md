# TODO — Multi-Agent System & Prompt Upkeep

Owner: @paulprae
Repo: Modular-Earth-LLC/AI-engineering-assistant
Date: 2025-10-09

This checklist covers the multi-agent AI Engineering Assistant system and automated prompt improvement workflows.

## Multi-Agent System Overview

**6 Specialized Agents:**
- **Supervisor Agent** (`supervisor_agent.system.prompt.md`) - Orchestrates all others
- **Requirements Agent** (`ai_agents/requirements_agent.system.prompt.md`) - Discovery & requirements
- **Architecture Agent** (`ai_agents/architecture_agent.system.prompt.md`) - System design & planning
- **Engineering Agent** (`ai_agents/engineering_agent.system.prompt.md`) - Prototype building
- **Deployment Agent** (`ai_agents/deployment_agent.system.prompt.md`) - Platform deployment
- **Optimization Agent** (`ai_agents/optimization_agent.system.prompt.md`) - System improvement
- **Prompt Engineering Agent** (`ai_agents/prompt_engineering_assistant.system.prompt.md`) - Prompt creation

**Knowledge Base Integration:**
- `knowledge_base/system_config.json` - Platform constraints, team info
- `knowledge_base/user_requirements.json` - Customer needs, use cases
- `knowledge_base/design_decisions.json` - Architecture decisions, costs

**Workflow:** Start with Supervisor Agent → Routes to specialized agents → Complete AI system development

## Quick Setup

**how to use (trivial steps)**

Use the Issue template (preferred):

- New Issue → “Prompt Improvement: Copilot Agent”
- Fill fields (scope defaults to user_prompts/**), set IMPROVEMENT_TYPE=incremental, CHANGE_THRESHOLD=15%
- Submit and assign to github-copilot-agent
- Copilot will open a PR and iterate based on your review comments

Start from VS Code chat (handoff):

- In your Prompt Engineering Assistant mode chat: paste
  - #github-pull-request_copilot-coding-agent
- Copilot coding agent takes it from there and opens a PR

Scheduled upkeep (optional):

- Actions → “Copilot Prompt Improvement (Scheduled)” → Run workflow or let it run Mondays 14:00 UTC
- Edits the recurring “Weekly upkeep” issue and assigns to Copilot

## 1) Enable Copilot coding agent (one-time)

- Ensure your account/organization has Copilot coding agent enabled (Pro/Pro+/Business/Enterprise).
- Confirm the agent can run in this repository (not opted out).

Docs: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

## 2) Use the Issue template to delegate work (preferred)

- New issue → choose template: "Prompt Improvement: Copilot Agent"
  - File: .github/ISSUE_TEMPLATE/prompt-improvement-copilot-agent.yml
- Fill in:
  - Scope: e.g., `user_prompts/**`
  - IMPROVEMENT_TYPE: incremental (default)
  - CHANGE_THRESHOLD: 15%
  - OPTIMIZATION_FOCUS: clarity (or redundancy/modularity)
  - Goals & Success Criteria: keep concise; preserve behavior & guardrails
- Submit the issue and assign to `github-copilot-agent`.
- Copilot opens a PR; review and iterate in the PR.

Tip: You can also paste this handoff tag in VS Code Copilot Chat to start the agent:

#github-pull-request_copilot-coding-agent

## 3) Schedule weekly upkeep (automated)

- Verify the workflow exists: .github/workflows/copilot-prompt-improvement.yml
- It opens/updates a weekly issue and assigns it to the agent.
- Default schedule: Mondays 14:00 UTC; adjust the CRON as desired.
- Optional: Run on demand via GitHub Actions → "Run workflow" and customize inputs.

Inputs:
- scope: defaults to `user_prompts/**`
- improvement_type: incremental | comprehensive | targeted
- change_threshold: e.g., 15%
- optimization_focus: all | clarity | redundancy | modularity

## 4) Use the VS Code chat mode for manual sessions

- File: .github/chatmodes/prompt_engineering_assistant.chatmode.md
- In VS Code:
  - Open Chat (⌃⌘I) → Select the Prompt Engineering Assistant mode.
  - Tools: ensure codebase, search, fetch, websearch are available; approve when prompted.
  - Use Prompt Builder by default; ask for Prompt Tester when validating.

## 5) Review & merge PRs safely

- Verify PR diffs are within CHANGE_THRESHOLD and preserve behavior.
- Require green checks and at least one review approval.
- Leave PR comments to iterate. Copilot will push updates to the same PR.

## 6) Optional repo hygiene

- Add labels: `copilot-agent`, `prompt-improvement`.
- Protect main branch with required checks and reviews.
- Consider adding CODEOWNERS for prompt files.

## Future Improvements

- If you want the scheduled issue to immediately trigger Copilot after creation, just ensure you (or a rule) assigns the issue to github-copilot-agent—the workflow already sets assignees to that user in the issue creation step.
- Consider adding a CODEOWNERS entry for user_prompts/** and the system prompt files for PR routing.
- If websearch isn’t available in your VS Code environment, you can still use the chat mode; add an MCP web search server later if desired.

## Validation

- Lint/format: Markdown/YAML shapes are valid; no file path errors were found by the problem scanner.
- Copilot chat mode: The .chatmode.md front matter follows the VS Code docs (description, tools). Tools set to: ['codebase', 'search', 'fetch', 'websearch']. Body is the same platform-agnostic system prompt content. This mode should show in the mode dropdown.
- Workflow: Uses actions/checkout@v4 and peter-evans/create-issue-from-file@v5. It creates/updates an issue; labels and assignee applied. Permissions (contents: read, issues: write) are defined. The file includes clear comments.
- Issue template: GitHub Issue Forms YAML—fields for scope, improvement type, etc. Simple and actionable.

## Reference files

- Chat mode: .github/chatmodes/prompt_engineering_assistant.chatmode.md
- Issue template: .github/ISSUE_TEMPLATE/prompt-improvement-copilot-agent.yml
- Scheduled workflow: .github/workflows/copilot-prompt-improvement.yml
- System prompt: ai_agents/prompt_engineering_assistant.system.prompt.md

## Notes for future iterations

- Keep improvements incremental (≤ 15%) for easier review.
- Expand scope only after a few successful weekly runs.
- Consider adding lightweight tests for prompt structure checks if behavior changes.
