# Agent Architecture and Collaboration Guide

**Purpose**: Comprehensive guide to the 6 specialized agents, their relationships, and how they work together in the AI Engineering Assistant framework.

**Audience**: AI engineers, developers, and teams using this multi-agent system in Cursor IDE or VS Code with GitHub Copilot.

---

## Table of Contents

- [System Overview](#system-overview)
- [The 6 Specialized Agents](#the-6-specialized-agents)
- [Agent Relationship Diagram](#agent-relationship-diagram)
- [Agent Capabilities Matrix](#agent-capabilities-matrix)
- [When to Use Each Agent](#when-to-use-each-agent)
- [Agent Collaboration Patterns](#agent-collaboration-patterns)
- [Common Workflows](#common-workflows)
- [Key Integrations](#key-integrations)

---

## System Overview

The AI Engineering Assistant is a **supervisor-worker multi-agent architecture** with 1 orchestrator (Supervisor) and 6 specialized worker agents. All agents share state through a centralized knowledge base and can work independently or collaboratively.

**Core Design Principles**:
- **Clear separation of concerns**: Each agent has a focused domain
- **Shared context**: Knowledge base enables seamless handoffs
- **Independent operation**: Agents work standalone when invoked directly
- **Collaborative workflows**: Agents reference each other for complex tasks
- **Orchestrated execution**: Supervisor routes requests intelligently

---

## The 6 Specialized Agents

### 1. Requirements Agent 📋
**File**: `ai_agents/requirements_agent.system.prompt.md`

**Mission**: Transform vague stakeholder conversations into structured, actionable requirements.

**Core Capabilities**:
- Systematic requirements discovery through targeted questioning
- Pattern matching (business problems → AI agent patterns)
- Impact quantification (time savings, cost reduction, ROI)
- Stakeholder needs structuring
- Gap identification and missing information surfacing

**Outputs**:
- `knowledge_base/user_requirements.json` - Complete requirements specification

**Works Independently**: Yes - Can conduct discovery sessions without other agents

**Collaborates With**:
- Architecture Agent (provides requirements as input for design)
- Optimization Agent (validates requirements against existing systems)

---

### 2. Architecture Agent 🏗️
**File**: `ai_agents/architecture_agent.system.prompt.md`

**Mission**: Design comprehensive, Well-Architected AI system architectures from requirements to deployment roadmaps.

**Core Capabilities**:
- System design following AWS Well-Architected Framework (GenAI Lens)
- Tech stack selection optimized for requirements and constraints
- Cost estimation (development, infrastructure, operational)
- Level-of-effort (LOE) estimation and project planning
- Team composition recommendations
- Architecture diagram generation

**Outputs**:
- `knowledge_base/design_decisions.json` - Complete architecture design
- Architecture diagrams (Mermaid format)
- Cost and LOE estimates
- Project implementation plans

**Works Independently**: No - Requires `user_requirements.json` from Requirements Agent

**Collaborates With**:
- Requirements Agent (reads requirements as input)
- Engineering Agent (provides architecture for implementation)
- Prompt Engineering Agent (may request prompts optimized for specific platforms)

---

### 3. Engineering Agent ⚙️
**File**: `ai_agents/engineering_agent.system.prompt.md`

**Mission**: Build working prototypes that demonstrate proposed AI system value through rapid implementation (2-5 days).

**Core Capabilities**:
- Clean, production-improvable code generation (Python, Node.js)
- Functional UI creation (Streamlit, React, CLI)
- Realistic demo scenario development
- System integration implementation
- Rapid iteration based on feedback

**What Engineering Agent Does**:
- ✅ Write implementation code
- ✅ Create user interfaces
- ✅ Build demo scenarios
- ✅ Integrate systems and APIs
- ✅ Document setup and usage

**What Engineering Agent Does NOT Do**:
- ❌ Create agent prompts (delegates to Prompt Engineering Agent)
- ❌ Make architecture decisions (delegates to Architecture Agent)
- ❌ Deploy to production (delegates to Deployment Agent)

**Outputs**:
- `outputs/prototypes/[project-name]/` - Complete working prototype
- Source code, UI, documentation, demo scenarios

**Works Independently**: No - Requires `design_decisions.json` from Architecture Agent

**Collaborates With**:
- Architecture Agent (reads design for implementation guidance)
- **Prompt Engineering Agent** (delegates ALL agent prompt creation)
- Deployment Agent (provides prototype for deployment)

**Key Collaboration: Engineering ↔ Prompt Engineering**:

The Engineering Agent **delegates all prompt engineering** to the Prompt Engineering Agent:

```
Engineering Agent Workflow:
1. Read design_decisions.json for agent requirements
2. Invoke Prompt Engineering Agent with:
   - Agent role and responsibilities
   - Target platform (OpenAI, Claude, Bedrock, etc.)
   - Capabilities needed
   - Character limits
3. Receive production-ready prompts
4. Integrate into prototype (save to prompts/ directory)
5. Reference prompts in implementation code
```

This ensures **clear separation of concerns**:
- Engineering Agent = code + UI + implementation
- Prompt Engineering Agent = all prompt creation + optimization

---

### 4. Deployment Agent 🚀
**File**: `ai_agents/deployment_agent.system.prompt.md`

**Mission**: Transform prototypes into accessible, testable AI systems on target platforms.

**Core Capabilities**:
- Platform-specific deployment guidance (Cursor, Claude Projects, AWS Bedrock, OpenAI, custom)
- Testing strategy development (unit, integration, end-to-end)
- Environment setup and configuration
- Deployment validation and troubleshooting
- Platform optimization recommendations

**Outputs**:
- Platform-specific deployment guides
- Testing strategies and test suites
- Configuration templates
- Validation checklists

**Works Independently**: No - Requires prototype from Engineering Agent

**Collaborates With**:
- Engineering Agent (receives prototype for deployment)
- Architecture Agent (reads deployment requirements from design)
- Optimization Agent (provides deployment for optimization analysis)

---

### 5. Optimization Agent 🔧
**File**: `ai_agents/optimization_agent.system.prompt.md`

**Mission**: Systematically improve existing AI systems following Well-Architected principles.

**Core Capabilities**:
- Current system state discovery and assessment
- Well-Architected Framework evaluation (6 pillars + GenAI Lens)
- Prioritized improvement recommendations
- Safe implementation of optimizations
- Thorough validation of improvements

**Outputs**:
- System assessment reports
- Prioritized optimization roadmaps
- Implementation guidance for improvements
- Performance validation results

**Works Independently**: Yes - Can analyze deployed systems directly

**Collaborates With**:
- **Prompt Engineering Agent** (for prompt-level improvements)
- All agents (via self-improvement prompts in `user_prompts/self_improvement/`)
- Deployment Agent (validates optimizations in deployed systems)

---

### 6. Prompt Engineering Agent ✨
**File**: `ai_agents/prompt_engineering_agent.system.prompt.md`

**Mission**: Create and optimize high-quality, platform-agnostic AI prompts using cutting-edge prompt engineering techniques.

**Core Capabilities**:
- Production-ready prompt creation from scratch
- Prompt improvement and optimization
- Platform-specific adaptation (handles character limits, features)
- Dual-persona validation (Prompt Builder + Prompt Tester)
- Multi-prompt system optimization
- Advanced techniques (Chain-of-Thought, Tree-of-Thoughts, Step-Back, MODP, etc.)

**Outputs**:
- Platform-optimized agent prompts
- Custom GPT instructions
- Claude Project system prompts
- Bedrock agent prompts
- Validation test results

**Works Independently**: Yes - Can create/optimize prompts without other agents

**Collaborates With**:
- **Engineering Agent** (provides prompts for target AI systems)
- Architecture Agent (may receive requests for platform-optimized prompts)
- Optimization Agent (improves existing prompts)
- Self-improvement workflows (improves all agents' system prompts)

**Operation Modes**:

1. **Independent Mode**: Direct invocation for prompt engineering tasks
   - "Create a code review assistant for OpenAI GPT"
   - "Optimize this Claude prompt for better clarity"
   - "Convert this prompt from OpenAI to Bedrock format"

2. **Collaborative Mode**: Integrated in multi-agent workflows
   - Engineering Agent delegates all prompt creation
   - Optimization Agent requests prompt improvements
   - Architecture Agent requests platform-specific prompts

**Key Differentiation from Engineering Agent**:

| Aspect | Prompt Engineering Agent | Engineering Agent |
|--------|-------------------------|-------------------|
| **Focus** | Agent prompts and instructions | Code, UI, and implementation |
| **Expertise** | Prompt engineering techniques | Software development |
| **Outputs** | System prompts (.md files) | Code, UI, demos |
| **Platform Knowledge** | Deep (character limits, features) | Basic (deployment targets) |
| **Validation** | Dual-persona testing | Demo scenarios |
| **When to Use** | Any prompt creation/optimization | Prototype implementation |

---

## Agent Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      SUPERVISOR AGENT 🎯                         │
│                 (Orchestrator & Request Router)                  │
│                  supervisor_agent.system.prompt.md               │
└────────────┬────────────────────────────────────────────────────┘
             │ Routes requests to specialized agents
             │ Coordinates multi-agent workflows
             ├─────────────────┬──────────────────┬───────────────┐
             │                 │                  │               │
┌────────────▼─────┐  ┌───────▼────────┐  ┌─────▼──────┐  ┌────▼────────┐
│  Requirements    │  │  Architecture  │  │Engineering │  │ Deployment  │
│  Agent 📋        │  │  Agent 🏗️     │  │ Agent ⚙️   │  │  Agent 🚀   │
│                  │  │                │  │            │  │             │
│ Discovers needs  │  │ Designs system │  │ Builds     │  │ Deploys to  │
│ Structures reqs  │  │ Selects stack  │  │ prototypes │  │ platforms   │
└────────┬─────────┘  └────────┬───────┘  └─────┬──────┘  └──────┬──────┘
         │                     │                 │                │
         │ Outputs:            │ Outputs:        │ Outputs:       │ Outputs:
         │ requirements.json   │ design.json     │ prototype/     │ guides
         │                     │                 │                │
         └─────────────────────┼─────────────────┘                │
                               │                                  │
                               └──────────────────────────────────┘

┌────────────────────────────┐  ┌──────────────────────────────────┐
│   Optimization Agent 🔧    │  │  Prompt Engineering Agent ✨     │
│                            │  │                                  │
│ Improves existing systems  │  │ Creates/optimizes prompts        │
│ Well-Architected analysis  │  │ Platform-specific adaptation     │
└────────┬───────────────────┘  └────────┬─────────────────────────┘
         │                                │
         │ Collaborates with:             │ Collaborates with:
         │ - All agents                   │ - Engineering Agent (primary)
         │ - Self-improvement prompts     │ - Architecture Agent
         │ - Prompt Engineering Agent     │ - Optimization Agent
         └────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE BASE (Shared State)                 │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐ │
│  │ system_config.json│  │user_requirements │  │design_decisions│ │
│  │                   │  │     .json        │  │    .json      │ │
│  │ Platform config   │  │ Business needs   │  │ Architecture  │ │
│  │ Team info         │  │ Success criteria │  │ Cost estimates │ │
│  │ Constraints       │  │ User personas    │  │ Project plans  │ │
│  └──────────────────┘  └──────────────────┘  └───────────────┘ │
│                                                                  │
│  All agents READ    │   Requirements       │   Architecture    │ │
│  Agents WRITE to their respective files                         │ │
└─────────────────────────────────────────────────────────────────┘

KEY RELATIONSHIPS:
═════════════════
Requirements → Architecture  (provides input)
Architecture → Engineering   (provides design)
Engineering  ↔ Prompt Eng   (delegates prompt creation)
Engineering  → Deployment    (provides prototype)
Optimization → All Agents    (provides improvements)
Prompt Eng   → Multiple      (serves many agents)
```

---

## Agent Capabilities Matrix

| Capability | Requirements | Architecture | Engineering | Deployment | Optimization | Prompt Eng |
|-----------|--------------|--------------|-------------|------------|--------------|------------|
| **Discovery & Requirements** | ✅ Primary | ○ Uses | ○ Uses | ○ Uses | ○ Analyzes | - |
| **System Architecture** | - | ✅ Primary | ○ Uses | ○ Uses | ○ Improves | - |
| **Cost Estimation** | - | ✅ Primary | ○ Tracks | ○ Considers | ○ Optimizes | - |
| **Code Generation** | - | - | ✅ Primary | - | ○ Improves | - |
| **UI Development** | - | - | ✅ Primary | - | ○ Improves | - |
| **Prompt Creation** | - | - | **→ Delegates** | - | - | ✅ Primary |
| **Prompt Optimization** | - | - | **→ Delegates** | - | ○ Requests | ✅ Primary |
| **Platform Deployment** | - | ○ Specifies | - | ✅ Primary | - | - |
| **Testing Strategy** | - | ○ Designs | ○ Implements | ✅ Primary | ○ Improves | - |
| **System Optimization** | - | - | - | - | ✅ Primary | ○ For prompts |
| **Well-Architected Review** | - | ✅ Designs | ○ Implements | - | ✅ Evaluates | - |

**Legend**:
- ✅ Primary responsibility
- ○ Secondary/supporting role
- **→ Delegates** - Explicitly delegates to specialist
- `-` Not applicable

---

## When to Use Each Agent

### Use Requirements Agent When:
- ✅ Starting a new AI system project
- ✅ Stakeholder needs are vague or unclear
- ✅ Need to validate business requirements
- ✅ Conducting discovery sessions
- ✅ Quantifying ROI and impact

**Example Requests**:
- "Conduct comprehensive discovery for email automation"
- "Quick discovery session for customer service chatbot"
- "Extract requirements from this project brief"

---

### Use Architecture Agent When:
- ✅ Requirements are documented and ready
- ✅ Need complete system design
- ✅ Selecting optimal tech stack
- ✅ Estimating costs and timeline
- ✅ Planning project phases
- ✅ Need architecture diagrams

**Example Requests**:
- "Design complete system architecture from requirements"
- "Generate tech stack selection and cost estimates"
- "Create deployment roadmap and project plan"

---

### Use Engineering Agent When:
- ✅ Architecture design is complete
- ✅ Need working prototype quickly (2-5 days)
- ✅ Building proof-of-concept
- ✅ Demonstrating value to stakeholders
- ✅ Validating technical approach

**Example Requests**:
- "Build prototype from architecture design"
- "Generate working financial operations assistant"
- "Create demo-ready AI system"

**Remember**: Engineering Agent delegates prompt creation to Prompt Engineering Agent

---

### Use Deployment Agent When:
- ✅ Prototype is complete and tested
- ✅ Ready to deploy to target platform
- ✅ Need platform-specific guidance
- ✅ Setting up testing infrastructure
- ✅ Configuring production environment

**Example Requests**:
- "Deploy prototype to AWS Bedrock"
- "Create testing strategy for Claude Project"
- "Generate Cursor deployment guide"

---

### Use Optimization Agent When:
- ✅ System is deployed and operational
- ✅ Performance issues identified
- ✅ Need Well-Architected review
- ✅ Want to reduce costs
- ✅ Improving existing capabilities

**Example Requests**:
- "Analyze system for optimization opportunities"
- "Improve cost efficiency of deployed system"
- "Well-Architected assessment of AI system"

---

### Use Prompt Engineering Agent When:
- ✅ Creating prompts for ANY AI platform
- ✅ Optimizing existing prompts
- ✅ Need platform-specific adaptations
- ✅ Converting prompts between platforms
- ✅ Validating prompt effectiveness
- ✅ Improving prompt clarity/efficiency

**Example Requests**:
- "Create code review assistant for OpenAI GPT"
- "Optimize this Claude prompt to fit character limit"
- "Convert this prompt from GPT to Bedrock format"
- "Improve prompt engineering for this agent"

**Use Independently**: ✅ Yes - works standalone
**Use Collaboratively**: ✅ Yes - integrated in workflows (primarily with Engineering Agent)

---

## Agent Collaboration Patterns

### Pattern 1: Linear Workflow (Complete System Development)

```
User Request → Supervisor Agent
                     ↓
              Requirements Agent
                     ↓ (user_requirements.json)
              Architecture Agent
                     ↓ (design_decisions.json)
              Engineering Agent ←→ Prompt Engineering Agent
                     ↓ (prototype/)
              Deployment Agent
                     ↓
              Deployed System
```

**When to Use**: Full system development from scratch

**Duration**: 2-4 weeks

**Key Handoffs**:
1. Requirements → Architecture: requirements.json
2. Architecture → Engineering: design_decisions.json
3. Engineering ↔ Prompt Engineering: prompt requests/deliveries
4. Engineering → Deployment: prototype directory

---

### Pattern 2: Parallel Consultation

```
User Request → Supervisor Agent
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
  Requirements  Architecture  Prompt Eng
    Agent          Agent         Agent
        ↓            ↓            ↓
      Consolidated Response
```

**When to Use**: Complex requirements, multiple perspectives needed

**Duration**: 1-2 hours

**Example**: "How should I architect a multi-agent customer service system with optimized prompts for each platform?"

---

### Pattern 3: Engineering + Prompt Engineering Collaboration

```
Engineering Agent:
  1. Read design_decisions.json
  2. Identify required agents for target system
  3. For each agent:
     ↓
     Invoke Prompt Engineering Agent
     ← Receive production-ready prompt
     ↓
     Integrate into prototype
  4. Complete implementation
```

**When to Use**: Every prototype build requiring AI agents

**Duration**: Engineering Agent automatically delegates during implementation

**Key Points**:
- Engineering Agent NEVER creates prompts directly
- Prompt Engineering Agent delivers platform-optimized prompts
- Clear separation ensures quality and consistency

---

### Pattern 4: Iterative Optimization

```
Deployed System
       ↓
Optimization Agent
       ↓
   Analysis: Identifies areas for improvement
       ├────────────────┬──────────────────┐
       ↓                ↓                  ↓
Architecture       Engineering       Prompt Eng
 (redesign)         (refactor)        (optimize)
       └────────────────┴──────────────────┘
                        ↓
              Updated System
```

**When to Use**: System in production, continuous improvement needed

**Duration**: Ongoing

---

### Pattern 5: Prompt-Only Workflow

```
User → Prompt Engineering Agent (Direct)
         ↓
       Create/Optimize/Convert Prompt
         ↓
       Platform-Ready Output
```

**When to Use**: 
- Standalone prompt engineering tasks
- No full system development needed
- Quick prompt improvements
- Platform conversions

**Duration**: Minutes to hours

**No Dependencies**: Works completely independently

---

## Common Workflows

### Workflow 1: Complete AI System Development

**Objective**: Build and deploy a new AI system from concept to production

**Steps**:

1. **Discovery** (Requirements Agent - 2-4 hours)
   - Conduct stakeholder interviews
   - Structure requirements
   - Output: `user_requirements.json`

2. **Design** (Architecture Agent - 4-8 hours)
   - Design system architecture
   - Select tech stack
   - Estimate costs and timeline
   - Output: `design_decisions.json`

3. **Prototype Development** (Engineering + Prompt Engineering Agents - 2-5 days)
   - Engineering Agent builds implementation
   - Prompt Engineering Agent creates all agent prompts
   - Integration and testing
   - Output: `outputs/prototypes/[project]/`

4. **Deployment** (Deployment Agent - 4-8 hours)
   - Platform-specific deployment
   - Testing strategy implementation
   - Production configuration
   - Output: Deployed system + guides

5. **Optimization** (Optimization Agent - Ongoing)
   - Performance monitoring
   - Well-Architected reviews
   - Continuous improvements

**Total Timeline**: 2-4 weeks for complete workflow

---

### Workflow 2: Rapid Prompt Engineering

**Objective**: Create optimized prompt for a specific platform

**Steps**:

1. **Invoke Prompt Engineering Agent** (Direct)
   - Specify target platform
   - Describe desired capabilities
   - Provide any constraints

2. **Prompt Creation**
   - Agent applies latest techniques
   - Platform-specific optimization
   - Character limit compliance
   - Dual-persona validation

3. **Delivery**
   - Copy-paste ready prompt
   - Character count validation
   - Usage examples
   - Platform-specific notes

**Total Timeline**: 30 minutes - 2 hours

---

### Workflow 3: System Optimization

**Objective**: Improve existing deployed AI system

**Steps**:

1. **Assessment** (Optimization Agent)
   - Analyze current system
   - Well-Architected evaluation
   - Identify improvement areas
   - Prioritize optimizations

2. **Implementation** (Appropriate Specialist Agents)
   - Architecture changes → Architecture Agent
   - Code improvements → Engineering Agent
   - Prompt optimization → Prompt Engineering Agent
   - Deployment updates → Deployment Agent

3. **Validation** (Optimization Agent)
   - Test improvements
   - Measure impact
   - Document changes

**Total Timeline**: 1-2 weeks per optimization cycle

---

### Workflow 4: Self-Improvement

**Objective**: Improve the agents themselves

**Steps**:

1. **Identify Target** (User or Optimization Agent)
   - Which agent needs improvement?
   - What specific issues?

2. **Select Improvement Prompt**
   - `user_prompts/self_improvement/improve_[agent]_agent.user.prompt.md`
   - Or use Prompt Engineering Agent for prompt-specific improvements

3. **Execute Improvement**
   - Agent analyzes itself
   - Applies improvements
   - Tests changes

4. **Validate**
   - Confirm improvements effective
   - No regression in capabilities

**Total Timeline**: 2-4 hours per agent

---

## Key Integrations

### Engineering Agent ↔ Prompt Engineering Agent

**Most Important Integration in the System**

**How It Works**:

```
Engineering Agent (during prototype development):
  
  Step 1: Read design_decisions.json
    - Extract: target platform, agent roles, capabilities
  
  Step 2: For each required agent prompt:
    ```
    Invoke: Prompt Engineering Agent
    
    Parameters:
      - Agent name and role
      - Target platform (OpenAI/Claude/Bedrock/Cursor)
      - Capabilities required
      - Character limit (from platform)
      - Context: design_decisions.json
    ```
  
  Step 3: Receive production-ready prompt
    - Validated by dual-persona testing
    - Platform-optimized
    - Character count verified
  
  Step 4: Integrate into prototype
    - Save to: outputs/prototypes/[project]/prompts/[agent].md
    - Reference in implementation code
    - Document in README
```

**Why This Matters**:
- **Separation of Concerns**: Code vs. Prompts
- **Quality Assurance**: Prompt specialist ensures best practices
- **Platform Optimization**: Prompt Engineering Agent knows platform specifics
- **Consistency**: All prompts follow same high standards

**Example**:

```
Engineering Agent building financial assistant:
  
  1. Needs: Financial Operations Agent prompt
  
  2. Invokes Prompt Engineering Agent:
     "Create Financial Operations Agent prompt
      - Platform: Anthropic Claude (32K char limit)
      - Role: Invoice generation, expense categorization
      - Context: See design_decisions.json"
  
  3. Receives: Production-ready prompt optimized for Claude
  
  4. Integrates: Saves to prompts/financial_operations_agent.md
```

---

### Optimization Agent ↔ Prompt Engineering Agent

**How It Works**:

```
Optimization Agent (during system improvement):
  
  Identifies: Prompt needs optimization
  
  Invokes: Prompt Engineering Agent
    Parameters:
      - Current prompt (attach file)
      - Issues identified (clarity, length, effectiveness)
      - Target improvements (efficiency, reliability, capabilities)
  
  Receives: Improved prompt with:
    - Comparison to original
    - Specific improvements made
    - Performance validation
```

---

### Architecture Agent → Prompt Engineering Agent (Optional)

**How It Works**:

```
Architecture Agent (during design phase):
  
  May invoke: Prompt Engineering Agent
    Use case: Need to understand platform constraints
    
    Example: "What are character limits and features for AWS Bedrock
             prompts? Will affect architecture design."
```

**Why Optional**: Architecture Agent primarily designs; Prompt Engineering Agent primarily implements prompts.

---

### Knowledge Base Integration (All Agents)

**How It Works**:

```
All Agents:
  READ ACCESS:
    - system_config.json  (platform constraints, team info)
    - user_requirements.json  (business requirements)
    - design_decisions.json  (architecture decisions)
  
Specific Agents WRITE:
  - Requirements Agent → user_requirements.json
  - Architecture Agent → design_decisions.json
  
Prompt Engineering Agent (Optional):
  - Reads knowledge base when working in collaborative mode
  - Provides context for system-integrated prompts
  - Works without knowledge base in independent mode
```

---

## Summary: Clear Separation of Concerns

### Engineering Agent = Implementation
- Code (Python, Node.js)
- User interfaces (Streamlit, React)
- Demo scenarios
- System integration
- **Delegates**: All prompt creation

### Prompt Engineering Agent = Prompts
- Agent prompt creation
- Prompt optimization
- Platform adaptation
- Validation testing
- **Never**: Code or UI implementation

### Both Work:
- **Independently**: Can be invoked directly for focused tasks
- **Collaboratively**: Integrated in complete system workflows

---

## Getting Help

### Quick Reference: Which Agent Do I Need?

| I Want To... | Use This Agent |
|-------------|----------------|
| Start a new project from an idea | Supervisor → Requirements Agent |
| Design a complete system | Architecture Agent |
| Build a working prototype | Engineering Agent |
| Create or optimize prompts | **Prompt Engineering Agent** |
| Deploy to a specific platform | Deployment Agent |
| Improve an existing system | Optimization Agent |
| Convert prompts between platforms | **Prompt Engineering Agent** |

### Still Not Sure?

**Start with Supervisor Agent**:
```
File: supervisor_agent.system.prompt.md
```

The Supervisor analyzes your request and routes to the appropriate specialist agent(s).

---

**Version**: 1.0  
**Last Updated**: 2025-10-10  
**Related Documentation**:
- `README.md` - Quick start and overview
- `ARCHITECTURE.md` - Technical system architecture
- `docs/getting-started.md` - Step-by-step tutorials
- `docs/workflow_guide.md` - Complete workflow guide
- `docs/agent-design-patterns.md` - Design patterns and best practices
- `outputs/README.md` - Output directory structure

