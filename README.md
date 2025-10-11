# Multi-Agent AI Development Framework

**Supervisor-worker architecture for building production AI systems.** Orchestrates specialized agents through the complete lifecycle: requirements → architecture → engineering → deployment. Supports Cursor IDE, GitHub Copilot, Claude Projects, AWS Bedrock.

**Build production AI systems in days, not months.** This open-source framework eliminates 70% of repetitive AI development tasks, letting you focus on solving real problems instead of reinventing infrastructure.

**Deploy this framework to:** Cursor IDE • GitHub Copilot • Claude Projects  
**Build systems for:** Cursor IDE • GitHub Copilot • Claude Projects • AWS Bedrock • Self-hosted platforms

## Why This Framework Exists

AI engineers waste weeks on repetitive tasks: structuring requirements, estimating costs, writing boilerplate code, creating deployment guides. Every new project starts from scratch. Every team reinvents the same wheels.

**This framework changes that.** Six specialized agents handle the heavy lifting automatically:
- **Requirements gathering**: 2 hours instead of 2 days
- **Architecture design**: Production-ready designs in 4 hours, not 2 weeks
- **Cost estimation**: Accurate projections without spreadsheets
- **Prototype development**: Working code in days, not weeks
- **Deployment planning**: Platform-specific guides generated automatically

**Real returns**: Teams report 3-5x faster project delivery, 60% reduction in rework, and consistent quality across all projects.

## Who This Helps

**Junior AI Engineers**: Learn industry best practices from agents that embody AWS Well-Architected principles. Build confidence through guided workflows. Ship production systems without years of experience.

**Senior Engineers**: Eliminate grunt work. Focus on complex architecture decisions while agents handle documentation, cost estimation, and deployment planning. Mentor teams at scale through consistent, repeatable processes.

**Freelance Consultants**: Accelerate client delivery from months to weeks. Generate professional proposals, accurate estimates, and comprehensive documentation automatically. Win more projects with faster turnarounds.

**Engineering Managers**: Standardize team processes. Reduce knowledge silos. Onboard new engineers 5x faster. Deliver predictable results regardless of individual experience levels.

**CTOs and Technical Leaders**: De-risk AI investments with systematic requirements validation and cost projections. Scale engineering capacity without proportional headcount growth. Maintain quality across distributed teams.

## Understanding Multi-Agent AI Systems

**Why multiple agents beat single agents**: Traditional AI assistants try to do everything—answer questions, write code, analyze data, manage workflows. They're generalists, mediocre at each task. Multi-agent systems flip this: each agent specializes in one domain and masters it.

**Real-world analogy**: You don't hire one person to do accounting, engineering, marketing, and legal. You build a team of specialists. Multi-agent AI systems work the same way.

**Key advantages**:
- **Cost efficiency**: Use expensive models (GPT-4, Claude Opus) only for complex reasoning. Use fast, cheap models (GPT-3.5, Claude Haiku) for simple tasks. Result: 60-80% cost reduction.
- **Better accuracy**: Specialized prompts outperform generic ones. Each agent knows its domain deeply, avoiding the confusion of context-switching.
- **Scalability**: Add new capabilities by adding new agents, not by bloating existing ones. Replace underperforming agents without touching the rest.
- **Maintainability**: Debug one agent at a time. Update prompts independently. Clear separation of concerns.

## The Well-Architected Framework Advantage

This framework enforces AWS Well-Architected principles—the industry standard for building reliable, secure, and efficient systems. Six pillars ensure your AI systems are production-ready:

**Operational Excellence**: Automated documentation, consistent workflows, clear monitoring strategies  
**Security**: Input validation, prompt injection protection, data encryption, access control  
**Reliability**: Fault tolerance, graceful degradation, retry logic, comprehensive testing  
**Performance Efficiency**: Model right-sizing, caching strategies, latency optimization  
**Cost Optimization**: Smart model selection, API call reduction, infrastructure right-sizing  
**Sustainability**: Efficient resource utilization, minimal computational waste

**The GenAI Lens**: AWS extended the Well-Architected Framework specifically for generative AI with best practices for:
- Model selection (matching capability to task complexity)
- Prompt engineering (structured, testable, version-controlled)
- RAG optimization (retrieval-augmented generation patterns)
- Multi-agent coordination (handoffs, shared state, error handling)
- Responsible AI (bias detection, content filtering, explainability)
- Knowledge base design (structured data, efficient retrieval, versioning)

**Why this matters**: Following established patterns means your systems are reliable, secure, and maintainable from day one. No trial-and-error. No learning from expensive production failures. Battle-tested architectures built in.

## Overview

Building reliable AI systems demands expertise across requirements analysis, system architecture, software engineering, and platform deployment. Most teams struggle with inconsistent processes, knowledge silos, and reinventing solutions for every project.

**This framework solves that.** Six specialized agents embody industry best practices, AWS Well-Architected principles, and battle-tested workflows. Each agent is an expert in its domain, working together to deliver complete, production-ready AI systems.

**What it does**: Transforms vague ideas into deployable AI systems through systematic workflows. Handles requirements discovery, architecture design, cost estimation, prototype development, and deployment planning automatically.

**Where THIS framework runs**: Cursor IDE, GitHub Copilot (VS Code), or Claude Projects—choose the platform that fits your workflow.

**What it BUILDS**: Complete AI systems deployable to Cursor, GitHub Copilot, Claude Projects, AWS Bedrock, or self-hosted platforms. From simple chatbots to complex multi-agent systems.

## Quick Start

### Choose Your Deployment Platform

**Option A: Cursor IDE** (Recommended for solo developers)
- Full multi-agent support (7 custom chat modes)
- Local execution with file system access
- Best for: Individual developers, rapid iteration, full control

**Option B: GitHub Copilot** (VS Code integration)
- Native VS Code integration with familiar interface
- Git-based collaboration for teams
- Best for: VS Code users, GitHub-centric teams, enterprise environments

**Option C: Claude Projects** (Cloud collaboration)
- Cloud-based with persistent project knowledge
- No local setup required
- Best for: Remote teams, collaborative design, distributed workflows

### Platform-Specific Setup

**Cursor (5 minutes):**
1. **Install**: Copy `supervisor_agent.system.prompt.md` to Cursor Settings → Chat → Custom Modes
2. **Start**: Open Cursor AI Pane, select "Supervisor Agent"
3. **Request**: "Build a customer support chatbot"
4. **Follow**: Requirements → Architecture → Engineering → Deployment
5. **Outputs**: All deliverables saved to `outputs/` directory

**GitHub Copilot (10 minutes):**
1. **Configure**: Create `.github/copilot-instructions.md` in your workspace
2. **Paste**: Contents of `supervisor_agent.system.prompt.md`
3. **Start**: Open VS Code, invoke Copilot Chat
4. **Request**: "Build a customer support chatbot"
5. **Outputs**: Copy deliverables to your workspace

**Claude Projects (10 minutes):**
1. **Create**: New Claude Project named "Multi-Agent AI Development Framework"
2. **Upload**: All files from `knowledge_base/` to Project Knowledge
3. **Configure**: Paste `supervisor_agent.system.prompt.md` into Custom Instructions
4. **Request**: "Build a customer support chatbot"
5. **Outputs**: Copy deliverables to your repository or documentation

**Framework deployment guide:** [docs/deployment-guide.md](docs/deployment-guide.md) (Deploy THIS repository)  
**Generated systems deployment:** [docs/platform_deployment.md](docs/platform_deployment.md) (Deploy systems you built)

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

### Clone Repository

```bash
git clone https://github.com/paulpham157/multi-agent-ai-development-framework.git
cd multi-agent-ai-development-framework
```

### Deploy to Platform

Choose your platform and follow the setup guide:

**Cursor IDE** (5-10 minutes):
1. Open Cursor → Settings → Chat → Custom Modes
2. Create mode: "Supervisor Agent"
3. Paste `supervisor_agent.system.prompt.md`
4. Enable "All tools" → Save
5. Repeat for specialized agents (optional)

**Claude Projects** (10-15 minutes):
1. Create new project at [claude.ai/projects](https://claude.ai/projects)
2. Upload `knowledge_base/*.json` to Project Knowledge
3. Paste `supervisor_agent.system.prompt.md` to Custom Instructions
4. Save and start using

**Complete deployment guide:** [docs/deployment-guide.md](docs/deployment-guide.md)

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

### Financial Operations AI System
**Challenge**: Organization needs AI-powered financial operations automation  
**Workflow**: Work alongside human AI engineer and financial operations consultant  
**Process**: Requirements discovery → System architecture → Multi-agent design → Prototype development  
**Output**: Multi-agent AI team for financial operations (invoicing, expense tracking, analytics)  
**Result**: Production-ready system architecture deployable to AWS Bedrock, Claude Projects, or custom infrastructure

### Customer Support Bot
**Challenge**: E-commerce needs 24/7 support with product knowledge  
**Workflow**: Complete lifecycle through all agents  
**Output**: Single agent with knowledge base for Claude Projects  
**Result**: Team-accessible support assistant with knowledge retrieval

### Code Review Assistant
**Challenge**: Development team needs automated Python code review  
**Workflow**: Prompt Engineering Agent only (5-10 minutes)  
**Output**: Security-focused prompt for OpenAI GPT  
**Result**: Copy-paste deployment ready for immediate use

## Platform Deployment

### Where This Framework Runs
**Cursor IDE** (or VS Code with Copilot) — Required for the agents in this repository

### Where Generated Systems Deploy
- **OpenAI Custom GPTs**: Character limit ~1,500
- **Anthropic Claude Projects**: Character limit ~32,000
- **AWS Bedrock Agents**: Production-grade infrastructure
- **Cursor IDE**: Custom chat modes for teams
- **Self-hosted platforms**: Ollama, LangChain, AutoGen, custom LLM infrastructure, on-premise deployments

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

**Essential Reading:**
- **[README.md](README.md)**: Quick start and system overview (you are here)
- **[docs/getting-started.md](docs/getting-started.md)**: Step-by-step walkthrough for first project
- **[docs/workflow_guide.md](docs/workflow_guide.md)**: Complete workflow documentation
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: System architecture and design

**Reference Documentation:**
- **[docs/agent-architecture-and-collaboration.md](docs/agent-architecture-and-collaboration.md)**: Comprehensive agent guide, capabilities, and collaboration patterns
- **[docs/agent-design-patterns.md](docs/agent-design-patterns.md)**: Reusable AI agent design patterns
- **[docs/deployment-guide.md](docs/deployment-guide.md)**: Deploy framework to Cursor/Claude/Copilot (Tier 1)
- **[docs/platform_deployment.md](docs/platform_deployment.md)**: Deploy generated systems to target platforms (Tier 2)
- **[docs/executive_overview.md](docs/executive_overview.md)**: Business perspective and value proposition

**Specialized Documentation:**
- **[knowledge_base/README.md](knowledge_base/README.md)**: Knowledge base usage and schema guide
- **[user_prompts/self_improvement/README.md](user_prompts/self_improvement/README.md)**: Self-improvement prompts guide
- **[outputs/README.md](outputs/README.md)**: Output directory structure and organization
- **[templates/](templates/)**: Reusable templates for requirements, architecture, and checklists

## User Prompts

Specialized task instructions organized by category in `user_prompts/`:
- `requirements/`: Discovery tasks (4 prompts)
- `architecture/`: System design tasks (6 prompts)
- `engineering/`: Prototype generation (1 prompt)
- `deployment/`: Deployment and testing (2 prompts)
- `self_improvement/`: Improve agents in THIS repo (10 prompts)
- `prompt_engineering/`: Prompt creation and optimization (5 prompts)
- `proposals/`: Executive presentations (4 prompts)

**Total**: 32 user prompts organized across 7 categories

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

**Meta-level** — This Multi-Agent AI Development Framework itself, running in Cursor IDE, GitHub Copilot, or Claude Projects to help developers build AI systems.

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

We welcome contributions! See **[CONTRIBUTING.md](CONTRIBUTING.md)** for comprehensive guidelines.

**Quick Start:**
- **Agent improvements**: Use `user_prompts/self_improvement/` prompts
- **Bug fixes**: Fork, fix, test, submit PR
- **Documentation**: PRs welcome for clarity improvements
- **Questions**: Open GitHub Discussion

**All contributions** follow conventional commits and include tests where applicable.

## License

MIT License — Full commercial use permitted

## Repository

[Multi-Agent AI Development Framework](https://github.com/paulpham157/multi-agent-ai-development-framework) — Open-source production-ready framework for building AI systems across Cursor IDE, GitHub Copilot, and Claude Projects
