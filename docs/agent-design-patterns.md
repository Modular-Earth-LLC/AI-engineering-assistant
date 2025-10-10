# AI Agent Design Patterns

**Purpose:** Reusable patterns for designing effective AI agents  
**When to use:** During agent specification and prompt engineering

---

## Quick Reference

| Pattern | Use When | Complexity |
|---------|----------|------------|
| **Specialist Agent** | Single focused task | ⭐ Simple |
| **Workflow Agent** | Multi-step process | ⭐⭐ Moderate |
| **Document Generator** | Create formatted outputs | ⭐ Simple |
| **Research & Synthesis** | Gather and summarize information | ⭐⭐ Moderate |
| **Review & Validation** | Quality control, compliance | ⭐ Simple |
| **Coordinator/Router** | Direct work to specialists | ⭐⭐⭐ Complex |
| **Chain-of-Thought** | Complex reasoning, problem-solving | ⭐⭐ Moderate |
| **Feedback Loop** | Learn from corrections | ⭐⭐⭐ Complex |
| **Adaptive Agent** | Adjust to user expertise level | ⭐⭐⭐ Complex |

**Quick tips:**
- **First-time builders:** Start with Specialist, Document Generator, or Review & Validation
- **Most common:** 80% of use cases need Specialist, Workflow, or Document Generator
- **Multi-agent systems:** Coordinator/Router orchestrates multiple Specialists

---

## Core Patterns

### Pattern 1: Specialist Agent

**Use when:** Single, well-defined task

**Structure:**
- Clear, narrow purpose
- Specific input format
- Deterministic output format
- Domain-specific knowledge

**Example:** Financial report analyzer, expense categorizer, invoice generator

**Build time:** 2-4 hours

---

### Pattern 2: Workflow Agent

**Use when:** Multi-step process with state tracking

**Structure:**
- State tracking (where in process)
- Step-by-step execution
- Validation at each step
- Clear completion criteria

**Example:** Onboarding coordinator, troubleshooting guide, application processor

**Build time:** 4-8 hours

---

### Pattern 3: Document Generator

**Use when:** Create formatted outputs (reports, proposals, emails)

**Structure:**
- Template-based generation
- Structured input data
- Consistent output format
- Quality validation

**Example:** Proposal generator, report creator, email drafter

**Build time:** 3-6 hours

---

### Pattern 4: Research & Synthesis Agent

**Use when:** Gather and summarize information from multiple sources

**Structure:**
- Research methodology (how to gather info)
- Source evaluation (credibility assessment)
- Synthesis logic (combining information)
- Output structure (organized findings)

**Example:** Market research, competitive analysis, literature review

**Build time:** 4-6 hours

---

### Pattern 5: Review & Validation Agent

**Use when:** Quality control, compliance checking, error detection

**Structure:**
- Clear validation criteria
- Checklist-based review
- Pass/fail/needs-work classification
- Specific feedback on issues

**Example:** Code reviewer, compliance checker, quality assurance

**Build time:** 3-5 hours

---

### Pattern 6: Coordinator/Router Agent

**Use when:** Direct work to specialized agents (multi-agent orchestration)

**Structure:**
- Intent detection (what does user want)
- Agent selection logic (which agent to use)
- Context handoff (share information)
- Response aggregation (combine results)

**Example:** Supervisor agent, customer service router, task dispatcher

**Build time:** 6-10 hours

---

### Pattern 7: Chain-of-Thought Agent

**Use when:** Complex reasoning, problem-solving requiring explanation

**Structure:**
- Problem decomposition (break into steps)
- Explicit reasoning (show thinking)
- Step-by-step solution
- Verification (check answer)

**Example:** Financial advisor, technical troubleshooter, strategic planner

**Build time:** 4-8 hours

---

### Pattern 8: Feedback Loop Agent

**Use when:** System needs to learn from user corrections over time

**Structure:**
- Initial attempt (first response)
- User feedback collection
- Learning mechanism (improve from feedback)
- Improved attempt (revised response)

**Example:** Writing assistant, recommendation engine, personalized tutor

**Build time:** 6-10 hours

---

### Pattern 9: Adaptive Agent

**Use when:** Users have varying expertise levels (novice to expert)

**Structure:**
- Expertise detection (assess user level)
- Adaptive explanations (adjust detail level)
- Progressive disclosure (show more as needed)
- User control (let user set preference)

**Example:** Technical documentation assistant, learning platform, help desk

**Build time:** 6-10 hours

---

## Combining Patterns

**Common Combinations:**

**Multi-Agent System (Coordinator + Specialists)**
- 1 Coordinator/Router Agent
- 3-5 Specialist Agents
- Build time: 20-40 hours
- Example: Customer service system, operations automation

**Research Pipeline (Research + Document Generator)**
- 1 Research & Synthesis Agent
- 1 Document Generator Agent
- Build time: 8-12 hours
- Example: Market analysis reports, competitive intelligence

**Quality Assurance Workflow (Workflow + Review)**
- 1 Workflow Agent (guides process)
- 1 Review & Validation Agent (checks quality)
- Build time: 8-12 hours
- Example: Content publishing, compliance workflows

---

## Pattern Selection Guide

**Ask yourself:**

1. **What's the agent's primary purpose?**
   - Single task → Specialist
   - Multi-step process → Workflow
   - Create documents → Document Generator
   - Gather info → Research & Synthesis
   - Check quality → Review & Validation
   - Route to others → Coordinator/Router
   - Complex reasoning → Chain-of-Thought
   - Learn over time → Feedback Loop
   - Adapt to user → Adaptive

2. **How complex is the task?**
   - Simple, clear rules → Specialist, Document Generator, Review
   - Moderate complexity → Workflow, Research, Chain-of-Thought
   - High complexity → Coordinator, Feedback Loop, Adaptive

3. **Do you need multiple agents?**
   - No → Choose appropriate single pattern
   - Yes → Start with Coordinator/Router pattern

---

## Best Practices

**For All Patterns:**
- ✅ Clear role definition
- ✅ Explicit input/output format
- ✅ Error handling and edge cases
- ✅ Examples in the prompt
- ✅ Validation and quality checks

**What to Avoid:**
- ❌ Trying to do too much in one agent
- ❌ Vague or ambiguous instructions
- ❌ No examples or edge case handling
- ❌ Forgetting error scenarios

---

## Implementation Steps

**1. Choose Pattern** - Based on your use case  
**2. Define Role** - What does this agent do?  
**3. Specify Input/Output** - Clear formats  
**4. Add Examples** - Show expected behavior  
**5. Handle Errors** - What if something goes wrong?  
**6. Test** - Validate with real scenarios

---

## Examples in This Repository

**Supervisor Agent** - Coordinator/Router pattern  
**Requirements Agent** - Research & Synthesis + Workflow  
**Architecture Agent** - Specialist + Document Generator  
**Engineering Agent** - Document Generator + Chain-of-Thought  
**Deployment Agent** - Workflow + Review & Validation  
**Optimization Agent** - Review & Validation + Chain-of-Thought

See `ai_agents/` for full implementations.

---

**Version:** 0.1  
**Last Updated:** 2025-10-08  
**Next:** Review agent implementations in `ai_agents/` directory
