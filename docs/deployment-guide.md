# Deployment Guide - Cursor & Claude Projects

**Complete deployment instructions** for running the AI Engineering Assistant on Cursor IDE and Claude Projects.

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
4. Name: `AI Engineering Assistant`
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

## Deployment Comparison

| Feature | Cursor Custom Modes | Claude Projects |
|---------|-------------------|-----------------|
| **Multiple Agents** | ✅ 7 separate custom modes | ⚠️ 1 supervisor in custom instructions |
| **Knowledge Base** | ✅ File system access | ✅ Project Knowledge upload |
| **Team Collaboration** | ⚠️ Same Cursor workspace | ✅ Cloud-based sharing |
| **Context Persistence** | ⚠️ Per conversation | ✅ Project-level persistence |
| **Setup Complexity** | ⭐ Simple (paste prompts) | ⭐⭐ Moderate (upload files) |
| **Agent Switching** | ✅ Dropdown selection | ⚠️ Request in conversation |
| **Local Execution** | ✅ Runs locally | ❌ Cloud-based only |
| **Cost** | ✅ Cursor license only | 💰 Claude Pro/Team required |
| **Best For** | Solo developers, teams in Cursor | Remote teams, cloud preference |

---

## Hybrid Deployment

**Use both platforms simultaneously:**

1. **Design in Cursor** (full agent access)
   - Use all 7 agents as custom modes
   - Generate content to `outputs/`
   - Full file system integration

2. **Collaborate in Claude Projects** (team access)
   - Upload final designs to Claude Project
   - Team reviews and provides feedback
   - Shared project knowledge

3. **Deploy from Cursor** (implementation)
   - Use Deployment Agent in Cursor
   - Generate platform-specific guides
   - Execute deployment

**Benefits:**
- ✅ Best of both worlds
- ✅ Solo work in Cursor (full capabilities)
- ✅ Team collaboration in Claude (shared context)
- ✅ Version control in git (Cursor workspace)

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
- [ ] Name: "AI Engineering Assistant"

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
