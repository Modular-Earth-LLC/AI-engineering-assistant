# Deployment Guide - Multi-Agent AI Development Framework

**Complete deployment instructions** for running the Multi-Agent AI Development Framework (THIS repository) on Cursor IDE, GitHub Copilot, and Claude Projects.

**Scope:** Tier 1 deployment (the framework itself)  
**For deploying generated AI systems:** See `platform_deployment.md` (Tier 2 deployment)

**Quick Navigation:**
- Need to deploy THIS framework? → You're in the right place
- Need to deploy a system you built WITH this framework? → See `platform_deployment.md`

---

## Deployment Option 1: Cursor Custom Chat Modes

**Best for:** Individual developers or teams using Cursor IDE  
**Setup time:** 5-10 minutes  
**Complexity:** ⭐ Simple

### Prerequisites

- Cursor IDE installed ([cursor.com](https://cursor.com))
- This repository cloned locally
- Basic familiarity with Cursor settings

### Setup Instructions

#### 1. Install Supervisor Agent (Primary Entry Point)

1. Open Cursor → **Settings** (Ctrl/Cmd + ,)
2. Navigate to **Chat** → **Custom Modes**
3. Click **"+ New Mode"**
4. Configure:
   - **Name:** `Supervisor Agent`
   - **System Prompt:** Copy entire contents of `supervisor_agent.system.prompt.md`
   - **Tools:** Enable "All tools"
5. Click **Save**

#### 2. Install Specialized Agents (Optional but Recommended)

Repeat the above process for each specialized agent:

| Agent Name | File Location | Purpose |
|------------|---------------|---------|
| Requirements Agent | `ai_agents/requirements_agent.system.prompt.md` | Discovery & requirements gathering |
| Architecture Agent | `ai_agents/architecture_agent.system.prompt.md` | System design & planning |
| Engineering Agent | `ai_agents/engineering_agent.system.prompt.md` | Prototype development |
| Deployment Agent | `ai_agents/deployment_agent.system.prompt.md` | Platform deployment guidance |
| Optimization Agent | `ai_agents/optimization_agent.system.prompt.md` | System improvement |
| Prompt Engineering Agent | `ai_agents/prompt_engineering_agent.system.prompt.md` | Prompt creation & optimization |

**Why install all agents?**
- Direct access without supervisor routing
- Faster for repetitive tasks
- Specialized workflows more efficient

**Why install only Supervisor?**
- Simpler setup (1 agent vs 7)
- Guided workflow for beginners
- Supervisor routes to specialists automatically

### 3. Verify Installation

1. Open Cursor AI Pane (`Ctrl+Shift+L` or `Cmd+Shift+L`)
2. Click the mode dropdown
3. Confirm your agents appear in the list
4. Select "Supervisor Agent"
5. Test: Type "I want to build an AI system"
6. Verify: Supervisor explains routing to specialized agents

### 4. Configure Knowledge Base Access

The agents read/write to `knowledge_base/*.json` files automatically via Cursor's file access.

**Ensure:**
- You're working from repository root directory
- Knowledge base files are accessible: `knowledge_base/system_config.json`, etc.
- Agents have "All tools" enabled (for file reading)

### 5. Start Using

**Simple workflow:**
```
1. Select "Supervisor Agent" in Cursor AI Pane
2. Request: "Build a customer support chatbot"
3. Supervisor routes you through:
   - Requirements Agent (discovery)
   - Architecture Agent (design)
   - Engineering Agent (build)
   - Deployment Agent (deploy)
```

**Direct agent workflow:**
```
1. Select specific agent (e.g., "Prompt Engineering Agent")
2. Request: "Create a code review assistant"
3. Agent executes task directly
```

---

## Deployment Option 2: Claude Projects

**Best for:** Teams wanting collaborative AI workspace  
**Setup time:** 10-15 minutes  
**Complexity:** ⭐⭐ Moderate

### Prerequisites

- Claude Pro or Claude Team subscription
- This repository downloaded
- Access to Claude Projects ([claude.ai/projects](https://claude.ai/projects))

### Setup Instructions

#### 1. Create Claude Project

1. Go to [claude.ai](https://claude.ai)
2. Click **Projects** in sidebar
3. Click **"+ New Project"**
4. Name: `Multi-Agent AI Development Framework`
5. Click **Create**

#### 2. Upload Knowledge Base

1. In your project, click **Project Knowledge** tab
2. Upload files:
   - `knowledge_base/system_config.json`
   - `knowledge_base/user_requirements.json`
   - `knowledge_base/design_decisions.json`
   - `knowledge_base/README.md`
3. Click **Add Files** and select all 4 files
4. Wait for processing to complete (usually <1 minute)

#### 3. Configure Project Instructions (Primary Method)

Claude Projects supports **one custom instruction** per project. You have two options:

**Option A: Supervisor-Only (Recommended)**

1. Copy entire contents of `supervisor_agent.system.prompt.md`
2. In Claude Project → **Custom Instructions** tab
3. Paste the supervisor prompt
4. Click **Save**

**Result:** Supervisor routes to specialized capabilities within the conversation

**Option B: Create Multiple Projects (Advanced)**

Create separate Claude Projects for each agent:
- Project: "AI Requirements Agent" → Use `requirements_agent.system.prompt.md`
- Project: "AI Architecture Agent" → Use `architecture_agent.system.prompt.md`
- etc.

**Result:** Direct access to each agent, but requires switching between projects

#### 4. Add Documentation (Optional but Helpful)

Upload to Project Knowledge for reference:
- `README.md`
- `ARCHITECTURE.md`
- `docs/getting-started.md`
- `docs/workflow_guide.md`

This allows agents to reference framework documentation during execution.

#### 5. Test Installation

In your Claude Project chat:

```
Test 1: "I want to build an AI system for customer support"
Expected: Supervisor routes to Requirements Agent

Test 2: "Conduct quick discovery session"
Expected: Starts asking discovery questions

Test 3: "Read the knowledge base system_config file"
Expected: Successfully reads and references the JSON content
```

### Claude-Specific Considerations

**Limitations:**
- ⚠️ Claude Projects support 1 custom instruction per project (not 7 separate agents)
- ⚠️ Can't dynamically switch between agent modes in one conversation

**Workarounds:**
- ✅ Use Supervisor Agent (routes to specialized capabilities within conversation)
- ✅ Create explicit prompts: "Act as the Requirements Agent and conduct discovery"
- ✅ Reference specific sections: "Use the Architecture Agent process from the knowledge base"

**Advantages:**
- ✅ Team collaboration (entire team accesses same project)
- ✅ Persistent context (project knowledge persists across conversations)
- ✅ No local setup needed (cloud-based)
- ✅ Knowledge base automatically available to Claude

---

## Deployment Option 3: GitHub Copilot (VS Code)

**Best for:** VS Code users and teams already using GitHub Copilot  
**Setup time:** 10-15 minutes  
**Complexity:** ⭐⭐ Moderate

### Prerequisites

- VS Code installed with GitHub Copilot extension
- GitHub Copilot subscription (Individual, Business, or Enterprise)
- This repository cloned locally
- Basic familiarity with Copilot Chat

### Setup Instructions

#### 1. Configure Workspace Instructions

GitHub Copilot supports workspace-level instructions that guide AI behavior. Create a configuration file:

1. **Create file**: `.github/copilot-instructions.md` in your workspace root
2. **Paste content**: Copy entire contents of `supervisor_agent.system.prompt.md`
3. **Save**: Copilot will automatically detect and use these instructions

**File structure:**
```
multi-agent-ai-development-framework/
├── .github/
│   └── copilot-instructions.md    ← Supervisor Agent prompt here
├── ai_agents/
├── knowledge_base/
└── ... other files
```

#### 2. Add Knowledge Base Context

Since Copilot Chat can reference workspace files, structure your knowledge base for easy access:

1. **Keep organized**: Leave `knowledge_base/*.json` files in their current location
2. **Reference explicitly**: When prompting, mention files: "Using @knowledge_base/system_config.json, show me..."
3. **Use @workspace**: Copilot can search across all files with @workspace

#### 3. Configure Additional Agents (Optional)

For specialized agent access, create additional instruction files:

```
.github/
├── copilot-instructions.md           ← Supervisor (main)
└── agents/
    ├── requirements-agent.md         ← Requirements Agent
    ├── architecture-agent.md         ← Architecture Agent
    ├── engineering-agent.md          ← Engineering Agent
    ├── deployment-agent.md           ← Deployment Agent
    ├── optimization-agent.md         ← Optimization Agent
    └── prompt-engineering-agent.md   ← Prompt Engineering Agent
```

**To switch agents**: Copy the relevant agent prompt from `ai_agents/` and use it in your conversation context.

#### 4. Verify Setup

**Test the supervisor:**
```
1. Open VS Code Copilot Chat (Ctrl+Alt+I or Cmd+Alt+I)
2. Type: "I want to build a customer support chatbot"
3. Copilot should respond using the Supervisor Agent behavior
4. Verify: It explains the workflow and asks discovery questions
```

**Test knowledge base access:**
```
1. In Copilot Chat, type: "Show me the contents of @knowledge_base/system_config.json"
2. Expected: Copilot reads and references the file
3. Confirm: File content is accessible and parsed
```

### 5. Start Using

**Supervisor-guided workflow:**
```
1. Open Copilot Chat in VS Code
2. Request: "Build an email automation system"
3. Copilot (as Supervisor) routes through:
   - Requirements discovery
   - Architecture design
   - Implementation guidance
   - Deployment recommendations
```

**Direct agent workflow:**
```
1. Open relevant agent file from ai_agents/
2. Copy the agent prompt
3. In Copilot Chat: "Act as [Agent Name] and [specific task]"
4. Provide the agent prompt context if needed
```

### GitHub Copilot-Specific Considerations

**Limitations:**
- ⚠️ Workspace instructions are project-wide (not per-conversation modes)
- ⚠️ Can't switch between discrete agent modes like Cursor
- ⚠️ File access requires explicit @mentions or @workspace

**Workarounds:**
- ✅ Use Supervisor approach (single instruction file with routing logic)
- ✅ Explicitly reference agents: "Act as the Architecture Agent and..."
- ✅ Use @workspace and @file mentions for knowledge base access
- ✅ Copy specific agent prompts into conversations for specialized tasks

**Advantages:**
- ✅ Native VS Code integration (familiar interface)
- ✅ Works with existing GitHub Copilot subscription
- ✅ Team-wide consistency (same instructions across team)
- ✅ Automatic workspace file access
- ✅ Version control friendly (instructions in git)

---

## Deployment Comparison

| Feature | Cursor Custom Modes | Claude Projects | GitHub Copilot |
|---------|-------------------|-----------------|-----------------|
| **Multiple Agents** | ✅ 7 separate custom modes | ⚠️ 1 supervisor in custom instructions | ⚠️ 1 supervisor in workspace instructions |
| **Knowledge Base** | ✅ File system access | ✅ Project Knowledge upload | ✅ @workspace and @file mentions |
| **Team Collaboration** | ⚠️ Same Cursor workspace | ✅ Cloud-based sharing | ✅ Git-based (shared instructions) |
| **Context Persistence** | ⚠️ Per conversation | ✅ Project-level persistence | ⚠️ Per conversation |
| **Setup Complexity** | ⭐ Simple (paste prompts) | ⭐⭐ Moderate (upload files) | ⭐⭐ Moderate (create config files) |
| **Agent Switching** | ✅ Dropdown selection | ⚠️ Request in conversation | ⚠️ Request in conversation |
| **Local Execution** | ✅ Runs locally | ❌ Cloud-based only | ✅ Runs locally |
| **Cost** | ✅ Cursor license only | 💰 Claude Pro/Team required | ✅ GitHub Copilot subscription |
| **Best For** | Solo developers, teams in Cursor | Remote teams, cloud preference | VS Code users, GitHub teams |

---

## Multi-Platform Deployment

**Use multiple platforms simultaneously:**

1. **Design in Cursor** (full agent access)
   - Use all 7 agents as custom modes
   - Generate content to `outputs/`
   - Full file system integration

2. **Collaborate in Claude Projects** (team access)
   - Upload final designs to Claude Project
   - Team reviews and provides feedback
   - Shared project knowledge

3. **Develop in VS Code with Copilot** (familiar IDE)
   - Use workspace instructions for consistency
   - Leverage existing Copilot workflows
   - Git-based collaboration

**Benefits:**
- ✅ Choose the best platform for each task
- ✅ Team members use their preferred tools
- ✅ Consistent agent behavior across platforms
- ✅ Version control for all configurations

---

## Troubleshooting

### Cursor Issues

**Agent can't find knowledge base:**
- Ensure you're in repository root directory
- Check paths: `knowledge_base/system_config.json`
- Verify "All tools" enabled for the agent

**Agent not appearing in dropdown:**
- Restart Cursor
- Check custom mode saved correctly
- Verify system prompt pasted completely

**Agent returns errors:**
- Check if prompt exceeds character limits
- Verify no syntax errors in copied content
- Try creating fresh custom mode

### Claude Projects Issues

**Knowledge base not accessible:**
- Verify files uploaded to Project Knowledge
- Wait for processing (can take 30-60 seconds)
- Re-upload if files show errors

**Agent not behaving correctly:**
- Verify custom instruction pasted completely
- Check for character limit (32K) - supervisor fits
- Try explicit prompting: "Act as Requirements Agent"

**Multiple agents needed:**
- Use supervisor routing: "Route me to Architecture Agent"
- Or create separate projects for each agent
- Or request agent mode in conversation

---

## Platform-Specific Tips

### Cursor Best Practices

✅ **Use keyboard shortcuts:**
- `Ctrl+Shift+L` / `Cmd+Shift+L` - Open AI pane
- Quick agent switching via dropdown

✅ **Reference files:**
- Use `@filename` to reference knowledge base files
- Agents can read project files directly

✅ **Organize workspace:**
- Keep repository root open
- Use Cursor's file tree for navigation

### Claude Projects Best Practices

✅ **Leverage Project Knowledge:**
- Upload all relevant documentation
- Reference in prompts: "Check the knowledge base for requirements"

✅ **Explicit agent requests:**
- "Act as the Requirements Agent and conduct discovery"
- "Switch to Architecture Agent mode and design system"

✅ **Share with team:**
- Add team members to project
- Everyone sees same context and history
- Collaborative AI engineering

---

## Advanced: Automated Deployment

### Cursor Deployment Script (Optional)

Create `.cursor/deploy_agents.ps1`:

```powershell
# Automated Cursor agent deployment
$agents = @(
    @{name="Supervisor Agent"; file="supervisor_agent.system.prompt.md"},
    @{name="Requirements Agent"; file="ai_agents/requirements_agent.system.prompt.md"},
    @{name="Architecture Agent"; file="ai_agents/architecture_agent.system.prompt.md"},
    @{name="Engineering Agent"; file="ai_agents/engineering_agent.system.prompt.md"},
    @{name="Deployment Agent"; file="ai_agents/deployment_agent.system.prompt.md"},
    @{name="Optimization Agent"; file="ai_agents/optimization_agent.system.prompt.md"},
    @{name="Prompt Engineering Agent"; file="ai_agents/prompt_engineering_agent.system.prompt.md"}
)

Write-Host "Copy each agent prompt to Cursor Settings → Chat → Custom Modes"
Write-Host ""
foreach ($agent in $agents) {
    Write-Host "Agent: $($agent.name)"
    Write-Host "File: $($agent.file)"
    Write-Host "---"
}
```

Run: `.\\.cursor\deploy_agents.ps1`

### Claude Project Setup Script (Optional)

Create `.claude/setup_project.md`:

```markdown
# Claude Project Setup Checklist

## Step 1: Create Project
- [ ] Go to claude.ai/projects
- [ ] Click "+ New Project"
- [ ] Name: "Multi-Agent AI Development Framework"

## Step 2: Upload Knowledge Base
- [ ] Upload: knowledge_base/system_config.json
- [ ] Upload: knowledge_base/user_requirements.json
- [ ] Upload: knowledge_base/design_decisions.json
- [ ] Upload: knowledge_base/README.md

## Step 3: Set Custom Instructions
- [ ] Copy: supervisor_agent.system.prompt.md
- [ ] Paste into Project → Custom Instructions
- [ ] Save

## Step 4: Optional Documentation
- [ ] Upload: README.md
- [ ] Upload: ARCHITECTURE.md
- [ ] Upload: docs/getting-started.md

## Step 5: Test
- [ ] Test: "I want to build an AI system"
- [ ] Verify: Supervisor routing works
- [ ] Test: Knowledge base accessible
```

---

## Next Steps

After deployment:

1. **Test with real project** - Build something to validate
2. **Save outputs** - All deliverables go to `outputs/`
3. **Iterate** - Improve based on real usage
4. **Share with team** - Invite collaborators (Claude) or share workspace (Cursor)

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Platforms Supported:** Cursor IDE (custom chat modes) | Claude Projects (custom instructions + knowledge base)  
**Deployment Methods:** Manual (copy-paste) | Scripted (optional automation)
