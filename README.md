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

1. **Load**: `ai_agents/prompt_engineering_agent.system.prompt.md` in Cursor
2. **Request**: "Create a code review assistant for OpenAI GPT"
3. **Deploy**: Copy generated prompt to target platform

## The 6 Specialized Agents

### 🎯 Supervisor Agent
**Orchestrates** all agents and intelligently routes user requests to specialized agents  
**File**: `supervisor_agent.system.prompt.md`  
**Use**: Start here for complete AI system development workflows

### 📋 Requirements Agent
**Discovers** stakeholder needs and structures requirements through systematic inquiry  
**File**: `ai_agents/requirements_agent.system.prompt.md`  
**Use**: "Conduct discovery session for email automation"

### 🏗️ Architecture Agent
**Designs** comprehensive system architecture following AWS Well-Architected principles  
**File**: `ai_agents/architecture_agent.system.prompt.md`  
**Use**: "Design complete system architecture and select optimal tech stack"

### ⚙️ Engineering Agent
**Builds** functional prototypes with production-ready implementation code  
**File**: `ai_agents/engineering_agent.system.prompt.md`  
**Use**: "Generate working prototype implementation"

### 🚀 Deployment Agent
**Guides** platform-specific deployment processes and testing strategies  
**File**: `ai_agents/deployment_agent.system.prompt.md`  
**Use**: "Deploy system to AWS Bedrock" or "Create comprehensive testing strategy"

### 🔧 Optimization Agent
**Improves** existing AI systems systematically following Well-Architected principles  
**File**: `ai_agents/optimization_agent.system.prompt.md`  
**Use**: "Analyze deployed system for optimization opportunities"

### ✨ Prompt Engineering Agent
**Creates** and optimizes high-quality prompts for any AI platform  
**File**: `ai_agents/prompt_engineering_agent.system.prompt.md`  
**Use**: "Create production-ready technical documentation assistant"

## Agent Relationships & Collaboration

### System Architecture

```
         ┌─────────────────────────┐
         │   Supervisor Agent 🎯   │
         │   (Orchestrator)        │
         └───────────┬─────────────┘
                     │ Routes requests
         ┌───────────┼───────────────────┐
         │           │                   │
    ┌────▼───┐  ┌───▼────┐  ┌──────▼──────┐
    │Require │  │  Arch  │  │ Engineering │←─┐
    │ments📋 │  │ ecture │  │     ⚙️      │  │
    └────┬───┘  │  🏗️   │  └──────┬──────┘  │
         │      └───┬────┘         │         │
         └──────────┼──────────────┘         │
                    │                        │
         ┌──────────┼────────────┐           │
         │          │            │           │
    ┌────▼────┐ ┌──▼────┐  ┌───▼──────┐    │
    │Deployment│ │Optimi-│  │  Prompt  │────┘
    │   🚀    │ │zation │  │Engineering|
    └─────────┘ │  🔧   │  │    ✨    │
                └───────┘  └──────────┘
                               ↑
                               │ Delegated
                               │ by Eng
```

**Key Integrations**:
- **Requirements → Architecture**: Provides structured requirements
- **Architecture → Engineering**: Delivers complete design
- **Engineering ↔ Prompt Engineering**: Engineering **delegates all prompt creation**
- **Engineering → Deployment**: Provides working prototype
- **Optimization ↔ All Agents**: Provides systematic improvements

**Separation of Concerns**:
- **Engineering Agent** = Code + UI + Implementation
- **Prompt Engineering Agent** = ALL Prompts + Optimization

**📚 Comprehensive Guide**: See `docs/agent-architecture-and-collaboration.md` for detailed workflows, collaboration patterns, and when to use each agent.

### Knowledge Base State Management
All agents share context through JSON files in `knowledge_base/`:
- `system_config.json`: Platform constraints, team info, Well-Architected definitions
- `user_requirements.json`: Business requirements, success criteria (Requirements Agent)
- `design_decisions.json`: Architecture decisions, costs, plans (Architecture Agent)

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

## When to Use Each Agent

| I Want To... | Use This Agent | Example Request |
|-------------|----------------|-----------------|
| Start a new project | Requirements Agent | "Conduct discovery for email automation" |
| Design complete system | Architecture Agent | "Design architecture and select tech stack" |
| Build working prototype | Engineering Agent | "Build prototype from architecture design" |
| **Create/optimize prompts** | **Prompt Engineering Agent** | **"Create code review assistant for GPT"** |
| Deploy to platform | Deployment Agent | "Deploy to AWS Bedrock" |
| Improve existing system | Optimization Agent | "Analyze system for optimizations" |
| Not sure where to start? | **Supervisor Agent** | "Help me build [describe system]" |

## Common Workflows

### Complete System Development (2-4 weeks)
```
1. Requirements Agent → Discovers needs (2-4 hours)
2. Architecture Agent → Designs system (4-8 hours)
3. Engineering Agent ↔ Prompt Engineering Agent → Builds prototype (2-5 days)
   │ Engineering creates code/UI
   └ Prompt Engineering creates ALL agent prompts
4. Deployment Agent → Deploys to platform (4-8 hours)
5. Optimization Agent → Continuous improvement (Ongoing)
```

### Rapid Prompt Engineering (30 min - 2 hours)
```
Prompt Engineering Agent (Direct) → Creates/optimizes prompt → Validates → Delivers
```

**Use Cases**:
- Create custom GPT instructions
- Optimize Claude Project prompts
- Convert prompts between platforms
- Improve existing prompts

### System Optimization (1-2 weeks/cycle)
```
1. Optimization Agent → Analyzes system
2. Identifies improvements:
   - Code → Engineering Agent
   - Prompts → Prompt Engineering Agent
   - Architecture → Architecture Agent
3. Optimization Agent → Validates improvements
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

### Process Terms

**Optimize** — Comprehensive system-level improvements following Well-Architected principles. Use the Optimization Agent for entire AI systems.

**Improve** — Targeted enhancements to specific components. Agent improvements use `self_improvement/` prompts; prompt improvements use the Prompt Engineering Agent.

**Enhance** — User experience and documentation improvements.

**Multi-shot prompting** — Breaking complex tasks into a sequence of focused user prompts, each producing specific deliverables that inform the next step (e.g., Architecture Agent's 6-step design process).

### System Architecture Terms

**Supervisor-worker pattern** — Architecture where a Supervisor Agent analyzes user intent and routes requests to specialized worker agents (Requirements, Architecture, Engineering, Deployment, Optimization, Prompt Engineering).

**Knowledge base** — JSON files in `knowledge_base/` that store shared state across agents: `system_config.json` (platform constraints), `user_requirements.json` (business requirements), `design_decisions.json` (architecture decisions).

**Agent** — Specialized AI assistant (system prompt) with a specific domain of expertise. This framework contains 6 agents plus 1 supervisor.

**User prompt** — Task-specific instructions that guide an agent to execute a particular workflow (e.g., `tech_stack_selection.user.prompt.md`). Distinct from system prompts which define an agent's core capabilities.

### Deployment Terms

**Meta-level** — This AI Architecture Assistant framework itself, running in Cursor IDE to help developers build AI systems.

**Target-level** — The AI systems that users design and build using this framework, which are deployed to external platforms (OpenAI, Claude Projects, AWS Bedrock, etc.).

**Platform** — Where an AI system runs. This framework runs in Cursor/VS Code. Generated systems can deploy to multiple platforms with different constraints (character limits, features, APIs).

### Quality Framework Terms

**Well-Architected Framework** — AWS framework with 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability) used to assess and design robust AI systems. Definitions in `knowledge_base/system_config.json`.

**GenAI Lens** — AWS Well-Architected Lens specifically for generative AI systems, covering Model Selection, Prompt Engineering, RAG Optimization, Multi-Agent Coordination, Responsible AI, and Knowledge Base Design.

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
