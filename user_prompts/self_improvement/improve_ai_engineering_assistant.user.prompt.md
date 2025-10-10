# Improve AI Engineering Assistant - System-Wide Optimization

**Purpose:** Comprehensively optimize the entire AI Engineering Assistant multi-agent framework for maximum effectiveness, usability, and maintainability.

**Target System:** {{TARGET_SYSTEM}} = AI Engineering Assistant (this repository)  
**Scope:** All agents, user prompts, knowledge base, documentation, workflows, and templates  

**Role Clarity:** This user prompt specifies WHAT to optimize (target system, components, scope). Your system prompt defines HOW to optimize (methodology, assessment framework, validation protocols). Follow your standard Discover → Assess → Improve → Validate process.

---

## 🛡️ Recursion Prevention (CRITICAL)

<recursion_guardrails>

**MANDATORY PRE-EXECUTION CHECK:**

This prompt orchestrates system-wide optimization that could trigger infinite loops. Before starting ANY work:

```
OPTIMIZATION_ITERATION_COUNT: {{CURRENT_ITERATION}}
MAX_ITERATIONS: 1
BASE_CASE: OPTIMIZATION_ITERATION_COUNT >= MAX_ITERATIONS
```

**Execution Rules:**

1. **Check iteration count FIRST:**
   - If `OPTIMIZATION_ITERATION_COUNT = 0`: Proceed, set to 1
   - If `OPTIMIZATION_ITERATION_COUNT >= 1`: STOP IMMEDIATELY

2. **If recursion detected, report and halt:**

   ```
   ⚠️ RECURSION DETECTED: System optimization already completed this session.
   
   Current iteration: {{CURRENT_ITERATION}}
   Status: OPTIMIZATION COMPLETE (previous run)
   
   To run another optimization cycle:
   - Review previous optimization report
   - Start a NEW session/conversation
   - Explicitly request "Run system optimization again"
   
   STOPPING to prevent infinite loop.
   ```

3. **Single execution guarantee:** This prompt runs ONCE per session, then increments counter to prevent re-execution

</recursion_guardrails>

---

## Optimization Scope

Systematically analyze and improve ALL components of the AI Engineering Assistant:

### 1. Agent System Prompts (`ai_agents/`)

**Agents to optimize:**
- `supervisor_agent.system.prompt.md` - Multi-agent orchestration
- `requirements_agent.system.prompt.md` - Discovery & requirements gathering
- `architecture_agent.system.prompt.md` - System design & planning
- `engineering_agent.system.prompt.md` - Prototype & code generation
- `deployment_agent.system.prompt.md` - Testing & deployment
- `optimization_agent.system.prompt.md` - System improvement (self-improvement with extra validation)
- `prompt_engineering_agent.system.prompt.md` - Prompt creation & optimization

**Assessment focus:**
- Anthropic/OpenAI prompt engineering best practices
- Clear role definitions, structured instructions, concrete examples
- Chain-of-thought reasoning, tool usage patterns
- Separation of concerns, no capability overlap
- AWS Well-Architected alignment

---

### 2. User Prompts (`user_prompts/`)

**Categories:**
- `requirements/*.user.prompt.md` - Discovery workflows (4 prompts)
- `architecture/*.user.prompt.md` - Architecture tasks (6 prompts)
- `engineering/*.user.prompt.md` - Engineering tasks (1 prompt)
- `deployment/*.user.prompt.md` - Deployment tasks (2 prompts)
- `self_improvement/*.user.prompt.md` - Agent improvement tasks (8 prompts, including THIS prompt)
- `prompt_engineering/*.user.prompt.md` - Prompt engineering tasks (6 prompts)
- `proposals/*.user.prompt.md` - Proposal assembly (4 prompts)

**Assessment focus:**
- Clarity and conciseness
- Appropriate level of detail (task specification vs. methodology duplication)
- Consistency across similar prompt types
- Integration with agent system prompts
- Token efficiency

---

### 3. Knowledge Base (`knowledge_base/`)

**Files:**
- `user_requirements.json` - Customer needs, use cases
- `design_decisions.json` - Architecture, estimates, costs
- `system_config.json` - Platform settings, constraints
- `README.md` - Usage documentation

**Assessment focus:**
- Schema completeness and extensibility
- Documentation clarity
- Access patterns across agents
- Version control friendliness

---

### 4. Documentation & Templates (`guides/`, `docs/`, `templates/`)

**Files to optimize:**
- User guides (workflow_guide.md, getting-started.md, platform_deployment.md, etc.)
- Technical documentation (agent-design-patterns.md, agent-relationships.md)
- Templates (requirements-template.md, architecture-template.md, etc.)
- Executive overview and deployment guides

**Assessment focus:**
- Beginner accessibility (<15 min to productivity)
- Completeness (all workflows documented)
- Accuracy (examples work as documented)
- Platform-specific guidance (Cursor, AWS Bedrock, GitHub Copilot)
- Terminology clarity and consistency

---

### 5. Cross-Cutting Concerns

**End-to-end workflows:**
- Requirements → Architecture → Engineering → Deployment (complete lifecycle)
- Multi-shot Architecture Agent workflow (6 orchestrated user prompts)
- Knowledge base read/write patterns
- Supervisor routing logic
- Prompt Engineering Agent integration with other agents

**User experience:**
- Clear entry points (which agent/prompt for which task)
- Time to first result (<15 minutes for simple workflows)
- Example consistency (financial operations assistant throughout)
- Error handling and troubleshooting guidance

---

## Assessment Framework

Use your standard optimization dimensions and assessment criteria from your system prompt, with special attention to:

- **Prompt Engineering Excellence**: Anthropic/OpenAI best practices across all agents
- **Multi-Agent Coordination**: Clean separation of concerns, smooth handoffs, supervisor orchestration
- **Knowledge Management**: JSON schema quality, access patterns, documentation
- **User Experience**: Time to first result (<15 min), navigation clarity, platform deployment completeness
- **Documentation Quality**: Onboarding, examples, troubleshooting guidance
- **AWS Well-Architected Alignment**: Architecture Agent enforcement of 6 pillars + GenAI Lens
- **Terminology Clarity**: Consistent use of "optimize" vs "improve" vs "enhance"

*Note: Your system prompt contains the detailed assessment framework. This section highlights areas of particular importance for the AI Engineering Assistant.*

---

## Special Considerations

### Meta-Optimization Awareness
You're optimizing the system you're part of. Handle carefully:

- **Self-improvement:** When optimizing `optimization_agent.system.prompt.md` or `prompt_engineering_agent.system.prompt.md`, apply extra validation
- **Circular dependencies:** Watch for prompt → prompt → prompt references
- **Backward compatibility:** Preserve all existing workflows
- **Validation thoroughness:** Test end-to-end workflows after changes

### Agent-Specific Improvement Prompts
Consider whether to use specialized improvement prompts for each agent (in `user_prompts/self_improvement/`):
- `improve_requirements_agent.user.prompt.md`
- `improve_architecture_agent.user.prompt.md`
- `improve_engineering_agent.user.prompt.md`
- `improve_deployment_agent.user.prompt.md`
- `improve_optimization_agent.user.prompt.md`
- `improve_supervisor_agent.user.prompt.md`

**Decision:** Use if they provide value beyond your standard optimization workflow. Skip if redundant.

---

## Success Criteria

This optimization succeeds when these **system-specific outcomes** are achieved:

✅ **Complete System Coverage**
- All 7 agents optimized (supervisor + 6 specialized agents)
- All 30+ user prompts reviewed and improved
- Knowledge base schemas validated (3 JSON files)
- Documentation updated (guides, templates, README)

✅ **Measurable System Improvements**
- Overall system quality: 10%+ improvement across assessment dimensions
- User time to first result: ≤15 minutes maintained or improved
- Prompt engineering consistency: Common patterns across all agents
- End-to-end workflows: Requirements → Architecture → Engineering → Deployment validated
- Terminology clarity: Consistent "optimize" vs "improve" vs "enhance" usage

✅ **No Regressions**
- All existing capabilities preserved
- Multi-agent coordination functional
- Knowledge base integration working
- All cross-references valid
- Examples remain functional

✅ **Recursion Safety**
- OPTIMIZATION_ITERATION_COUNT = 1 (single execution)
- No infinite loops triggered
- All changes version controlled (git)

---

## Optimization Report Requirements

Generate your standard optimization report (as defined in your system prompt), ensuring it includes these **system-specific elements**:

### System-Specific Validation Tests

Test these critical workflows:
- **Complete Lifecycle**: Requirements Agent → Architecture Agent → Engineering Agent → Deployment Agent
- **Multi-shot Architecture Workflow**: Orchestration of 6 user prompts (tech stack → diagram → team → LOE → cost → plan)
- **Knowledge Base Operations**: Write user_requirements.json → Read → Write design_decisions.json
- **Supervisor Routing**: Correct agent selection based on user request types
- **Cross-references**: All agent ↔ knowledge base references valid
- **Terminology Consistency**: Verify correct usage of "optimize" vs "improve" vs "enhance" across all files

### System-Specific Metrics to Track

| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Prompt Engineering Quality | X/10 | Y/10 | +N |
| Multi-Agent Coordination | X/10 | Y/10 | +N |
| Knowledge Management | X/10 | Y/10 | +N |
| User Experience | X/10 | Y/10 | +N |
| Documentation Quality | X/10 | Y/10 | +N |
| AWS Well-Architected Enforcement | X/10 | Y/10 | +N |
| Terminology Clarity | X/10 | Y/10 | +N |

### Files Modified by Category
- Agent prompts (ai_agents/*.system.prompt.md): [COUNT]
- User prompts (user_prompts/*/*.user.prompt.md): [COUNT]
- Knowledge base (knowledge_base/*.json): [COUNT]
- Documentation (guides/, docs/, templates/): [COUNT]
- Root files (README.md, etc.): [COUNT]

### Recursion Status
- ✅ OPTIMIZATION_ITERATION_COUNT: 1/1 (complete)
- ✅ No infinite loops detected
- ✅ Next cycle: Requires new session

---

## Usage Instructions

**Execution Triggers:**
- Quarterly system reviews
- After significant AI research updates (new Anthropic/OpenAI guidance)
- Following 5+ user projects (incorporate learnings)
- When user feedback indicates systemic issues
- After major feature additions or structural changes

**Execution Steps:**
1. Start **fresh session** (ensures OPTIMIZATION_ITERATION_COUNT = 0)
2. Load Optimization Agent with `optimization_agent.system.prompt.md`
3. Reference this prompt: `@improve_ai_engineering_assistant.user.prompt.md`
4. Monitor execution and review optimization report
5. Next cycle: 3-6 months or as triggered by conditions above

---

## Notes

**Meta-Optimization Context:** You're optimizing the system you're part of—handle with extra validation rigor.

**Recursion Safety (Critical):** The iteration tracking mechanism (OPTIMIZATION_ITERATION_COUNT = 1) is non-negotiable. This prevents infinite loops during meta-optimization.

**Validation Emphasis:** Test all critical workflows end-to-end before completion, including supervisor routing and multi-agent coordination.

**Terminology Note:** This repository uses precise terminology (see README.md glossary):
- **Optimize**: System-level improvements (Optimization Agent's role)
- **Improve**: Agent-level enhancements (this prompt's purpose) and prompt-level refinements
- **Enhance**: User experience and documentation improvements

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Maintained By:** AI Engineering Assistant Core Team  
**Optimization Cycle:** Quarterly or as-needed  
**Safety Mechanism:** Iteration tracking prevents infinite loops (MAX_ITERATIONS = 1)
