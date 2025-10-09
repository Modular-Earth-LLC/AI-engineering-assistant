# Improve Requirements Agent - Targeted Optimization

**Purpose:** Optimize the Requirements Agent for better discovery workflows, question quality, and requirement elicitation effectiveness.

**Target Agent:** `ai_agents/requirements_agent.system.prompt.md`  
**Focus Areas:** Discovery facilitation, workshop execution, requirement extraction, pain point classification  
**Approach:** Domain-specific best practices + validation  
**Output:** Enhanced requirements agent + validation report

---

## Agent Context

The Requirements Agent is the **first touchpoint** in the AI Architecture Assistant workflow. It:

- Conducts discovery sessions (15-min quick, 30-min standard, 90-min comprehensive)
- Extracts requirements from unstructured notes
- Classifies pain points by AI suitability (HIGH/MEDIUM/LOW)
- Writes structured requirements to `knowledge_base/user_requirements.json`
- Enables Architecture Agent to make evidence-based design decisions

**Critical Success Factor:** Quality of requirements directly impacts downstream architecture and implementation quality.

---

## Improvement Focus Areas

### 1. Question Quality & Sequencing

**Current State Assessment:**
- Review discovery workflows for question effectiveness
- Evaluate logical flow and cognitive load
- Assess information gathering completeness

**Best Practices to Apply:**
- **Anthropic Prompt Patterns:** Use examples of excellent discovery questions
- **Cognitive Load Management:** Structure questions from easy → complex
- **Follow-up Triggers:** When to ask probing questions
- **Silence Handling:** Guide for when stakeholders are stuck

**Target Improvements:**
- Questions uncover hidden requirements
- Natural conversational flow
- Balanced breadth vs depth
- Stakeholder engagement maintained

---

### 2. Pain Point Classification Accuracy

**Current State Assessment:**
- Review AI suitability classification logic (HIGH/MEDIUM/LOW)
- Evaluate accuracy of classifications
- Check for edge cases and ambiguous scenarios

**Best Practices to Apply:**
- **Pattern Matching:** Clear criteria for each classification level
- **Examples Library:** Representative cases for each category
- **Edge Case Handling:** Guidance for ambiguous situations
- **Justification Quality:** Explanations for classifications

**Target Improvements:**
- Consistent classification across similar problems
- Clear rationale provided to users
- Reduced false positives (HIGH when actually MEDIUM)
- Better edge case handling

---

### 3. Workshop Facilitation Techniques

**Current State Assessment:**
- Review comprehensive workshop structure (90-min)
- Evaluate stakeholder alignment approaches
- Assess time management and pacing

**Best Practices to Apply:**
- **Facilitation Patterns:** Proven workshop techniques
- **Stakeholder Management:** Handling competing priorities
- **Time Boxing:** Effective pacing strategies
- **Conflict Resolution:** When stakeholders disagree

**Target Improvements:**
- Stakeholder alignment achieved
- All voices heard
- Productive use of time
- Actionable outcomes

---

### 4. Requirements Structure & Completeness

**Current State Assessment:**
- Review output format (user_requirements.json schema)
- Evaluate completeness of captured information
- Check for missing critical fields

**Best Practices to Apply:**
- **Schema Optimization:** Ensure all necessary fields present
- **Validation Rules:** Completeness checks before handoff
- **Missing Information Flags:** Clear "[TO BE DETERMINED]" usage
- **Handoff Quality:** Architecture Agent has what it needs

**Target Improvements:**
- No critical information gaps
- Structured format easy for Architecture Agent to parse
- Clear indication of unknowns
- Measurable requirements quality

---

### 5. Extraction from Unstructured Notes

**Current State Assessment:**
- Review extraction workflow effectiveness
- Evaluate accuracy of information parsing
- Check handling of ambiguous or conflicting notes

**Best Practices to Apply:**
- **NLP Patterns:** Identify key information types
- **Ambiguity Resolution:** How to handle unclear notes
- **Conflict Detection:** Flag contradictory information
- **Follow-up Recommendations:** What questions to ask

**Target Improvements:**
- Higher extraction accuracy
- Better handling of messy notes
- Clear flagging of ambiguities
- Actionable follow-up questions

---

## Improvement Workflow

### Step 1: Analyze Current Agent (20-30 minutes)

```
<thinking>
Analyzing Requirements Agent...

1. Read ai_agents/requirements_agent.system.prompt.md in full
2. Review all user prompts in user_prompts/requirements/
3. Analyze example outputs (if available)
4. Identify gaps against best practices

Key questions:
- Are discovery questions comprehensive and well-sequenced?
- Is pain point classification logic clear and accurate?
- Are workshop facilitation techniques effective?
- Is requirements structure complete?
- Does extraction workflow handle edge cases?
</thinking>

✅ **Analysis Complete**

**Strengths:**
- [What's working well]

**Improvement Opportunities:**
- [Specific gaps identified]
- [Anti-patterns found]
- [Missing capabilities]

**Priority Improvements:** [Ranked list]
```

---

### Step 2: Apply Domain-Specific Best Practices (30-45 minutes)

**Research Current Best Practices:**

**A. Discovery Methodologies:**
- Jobs-to-be-Done framework
- Design thinking discovery patterns
- Lean startup customer development
- User story mapping techniques

**B. Requirements Engineering:**
- IEEE 29148 standards (adapted for AI)
- Agile requirements practices
- Business analysis frameworks (BABOK)
- AI-specific requirement patterns

**C. Workshop Facilitation:**
- Liberating Structures techniques
- Agile retrospective patterns
- Design sprint methodologies
- Virtual facilitation best practices

**D. Pain Point Analysis:**
- Problem-solution fit frameworks
- Impact/effort prioritization
- AI suitability assessment frameworks
- ROI estimation patterns

**Apply Improvements:**
- Enhance question libraries
- Refine classification criteria
- Improve workshop structures
- Optimize requirements schemas
- Strengthen extraction logic

---

### Step 3: Validate Improvements (30 minutes)

**Test Scenarios:**

**Scenario 1: Simple Discovery (Quick 15-min)**
```
Context: Solo entrepreneur wants to automate customer support
Task: Execute quick discovery
Success Criteria:
- ✅ 10 questions complete in 15 minutes
- ✅ Pain points classified correctly
- ✅ Requirements ready for architecture
- ✅ User feels understood
```

**Scenario 2: Complex Multi-Stakeholder Workshop**
```
Context: Enterprise with competing priorities across 4 departments
Task: Execute 90-min comprehensive workshop
Success Criteria:
- ✅ All stakeholders aligned
- ✅ Priorities clarified
- ✅ Requirements complete and unambiguous
- ✅ Political conflicts navigated successfully
```

**Scenario 3: Messy Notes Extraction**
```
Context: Scattered meeting notes with contradictions
Task: Extract structured requirements
Success Criteria:
- ✅ Key requirements identified
- ✅ Contradictions flagged
- ✅ Follow-up questions generated
- ✅ Stakeholder validation needed items listed
```

**Validation Metrics:**
- Discovery workflow completion time
- Requirements completeness score (% of fields filled)
- Classification accuracy (manual review)
- User satisfaction (simulated feedback)

---

### Step 4: Generate Improvement Report (15 minutes)

```markdown
# Requirements Agent - Improvement Report

**Date:** [ISO 8601]
**Changes Implemented:** [COUNT]

---

## Improvements by Category

### Question Quality & Sequencing
**Changes:** [COUNT]
- [Improvement 1]
- [Improvement 2]

**Impact:** [Measurable outcome]

---

### Pain Point Classification
**Changes:** [COUNT]
- [Improvement 1]
- [Improvement 2]

**Impact:** [Measurable outcome]

---

### Workshop Facilitation
**Changes:** [COUNT]
- [Improvement 1]
- [Improvement 2]

**Impact:** [Measurable outcome]

---

### Requirements Structure
**Changes:** [COUNT]
- [Improvement 1]
- [Improvement 2]

**Impact:** [Measurable outcome]

---

### Note Extraction
**Changes:** [COUNT]
- [Improvement 1]
- [Improvement 2]

**Impact:** [Measurable outcome]

---

## Validation Results

| Test Scenario | Before | After | Improvement |
|---------------|--------|-------|-------------|
| Simple Discovery | [Score] | [Score] | +[X]% |
| Complex Workshop | [Score] | [Score] | +[X]% |
| Notes Extraction | [Score] | [Score] | +[X]% |

**Overall Quality:** [Before X/10] → [After Y/10]

---

## Files Modified

- `ai_agents/requirements_agent.system.prompt.md`: [Changes]
- `user_prompts/requirements/[file].user.prompt.md`: [Changes]

---

## Backward Compatibility

✅ All existing workflows preserved
✅ Knowledge base schema unchanged (or documented if changed)
✅ No breaking changes to Architecture Agent handoff

---

## Recommended Next Steps

- [Action 1]
- [Action 2]

---

**Status:** COMPLETE ✅
```

---

## Success Criteria

✅ **Discovery Effectiveness**
- Questions uncover hidden requirements
- Stakeholders feel understood
- Complete information gathered in appropriate timeframes

✅ **Classification Accuracy**
- Pain points correctly classified (>90% accuracy)
- Clear rationale provided
- Edge cases handled appropriately

✅ **Workshop Quality**
- Stakeholder alignment achieved
- Competing priorities resolved
- Actionable requirements produced

✅ **Requirements Completeness**
- All critical fields populated
- Missing information clearly flagged
- Architecture Agent has sufficient information

✅ **Extraction Accuracy**
- Key information correctly identified
- Ambiguities and conflicts flagged
- Follow-up questions actionable

---

## Safety Guardrails

**MUST Preserve:**
- All existing user prompts must continue to work
- Knowledge base schema compatibility (unless explicitly updated)
- Handoff format to Architecture Agent
- Discovery workflow entry points

**MUST NOT:**
- Change JSON schema without updating all dependent agents
- Remove existing capabilities
- Break backward compatibility
- Introduce ambiguity where clarity existed

**Validation Required:**
- Test all discovery workflows after changes
- Verify Architecture Agent can read outputs
- Confirm no regression in user experience

---

## Execution Context

This prompt is **context-agnostic** and can be executed in multiple ways:

### Usage Pattern 1: Orchestrated Improvement
- Called automatically by system-wide optimization workflow
- Part of comprehensive framework improvement cycle
- Results integrated into overall optimization report

### Usage Pattern 2: Standalone Improvement
- Executed directly by user for targeted optimization
- Focuses solely on Requirements Agent improvements
- Generates independent improvement report

**Both patterns produce equivalent results.** The prompt adapts to its execution context automatically.

---

## Usage Instructions

**When to run:**
- Quarterly optimization cycles
- After gathering user feedback on discovery quality
- When new discovery methodologies emerge
- Before major framework updates

**How to execute:**

1. Ensure you have access to the target agent file: `ai_agents/requirements_agent.system.prompt.md`
2. Send/execute this improvement prompt
3. Review improvements and validation results
4. Test with representative scenarios
5. Deploy changes if validation passes

**Platform Support:**
- ✅ Cursor (Claude Sonnet 4.5+)
- ✅ GitHub Copilot (GPT-4+)
- ✅ AWS Bedrock
- ✅ Generic LLM platforms with file access

---

**Version:** 0.1  
**Last Updated:** 2025-10-04  
**Target Agent:** Requirements Agent  
**Optimization Cycle:** Quarterly or as-needed  
**Execution Mode:** Context-agnostic (orchestrated or standalone)
