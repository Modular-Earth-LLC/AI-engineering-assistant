# System Architecture

**Multi-agent AI development framework** featuring supervisor-worker architecture pattern, shared knowledge base state management, and two-tier deployment model supporting three primary platforms: Cursor IDE, Claude Projects, and GitHub Copilot.

## Core Architecture

### Supervisor-Worker Pattern

```
User Request
     ↓
Supervisor Agent (Orchestrator)
     ↓
     ├─→ Requirements Agent      → Discovery, requirements
     ├─→ Architecture Agent       → Design, tech stack, estimates
     ├─→ Engineering Agent        → Prototypes, implementation
     ├─→ Deployment Agent         → Platform deployment, testing
     ├─→ Optimization Agent       → System improvement
     └─→ Prompt Engineering Agent → Prompt creation, optimization

Shared Knowledge Base
├─→ system_config.json     → Platform constraints, team info
├─→ user_requirements.json → Customer needs, use cases
└─→ design_decisions.json  → Architecture decisions, costs
```

### Agent Responsibilities

| Agent | Primary Function | Reads | Writes |
|-------|-----------------|-------|--------|
| **Supervisor** | Orchestration, routing | All files | None (routes only) |
| **Requirements** | Discovery, validation | system_config.json | user_requirements.json |
| **Architecture** | System design, planning | user_requirements.json, system_config.json | design_decisions.json |
| **Engineering** | Prototypes, code generation | user_requirements.json, design_decisions.json | Code files, prototypes |
| **Deployment** | Platform deployment | design_decisions.json | Deployment guides |
| **Optimization** | System improvement | All files | Recommendations |
| **Prompt Engineering** | Prompt creation | Optional: knowledge base | Prompts, optimization reports |

## Two-Tier Architecture

### Tier 1: This Repository (Development Workspace)

**Execution Environment**: Cursor IDE • Claude Projects • GitHub Copilot (VS Code)
**Purpose**: AI engineering assistance for developers  
**Components**: 6 specialized agents + Supervisor + User prompts

**Platform Options:**

**Cursor IDE Installation**:
```bash
.\scripts\deploy_cursor.ps1    # Windows
./scripts/deploy_cursor.sh     # Linux/Mac
```

**Claude Projects Installation**:
- Upload knowledge base files to Project Knowledge
- Add supervisor prompt to Custom Instructions

**GitHub Copilot Installation**:
- Configure `.github/copilot-instructions.md` with supervisor prompt
- Use Copilot Chat in VS Code

**Usage**: Agents run as custom chat modes (Cursor), project assistants (Claude), or Copilot instructions (VS Code)

### Tier 2: Generated Systems (External Deployment)

**Execution Environment**: Cursor IDE • Claude Projects • GitHub Copilot • AWS Bedrock • Self-hosted platforms
**Purpose**: Production AI systems for end users  
**Components**: Complete systems created by Tier 1 agents

**Deployment**: Platform-specific (guided by Deployment Agent)

### Visual Distinction

```
┌───────────────────────────────────────────────┐
│ TIER 1: YOUR WORKSPACE (This Repository)     │
│ Runs on: Cursor • Claude Projects • Copilot  │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Supervisor Agent                      │    │
│ │   ├─ Requirements Agent               │    │
│ │   ├─ Architecture Agent               │    │
│ │   ├─ Engineering Agent                │    │
│ │   ├─ Deployment Agent                 │    │
│ │   ├─ Optimization Agent               │    │
│ │   └─ Prompt Engineering Agent         │    │
│ └───────────────────────────────────────┘    │
│                                               │
│ Knowledge Base: JSON state files             │
└───────────────────────────────────────────────┘
                      ↓
                  Generates
                      ↓
┌───────────────────────────────────────────────┐
│ TIER 2: GENERATED SYSTEMS (External)          │
│ Deploy to: OpenAI • Claude • Bedrock • Self-hosted │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Financial Operations Assistant        │    │
│ │   • AWS Bedrock deployment            │    │
│ │   • 2-agent system                    │    │
│ └───────────────────────────────────────┘    │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Customer Support Bot                  │    │
│ │   • Claude Projects deployment        │    │
│ │   • Single agent + knowledge base     │    │
│ └───────────────────────────────────────┘    │
└───────────────────────────────────────────────┘
```

## Knowledge Base Architecture

### File Structure

**system_config.json**
```json
{
  "platform_constraints": {...},
  "team_info": {...},
  "well_architected_framework": {...}
}
```

**user_requirements.json**
```json
{
  "problem_statement": "...",
  "success_criteria": [...],
  "ai_suitability": {...}
}
```

**design_decisions.json**
```json
{
  "architecture": {...},
  "tech_stack": [...],
  "cost_estimate": {...},
  "project_plan": {...}
}
```

### Access Patterns

1. **Requirements Phase**: Requirements Agent writes user_requirements.json
2. **Architecture Phase**: Architecture Agent reads requirements, writes design_decisions.json
3. **Engineering Phase**: Engineering Agent reads both files to generate code
4. **Deployment Phase**: Deployment Agent reads design_decisions.json for deployment
5. **Optimization Phase**: Optimization Agent reads all files for analysis

## Workflow Patterns

### Complete System Development

```
1. User → Supervisor Agent: "Build financial operations assistant"
2. Supervisor → Requirements Agent
   → Gathers needs, writes user_requirements.json
3. Requirements → Architecture Agent (automatic handoff)
   → Designs system, writes design_decisions.json
4. Architecture → Engineering Agent
   → Builds prototype, generates code
5. Engineering → Deployment Agent
   → Creates deployment guide
6. User executes deployment → System runs on target platform
```

### System Improvement

```
1. User → Optimization Agent: "Analyze my system"
2. Optimization Agent reads knowledge base
3. Identifies improvement opportunities
4. May invoke Engineering Agent for code changes
5. Hands off to Deployment Agent if deployment needed
```

### Prompt Engineering

```
1. User → Prompt Engineering Agent: "Create code review assistant"
2. Agent gathers requirements interactively
3. Generates platform-optimized prompt
4. Validates character limits
5. Delivers copy-paste ready output
```

## Agent Collaboration

### Cross-Agent Communication

**Via Knowledge Base**: Agents read/write JSON files for persistent state  
**Via Supervisor**: Explicit handoffs through orchestration  
**Via User**: User can manually route between agents

### Example Collaboration

```
Optimization Agent identifies prompt needs
     ↓
Invokes Prompt Engineering Agent
     ↓
Prompt Engineering creates improved prompt
     ↓
Engineering Agent implements in code
     ↓
Deployment Agent deploys update
```

## File Organization

```
multi-agent-ai-development-framework/
├── supervisor_agent.system.prompt.md    # Entry point
├── ai_agents/                           # Specialized agents
│   ├── requirements_agent.system.prompt.md
│   ├── architecture_agent.system.prompt.md
│   ├── engineering_agent.system.prompt.md
│   ├── deployment_agent.system.prompt.md
│   ├── optimization_agent.system.prompt.md
│   └── prompt_engineering_agent.system.prompt.md
├── user_prompts/                        # Task instructions by category
│   ├── architecture/                    # 6 prompts
│   ├── requirements/                    # 4 prompts
│   ├── engineering/                     # 1 prompt
│   ├── deployment/                      # 2 prompts
│   ├── self_improvement/                # 9 prompts
│   ├── prompt_engineering/              # 6 prompts
│   └── proposals/                       # 4 prompts
├── knowledge_base/                      # JSON state management
│   ├── system_config.json               # Platform constraints
│   ├── user_requirements.json           # Business requirements
│   ├── design_decisions.json            # Architecture decisions
│   └── README.md                        # Knowledge base guide
├── docs/                                # Complete documentation (GitHub Pages-ready)
├── docs/                                # Technical documentation
├── templates/                           # Reusable templates
└── outputs/                             # Agent-generated content (created during use)
```

## Deployment Architecture

### Tier 1 Deployment (This Framework)

**Target**: Cursor IDE custom chat modes  
**Method**: Copy `.system.prompt.md` files to Cursor Settings → Chat → Custom Modes  
**Scope**: Single developer or team using Cursor

**Setup**:
1. Open Cursor → Settings → Chat → Custom Modes
2. Create new mode, paste `supervisor_agent.system.prompt.md`
3. Enable "All tools"
4. Repeat for specialized agents as needed

### Tier 2 Deployment (Generated Systems)

**Targets**: OpenAI, Claude, Bedrock, Cursor, self-hosted platforms  
**Method**: Platform-specific (guided by Deployment Agent)  
**Scope**: End users, production systems

**Process**:
1. Engineering Agent generates system components
2. Deployment Agent creates deployment guide
3. User executes platform-specific deployment
4. System runs on target platform

## Security Architecture

### Tier 1 Security (Development)
- No external API dependencies (runs locally in Cursor)
- File access limited to repository directory
- Knowledge base files stored locally
- No data transmission outside IDE

### Tier 2 Security (Deployment)
- Platform-specific security models
- Deployment Agent provides security guidance
- Architecture Agent considers security requirements
- Well-Architected Framework compliance

## Performance Characteristics

### Agent Response Time
- Supervisor routing: Immediate
- Requirements gathering: 5-10 minutes (interactive)
- Architecture design: 10-15 minutes
- Engineering prototyping: 15-30 minutes
- Deployment planning: 5-10 minutes

### Knowledge Base Performance
- JSON file I/O: Negligible overhead
- State persistence: Automatic
- Cross-agent handoff: Seamless with full context

## Extensibility

### Adding New Agents
1. Create `.system.prompt.md` file in `ai_agents/`
2. Define responsibilities and knowledge base access
3. Update Supervisor Agent routing logic
4. Add corresponding user prompts
5. Document in agent-relationships.md

### Adding User Prompts
1. Create `.user.prompt.md` in appropriate category
2. Follow existing prompt structure
3. Reference correct knowledge base files
4. Test with target agent

## References

- **README.md**: Quick start and system overview
- **docs/getting-started.md**: Step-by-step walkthrough
- **docs/workflow_guide.md**: Complete workflow documentation
- **docs/agent-architecture-and-collaboration.md**: Comprehensive agent guide and collaboration patterns
- **docs/agent-design-patterns.md**: Reusable AI agent design patterns
- **outputs/README.md**: Output directory structure and organization

## Version

**Current**: 1.0  
**Framework Platform**: Cursor IDE • GitHub Copilot • Claude Projects  
**Generated System Platforms**: OpenAI • Claude • Bedrock • Cursor • Self-hosted
