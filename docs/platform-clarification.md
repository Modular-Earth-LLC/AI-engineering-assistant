# Platform Clarification - Where Things Run

**Purpose:** Eliminate confusion about execution platforms  
**Audience:** Developers, architects, documentation readers  
**TL;DR:** This framework runs IN Cursor. It CREATES systems for other platforms.

---

## The Two Levels

### Meta-Level: This AI Architecture Assistant Framework

**What it is:**
- 6 specialized AI agents (Supervisor, Requirements, Architecture, Engineering, Deployment, Optimization)
- Runs as Cursor custom chat modes
- Helps developers architect, engineer, and deploy OTHER AI systems

**Where it runs:**
- **ONLY in Cursor IDE** as custom chat modes
- Agents execute in Cursor's AI Pane
- NOT deployed to Claude Projects, AWS Bedrock, or other platforms

**Purpose:**
- Design tool for AI engineers
- Automates AI system architecture and engineering workflows
- Generates prompts, code, and deployment guides for TARGET systems

**Installation:**
```powershell
# Windows
.\scripts\deploy_cursor.ps1

# Linux/Mac
./scripts/deploy_cursor.sh
```

**Usage:**
1. Open Cursor IDE
2. AI Pane → Custom Chat Mode → "Supervisor Agent"
3. Start building your target system

---

### Target-Level: Systems You CREATE

**What they are:**
- AI systems, agents, and applications you design using this framework
- Examples: financial operations assistant, email automation, customer support bot

**Where they run:**
- **Cursor IDE** (as custom chat modes for yourself or others)
- **Claude Projects** (team collaboration, business users)
- **AWS Bedrock** (production, enterprise deployments)
- **Custom platforms** (Ollama, LangChain, AutoGen, self-hosted)

**How they're created:**
1. Requirements Agent gathers needs
2. Architecture Agent designs system
3. Engineering Agent generates:
   - Agent prompts (`.system.prompt.md` files)
   - Implementation code (Python, JavaScript, etc.)
   - UI (Streamlit, React, CLI)
   - Knowledge base files
4. Deployment Agent guides deployment to target platform

**Deployment:**
- Each target system deployed independently
- Platform-specific deployment instructions provided
- Can deploy to multiple platforms simultaneously

---

## Visual Distinction

```
┌─────────────────────────────────────────────┐
│ LEVEL 1: AI ARCHITECTURE ASSISTANT          │
│ (This Repository - Meta-Level)              │
│                                              │
│ Execution: Cursor IDE (custom chat modes)   │
│ Purpose: Build OTHER AI systems             │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Supervisor Agent                        │ │
│ │   ├─ Requirements Agent                 │ │
│ │   ├─ Architecture Agent                 │ │
│ │   ├─ Engineering Agent                  │ │
│ │   ├─ Deployment Agent                   │ │
│ │   └─ Optimization Agent                 │ │
│ └─────────────────────────────────────────┘ │
│                                              │
│ Knowledge Base: user_requirements.json,     │
│                 design_decisions.json        │
│                 (for target systems)         │
└─────────────────────────────────────────────┘
                     ↓
                  Generates
                     ↓
┌─────────────────────────────────────────────┐
│ LEVEL 2: YOUR TARGET SYSTEMS                │
│ (Output - Target-Level)                     │
│                                              │
│ Execution: YOUR CHOSEN PLATFORM             │
│ Purpose: Solve business problems            │
│                                              │
│ Examples:                                    │
│ ┌─────────────────────────────────────────┐ │
│ │ Financial Operations Assistant          │ │
│ │   - Deployed to: AWS Bedrock            │ │
│ │   - Operations Agent + Analytics Agent  │ │
│ └─────────────────────────────────────────┘ │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Email Automation System                 │ │
│ │   - Deployed to: Claude Projects        │ │
│ │   - Routing Agent + Response Agent      │ │
│ └─────────────────────────────────────────┘ │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Customer Support Bot                    │ │
│ │   - Deployed to: Cursor (for team)      │ │
│ │   - Single agent                        │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

---

## Common Confusions Resolved

### ❓ "Can I deploy this framework to AWS Bedrock?"

**No.** This framework runs ONLY in Cursor IDE. 

However, you can use this framework (in Cursor) to CREATE systems that you THEN deploy to AWS Bedrock.

**Workflow:**
1. Use AI Architecture Assistant in Cursor
2. Design a system (e.g., financial assistant)
3. Engineering Agent generates prompts and code for that system
4. Deployment Agent guides you to deploy THAT SYSTEM to AWS Bedrock

---

### ❓ "Can I use Claude Projects instead of Cursor?"

**No.** This framework requires Cursor IDE because it uses Cursor's custom chat modes feature.

However, you can use this framework (in Cursor) to CREATE systems that you THEN deploy to Claude Projects.

**Example:**
1. You (developer) use AI Architecture Assistant in Cursor
2. Design a customer support system
3. Engineering Agent generates agent prompts and knowledge base
4. You deploy that system to a Claude Project for your support team to use

---

### ❓ "Why not just use Claude Projects for everything?"

Claude Projects are excellent for:
- Team collaboration on specific projects
- Business users (non-developers)
- Persistent knowledge across conversations

This framework (in Cursor) is better for:
- AI system design and architecture workflows
- Rapid prototyping and iteration
- Code generation and engineering tasks
- Developer-centric tools

**Best of both worlds:** Use this framework in Cursor to BUILD systems, then deploy those systems to Claude Projects for your team.

---

### ❓ "What's the relationship to AWS Bedrock?"

**This framework:** Design tool running in Cursor

**AWS Bedrock:** Production deployment platform for systems you create

**Relationship:**
1. Architecture Agent designs a system following AWS Well-Architected principles
2. Engineering Agent generates Bedrock-compatible prompts and infrastructure code
3. Deployment Agent provides step-by-step Bedrock deployment guide
4. You execute the deployment to Bedrock
5. Your system runs on Bedrock in production

---

### ❓ "Can I create Cursor agents with this framework?"

**Yes!** One of the output options is to create Cursor custom chat modes.

**Workflow:**
1. Use AI Architecture Assistant (in Cursor) to design an agent
2. Engineering Agent generates a `.system.prompt.md` file for that agent
3. Copy that file to Cursor's custom chat modes directory
4. Now you (or others) can use that agent in Cursor

**Example:** Create a "SQL Query Assistant" agent for your team, deploy it as a Cursor custom chat mode for all team members.

---

### ❓ "What about multi-platform deployment?"

**Yes!** You can deploy the SAME target system to MULTIPLE platforms.

**Example:**
1. Design financial operations assistant with AI Architecture Assistant (in Cursor)
2. Engineering Agent generates prompts and code
3. Deploy to:
   - **Cursor** (for yourself to test and use locally)
   - **Claude Projects** (for your business team to collaborate)
   - **AWS Bedrock** (for production API access)

All three deployments run the SAME system on different platforms.

---

## File Naming Conventions

To maintain clarity, this repository uses consistent naming:

### System Prompts (`.system.prompt.md`)

**Meta-Level (this framework):**
- `supervisor_agent.system.prompt.md`
- `ai_agents/requirements_agent.system.prompt.md`
- `ai_agents/architecture_agent.system.prompt.md`
- etc.

**Target-Level (generated by Engineering Agent):**
- `outputs/prototypes/financial-ops/financial_operations_agent.system.prompt.md`
- `outputs/prototypes/email-automation/email_routing_agent.system.prompt.md`
- etc.

### User Prompts (`.user.prompt.md`)

**Meta-Level (messages TO this framework's agents):**
- `user_prompts/architecture/tech_stack_selection.user.prompt.md`
- `user_prompts/engineering/prototype_generation.user.prompt.md`
- etc.

**Target-Level (generated messages for target systems):**
- Engineering Agent MAY generate user prompts for complex target systems

---

## Decision Tree: Where Should My System Run?

```
START: I want to build an AI system
    ↓
Use AI Architecture Assistant (in Cursor) to design it
    ↓
Engineering Agent generates prompts and code
    ↓
Choose deployment platform for YOUR system:
    ↓
    ├─ Developers only? 
    │    → Deploy to Cursor (custom chat modes)
    │
    ├─ Team collaboration, non-technical users?
    │    → Deploy to Claude Projects
    │
    ├─ Production, API access, enterprise scale?
    │    → Deploy to AWS Bedrock
    │
    └─ Custom infrastructure, self-hosted?
         → Deploy to Ollama, LangChain, etc.
```

---

## Summary Table

| Aspect | AI Architecture Assistant (Meta) | Your Target Systems (Output) |
|--------|----------------------------------|------------------------------|
| **Runs where?** | Cursor IDE ONLY | Cursor, Claude Projects, Bedrock, custom |
| **Purpose** | Design tool for developers | Production systems for users |
| **Who uses?** | AI engineers, developers | End users, business teams |
| **How deployed?** | Copy to Cursor chat modes | Platform-specific deployment |
| **Repository location** | Root + `ai_agents/` | `outputs/prototypes/[project]/` |
| **Generates** | Designs, code, deployment guides | Solves business problems |
| **Example** | Supervisor Agent, Architecture Agent | Financial assistant, Email bot |

---

## References

- **README.md:** Updated with platform clarification
- **guides/platform_deployment.md:** Comprehensive deployment guide (meta + target)
- **guides/workflow_guide.md:** Phase-by-phase workflow with platform context
- **System prompts:** All agents include "Execution Context" sections

---

**Version:** 1.0  
**Last Updated:** 2025-10-08  
**Framework Platform:** Cursor IDE (ONLY)  
**Target System Platforms:** Cursor | Claude Projects | AWS Bedrock | Custom

---

**Still confused?** Open an issue or chat with the Supervisor Agent in Cursor: "Explain the difference between this framework and the systems it creates."
