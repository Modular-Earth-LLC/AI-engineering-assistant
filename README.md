# AI Engineering Assistant

**Systematic AI development framework** for Cursor IDE. Design, architect, and deploy production AI systems through a multi-agent workflow—from requirements gathering to deployment guidance.

## Overview

Developing AI systems requires coordinated expertise across requirements, architecture, engineering, and deployment. This framework provides 6 specialized agents running in Cursor IDE that guide you through the complete development lifecycle with systematic rigor.

**What it does**: Transforms your AI system concept into production-ready implementations through structured, multi-agent workflows.

**Where it runs**: Cursor IDE (or VS Code with GitHub Copilot). Generates AI systems deployable to any platform including OpenAI, Claude Projects, AWS Bedrock, and custom infrastructure.

## Quick Start

### Complete System Development (15 minutes)

1. **Install**: Copy `supervisor_agent.system.prompt.md` to Cursor Settings → Chat → Custom Modes
2. **Start**: Open Cursor AI Pane, select "Supervisor Agent"
3. **Request**: "Build a financial operations assistant"
4. **Follow**: Requirements → Architecture → Engineering → Deployment
5. **Deploy**: To your chosen platform

### Prompt Engineering Only (5 minutes)

1. **Load**: `ai_agents/prompt_engineering_assistant.system.prompt.md` in Cursor
2. **Request**: "Create a code review assistant for OpenAI GPT"
3. **Deploy**: Copy generated prompt to target platform

## The 6 Specialized Agents

### 🎯 Supervisor Agent
**Orchestrates** all agents and intelligently routes user requests to specialized agents  
**File**: `supervisor_agent.system.prompt.md`  
**Use**: Start here for complete AI system development workflows

### 📋 Requirements Agent
**Discovers** what you need to build through structured inquiry  
**File**: `ai_agents/requirements_agent.system.prompt.md`  
**Use**: "Conduct discovery for email automation"

### 🏗️ Architecture Agent
**Designs** system architecture following AWS Well-Architected principles  
**File**: `ai_agents/architecture_agent.system.prompt.md`  
**Use**: "Design system architecture and select tech stack"

### ⚙️ Engineering Agent
**Builds** working prototypes with production-ready code  
**File**: `ai_agents/engineering_agent.system.prompt.md`  
**Use**: "Generate prototype implementation"

### 🚀 Deployment Agent
**Guides** platform-specific deployment with testing strategies  
**File**: `ai_agents/deployment_agent.system.prompt.md`  
**Use**: "Deploy to AWS Bedrock" or "Set up testing"

### 🔧 Optimization Agent
**Improves** existing systems following Well-Architected principles  
**File**: `ai_agents/optimization_agent.system.prompt.md`  
**Use**: "Analyze system for optimization opportunities"

### ✨ Prompt Engineering Agent
**Creates** and optimizes prompts for any platform  
**File**: `ai_agents/prompt_engineering_assistant.system.prompt.md`  
**Use**: "Create a technical documentation assistant"

## Key Capabilities

### Knowledge Base State Management
All agents share context through JSON files in `knowledge_base/`:
- `system_config.json`: Platform constraints, team info, Well-Architected definitions
- `user_requirements.json`: Business requirements, success criteria (Requirements Agent)
- `design_decisions.json`: Architecture decisions, costs, plans (Architecture Agent)

### Multi-Agent Orchestration
- Supervisor routes requests to specialized agents based on intent analysis
- Seamless agent handoffs preserve full context across transitions
- Agents collaborate effectively on complex multi-phase workflows
- Clear separation of concerns across agent domains

### Production-Ready Outputs
- Working prototypes with production-ready implementation code
- Platform-optimized prompts for OpenAI, Claude, Bedrock, and Cursor
- Deployment guides with detailed step-by-step instructions
- Comprehensive cost estimates and project implementation plans

## Installation

### Automated Setup (Recommended)

```bash
# Clone repository
git clone https://github.com/Modular-Earth-LLC/AI-engineering-assistant.git
cd AI-engineering-assistant

# Deploy to Cursor
.\scripts\deploy_cursor.ps1    # Windows
./scripts/deploy_cursor.sh     # Linux/Mac
```

### Manual Setup

1. Open Cursor Settings → Chat → Custom Modes
2. Create mode: "Supervisor Agent"
3. Copy contents of `supervisor_agent.system.prompt.md`
4. Enable "All tools"
5. Save and start using

## Common Workflows

### New AI System
```
Supervisor Agent → Requirements Agent → Architecture Agent 
→ Engineering Agent → Deployment Agent
```

### System Improvement
```
Optimization Agent → analyzes system → recommends improvements
→ Engineering Agent (if code changes) → Deployment Agent
```

### Prompt Creation
```
Prompt Engineering Agent → creates/optimizes → validates → deploys
```

## Implementation Examples

### Financial Operations Assistant
**Challenge**: Solo entrepreneur needs AI for invoicing and expense tracking  
**Workflow**: Requirements (5min) → Architecture (10min) → Engineering (15min)  
**Output**: 2-agent system (Operations + Analytics) deployable to AWS Bedrock  
**Result**: Production system with Streamlit UI and Claude integration

### Customer Support Bot
**Challenge**: E-commerce needs 24/7 support with product knowledge  
**Workflow**: Complete lifecycle through all agents  
**Output**: Single agent with knowledge base for Claude Projects  
**Result**: Team-accessible support assistant

### Code Review Assistant
**Challenge**: Development team needs automated Python code review  
**Workflow**: Prompt Engineering Agent only  
**Output**: Security-focused prompt for OpenAI GPT  
**Result**: Copy-paste deployment in 5 minutes

## Platform Deployment

### Where This Framework Runs
**Cursor IDE** (or VS Code with Copilot) — Required for the agents in this repository

### Where Generated Systems Deploy
- **OpenAI Custom GPTs**: Character limit ~1,500
- **Anthropic Claude Projects**: Character limit ~32,000
- **AWS Bedrock Agents**: Production-grade infrastructure
- **Cursor IDE**: Custom chat modes for teams
- **Custom platforms**: Ollama, LangChain, AutoGen, self-hosted

### Deployment Process
1. Engineering Agent generates prompts, code, and infrastructure
2. Deployment Agent creates platform-specific deployment guide
3. Execute deployment steps
4. System runs on target platform

## System Requirements

### For This Framework
- Cursor IDE (recommended) or VS Code with GitHub Copilot
- File system access for knowledge base
- Internet connection for AI APIs

### For Generated Systems
- Platform-specific (varies by deployment target)
- Deployment Agent provides complete requirements

## Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Multi-agent system design and two-tier architecture
- **[guides/getting-started.md](guides/getting-started.md)**: Detailed walkthrough
- **[guides/workflow_guide.md](guides/workflow_guide.md)**: Complete workflow documentation
- **[docs/agent-relationships.md](docs/agent-relationships.md)**: Agent capabilities and collaboration

## User Prompts

Specialized task instructions organized by category in `user_prompts/`:
- `requirements/`: Discovery tasks (4 prompts)
- `architecture/`: System design tasks (6 prompts)
- `engineering/`: Prototype generation (1 prompt)
- `deployment/`: Deployment and testing (2 prompts)
- `self_improvement/`: Improve agents in THIS repo (8 prompts)
- `prompt_engineering/`: Generic prompt engineering (6 prompts)
- `proposals/`: Executive presentations (4 prompts)

## Glossary

**Optimize** — Comprehensive system-level improvements following Well-Architected principles. Use the Optimization Agent for entire AI systems.

**Improve** — Targeted enhancements to specific components. Agent improvements use `self_improvement/` prompts; prompt improvements use the Prompt Engineering Assistant.

**Enhance** — User experience and documentation improvements.

## Troubleshooting

**Agent can't find knowledge base**  
Ensure running from repository root. Paths: `knowledge_base/*.json`

**Supervisor not routing correctly**  
Be specific: "Build a customer support system" not "I need help"

**Missing context between agents**  
Verify knowledge base files populated by previous agent

**Wrong platform deployment**  
Specify target: "Deploy to AWS Bedrock" not just "Deploy"

## Contributing

**Improvements**: Fork repository, submit pull requests  
**Issues**: Report bugs via GitHub Issues  
**Documentation**: PRs welcome for clarity improvements

## License

MIT License — Full commercial use permitted

## Repository

[AI Engineering Assistant](https://github.com/Modular-Earth-LLC/AI-engineering-assistant) — Production-ready multi-agent AI development framework for Cursor IDE
