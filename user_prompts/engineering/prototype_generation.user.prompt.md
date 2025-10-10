# Prototype Generation - User Prompt

**Phase:** Implementation (Phase 2)  
**Purpose:** Build working AI system prototype from architecture design  
**Agent:** Engineering Agent  
**Input:** `knowledge_base/user_requirements.json`, `knowledge_base/design_decisions.json`  
**Output:** `outputs/prototypes/[project-name]/`  
**Duration:** 2-5 days (depending on complexity)

---

## Purpose

Transform architecture designs into functional, demonstrable AI system prototypes. This prompt guides the Engineering Agent through rapid prototype development following the tech stack, architecture, and requirements specified in the knowledge base.

---

## When to Use This Prompt

**Prerequisites:**
- ✅ Requirements gathering complete (`user_requirements.json` populated)
- ✅ Architecture design complete (`design_decisions.json` populated)
- ✅ Tech stack selected and documented
- ✅ Go-ahead received from stakeholders (proposals approved)

**Best for:**
- Building initial working prototypes (MVP/POC)
- Demonstrating AI system capabilities to stakeholders
- Validating architecture decisions with real code
- Creating foundation for production development

**Not for:**
- Production-ready systems (use after prototype validation)
- Architecture design (use Architecture Agent)
- Requirements gathering (use Requirements Agent)

---

## Instructions for Engineering Agent

### Phase 1: Design Review & Setup (30 minutes)

```
<thinking>
1. Read knowledge base files:
   - user_requirements.json → Business context, functional requirements
   - design_decisions.json → Tech stack, architecture, estimates
   - system_config.json → Platform constraints, team skills

2. Extract key information:
   - Tech stack: [LLM provider, frameworks, languages]
   - Architecture pattern: [Single agent / Multi-agent / RAG / etc.]
   - Target deployment: [Cursor / AWS Bedrock / Self-hosted]
   - Timeline: [Estimated hours from design_decisions]
   
3. Identify deliverables:
   - Agent prompts: [COUNT] agents needed
   - Backend code: [Language, framework]
   - Frontend: [Framework or CLI]
   - Demo scenarios: [COUNT] test cases
   - Documentation: [What to include]
</thinking>

✅ **Design Review Complete**

**Project:** [Project Name]  
**Architecture Pattern:** [Pattern]  
**Tech Stack:**
- LLM: [Provider and models]
- Backend: [Language/framework]
- Frontend: [Framework]
- Infrastructure: [Deployment target]

**Deliverables:**
1. [Deliverable 1]
2. [Deliverable 2]
3. [Deliverable 3]

**Estimated Effort:** [Hours from design_decisions.json]

Beginning prototype development...
```

---

### Phase 2: Agent Prompt Generation (2-4 hours)

Generate production-quality system prompts for each AI agent in the design:

```
✅ **Agent Prompts Generated**

**Agents Created:** [COUNT]

1. **[Agent Name]** - `prompts/[agent_name].system.prompt.md`
   - Role: [Description]
   - Capabilities: [Key capabilities]
   - Line count: [Approximate lines]

2. **[Agent Name 2]** - `prompts/[agent_name_2].system.prompt.md`
   - Role: [Description]
   - Capabilities: [Key capabilities]
   - Line count: [Approximate lines]

[... more agents]

**Quality checks:**
- ✅ Clear role and mission statements
- ✅ Structured instructions with XML tags
- ✅ Concrete examples provided
- ✅ Error handling guidance included
- ✅ Success criteria defined

Next: Backend implementation...
```

**Agent Prompt Template:**

```markdown
# [Agent Name] - [Agent Type]

## Role

You are a [ROLE] specializing in [DOMAIN]. Your purpose is [ONE_SENTENCE_DESCRIPTION].

## Your Capabilities

- [Capability 1 with details]
- [Capability 2 with details]
- [Capability 3 with details]

## Instructions

### When [TRIGGER_CONDITION]

1. [Step 1 with details]
2. [Step 2 with details]
3. [Step 3 with details]

### Input Format

[Specify expected input structure with example]

### Output Format

[Specify exact output structure with example]

### Error Handling

- If [error_condition]: [recovery_action]
- If [error_condition]: [recovery_action]

## Examples

<example>
User: [Example input]

Agent: [Example output with reasoning]
</example>

<example>
User: [Another example input]

Agent: [Another example output]
</example>

## Constraints

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Success Criteria

You are succeeding when:
- ✅ [Success criterion 1]
- ✅ [Success criterion 2]
- ✅ [Success criterion 3]
```

---

### Phase 3: Backend Implementation (4-12 hours, varies by complexity)

Build the backend infrastructure per tech stack specifications:

```
✅ **Backend Implementation Complete**

**Technology:** [Language/Framework from design_decisions]

**Files Created:**
- `src/main.[ext]` - Application entry point
- `src/agents/[agent_name].[ext]` - Agent orchestration
- `src/utils/llm_client.[ext]` - LLM API integration
- `src/utils/knowledge_base.[ext]` - Data access layer
- `requirements.txt` or `package.json` - Dependencies
- `config/settings.[ext]` - Configuration management
- `.env.example` - Environment variables template

**Key Components:**
1. **LLM Integration**
   - Provider: [Provider name]
   - Models: [Models used]
   - Error handling: Retry logic, fallbacks

2. **Agent Orchestration**
   - Pattern: [Supervisor-worker / Sequential / Parallel]
   - Context management: [How context is maintained]

3. **Data Management**
   - Knowledge base access: [How agents read/write]
   - State persistence: [Session management approach]

**Testing:**
- ✅ LLM API connectivity tested
- ✅ Agent instantiation working
- ✅ Basic workflows functional

Next: Frontend/UI implementation...
```

---

### Phase 4: Frontend/UI Implementation (3-8 hours)

Create user interface per design specifications:

```
✅ **Frontend Implementation Complete**

**Technology:** [Framework from design_decisions]

**Files Created:**
- `ui/app.[ext]` - Main application
- `ui/components/[component].[ext]` - Reusable components
- `ui/styles/[style].[ext]` - Styling
- `ui/config.[ext]` - UI configuration

**Features Implemented:**
- [Feature 1]: [Description]
- [Feature 2]: [Description]
- [Feature 3]: [Description]

**User Experience:**
- Input methods: [Text, file upload, etc.]
- Output display: [Formatting, visualization]
- Error handling: [User-friendly error messages]

**Testing:**
- ✅ UI renders correctly
- ✅ Agent interaction working
- ✅ Error states handled gracefully

Next: Demo scenarios...
```

---

### Phase 5: Demo Scenario Creation (2-3 hours)

Build realistic test cases that demonstrate capabilities:

```
✅ **Demo Scenarios Created**

**Scenarios:** [COUNT] test cases in `demos/`

1. **[Scenario Name]** - `demos/scenario_1_[name].md`
   - Purpose: [What this demonstrates]
   - Test data: [Input data provided]
   - Expected outcome: [What should happen]
   - Success criteria: [How to validate]

2. **[Scenario Name 2]** - `demos/scenario_2_[name].md`
   - Purpose: [What this demonstrates]
   - Test data: [Input data provided]
   - Expected outcome: [What should happen]
   - Success criteria: [How to validate]

[... more scenarios]

**Coverage:**
- ✅ Happy path workflows
- ✅ Edge cases
- ✅ Error handling
- ✅ Integration points

Next: Documentation...
```

---

### Phase 6: Documentation (2-3 hours)

Create comprehensive documentation for the prototype:

```
✅ **Documentation Complete**

**Files Created:**

1. **README.md** - Quick start guide
   - Setup instructions (5-10 minutes)
   - Dependencies and installation
   - Configuration steps
   - How to run demos
   - Troubleshooting

2. **docs/ARCHITECTURE.md** - Technical details
   - System architecture overview
   - Component descriptions
   - Data flows
   - LLM integration patterns

3. **docs/USER_GUIDE.md** - End-user instructions
   - How to use each feature
   - Example interactions
   - Tips and best practices

4. **docs/API.md** - API documentation (if applicable)
   - Endpoints
   - Request/response formats
   - Authentication
   - Rate limits

**Quality checks:**
- ✅ Clear and concise
- ✅ Examples provided
- ✅ Troubleshooting included
- ✅ Platform-specific notes

Next: Final validation...
```

---

### Phase 7: Validation & Testing (1-2 hours)

Validate the prototype before handoff:

```
✅ **Prototype Validation Complete**

**Functionality Tests:**
- ✅ All demo scenarios executed successfully
- ✅ Agent responses appropriate and helpful
- ✅ Error handling working correctly
- ✅ LLM API integration stable

**Quality Checks:**
- ✅ Code follows best practices
- ✅ Documentation complete and accurate
- ✅ Dependencies documented
- ✅ Configuration clear and simple

**Readiness Assessment:**
- ✅ Demo-ready: Can be shown to stakeholders reliably
- ✅ Iteration-ready: Can be improved based on feedback
- ⚠️ Not production-ready: Needs hardening (see deployment agent)

**Known Limitations:**
- [Limitation 1]
- [Limitation 2]

**Recommended Next Steps:**
1. Demo to stakeholders and gather feedback
2. Iterate based on feedback
3. When validated, proceed to Deployment Agent for production hardening

**Prototype Location:** `outputs/prototypes/[project-name]/`
```

---

### Phase 8: Handoff Package (30 minutes)

Create complete handoff package:

```
✅ **Prototype Handoff Package Ready**

**Deliverables:**

📁 `outputs/prototypes/[project-name]/`
  ├── 📄 README.md (Quick start)
  ├── 📁 prompts/ (Agent system prompts)
  ├── 📁 src/ (Backend code)
  ├── 📁 ui/ (Frontend code)
  ├── 📁 demos/ (Test scenarios)
  ├── 📁 docs/ (Documentation)
  ├── 📁 config/ (Configuration files)
  └── 📄 requirements.txt or package.json

**Metrics:**
- Total files: [COUNT]
- Lines of code: [APPROXIMATE]
- Agent prompts: [COUNT]
- Demo scenarios: [COUNT]
- Documentation pages: [COUNT]

**Time to Value:**
- Setup time: [5-10 minutes]
- First demo: [< 5 minutes after setup]
- Learning curve: [Low / Medium / High]

**Next Agent:** Deployment Agent (for platform deployment)

---

🎉 **Prototype Development Complete!**

Your AI system prototype is ready for stakeholder demonstration and feedback.
```

---

## Output Structure

All prototype files go into `outputs/prototypes/[project-name]/` with this structure:

```
outputs/prototypes/[project-name]/
├── README.md                          # Quick start guide
├── requirements.txt (or package.json) # Dependencies
├── .env.example                       # Environment variables template
├── prompts/                          # Agent system prompts
│   ├── [agent_1].system.prompt.md
│   └── [agent_2].system.prompt.md
├── src/                              # Backend code
│   ├── main.[ext]                    # Entry point
│   ├── agents/                       # Agent implementations
│   ├── utils/                        # Utilities (LLM client, etc.)
│   └── config/                       # Configuration
├── ui/ (or cli/)                     # Frontend or CLI
│   ├── app.[ext]                     # Main UI file
│   └── components/                   # UI components
├── demos/                            # Test scenarios
│   ├── scenario_1_[name].md
│   └── scenario_2_[name].md
├── docs/                             # Documentation
│   ├── ARCHITECTURE.md               # Technical details
│   ├── USER_GUIDE.md                 # End-user guide
│   └── API.md                        # API docs (if applicable)
├── tests/ (optional)                 # Unit tests
└── data/ (optional)                  # Sample data
```

---

## Technology-Specific Guidelines

### Python + Streamlit (Common Stack)

**Structure:**
- Entry point file that initializes the app
- Imports agent classes
- Creates UI elements (title, chat input)
- Processes user input through agent
- Displays responses

### Python + FastAPI (API-based)

**Structure:**
- Entry point that creates API server
- Imports and initializes agents
- Defines API endpoints for chat/processing
- Handles async requests
- Returns JSON responses

### Node.js + Express

```javascript
// src/main.js - Entry point
const express = require('express');
const SupervisorAgent = require('./agents/supervisor');

const app = express();
const agent = new SupervisorAgent();

app.post('/chat', async (req, res) => {
  const response = await agent.process(req.body.message);
  res.json({ response });
});

app.listen(3000);
```

---

## Success Criteria

The prototype is successful when:

✅ **Functional**
- All demo scenarios execute correctly 10+ times
- Agent responses are appropriate and helpful
- Error handling prevents crashes

✅ **Demonstrable**
- Can be shown to stakeholders confidently
- Setup takes < 10 minutes
- Clear value proposition evident in < 5 minutes

✅ **Documented**
- README enables quick start without assistance
- Architecture documentation explains design decisions
- User guide covers all features

✅ **Iterable**
- Code is clean and modular
- Easy to modify based on feedback
- Clear separation of concerns

✅ **Foundation for Production**
- Follows architecture design
- Uses specified tech stack
- Demonstrates key capabilities
- Ready for hardening by Deployment Agent

---

## Common Patterns by AI System Type

### Pattern 1: Single Agent Assistant

**Example:** Personal financial advisor, writing assistant, code helper

**Structure:**
- 1 agent prompt
- Simple UI (Streamlit or CLI)
- Direct LLM integration
- Session state management

**Timeline:** 1-2 days

---

### Pattern 2: Multi-Agent System (Supervisor-Worker)

**Example:** Financial operations assistant, customer support system

**Structure:**
- 1 supervisor agent
- 2-5 specialized worker agents
- Agent orchestration logic
- Shared knowledge base
- Complex UI with agent routing

**Timeline:** 3-5 days

---

### Pattern 3: RAG (Retrieval-Augmented Generation)

**Example:** Document Q&A, knowledge base assistant

**Structure:**
- 1-2 agents
- Vector database integration
- Document ingestion pipeline
- Semantic search
- Citation generation

**Timeline:** 2-4 days

---

### Pattern 4: Agentic Workflow

**Example:** Research assistant, competitive analysis tool

**Structure:**
- Multiple sequential agents
- Tool use (web search, calculators, APIs)
- Workflow orchestration
- Result aggregation

**Timeline:** 3-5 days

---

## Troubleshooting

**Problem: LLM API errors**
- Check API keys in `.env`
- Verify network connectivity
- Check rate limits and quotas
- Add retry logic with exponential backoff

**Problem: Agent responses inconsistent**
- Review agent prompts for clarity
- Add more examples to prompts
- Increase temperature for creativity or decrease for consistency
- Validate input preprocessing

**Problem: UI not rendering correctly**
- Check browser console for errors
- Verify dependencies installed
- Check framework version compatibility
- Test in different browsers

**Problem: Slow response times**
- Profile LLM API call latency
- Add caching for repeated queries
- Optimize prompt length
- Consider using smaller/faster models for simple tasks

---

## Quality Gates

Before marking prototype complete, verify:

- [ ] All functional requirements from `user_requirements.json` addressed
- [ ] Tech stack from `design_decisions.json` correctly implemented
- [ ] All demo scenarios pass consistently
- [ ] Documentation enables independent setup
- [ ] No hardcoded secrets (use `.env`)
- [ ] Error handling prevents crashes
- [ ] Code follows language best practices
- [ ] Git repository initialized with appropriate `.gitignore`

---

## Next Steps

After prototype is complete and validated:

1. **Demo to stakeholders** - Show working system, gather feedback
2. **Iterate** - Improve based on feedback (re-run this prompt if needed)
3. **Deploy** - Use Deployment Agent to deploy to target platform
4. **Production hardening** - Security, scalability, monitoring (Deployment Agent)

---

**Version:** 0.1  
**Last Updated:** 2025-10-04  
**Agent:** Engineering Agent  
**Typical Duration:** 2-5 days (16-40 hours) depending on complexity
