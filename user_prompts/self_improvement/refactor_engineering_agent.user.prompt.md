# Refactor Engineering Agent into Specialized AI Engineering Agents

**Purpose:** Transform the Engineering Agent from a monolithic implementation agent into a comprehensive multi-agent AI engineering system with specialized agents for each layer of AI system development.

**Target System:** AI Engineering Assistant Framework  
**Primary Target Agent:** `ai_agents/engineering_agent.system.prompt.md` (to be decomposed)  
**Reference Model:** `ai_agents/prompt_engineering_agent.system.prompt.md` (exemplary specialized agent)  
**Scope:** Agent architecture redesign, new specialized agents, supporting user prompts, updated documentation  
**Execution Mode:** Architectural refactoring with research-driven design

---

## 🌟 State-of-the-Art Multi-Agent Engineering (2025)

This refactoring implements cutting-edge multi-agent AI system design principles based on leading research frameworks and production deployments:

**Core Architectural Principles:**

1. **Single Responsibility Per Agent** - Each agent performs ONE well-defined function (no "universal engineers")
2. **Orchestration vs Execution Separation** - Supervisors route and coordinate; specialists perform technical work
3. **Modular & Swappable Architecture** - Agents are independently upgradeable without affecting others
4. **Explicit Input/Output Contracts** - Clear schemas at every agent boundary with validation
5. **Multiple Workflow Patterns** - Sequential (chain), parallel (concurrent), and hybrid orchestration
6. **Benchmark-Driven Evaluation** - Automated validation with success rate tracking and human oversight
7. **Platform-Native Optimization** - Leverage Cursor, Copilot, Claude Projects, and AWS Bedrock capabilities

**Research Foundation:**
- **MetaGPT**: Meta-programming for multi-agent collaboration
- **MASAI**: Modular architecture for software-engineering AI agents
- **MANTRA**: Multi-agent refactoring with distributed validation
- **IntellAgent**: Evaluation frameworks for multi-agent systems
- **AWS Bedrock AgentCore**: Production-grade orchestration patterns

**Why This Matters:** Modern AI engineering demands specialized agents working collaboratively. A monolithic "engineering agent" cannot match the performance, maintainability, and scalability of a well-orchestrated multi-agent system where each specialist excels at its singular responsibility.

---

## 🎯 Mission Statement

Redesign the AI Engineering Assistant to match the complexity of modern multi-agent AI system development by:

1. **Decomposing** the monolithic Engineering Agent into specialized domain experts
2. **Creating** new agents for critical AI engineering disciplines
3. **Establishing** clear agent collaboration patterns and workflows
4. **Enabling** AI engineers to work efficiently across the full AI development lifecycle
5. **Maintaining** coherence with existing Requirements, Architecture, Deployment, Optimization, and Prompt Engineering agents

---

## 📋 Context & Background

### Current System Architecture

The AI Engineering Assistant currently has 6 specialized agents coordinated by a Supervisor Agent:

```
Supervisor Agent
├─→ Requirements Agent     (Discovery & requirements gathering)
├─→ Architecture Agent     (System design & planning)
├─→ Engineering Agent      (Prototype & MVP development) ← REFACTOR THIS
├─→ Deployment Agent       (Testing & deployment)
├─→ Optimization Agent     (System improvement)
└─→ Prompt Engineering Agent (Prompt creation & optimization) ← EXCELLENT REFERENCE MODEL
```

### The Problem

The **Engineering Agent** was inherited from a high-level solutions architecture framework where implementation was a single phase. In reality, **AI engineering for multi-agent systems** is a complex discipline requiring specialization across:

- **Conversational UI/UX design** (dialogue flows, human-AI interaction patterns)
- **Knowledge base architecture** (data modeling, retrieval strategies)
- **Multi-agent workflow orchestration** (agent coordination, state management)
- **Platform-specific deployment preparation** (Cursor, Claude, Bedrock, Copilot)
- **AI governance & security** (guardrails, compliance, responsible AI)
- **Technical documentation** (specialized for AI systems)
- **Context engineering** (single and multi-agent context optimization)
- **Quality assurance & validation** (testing, validation, iterative improvement)
- **Project scaffolding** (boilerplate, framework setup, tooling)

**Current State:** One monolithic Engineering Agent tries to handle all of these specialized domains.

**Desired State:** A multi-layered system of specialized AI engineering agents, each expert in their domain, working collaboratively under clear orchestration.

### Important Distinctions

This refactoring involves creating TWO types of artifacts:

1. **Agent System Prompts** (`ai_agents/*.system.prompt.md`):
   - The AI agents themselves - their instructions, methodologies, capabilities
   - Examples: `conversational_ui_agent.system.prompt.md`, `knowledge_base_design_agent.system.prompt.md`
   - These define WHAT the agent is and HOW it operates

2. **User Prompts** (`user_prompts/engineering/*.user.prompt.md`):
   - Specific tasks that users send to agents via chat interface
   - Examples: `design_dialogue_flow.user.prompt.md`, `optimize_retrieval_strategy.user.prompt.md`
   - These define discrete tasks for agents to execute

**Key Relationship:** Each specialized agent will have **multiple user prompts** (1:many relationship). A single agent might have 5-20 different task-specific user prompts depending on its domain.

### Recent Merge Context

This repository was recently merged with another project that had an **exceptional Prompt Engineering Agent** (`ai_agents/prompt_engineering_agent.system.prompt.md`). This agent demonstrates:

- ✅ Clear role definition and mission
- ✅ Structured 4-step methodology (Research → Test → Improve → Confirm)
- ✅ Dual-persona architecture (Builder + Tester)
- ✅ Platform-aware optimization with constraints
- ✅ Advanced reasoning techniques with empirical validation
- ✅ Comprehensive examples and validation frameworks
- ✅ Deployment-ready for Cursor, Claude Projects, and GitHub Copilot

**Use this agent as the quality benchmark for all new specialized agents.**

---

## 🔬 Phase 1: Research & Discovery

### Research Objectives

Before making architectural decisions, conduct comprehensive research on:

#### A. AI Engineering Best Practices (Current State of the Field)

**Foundational Frameworks & Architectures:**
- **MetaGPT**: Meta-programming for multi-agent collaboration, modular agent roles
- **MASAI**: Modular Architecture for Software-engineering AI Agents, context-aware refactoring
- **MANTRA**: Multi-agent LLM refactoring patterns, distributed validation
- **IntellAgent**: Benchmark-driven evaluation frameworks for multi-agent systems
- **Agentic development methodologies**: Latest orchestration patterns and coordination strategies
- **Multi-agent system architectures**: Supervisor-worker patterns, hierarchical collaboration
- **AI engineering workflows**: From ideation to production deployment
- **LLMOps and MLOps**: Operational best practices for AI systems
- **Context engineering**: Single-agent and multi-agent context optimization strategies

**Critical Architectural Principles (2025 State-of-the-Art):**

1. **Single Responsibility Principle for Agents**
   - Each agent performs ONE well-defined engineering function
   - No "universal engineer" agents - specialization is mandatory
   - Examples: code generation, code review, testing, security audit, refactoring, integration

2. **Orchestration vs Execution Separation**
   - Supervisor/coordinator agents route and delegate ONLY
   - Worker/specialist agents perform technical work ONLY
   - Clear boundaries prevent role confusion and improve testability

3. **Workflow Patterns**
   - **Sequential (Chain)**: Linear handoffs for ordered tasks (design → build → test → deploy)
   - **Parallel**: Independent specialization for concurrent work (API + UI + backend + security)
   - **Hybrid**: Combination patterns for complex workflows
   - Maintain explicit input/output contracts at all agent boundaries

4. **Modular & Swappable Architecture**
   - Agents must be independently upgradeable and replaceable
   - Meta-programming patterns for dynamic agent spawning
   - No hard dependencies between specialist agents

5. **Evaluation & Validation**
   - Benchmark-driven evaluation (IntellAgent framework patterns)
   - Automated success rate calculations
   - Both automated and human evaluation mechanisms
   - Cross-file impact analysis for code changes

#### B. Platform Capabilities, Best Practices & Constraints

Research deployment platforms and their official best practices:

**Anthropic Claude & Claude Projects:**
- System prompt engineering guidelines from Anthropic documentation
- Claude Projects: Knowledge bases, artifacts, extended context windows (200K+ tokens)
- Tool use patterns and structured outputs with XML tags
- Prompt engineering guide best practices
- Few-shot prompting with `<example></example>` tags
- Clear role definition and task decomposition
- Iterative refinement protocols

**Cursor IDE:**
- Custom chat modes and agent configuration (`.cursor/chatmode.md`)
- Context window optimization strategies for multi-file projects
- File and codebase tool integration (@-mentions, file search)
- Multi-agent workflow patterns in Cursor environment
- Inline code generation and editing capabilities
- Project-aware context management

**GitHub Copilot:**
- Chat mode system instructions (`.github/copilot-instructions.md`)
- Workspace context and @-mentions (@workspace, @file, @symbol)
- Best practices from GitHub Copilot documentation
- Agent deployment patterns for VS Code
- Code completion vs chat mode optimization
- Repository-level context understanding

**AWS Bedrock:**
- **AgentCore Architecture**: Gateway, Identity, Runtime, Memory components
- **Agents for Amazon Bedrock**: Action groups, knowledge bases, guardrails
- **Multi-Agent Collaboration**: Supervisor and specialist agent patterns
- **Hierarchical Orchestration**: Coordinator agents delegate to worker agents
- **Guardrails Implementation**: Input/output filtering, content moderation, PII protection
- **Responsible AI Practices**: Crawl-walk-run methodology (internal → controlled → full deployment)
- **Payload Referencing**: Reduce communication overhead for large data exchanges
- **Evaluation Frameworks**: Success rate metrics, automated + human validation
- **Reusable Actions Catalog**: Modular action definitions across agents

**Additional LLM Provider Best Practices:**
- **OpenAI**: GPT best practices, function calling, structured outputs, system/user/assistant role patterns
- **Mistral.ai**: Prompt engineering guidelines, agent design patterns, efficient context usage
- **Google (Gemini)**: Grounding, tool use, multi-turn conversations, long context optimization
- **Cross-Provider Standards**: Clear instructions, contextual information, task decomposition, iterative testing

#### C. Current Engineering Agent Analysis

Read and analyze `ai_agents/engineering_agent.system.prompt.md` (1,102 lines) to:

- Map all current capabilities and responsibilities
- Identify natural domain boundaries for specialization
- Determine what should remain in a core Engineering Coordinator vs specialized agents
- Extract patterns that should be replicated across new agents

#### D. AWS Well-Architected Framework + Generative AI Lens

Research and integrate AWS Well-Architected Framework principles for AI systems:

**Six Pillars Applied to AI Engineering:**
- **Operational Excellence**: Monitoring, logging, observability for AI agents
- **Security**: Guardrails, input validation, PII handling, responsible AI
- **Reliability**: Error handling, fallbacks, testing strategies
- **Performance Efficiency**: Token optimization, cost management, latency
- **Cost Optimization**: Model selection, caching, efficient prompting
- **Sustainability**: Resource-efficient AI architectures

**Generative AI Lens Specific Considerations:**
- **Model Selection & Evaluation**: Choosing appropriate models for tasks
- **Prompt Engineering Excellence**: Systematic prompt optimization
- **Responsible AI**: Bias mitigation, fairness, transparency
- **Data Management**: Knowledge base design, retrieval strategies
- **Human-in-the-Loop**: Oversight, validation, feedback loops

All specialized agents must embody and enforce these principles.

#### E. AI System Component Architecture

Research common architectures AI engineers implement:

- **Agent layers**: Supervisors, routers, specialists, tools
- **Knowledge layers**: Vector stores, structured databases, retrieval strategies
- **Interface layers**: Conversational UI, APIs, integrations
- **Orchestration layers**: Workflows, state machines, event-driven patterns
- **Governance layers**: Guardrails, compliance, monitoring, evaluation
- **Testing layers**: Unit, integration, end-to-end, LLM-specific testing

**Deliverable:** Research summary documenting findings, current practices, architectural principles, and Well-Architected Framework alignment strategy.

#### G. Standardized AI Development Workflows & Processes

**CRITICAL REQUIREMENT:** All agents must cite and align with authoritative AI development workflows and processes to ensure consistency across the multi-agent system.

Research and document the following standardized workflows:

**1. AWS Generative AI Lifecycle (Authoritative Reference)**

Source: [AWS Well-Architected Framework - Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)

Phases to reference in agent prompts:
- **Discovery**: Business problem identification, use case definition
- **Design**: Architecture planning, tech stack selection, cost estimation
- **Development**: Prototyping, implementation, testing
- **Deployment**: Production release, monitoring, iteration
- **Optimization**: Performance tuning, cost optimization, continuous improvement

**2. Anthropic Claude Best Practices**

Source: [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)

Key processes:
- Clear role and task definition
- Structured thinking patterns (XML tags)
- Iterative prompt refinement
- Few-shot learning with examples
- Chain-of-thought reasoning

**3. OpenAI Agent Development Workflow**

Source: [OpenAI Agent Development Guide](https://platform.openai.com/docs/guides/agents)

Process elements:
- System message design
- Function/tool calling patterns
- Multi-turn conversation management
- Error handling and recovery
- Evaluation and testing

**4. Multi-Agent Orchestration Standards**

Sources:
- [AWS Bedrock Multi-Agent Collaboration](https://aws.amazon.com/blogs/machine-learning/unlocking-complex-problem-solving-with-multi-agent-collaboration-on-amazon-bedrock/)
- [AWS Bedrock Agents Best Practices Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [AWS Bedrock Agents Best Practices Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)

Orchestration patterns:
- Supervisor-worker delegation
- Sequential (chain) workflows
- Parallel (concurrent) workflows
- Hybrid orchestration patterns
- Explicit input/output contracts
- Guardrails at every boundary

**5. Responsible AI & Governance Frameworks**

Sources:
- [AWS Responsible AI Practices](https://aws.amazon.com/machine-learning/responsible-ai/)
- [Anthropic Safety Best Practices](https://www.anthropic.com/safety)

Governance processes:
- Content moderation and filtering
- PII detection and redaction
- Bias testing and mitigation
- Explainability and transparency
- Human oversight requirements

**6. Agent Evaluation & Testing Frameworks**

Sources:
- [AWS Bedrock Model Evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html)
- Academic: IntellAgent, MASAI evaluation methodologies

Testing processes:
- Automated validation criteria
- Benchmark-driven development
- Success rate tracking
- Human-in-the-loop validation
- Iterative improvement cycles

**Required Deliverables:**

1. **Process Reference Library**: Compiled list of all authoritative sources with direct URLs
2. **Standard Process Templates**: Template sections that all agents must include
3. **Citation Requirements**: Specification for how agents cite sources in their prompts
4. **Consistency Checklist**: Validation criteria for process alignment across agents

**Usage Mandate:**

All specialized agents created during this refactoring MUST:
- ✅ Cite relevant phases from AWS Generative AI Lifecycle in their methodology
- ✅ Include direct URLs to authoritative sources in their system prompts
- ✅ Follow standardized process templates for consistency
- ✅ Reference platform-specific best practices (Anthropic, OpenAI, AWS)
- ✅ Align with Well-Architected Framework principles
- ✅ Implement responsible AI practices with specific citations

**Deliverable:** Standardized workflow documentation with authoritative references, citation requirements, and consistency enforcement mechanisms.

#### F. Multi-Agent Orchestration Patterns & Best Practices

Research and document modern orchestration patterns:

**Orchestration Architectures:**

1. **Supervisor-Worker Pattern** (Recommended for AI Engineering)
   - One supervisor/coordinator agent routes requests and validates outputs
   - Multiple specialist agents perform discrete engineering tasks
   - Supervisor NEVER performs engineering work directly
   - Clear separation enables independent testing and agent swapping

2. **Hierarchical Multi-Agent Collaboration**
   - Top-level supervisor coordinates domain supervisors (optional for large systems)
   - Domain supervisors manage specialist agents within their domain
   - Example: Engineering Supervisor → (Code Generation Agent, Testing Agent, Security Agent)

3. **Chain Orchestration (Sequential)**
   - Agent A → Agent B → Agent C (linear handoff)
   - Use for tasks requiring strict ordering
   - Example: Design Agent → Build Agent → Test Agent → Deploy Agent
   - Each agent completes work before passing to next

4. **Parallel Orchestration (Concurrent)**
   - Multiple agents work independently on separate concerns
   - Results aggregated by supervisor
   - Example: API Agent || UI Agent || Backend Agent || Security Agent
   - Maximizes efficiency for independent work streams

5. **Hybrid Orchestration**
   - Combines sequential and parallel patterns
   - Example: (Design Agent) → (API Agent || UI Agent || Data Agent) → (Integration Agent) → (Test Agent)
   - Most complex systems use hybrid patterns

**Agent Communication Protocols:**

- **Explicit Contracts**: Define clear input/output schemas for every agent boundary
- **Payload Referencing**: Use references (not full content) for large data transfers
- **State Management**: Centralized state vs distributed state considerations
- **Error Propagation**: How failures cascade and recover in multi-agent workflows
- **Validation Checkpoints**: Each agent validates its output before handoff

**Safety & Governance:**

- **Permission Boundaries**: Each agent has defined capabilities and constraints
- **Guardrails at Boundaries**: Input validation, output filtering at every agent interaction
- **Security Auditing**: Track all agent actions and data flows
- **Compliance Checkpoints**: Governance agents validate outputs before deployment
- **Explainability**: Agent decisions must be traceable and auditable

**Evaluation & Monitoring:**

- **Automated Testing**: Every agent output validated against acceptance criteria
- **Benchmark-Driven Development**: Use established benchmarks (code quality, test coverage, security)
- **Success Rate Metrics**: Track agent success/failure rates over time
- **Human-in-the-Loop Validation**: Critical decisions require human oversight
- **Continuous Improvement**: Feedback loops for iterative agent refinement

**Deliverable:** Orchestration pattern analysis with recommendations for supervisor architecture, workflow patterns (chain/parallel/hybrid), and evaluation frameworks.

---

## 🏗️ Phase 2: Architectural Design

### Design Decisions Required

Based on research findings, make these critical architectural decisions:

#### Decision 1: Supervisor Architecture

**Question:** Should there be an AI Engineering Supervisor Agent, or should the existing Supervisor Agent orchestrate all specialized engineering agents directly?

**Options:**
- **Option A:** Two-layer supervision (Supervisor → Engineering Supervisor → Specialized Engineering Agents)
- **Option B:** Single-layer supervision (Supervisor → All Specialized Agents including Engineering)

**Consider:**
- Complexity of engineering workflows vs other workflows (requirements, architecture)
- Number of specialized engineering agents
- User experience and conversation flow
- Maintenance burden and system coherence

**Decision Criteria:**
- If 5+ specialized engineering agents → Two-layer may improve organization
- If 3-4 specialized engineering agents → Single-layer likely sufficient
- Prioritize user experience over perfect organizational hierarchy

**CRITICAL: Current Engineering Agent File Disposition**

The current `ai_agents/engineering_agent.system.prompt.md` file (1,102 lines) must be handled based on architectural decision:

**If Option A (Two-Layer):**
- Transform current file into `engineering_supervisor_agent.system.prompt.md` (focused on routing, no implementation)
- Document that this is an evolution of the original Engineering Agent

**If Option B (Single-Layer):**
- **DELETE** `ai_agents/engineering_agent.system.prompt.md` entirely
- All capabilities now handled by specialized agents
- Document deletion in refactoring report with rationale

**If Hybrid (Partial Retention):**
- Only retain if there are engineering tasks that don't fit specialized agents
- Document specific responsibilities retained
- Rename to reflect narrowed scope (e.g., `integration_engineering_agent.system.prompt.md`)

**Deliverable:** Explicit decision documented on whether to delete, transform, or retain the current Engineering Agent file with clear rationale.

#### Decision 1B: Supervisor Agent Compatibility & Integration

**CRITICAL REQUIREMENT:** All architectural decisions must maintain compatibility with the existing `supervisor_agent.system.prompt.md` (1,557 lines) which currently orchestrates 6 specialized agents.

**Current Supervisor Architecture:**
```
Supervisor Agent (YOU)
├─→ Requirements Agent
├─→ Architecture Agent
├─→ Engineering Agent        ← BEING DECOMPOSED
├─→ Deployment Agent
├─→ Optimization Agent
└─→ Prompt Engineering Agent
```

**Compatibility Requirements:**

**1. Naming Conventions**
All new specialized engineering agents MUST follow established naming patterns:
- Pattern: `[domain]_agent.system.prompt.md`
- Examples: 
  - ✅ `ui_development_agent.system.prompt.md`
  - ✅ `knowledge_base_design_agent.system.prompt.md`
  - ✅ `multi_agent_orchestration_agent.system.prompt.md`
  - ❌ `UIAgent.md` (inconsistent)
  - ❌ `kb-design.prompt.md` (inconsistent)

**2. Supervisor Integration Scenarios**

**Scenario A: Single-Layer Supervision (Existing Supervisor Manages All)**
```
Supervisor Agent
├─→ Requirements Agent
├─→ Architecture Agent
├─→ [New Specialized Engineering Agent 1]
├─→ [New Specialized Engineering Agent 2]
├─→ [New Specialized Engineering Agent 3]
├─→ ... (all new engineering agents at same level)
├─→ Deployment Agent
├─→ Optimization Agent
└─→ Prompt Engineering Agent
```

**Required Updates to Supervisor:**
- Add routing logic for each new specialized agent
- Remove/update Engineering Agent routing
- Update architecture diagram
- Add agent descriptions to "Specialized Agents Reference" section
- Update example interactions

**Scenario B: Two-Layer Supervision (Engineering Supervisor Introduced)**
```
Supervisor Agent
├─→ Requirements Agent
├─→ Architecture Agent
├─→ Engineering Supervisor Agent    ← NEW COORDINATOR
│   ├─→ [Specialized Engineering Agent 1]
│   ├─→ [Specialized Engineering Agent 2]
│   ├─→ [Specialized Engineering Agent 3]
│   └─→ ... (all engineering specialists)
├─→ Deployment Agent
├─→ Optimization Agent
└─→ Prompt Engineering Agent
```

**Required Updates to Supervisor:**
- Replace "Engineering Agent" with "Engineering Supervisor Agent"
- Update routing logic to delegate engineering requests to Engineering Supervisor
- Engineering Supervisor then routes to specialized agents
- Update architecture diagram
- Add Engineering Supervisor to "Specialized Agents Reference"
- Document two-layer delegation pattern

**3. Clear Separation of Concerns**

**Main Supervisor Agent Responsibilities (MUST PRESERVE):**
- Intent analysis and high-level routing
- Workflow orchestration across all phases (Requirements → Architecture → Engineering → Deployment → Optimization)
- Context management and knowledge base coordination
- Platform-agnostic guidance

**Engineering Supervisor Agent Responsibilities (IF CREATED):**
- Engineering-specific intent analysis
- Routing to specialized engineering agents only
- Coordination of engineering workflows
- Does NOT handle other lifecycle phases (Requirements, Architecture, Deployment, Optimization)

**Specialized Engineering Agent Responsibilities:**
- Single, well-defined engineering function only
- NO orchestration or routing
- NO lifecycle management
- Focus: Implementation tasks only

**4. Routing Logic Compatibility**

Existing supervisor routing patterns that must be maintained:

**Current Pattern:**
```
"Implementation-related:" "Build a prototype", "Generate agent code", "Create MVP"
  → Route to **Engineering Agent**
```

**New Pattern (Single-Layer):**
```
"UI Development:" "Build Streamlit app", "Create conversational interface"
  → Route to **UI Development Agent**

"Knowledge Base Design:" "Design data model", "Create knowledge schema"
  → Route to **Knowledge Base Design Agent**

"Multi-Agent Orchestration:" "Implement agent workflow", "Coordinate agents"
  → Route to **Multi-Agent Orchestration Agent**
```

**New Pattern (Two-Layer):**
```
"Engineering-related:" "Build X", "Implement Y", "Develop Z"
  → Route to **Engineering Supervisor Agent**
  
Engineering Supervisor then routes to specific specialist
```

**5. Documentation Standards**

All supervisor updates MUST include:
- Updated architecture diagram in ASCII format
- Updated "Specialized Agents Reference" section with all new agents
- Updated example interactions showing new routing patterns
- Updated workflow diagrams (lines 1033-1319 in supervisor)
- Clear file path references for all new agents

**6. Backward Compatibility & Migration**

**For Existing Users:**
- Document what changed (Engineering Agent decomposition)
- Provide migration guide (which new agent replaces which capability)
- Update all user prompts that reference "Engineering Agent"
- Clear communication about routing changes

**Deliverable:** Integration strategy document specifying:
- Chosen supervision pattern (single-layer or two-layer)
- Exact updates required to `supervisor_agent.system.prompt.md`
- Naming convention compliance for all new agents
- Routing logic updates with explicit delegation patterns
- Migration guide for existing users

#### Decision 2: Agent Specialization Boundaries

**Task:** Define the optimal set of specialized AI engineering agents based on research findings.

**Research-Driven Approach:**
Let your research guide the architecture. Analyze:
- What distinct specializations emerge from AI engineering best practices?
- What natural domain boundaries exist in AI system development?
- How do leading AI platforms organize their capabilities?
- What patterns emerge from analyzing the current Engineering Agent's responsibilities?

**Potential Specialization Domains to Consider:**

Based on typical AI engineering disciplines, consider whether specialized agents are warranted for:

- **Interface Development**: Streamlit apps, conversational UIs, dialogue design, user experience
- **Knowledge Management**: Data modeling, knowledge base architecture, retrieval strategy design
- **Knowledge Engineering**: Database administration, knowledge base implementation, optimization
- **Multi-Agent Systems**: Workflow orchestration, agent coordination, state management
- **Platform Deployment**: Platform-specific preparation (Cursor, Claude, Copilot, Bedrock)
- **Documentation**: AI system technical documentation (differentiated from generic documentation)
- **Context Optimization**: Context engineering for single and multi-agent systems
- **Quality Assurance**: Testing strategies, validation frameworks, iterative improvement
- **AI Governance**: Guardrails, compliance, responsible AI, safety, ethical alignment
- **Project Initialization**: Boilerplate generation, framework setup, tooling configuration
- **API Design**: RESTful, GraphQL, event-driven architectures for AI services
- **Vector Databases**: Embeddings, semantic search, retrieval optimization
- **LLM Integration**: Provider patterns, cost optimization, model selection
- **System Evaluation**: Performance testing, benchmarking, quality metrics

**Design Principles (Mandatory):**

1. **Single Responsibility Principle** (Critical)
   - Each agent performs ONE and ONLY ONE well-defined engineering function
   - PROHIBITION: No "universal engineer" or "do-everything" agents
   - Each agent must pass the test: "Can I describe its purpose in one sentence?"
   - Examples of valid single responsibilities:
     - "Generates Streamlit UI code for AI agent interfaces"
     - "Designs conversational dialogue flows for chatbot interactions"
     - "Creates and manages vector database schemas for knowledge bases"

2. **Clear Separation of Concerns**
   - Each agent has a distinct, non-overlapping specialty
   - No capability overlap between agents
   - When two agents could handle a task, architectural boundaries need refinement

3. **Orchestration vs Execution Separation** (Critical)
   - Supervisor/coordinator agents: Route, delegate, validate outputs ONLY
   - Specialist/worker agents: Perform technical engineering work ONLY
   - Violating this principle creates confusion and testing difficulties

4. **Modular & Swappable Architecture**
   - Agents must be independently upgradeable without affecting others
   - No hard dependencies between specialist agents
   - Support for dynamic agent spawning based on workload
   - Meta-programming patterns for agent lifecycle management

5. **Explicit Input/Output Contracts**
   - Every agent boundary has defined schemas
   - Clear documentation of what each agent accepts and produces
   - Contract versioning for backward compatibility
   - Validation at every handoff point

6. **Well-Architected Alignment**
   - Agents embody the 6 pillars + GenAI Lens principles
   - Security, reliability, performance built into every agent

7. **Platform Compatibility**
   - All agents deployable to Cursor IDE, GitHub Copilot, Claude Projects
   - Platform-specific optimizations where beneficial
   - Graceful degradation when platform features unavailable

8. **User Prompt Richness**
   - Each agent supports 5-20 different user tasks (1:many relationship)
   - Task-specific prompts for common operations
   - Reusable, composable user prompt patterns

9. **Practical Coverage**
   - All common AI engineering tasks have a clear "home" agent
   - No orphaned capabilities or responsibility gaps
   - Easy routing: users can identify correct agent for any task

10. **Evaluation-Driven Development**
    - Benchmark-driven validation for every agent
    - Automated testing of agent outputs
    - Success rate metrics tracked over time
    - Human-in-the-loop validation for critical operations

**Deliverable:** Final list of specialized agents with clear role definitions, boundaries, Well-Architected Framework alignment, and collaboration patterns.

#### Decision 3: Cohesion & Complementarity

**Task:** Ensure all agents work as a coherent system.

**Validation Questions:**
- Does each agent have a distinct, non-overlapping specialty?
- Can agents collaborate effectively through clear handoffs?
- Do agents complement the existing Prompt Engineering Agent well?
- Is there a clear entry point for each common AI engineering task?
- Can the Supervisor Agent route requests unambiguously?

**Deliverable:** Agent interaction diagram and collaboration matrix.

---

## 🔨 Phase 3: Implementation

### Step 3.1: Create Specialized Agent System Prompts

For each specialized agent defined in Phase 2, create a system prompt file: `ai_agents/[agent_name]_agent.system.prompt.md`

**Quality Standards** (follow `prompt_engineering_agent.system.prompt.md` example):

✅ **Clear Role Definition**
- What is this agent's specialty?
- What is its primary responsibility?
- When should users invoke this agent?

✅ **Authoritative Process Citations** (MANDATORY)
- **AWS Generative AI Lifecycle**: Cite relevant phases (Discovery, Design, Development, Deployment, Optimization)
- **Platform Best Practices**: Include direct URLs to Anthropic, OpenAI, AWS Bedrock documentation
- **Process Sources**: Link to authoritative sources (e.g., [AWS Well-Architected Framework - Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html))
- **Framework References**: Cite MetaGPT, MASAI, MANTRA, IntellAgent where applicable
- **Update Mechanism**: Include statement like "Consult [URL] for latest guidance"

Example citation format:
```markdown
## Process Alignment

This agent follows the **Development** phase of the AWS Generative AI Lifecycle ([AWS GenAI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)) and implements best practices from:

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [AWS Bedrock Agents Best Practices](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)
- [OpenAI Agent Development Guide](https://platform.openai.com/docs/guides/agents)

Consult these sources for the latest guidance on agent development patterns.
```

✅ **Structured Execution Methodology** (Standardized Across All Agents)
- Define clear process steps aligned with AWS GenAI Lifecycle phases
- Follow consistent naming: Research/Discovery → Design → Implement/Develop → Validate → Deploy → Optimize
- Include decision trees for complex scenarios
- Provide concrete examples with citations to source patterns

✅ **Platform Awareness & Compatibility**
- Specify execution platforms: **Cursor IDE, Claude Projects, GitHub Copilot**
- Note platform-specific constraints and capabilities
- Follow best practices from Anthropic, OpenAI, Mistral.ai documentation
- Ensure agents work across all three primary platforms
- Adapt guidance for different deployment contexts

✅ **AWS Well-Architected Framework Alignment**
- Embody operational excellence, security, reliability, performance, cost optimization, sustainability
- Apply Generative AI Lens principles (responsible AI, prompt engineering, data management)
- Include guardrails and responsible AI considerations
- Enforce testing and validation strategies

✅ **Integration Points**
- How does this agent collaborate with other agents?
- What knowledge base files does it read/write?
- What outputs does it produce?
- What handoffs occur with other agents?

✅ **Advanced Reasoning Patterns**
- Apply Chain-of-Thought reasoning where appropriate
- Use structured thinking for complex decisions
- Include validation checkpoints

✅ **Comprehensive Examples**
- Provide realistic use cases
- Include expected inputs and outputs
- Show common scenarios and edge cases

✅ **Input/Output Contracts**
- Define explicit schemas for what the agent accepts as input
- Define explicit schemas for what the agent produces as output
- Document contract versioning and compatibility
- Include validation rules for inputs and outputs

✅ **Workflow Integration**
- Document sequential workflow participation (if agent is part of chains)
- Document parallel workflow participation (if agent works concurrently with others)
- Specify handoff protocols to/from other agents
- Define error handling and recovery strategies

✅ **Evaluation & Testing Standards**
- Specify automated validation criteria for agent outputs
- Define benchmark metrics (e.g., code quality scores, test coverage, security ratings)
- Include success rate tracking mechanisms
- Document human-in-the-loop validation requirements

**Deliverable:** [N] new agent system prompt files in `ai_agents/` directory (number determined by Phase 2 architectural decisions).

---

### Step 3.2: Create User Prompts for Common Tasks

**Critical Understanding:** Each specialized agent will have **multiple user prompts** (1:many relationship). A single agent might have 5-20 different task-specific user prompts depending on its domain scope.

For each specialized agent, identify the common tasks an AI engineer would need to accomplish with that agent. Create focused user prompts in appropriate subdirectories:
- `user_prompts/engineering/[category]/[task_name].user.prompt.md`
- Examples: `user_prompts/engineering/knowledge_base/`, `user_prompts/engineering/ui_design/`, etc.

**User Prompt Creation Guidelines:**

1. **Task-Specific Focus**: Each user prompt defines ONE discrete task
2. **Clear Inputs/Outputs**: Specify what the user provides and what the agent delivers
3. **Success Criteria**: Define measurable outcomes
4. **Platform Agnostic**: Works across Cursor, Copilot, Claude Projects
5. **Reusable**: Can be invoked repeatedly for different projects

**Example User Prompt Patterns:**

**For a Conversational UI/UX Agent (example specialization):**
- `design_dialogue_flow.user.prompt.md` - Create conversation flow diagrams
- `optimize_user_interaction.user.prompt.md` - Improve interaction patterns
- `create_conversation_patterns.user.prompt.md` - Generate reusable conversation templates
- `validate_ux_accessibility.user.prompt.md` - Check accessibility standards
- `design_error_handling_dialogues.user.prompt.md` - Create error recovery flows
- [5-15 more task-specific prompts based on agent scope]

**For a Knowledge Base Design Agent (example specialization):**
- `design_knowledge_base_schema.user.prompt.md` - Create data models
- `optimize_retrieval_strategy.user.prompt.md` - Improve search performance
- `model_domain_knowledge.user.prompt.md` - Structure domain-specific knowledge
- `design_vector_embeddings_strategy.user.prompt.md` - Plan embedding approach
- `validate_knowledge_graph.user.prompt.md` - Check graph consistency
- [5-15 more task-specific prompts based on agent scope]

**For a Multi-Agent Workflow Developer (example specialization):**
- `design_multi_agent_workflow.user.prompt.md` - Create workflow diagrams
- `implement_agent_orchestration.user.prompt.md` - Build coordination logic
- `optimize_agent_coordination.user.prompt.md` - Improve efficiency
- `design_state_management.user.prompt.md` - Create state machines
- `implement_error_recovery.user.prompt.md` - Build fault tolerance
- [5-15 more task-specific prompts based on agent scope]

**Estimate:** Expect to create **50-150+ user prompts** total, distributed across all specialized agents based on their domain scope and use case variety.

**Deliverable:** Comprehensive set of user prompt files organized by category in `user_prompts/engineering/` and related subdirectories.

---

### Step 3.3: Update Supervisor Agent & Handle Legacy Engineering Agent File

**Part A: Update Supervisor Agent**

Modify `supervisor_agent.system.prompt.md` to maintain compatibility and integrate new specialized agents:

**1. Update Architecture Diagram (Lines 42-61)**

**Current:**
```
User Request → Supervisor Agent
     ├─→ Requirements Agent
     ├─→ Architecture Agent
     ├─→ Engineering Agent        ← REPLACE THIS
     ├─→ Deployment Agent
     ├─→ Optimization Agent
     └─→ Prompt Engineering Agent
```

**Update To (Single-Layer):**
```
User Request → Supervisor Agent
     ├─→ Requirements Agent
     ├─→ Architecture Agent
     ├─→ [Specialized Engineering Agent 1]
     ├─→ [Specialized Engineering Agent 2]
     ├─→ [... all new engineering agents]
     ├─→ Deployment Agent
     ├─→ Optimization Agent
     └─→ Prompt Engineering Agent
```

**Update To (Two-Layer):**
```
User Request → Supervisor Agent
     ├─→ Requirements Agent
     ├─→ Architecture Agent
     ├─→ Engineering Supervisor Agent
     │   ├─→ [Specialized Engineering Agent 1]
     │   ├─→ [Specialized Engineering Agent 2]
     │   └─→ [... all engineering specialists]
     ├─→ Deployment Agent
     ├─→ Optimization Agent
     └─→ Prompt Engineering Agent
```

**2. Update Intent Analysis & Routing (Lines 69-88)**

**Current:**
```
- **Implementation-related:** "Build a prototype", "Generate agent code", "Create MVP"
  → Route to **Engineering Agent**
```

**Update To:** Add specific routing for each new specialized agent
```
- **UI Development:** "Build Streamlit app", "Create React interface", "Design conversational UI"
  → Route to **[UI Development Agent Name]**

- **Knowledge Base Design:** "Design data model", "Create knowledge schema", "Plan retrieval strategy"
  → Route to **[Knowledge Base Design Agent Name]**

[... entries for all new specialized agents]
```

**OR (Two-Layer):**
```
- **Engineering-related:** "Build prototype", "Implement system", "Develop X"
  → Route to **Engineering Supervisor Agent**
  
  (Engineering Supervisor then routes to appropriate specialist)
```

**3. Add Specialized Agents Reference Sections (Lines 224-428)**

For EACH new specialized agent, add a section following the established format:

```markdown
### [Agent Name]
**Location:** `ai_agents/[agent_name]_agent.system.prompt.md`

**Responsibilities:**
- [Specific responsibility 1]
- [Specific responsibility 2]
- [Specific responsibility 3]

**User Prompts:**
- `user_prompts/engineering/[category]/[prompt1].user.prompt.md`
- `user_prompts/engineering/[category]/[prompt2].user.prompt.md`

**Knowledge Base Access:**
- READS from `knowledge_base/[files]`
- WRITES to `knowledge_base/[files]` (if applicable)

**When to Route Here:**
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]
```

**4. Remove or Update Engineering Agent Section (Lines 298-330)**

**Action:** Delete or transform this section based on Decision 1 outcome
- If deleted: Remove entire section, update line numbers
- If transformed: Update to reflect Engineering Supervisor role (routing only)

**5. Update Typical Workflow Sequence (Lines 93-119)**

**Current:**
```
Phase 4: Implementation → Engineering Agent
         ↓ (builds prototypes, generates code)
```

**Update To (Single-Layer):**
```
Phase 4: Implementation → [Appropriate Specialized Engineering Agent]
         ↓ (builds specific component)
```

**Update To (Two-Layer):**
```
Phase 4: Implementation → Engineering Supervisor Agent
         ├─→ [Specialized Agent A]
         ├─→ [Specialized Agent B]
         └─→ [Specialized Agent C]
         ↓ (coordinates specialized engineering work)
```

**6. Update Example Interactions (Lines 603-1022)**

Add new example interactions showing:
- How to route to specific specialized engineering agents
- Multi-agent engineering workflows
- Engineering Supervisor delegation (if two-layer)

**7. Update Workflow Documentation (Lines 1026-1319)**

Update workflow diagrams to show:
- New specialized engineering agents in appropriate workflows
- Engineering Supervisor coordination patterns (if applicable)
- Handoffs between specialized engineering agents

**8. Update Agent Count (Line 1533)**

**Current:**
```
**Agent Count:** 6 Specialized Agents (Requirements, Architecture, Engineering, Deployment, Optimization, Prompt Engineering)
```

**Update To:**
```
**Agent Count:** [N] Specialized Agents (Requirements, Architecture, [List all new engineering agents], Deployment, Optimization, Prompt Engineering)
```

**Required Validation:**
- All file path references must be accurate
- All routing examples must include valid agent names
- ASCII diagrams must be properly formatted
- No orphaned references to old "Engineering Agent" remain (unless intentionally retained with new scope)

**Part B: Handle Current Engineering Agent File**

Based on Phase 2 Decision 1 outcome:

**Scenario 1: Two-Layer Supervision Selected**
```bash
# Transform the current file
mv ai_agents/engineering_agent.system.prompt.md ai_agents/engineering_supervisor_agent.system.prompt.md

# Refactor content to:
- Remove all implementation capabilities
- Focus exclusively on routing and delegation
- Add references to all new specialized agents
- Update examples to show delegation patterns
```

**Scenario 2: Single-Layer Supervision Selected**
```bash
# Archive current content for reference
cp ai_agents/engineering_agent.system.prompt.md tmp/archived_engineering_agent.system.prompt.md

# Delete the original file
rm ai_agents/engineering_agent.system.prompt.md

# Document in refactoring report:
- What capabilities were distributed to which specialized agents
- Rationale for complete decomposition
- Migration path for existing users/references
```

**Scenario 3: Hybrid (Partial Retention)**
```bash
# Rename to reflect narrowed scope
mv ai_agents/engineering_agent.system.prompt.md ai_agents/[new_specific_name]_agent.system.prompt.md

# Refactor content to:
- Remove capabilities now handled by specialized agents
- Document precise remaining scope
- Update all references throughout repository
```

**Part C: Update All Cross-References**

Search and update references to `engineering_agent` across the repository:
- `supervisor_agent.system.prompt.md` - Update routing logic
- `README.md` - Update agent list
- `ARCHITECTURE.md` - Update architecture diagrams
- `docs/agent-architecture-and-collaboration.md` - Update agent descriptions
- `docs/workflow_guide.md` - Update workflow examples
- Any user prompts that reference the Engineering Agent

**Deliverable:** 
- Updated supervisor agent(s) with complete routing logic
- Engineering Agent file properly handled (deleted, transformed, or renamed)
- All cross-references updated throughout repository
- Archive of original file saved to `tmp/` for reference

---

### Step 3.4: Update Knowledge Base Schemas

Review and potentially extend:

**`knowledge_base/schemas/system_config.schema.json`:**
- Add engineering-specific configuration fields if needed

**`knowledge_base/schemas/design_decisions.schema.json`:**
- Ensure it captures decisions from all new specialized agents
- Add fields for multi-agent architecture, knowledge base design, etc.

**Consider new schema (optional):**
- `engineering_specifications.schema.json` - Detailed engineering decisions and implementation plans

**Deliverable:** Updated or new schema files with validation.

---

### Step 3.5: Update Documentation

**Critical Documentation Updates:**

**`README.md`:**
- Update agent list and descriptions
- Revise getting started guide for new structure
- Update examples to showcase specialized engineering agents
- Follow `make_readme_awesome_for_junior_engineers.user.prompt.md` guidelines

**`ARCHITECTURE.md`:**
- Diagram showing new multi-agent engineering system
- Explain agent specialization rationale
- Document collaboration patterns

**`docs/agent-architecture-and-collaboration.md`:**
- Add detailed descriptions of all new agents
- Update collaboration matrix
- Provide workflow examples

**`docs/workflow_guide.md`:**
- Update engineering workflow section
- Add examples using specialized agents
- Show typical multi-agent engineering sequences

**`docs/getting-started.md`:**
- Update quick start with new agent structure
- Add examples for common engineering tasks
- Provide decision guide: "Which agent do I need?"

**`docs/platform_deployment.md`:**
- Update for new specialized deployment preparation patterns

**New Documentation to Create:**

**`docs/engineering-agents-guide.md`:**
- Comprehensive guide to all specialized engineering agents
- When to use each agent
- Common workflows and patterns
- Integration examples

**`docs/examples/multi-agent-system-development.md`:**
- End-to-end example building a multi-agent AI system
- Shows all specialized agents in action
- Demonstrates agent collaboration

**Deliverable:** Updated and new documentation files.

---

### Step 3.6: Create Self-Improvement Prompts

For each new major agent, create an improvement prompt: `user_prompts/self_improvement/improve_[agent_name]_agent.user.prompt.md`

**Follow pattern from:**
- `improve_engineering_agent.user.prompt.md`
- `improve_prompt_engineering_agent.user.prompt.md`

**Key agents requiring improvement prompts:**
- Conversational UI/UX Agent
- Knowledge Base Design Agent
- Multi-Agent Workflow Developer Agent
- AI Governance & Security Agent
- Context Engineering Agent

**Deliverable:** 5-10 new self-improvement user prompts.

---

## ✅ Phase 4: Validation & Testing

### Validation Requirements

#### Test 1: Agent Specialization Validation

**Objective:** Verify each agent has a distinct specialty with no overlap.

**Method:**
- Create 30-50 representative AI engineering tasks covering all domains
- Map each task to the most appropriate agent
- Ensure no task is ambiguous (multiple equally-appropriate agents)
- Confirm no agent is idle (all agents have clear use cases)
- Apply "single responsibility test": Can each agent be described in one sentence?

**Success Criteria:** 
- 100% of tasks map clearly to exactly one agent
- Every agent passes the single responsibility test
- No capability overlaps identified
- No capability gaps identified

---

#### Test 2: End-to-End Workflow Validation

**Objective:** Verify agents work together coherently for complete AI system development.

**Scenarios:**

**Scenario A: Build a Multi-Agent Customer Support System**
```
1. Requirements Agent → Gather requirements
2. Architecture Agent → Design system architecture
3. Knowledge Base Design Agent → Design knowledge schema
4. Knowledge Base Engineering Agent → Implement knowledge base
5. Conversational UI/UX Agent → Design dialogue flows
6. Multi-Agent Workflow Developer → Implement agent orchestration
7. Prompt Engineering Agent → Create agent prompts
8. Project Scaffolding Agent → Generate framework code
9. Deployment Preparation Agent → Prepare for deployment
10. Validation Agent → Test and validate system
11. AI Governance Agent → Apply guardrails and compliance checks
```

**Scenario B: Optimize an Existing AI Agent**
```
1. Context Engineering Agent → Optimize context usage
2. Prompt Engineering Agent → Improve prompt quality
3. Validation Agent → Test improvements
```

**Success Criteria:** All scenarios complete successfully with clear agent handoffs.

---

#### Test 3: Orchestration Pattern Validation

**Objective:** Verify sequential, parallel, and hybrid workflow patterns work correctly.

**Sequential Workflow Test:**
```
Test: Code generation → Code review → Testing → Security audit
Validation:
- Each agent receives correct output from previous agent
- No data loss in handoffs
- Errors propagate correctly
- Validation checkpoints function at each boundary
```

**Parallel Workflow Test:**
```
Test: (API Development Agent || UI Development Agent || Database Agent)
Validation:
- All agents execute concurrently without conflicts
- Results aggregate correctly
- Independent failures don't cascade
- Resource contention handled appropriately
```

**Hybrid Workflow Test:**
```
Test: Design → (API || UI || Data) → Integration → Test → Deploy
Validation:
- Sequential and parallel patterns combine correctly
- State management across workflow stages
- Error recovery in complex workflows
- Performance optimization for mixed patterns
```

**Success Criteria:**
- All workflow patterns execute without errors
- Explicit contracts honored at every boundary
- Error handling and recovery work correctly
- Performance meets requirements (no blocking bottlenecks)

---

#### Test 4: Supervisor Routing Validation

**Objective:** Confirm Supervisor Agent correctly routes engineering requests.

**Test Cases:**
- "Help me design a conversation flow" → Conversational UI/UX Agent
- "I need to set up a knowledge base" → Knowledge Base Design Agent or Engineering Agent (based on context)
- "Create guardrails for my AI agent" → AI Governance & Security Agent
- "Build a Streamlit app for my agent" → Streamlit Agent
- "Optimize the context window usage" → Context Engineering Agent

**Success Criteria:** 95%+ accurate routing on 50+ test queries.

---

#### Test 5: Supervisor Agent Compatibility Validation

**Objective:** Verify complete integration with existing `supervisor_agent.system.prompt.md`.

**Supervisor Update Validation:**

1. **Architecture Diagram Accuracy (Lines 42-61)**
   - ✅ Diagram updated to show new structure (single-layer or two-layer)
   - ✅ Engineering Agent removed or transformed correctly
   - ✅ All new specialized agents listed
   - ✅ ASCII formatting correct

2. **Routing Logic Completeness (Lines 69-88)**
   - ✅ All new specialized agents have routing entries
   - ✅ Engineering Agent routing removed or updated
   - ✅ Example queries map to correct agents
   - ✅ No ambiguous routing cases

3. **Specialized Agents Reference (Lines 224-428)**
   - ✅ Each new agent has complete reference section
   - ✅ Follows established format (Location, Responsibilities, User Prompts, Knowledge Base Access, When to Route)
   - ✅ File paths are accurate
   - ✅ Engineering Agent section handled correctly (deleted, transformed, or retained)

4. **Workflow Sequences Updated (Lines 93-119, 1026-1319)**
   - ✅ Phase 4 (Implementation) reflects new structure
   - ✅ Workflow diagrams show specialized agents
   - ✅ Handoff patterns documented

5. **Example Interactions Updated (Lines 603-1022)**
   - ✅ New examples show specialized agent routing
   - ✅ Multi-agent engineering examples included
   - ✅ Engineering Supervisor examples (if two-layer)

6. **Agent Count Accurate (Line 1533)**
   - ✅ Count reflects total agents (5 existing + N new engineering agents)
   - ✅ List enumerates all agents correctly

**Naming Convention Validation:**
- ✅ All new agents follow `[domain]_agent.system.prompt.md` pattern
- ✅ No naming conflicts with existing agents
- ✅ Agent names are consistent across all files

**Separation of Concerns Validation:**
- ✅ Main Supervisor handles high-level lifecycle routing
- ✅ Engineering Supervisor (if exists) handles engineering-only routing
- ✅ Specialized engineering agents do NO routing or orchestration
- ✅ Clear boundaries: no overlapping responsibilities

**Integration Test Scenarios:**

**Test Scenario 1: User requests UI development**
```
User: "Build a Streamlit app for my AI system"
Expected: Supervisor routes to [UI Development Agent Name]
Validation: Correct agent invoked, no ambiguity
```

**Test Scenario 2: User requests multi-agent system**
```
User: "Implement a multi-agent workflow"
Expected: Supervisor routes to [Multi-Agent Orchestration Agent Name]
Validation: Correct agent invoked, workflow patterns applied
```

**Test Scenario 3: Generic engineering request (two-layer only)**
```
User: "Build a prototype"
Expected: Supervisor routes to Engineering Supervisor Agent
Then: Engineering Supervisor analyzes and routes to appropriate specialist
Validation: Two-layer delegation works correctly
```

**Success Criteria:**
- 100% of supervisor updates completed correctly
- All routing examples work as documented
- No broken file path references
- Naming conventions 100% compliant
- Clear separation of concerns validated
- Integration test scenarios pass

---

#### Test 6: Documentation Accuracy Validation

**Objective:** Ensure all documentation reflects the new architecture.

**Checklist:**
- ✅ All agent cross-references are valid
- ✅ All file paths are correct
- ✅ All examples work as documented
- ✅ Getting started guide leads to successful first experience (<15 min)
- ✅ No references to old monolithic Engineering Agent remain (unless intentionally retained)

**Legacy Engineering Agent File Validation:**
- ✅ Verify `ai_agents/engineering_agent.system.prompt.md` properly handled (deleted, transformed, or renamed)
- ✅ If deleted: Confirm archive exists in `tmp/archived_engineering_agent.system.prompt.md`
- ✅ If transformed: Confirm content updated to focus on routing/delegation only
- ✅ If renamed: Confirm new name accurately reflects narrowed scope
- ✅ All references to `engineering_agent` updated across repository:
  - `supervisor_agent.system.prompt.md`
  - `README.md`
  - `ARCHITECTURE.md`
  - `docs/agent-architecture-and-collaboration.md`
  - `docs/workflow_guide.md`
  - User prompts

**Cross-Reference Validation:**
- Run repository-wide search for "engineering_agent" and verify all results are intentional
- Check that no broken links to deleted/renamed files exist
- Validate workflow diagrams show new specialized agents, not monolithic Engineering Agent

**Success Criteria:** 
- 100% of documentation is accurate and functional
- Engineering Agent file disposition properly executed and documented
- Zero broken references to old Engineering Agent (unless it's intentionally retained with documented scope)

---

#### Test 6: Input/Output Contract Validation

**Objective:** Verify all agent boundaries have explicit, validated contracts.

**Validation Steps:**
1. **Schema Definition Check**: Every agent has documented input/output schemas
2. **Contract Testing**: Inputs/outputs conform to declared schemas
3. **Validation Rules**: All validation rules execute correctly
4. **Error Handling**: Invalid inputs rejected with clear error messages
5. **Versioning**: Contract versions documented and backward-compatible

**Test Cases:**
- Send valid inputs → verify expected outputs
- Send invalid inputs → verify graceful rejection
- Send edge case inputs → verify correct handling
- Test contract version compatibility

**Success Criteria:**
- 100% of agents have explicit input/output contracts
- All contracts tested and validated
- Error handling works correctly for all agents
- Contract versioning strategy documented

---

#### Test 7: Process Standardization & Citation Validation

**Objective:** Verify all agents cite authoritative sources and follow standardized workflows.

**Citation Requirements Check:**

1. **AWS Generative AI Lifecycle Citation**
   - Every agent cites relevant lifecycle phase(s)
   - Direct URL to AWS Well-Architected GenAI Lens included
   - Clear mapping: which phase(s) this agent implements

2. **Platform Best Practices Citations**
   - Anthropic documentation URLs included (where relevant)
   - OpenAI documentation URLs included (where relevant)
   - AWS Bedrock documentation URLs included (where relevant)
   - GitHub Copilot/Cursor best practices referenced (where relevant)

3. **Framework References**
   - Relevant frameworks cited (MetaGPT, MASAI, MANTRA, IntellAgent)
   - Academic or production sources linked
   - Multi-agent orchestration patterns referenced

4. **Update Mechanism**
   - Statement directing users to consult latest documentation
   - Clear acknowledgment that practices evolve

**Process Standardization Check:**

1. **Consistent Methodology Structure**
   - All agents use similar phase naming (Discovery → Design → Develop → Deploy → Optimize)
   - Process steps align with AWS GenAI Lifecycle where applicable
   - Consistent terminology across all agents

2. **Cross-Agent Consistency**
   - Similar capabilities described using similar language
   - Handoff protocols follow same patterns
   - Input/output contracts use consistent formats

3. **Template Compliance**
   - All agents include "Process Alignment" section
   - All agents document their lifecycle phase(s)
   - All agents cite authoritative sources

**Validation Method:**
- Review each agent's system prompt
- Check for presence of all required citations
- Verify URLs are direct and functional
- Confirm process terminology is consistent
- Validate alignment with AWS GenAI Lifecycle

**Success Criteria:**
- 100% of agents include Process Alignment section with citations
- All agents cite AWS Well-Architected GenAI Lens
- All agents reference platform-specific best practices
- Process terminology consistent across all agents (95%+ alignment)
- All URLs valid and point to authoritative sources

---

#### Test 8: Quality Benchmark Validation

**Objective:** Ensure new agents meet the quality standard set by Prompt Engineering Agent.

**Assessment Criteria** (score each agent 1-10):
- Clear role and mission definition
- Structured methodology with explicit steps
- Platform awareness and constraints
- Integration with other agents
- Advanced reasoning patterns
- Comprehensive examples
- Validation frameworks

**Success Criteria:** All new agents score 8+ / 10, average 9+ / 10.

---

#### Test 9: Evaluation Framework Validation

**Objective:** Verify evaluation and monitoring mechanisms are operational.

**Evaluation Components:**

1. **Automated Validation**
   - Agent outputs validated against acceptance criteria
   - Automated test suites execute for all agents
   - Validation failures trigger appropriate alerts

2. **Benchmark Metrics**
   - Code quality scores tracked (if applicable)
   - Test coverage metrics recorded (if applicable)
   - Security ratings monitored (if applicable)
   - Performance metrics logged

3. **Success Rate Tracking**
   - Agent success/failure rates calculated
   - Trends analyzed over time
   - Anomalies detected and reported

4. **Human-in-the-Loop Validation**
   - Critical operations flagged for human review
   - Approval workflows function correctly
   - Feedback mechanisms operational

**Test Scenarios:**
- Run agents with test inputs → verify automated validation works
- Check benchmark metric collection → verify data logging
- Review success rate calculations → verify accuracy
- Test human validation workflows → verify approval process

**Success Criteria:**
- Automated validation operational for all agents
- Benchmark metrics defined and tracked
- Success rate tracking implemented
- Human validation workflows function correctly

---

## 🎯 Success Criteria

This refactoring succeeds when ALL of the following are achieved:

### ✅ Architectural Success

- [ ] Engineering Agent successfully decomposed into specialized agents (number determined by research)
- [ ] Legacy `engineering_agent.system.prompt.md` file properly handled (deleted, transformed, or renamed with rationale)
- [ ] Archive of original file saved to `tmp/archived_engineering_agent.system.prompt.md`
- [ ] **Supervisor compatibility maintained:** `supervisor_agent.system.prompt.md` successfully updated and integrated
- [ ] **Naming conventions compliant:** All new agents follow `[domain]_agent.system.prompt.md` pattern
- [ ] **Separation of concerns clear:** Main Supervisor vs Engineering Supervisor (if exists) vs Specialists
- [ ] Clear agent collaboration patterns established
- [ ] Supervisor routing logic handles all engineering scenarios
- [ ] No capability gaps (all engineering tasks covered)
- [ ] No capability overlaps (clear specialization boundaries)
- [ ] AWS Well-Architected Framework principles integrated across all agents

### ✅ Quality Success

- [ ] All new agents meet quality benchmark (Prompt Engineering Agent standard)
- [ ] Consistent structure and style across all agents
- [ ] Comprehensive examples for all agents
- [ ] Advanced reasoning patterns applied appropriately
- [ ] Platform compatibility validated (Cursor, Copilot, Claude Projects)
- [ ] Best practices from Anthropic, OpenAI, Mistral.ai incorporated

### ✅ Process Standardization & Citation Success

- [ ] All agents cite AWS Generative AI Lifecycle with direct URLs
- [ ] 100% of agents include "Process Alignment" section
- [ ] Platform-specific best practices cited (Anthropic, OpenAI, AWS Bedrock)
- [ ] Framework references included (MetaGPT, MASAI, MANTRA, IntellAgent)
- [ ] Consistent process terminology across all agents (95%+ alignment)
- [ ] All citation URLs validated and functional
- [ ] Update mechanisms included ("Consult [URL] for latest guidance")

### ✅ Documentation Success

- [ ] README.md updated and follows best practices
- [ ] All documentation reflects new architecture
- [ ] New engineering agents guide created
- [ ] End-to-end examples provided
- [ ] All cross-references valid

### ✅ User Prompts Success

- [ ] Comprehensive user prompts created (50-150+ based on agent scope)
- [ ] 1:many relationship maintained (each agent has 5-20 user prompts)
- [ ] All common AI engineering tasks covered
- [ ] User prompts follow established patterns
- [ ] Self-improvement prompts created for major agents
- [ ] Platform-agnostic design (work across Cursor, Copilot, Claude)

### ✅ Integration Success

- [ ] Knowledge base schemas support new agents
- [ ] Output directory structure accommodates new agents
- [ ] Existing agents (Requirements, Architecture, Deployment, Optimization, Prompt Engineering) integrate seamlessly
- [ ] Platform deployment guidance updated

### ✅ Validation Success

- [ ] Agent specialization validation passed (100% clear mapping)
- [ ] End-to-end workflow validation passed (all scenarios)
- [ ] Orchestration pattern validation passed (sequential, parallel, hybrid)
- [ ] **Supervisor agent compatibility validation passed (100% integration)**
- [ ] Supervisor routing validation passed (95%+ accuracy)
- [ ] Documentation accuracy validation passed (100%)
- [ ] Input/output contract validation passed (all agents)
- [ ] Process standardization & citation validation passed (100% agents have citations)
- [ ] Quality benchmark validation passed (8+/10 all agents)
- [ ] Evaluation framework validation passed (automated + human)
- [ ] Platform compatibility validation (Cursor, Copilot, Claude Projects)
- [ ] Well-Architected Framework compliance check

### ✅ Architectural Compliance

- [ ] Single Responsibility Principle: Every agent has exactly one well-defined function
- [ ] Orchestration vs Execution Separation: Supervisors route only, specialists work only
- [ ] Modular Architecture: All agents independently upgradeable and swappable
- [ ] Explicit Contracts: All agent boundaries have defined input/output schemas
- [ ] Workflow Patterns: Chain, parallel, and hybrid orchestration patterns validated

---

## 🛡️ Safety Guardrails

### MUST Preserve

- ✅ All existing agent capabilities (Requirements, Architecture, Deployment, Optimization, Prompt Engineering)
- ✅ Archive of original `engineering_agent.system.prompt.md` in `tmp/archived_engineering_agent.system.prompt.md`
- ✅ Knowledge base structure and JSON schemas
- ✅ Output directory organization (`outputs/[category]/[project]/`)
- ✅ Platform compatibility (Cursor, Claude Projects, GitHub Copilot)
- ✅ Existing user prompts and workflows (update references to Engineering Agent as needed)
- ✅ Multi-agent orchestration patterns

### MUST NOT

- ❌ Break backward compatibility with existing workflows
- ❌ Remove any current capabilities without replacement
- ❌ Delete `engineering_agent.system.prompt.md` without archiving it to `tmp/`
- ❌ Leave broken references to `engineering_agent` after file deletion/transformation
- ❌ Create ambiguous agent boundaries (overlapping responsibilities)
- ❌ Introduce security vulnerabilities or unsafe patterns
- ❌ Generate untested or unvalidated agent prompts
- ❌ Create circular dependencies between agents

### MUST Follow

- ✅ Patterns from `prompt_engineering_agent.system.prompt.md` (quality benchmark)
- ✅ Guidelines from `improve_ai_engineering_assistant.user.prompt.md`
- ✅ Standards from `improve_engineering_agent.user.prompt.md`
- ✅ Documentation principles from `make_readme_awesome_for_junior_engineers.user.prompt.md`
- ✅ All quality standards from `optimization_agent.system.prompt.md`

---

## 📦 Deliverables Checklist

### Phase 1: Research & Discovery
- [ ] Research summary document (AI engineering best practices)
- [ ] Platform capabilities analysis (Cursor, Copilot, Claude Projects, AWS Bedrock)
- [ ] LLM provider best practices (Anthropic, OpenAI, Mistral.ai, Google)
- [ ] Current Engineering Agent capability mapping
- [ ] AI system component architecture research
- [ ] AWS Well-Architected Framework + GenAI Lens analysis
- [ ] Standardized AI development workflows documentation with authoritative citations
- [ ] Process reference library with direct URLs to all sources
- [ ] Standard process templates for agent consistency
- [ ] Citation requirements specification
- [ ] Orchestration pattern analysis with workflow recommendations

### Phase 2: Architectural Design
- [ ] Supervisor architecture decision documented (single vs two-layer)
- [ ] **Supervisor compatibility strategy defined:** Integration approach with existing `supervisor_agent.system.prompt.md`
- [ ] **Naming conventions established:** All agents follow `[domain]_agent.system.prompt.md` pattern
- [ ] Final specialized agents list with role definitions
- [ ] Agent interaction diagram showing collaboration patterns
- [ ] Collaboration matrix (agent-to-agent handoffs)
- [ ] Well-Architected Framework alignment strategy per agent

### Phase 3: Implementation
- [ ] [N] new agent system prompts (`ai_agents/*.system.prompt.md`) - number determined by Phase 2
- [ ] [M] new user prompts (`user_prompts/engineering/*/*.user.prompt.md`) - 50-150+ distributed across agents
- [ ] **`supervisor_agent.system.prompt.md` completely updated:**
  - [ ] Architecture diagram updated (lines 42-61)
  - [ ] Routing logic updated (lines 69-88)
  - [ ] Specialized agents reference sections added (lines 224-428)
  - [ ] Engineering Agent section handled (lines 298-330)
  - [ ] Workflow sequences updated (lines 93-119, 1026-1319)
  - [ ] Example interactions updated (lines 603-1022)
  - [ ] Agent count updated (line 1533)
- [ ] Legacy `engineering_agent.system.prompt.md` properly handled:
  - [ ] If deleted: Archived to `tmp/` and file removed
  - [ ] If transformed: Renamed and refactored for supervisor role
  - [ ] If renamed: Updated to reflect narrowed scope
  - [ ] Decision and rationale documented in refactoring report
- [ ] (Optional) New `engineering_supervisor_agent.system.prompt.md` if two-layer chosen
- [ ] All cross-references to `engineering_agent` updated throughout repository
- [ ] Updated knowledge base schemas (if needed)
- [ ] Updated core documentation (README, ARCHITECTURE, docs/)
- [ ] New `docs/engineering-agents-guide.md`
- [ ] New `docs/examples/multi-agent-system-development.md`
- [ ] 5-15 new self-improvement prompts for major agents

### Phase 4: Validation
- [ ] Agent specialization validation report (100% clear mapping, single responsibility test)
- [ ] End-to-end workflow validation results (all scenarios pass)
- [ ] Orchestration pattern validation results (chain, parallel, hybrid workflows)
- [ ] **Supervisor agent compatibility validation report (100% integration with existing supervisor)**
- [ ] Supervisor routing validation results (95%+ accuracy on 50+ queries)
- [ ] Documentation accuracy validation report (100% valid references)
- [ ] Input/output contract validation report (all agents have explicit schemas)
- [ ] Process standardization & citation validation report (100% compliance, all URLs functional)
- [ ] Quality benchmark validation scores (8+/10 all agents)
- [ ] Evaluation framework validation report (automated + human validation)
- [ ] Platform compatibility validation (Cursor, Copilot, Claude Projects)
- [ ] Well-Architected Framework compliance check
- [ ] Architectural compliance report (single responsibility, orchestration separation, modularity, explicit contracts)
- [ ] **Naming convention compliance report (100% follow `[domain]_agent.system.prompt.md` pattern)**

### Final Deliverable
- [ ] **Comprehensive refactoring report** documenting all changes, architectural decisions, validation results, and platform compatibility
- [ ] **Engineering Agent File Disposition Documentation**:
  - [ ] Decision recorded (deleted, transformed, or renamed)
  - [ ] Rationale explained
  - [ ] Capability mapping: which specialized agents now handle which responsibilities
  - [ ] Migration guide: how users should adapt to the new structure
  - [ ] Archive location confirmed: `tmp/archived_engineering_agent.system.prompt.md`

---

## 🚀 Execution Instructions

**Optimization Agent (You):**
1. **Phase 1:** Conduct research (2-3 hours)
2. **Phase 2:** Make architectural decisions and create designs (2-3 hours)
3. **Phase 3:** Implement all agents, user prompts, and documentation (6-10 hours)
4. **Phase 4:** Execute all validation tests (2-3 hours)
5. **Report:** Generate comprehensive refactoring report (1 hour)

**Estimated Total Time:** 13-19 hours of focused AI agent work

**Platform Support:** Cursor IDE, Claude Projects, GitHub Copilot

**Collaboration:** May invoke Prompt Engineering Agent for quality validation of new agent prompts

---

## 📝 Notes

**Research-Driven Design:** This prompt provides potential specialization domains for consideration, but the final architecture should be determined by comprehensive research into AI engineering best practices, platform capabilities, and natural domain boundaries. Let empirical evidence guide architectural decisions.

**Complexity Acknowledgment:** This is a major architectural refactoring that will significantly expand the system. Take time to research thoroughly and design carefully before implementing. The exact number of agents and user prompts will emerge from Phase 1-2 analysis.

**Reference Model:** The Prompt Engineering Agent (`ai_agents/prompt_engineering_agent.system.prompt.md`) represents the quality standard. All new agents should match or exceed its structure, clarity, comprehensiveness, and platform compatibility.

**Platform-First Mindset:** All agents must be deployable and effective across Cursor IDE, GitHub Copilot, and Anthropic Claude Projects. Follow official best practices from each platform and leading LLM providers (Anthropic, OpenAI, Mistral.ai).

**Well-Architected Framework Integration:** AWS Well-Architected Framework (6 pillars + Generative AI Lens) must be embedded in all agents, not just mentioned. Agents should enforce operational excellence, security, reliability, performance, cost optimization, and sustainability.

**1:Many Relationship:** Remember that each specialized agent will have multiple user prompts (5-20+). The goal is comprehensive task coverage, not minimal agent count.

**Coherence Priority:** The system must work as a unified whole. Each agent must have clear boundaries, distinct specialties, and smooth collaboration patterns.

**User Experience Focus:** Despite increased complexity, the system must remain easy to use. Clear routing, good documentation, and intuitive workflows are essential.

**Documentation Critical:** With an expanded agent system, comprehensive documentation becomes even more important. Invest heavily in guides, examples, and navigation aids.

**Framework References:** This prompt integrates best practices from leading multi-agent AI frameworks:
- **MetaGPT**: Meta-programming for multi-agent collaboration with modular agent roles
- **MASAI**: Modular architecture for software-engineering AI agents with context-aware capabilities
- **MANTRA**: Multi-agent LLM refactoring with distributed validation patterns
- **IntellAgent**: Benchmark-driven evaluation frameworks for multi-agent system assessment
- **AWS Bedrock AgentCore**: Production-grade multi-agent orchestration with supervisor-worker patterns

**Key Research Principles Applied:**
- Single Responsibility Principle for all agents (no universal engineers)
- Orchestration vs execution separation (supervisors route, specialists work)
- Sequential, parallel, and hybrid workflow patterns
- Explicit input/output contracts at all boundaries
- Benchmark-driven evaluation with automated and human validation
- Modular, swappable architecture with meta-programming support

**Process Standardization & Citation Requirements:** This refactoring mandates that ALL agents explicitly cite authoritative sources and align with standardized AI development workflows. Every agent must include:
1. **AWS Generative AI Lifecycle citations** with direct URLs
2. **Platform-specific best practices** from Anthropic, OpenAI, AWS Bedrock
3. **Framework references** to MetaGPT, MASAI, MANTRA, IntellAgent
4. **Consistent process terminology** aligned with industry standards
5. **Update mechanisms** directing users to latest documentation

This ensures consistency, enables effective collaboration, and keeps agents aligned with evolving best practices. Agents can reference the latest guidance directly from authoritative sources rather than relying on static knowledge.

---

**Version:** 2.3  
**Created:** 2025-10-11  
**Last Updated:** 2025-10-11  
**Task Type:** Major Architectural Refactoring  
**Execution Mode:** Research-Driven Multi-Phase Implementation (State-of-the-Art 2025)  
**Estimated Effort:** 15-25 hours (expanded scope with comprehensive validation)  
**Safety Level:** High (major system changes with comprehensive validation)  
**Research Foundation:** MetaGPT, MASAI, MANTRA, IntellAgent, AWS Bedrock AgentCore, Anthropic/OpenAI/Mistral.ai best practices  
**Process Standardization:** All agents must cite AWS GenAI Lifecycle and authoritative sources with direct URLs for consistency and collaboration  
**File Management:** Explicit handling of legacy `engineering_agent.system.prompt.md` - delete (with archive), transform, or rename based on architectural decisions  
**Supervisor Compatibility:** Mandatory integration with existing `supervisor_agent.system.prompt.md` (1,557 lines) with naming conventions, routing updates, and clear separation of concerns 