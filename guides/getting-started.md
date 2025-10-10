# Getting Started

**Complete setup and first project** in 15-30 minutes.

## What You'll Build

By the end of this guide:
- ✅ Multi-agent system installed in Cursor
- ✅ Complete AI system built from requirements to deployment
- ✅ Understanding of agent workflow and capabilities

## Prerequisites

- **Cursor IDE** (recommended) or VS Code with GitHub Copilot
- **Git** for cloning the repository
- **15-30 minutes** for complete walkthrough

## Step 1: Installation (5 minutes)

### Setup Process

1. **Clone repository**:
   ```bash
   git clone https://github.com/Modular-Earth-LLC/AI-engineering-assistant.git
   cd AI-engineering-assistant
   ```

2. **Configure Cursor**:
   - Open Cursor → Settings → Chat → Custom Modes
   - Click "New Mode"
   - Name: "Supervisor Agent"
   - Paste contents of `supervisor_agent.system.prompt.md`
   - Enable "All tools"
   - Save

3. **Verify**:
   - Open Cursor AI Pane (`Ctrl+Shift+L` or `Cmd+Shift+L`)
   - Confirm "Supervisor Agent" appears in dropdown
   - Select it to begin

**Optional**: Create additional custom modes for specialized agents (`ai_agents/*.system.prompt.md`) for direct access without routing through supervisor

## Step 2: Your First System (20 minutes)

### Start with Supervisor

1. **Open Cursor AI Pane**: `Ctrl+Shift+L` (or `Cmd+Shift+L`)
2. **Select**: "Supervisor Agent" from dropdown
3. **Request**: "Build a customer support AI assistant for my e-commerce business"

### Follow the Workflow

Supervisor guides you through:
- **Requirements** (5 min) — What you need
- **Architecture** (10 min) — System design
- **Engineering** (5 min) — Prototype generation
- **Deployment** (2 min) — Deployment planning

Each agent:
- Asks focused questions
- Updates knowledge base
- Hands off with full context
- Provides clear next steps

## Step 3: Understanding the Agents

### 🎯 Supervisor Agent
**Use**: Start here for any project  
**Does**: Routes to specialized agents  
**Example**: "Build AI system for [use case]"

### 📋 Requirements Agent
**Use**: Beginning of projects  
**Does**: Discovers what to build  
**Example**: "Help me understand what I need"

### 🏗️ Architecture Agent
**Use**: After requirements  
**Does**: Designs system architecture  
**Example**: "Design system for my requirements"

### ⚙️ Engineering Agent
**Use**: After architecture  
**Does**: Builds working prototypes  
**Example**: "Build prototype for my system"

### 🚀 Deployment Agent
**Use**: After prototyping  
**Does**: Guides platform deployment  
**Example**: "Deploy to AWS Bedrock"

### 🔧 Optimization Agent
**Use**: For existing systems  
**Does**: Analyzes and improves  
**Example**: "Improve my AI system"

### ✨ Prompt Engineering Agent
**Use**: Prompt creation/optimization  
**Does**: Creates and improves prompts  
**Example**: "Create code review assistant"

## Step 4: Knowledge Base

All agents share information through JSON files in `knowledge_base/`:

**system_config.json**
- Platform constraints and capabilities
- Team information and skills
- AWS Well-Architected definitions

**user_requirements.json**
- Business requirements
- Problem statement and success criteria
- AI suitability assessment
- Written by Requirements Agent

**design_decisions.json**
- Architecture decisions
- Tech stack selections
- Cost estimates and project plans
- Written by Architecture Agent

### How It Works

1. Requirements Agent writes `user_requirements.json`
2. Architecture Agent reads requirements, writes `design_decisions.json`
3. Engineering Agent reads both files, builds system
4. Deployment Agent reads design decisions, plans deployment

## Step 5: Common Workflows

### Complete System Development
```
Supervisor → Requirements → Architecture 
→ Engineering → Deployment
```

### Prompt Engineering Only
```
Prompt Engineering Agent → create/optimize 
→ validate → deploy
```

### System Improvement
```
Optimization Agent → analyze → recommend 
→ implement → test
```

## Step 6: Platform Deployment

### Where Your System Deploys

**Cursor IDE**
- Copy prompts to custom chat modes
- Best for: Development teams

**Claude Projects**
- Create project, upload prompts
- Best for: Team collaboration

**AWS Bedrock**
- Deploy as Bedrock Agents
- Best for: Production, enterprise

**Custom Platforms**
- Ollama, LangChain, self-hosted
- Best for: Specific needs

### Deployment Process

1. Engineering Agent generates system components
2. Deployment Agent creates deployment guide
3. Execute platform-specific deployment
4. System runs on target platform

## Troubleshooting

**Agent can't find knowledge base**  
→ Run from repository root: `cd AI-engineering-assistant`

**Supervisor not routing correctly**  
→ Be specific: "Build customer support system"

**Missing context between agents**  
→ Verify knowledge base files populated by previous agent

**Agent asks too many questions**  
→ Provide context upfront or reference existing knowledge base

## Next Steps

### Immediate Actions
1. Build complete system with real project
2. Explore individual agents for specific tasks
3. Review knowledge base files after each phase
4. Test deployment to chosen platform

### Advanced Usage
1. Customize agents for specific needs
2. Create custom user prompts
3. Integrate with development workflow
4. Set up automated improvement

### Learning Resources
- `docs/agent-relationships.md` — Agent capabilities
- `guides/workflow_guide.md` — Complete workflow
- `ARCHITECTURE.md` — System architecture
- `guides/executive_overview.md` — Business perspective

## Example Projects

### Financial Operations AI System
- Challenge: Automate financial operations for organizations
- Approach: Collaborative design with AI engineer and domain expert
- Architecture: Multi-agent system (Operations + Analytics + Reporting)
- Technology: Python + Claude/GPT + AWS Bedrock or Claude Projects
- Timeline: 2-4 weeks from requirements to deployment
- Value: Significant time reduction and operational efficiency gains

### Customer Support Bot
- Requirements: 24/7 e-commerce support
- Architecture: Single agent + knowledge base
- Engineering: Claude Projects integration
- Deployment: Claude Projects
- Impact: Instant responses, reduced support costs

### Code Review Assistant
- Requirements: Automated code review for dev team
- Architecture: Single specialized agent
- Engineering: Prompt optimized for OpenAI GPT
- Deployment: Cursor custom chat mode
- Impact: Consistent code quality, faster reviews

## Success Tips

**Do**:
- ✅ Start with Supervisor Agent
- ✅ Follow workflow sequence
- ✅ Let agents hand off naturally
- ✅ Review knowledge base after each phase
- ✅ Be specific about requirements

**Don't**:
- ❌ Skip requirements phase
- ❌ Rush architecture
- ❌ Deploy without testing
- ❌ Use all agents at once
- ❌ Provide vague requests

## Support

**GitHub Issues**: Report bugs, request features  
**Discussions**: Ask questions, share experiences  
**Documentation**: Comprehensive guides in `docs/` and `guides/`

## Contributing

**Agent Improvements**: Use Prompt Engineering Agent  
**Documentation**: Submit pull requests  
**Examples**: Share successful projects

---

**Ready?** Open Cursor, load Supervisor Agent, and say: "Build an AI system for [your use case]"
