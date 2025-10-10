# Discovery/Assessment Proposal Assembly - User Prompt

**Phase:** Post-Requirements or Early Architecture  
**Purpose:** Assemble proposal for discovery/technical assessment project (2-6 weeks)  
**Agent:** Architecture Agent  
**Inputs:** `knowledge_base/user_requirements.json`, partial `knowledge_base/design_decisions.json`  
**Output:** Discovery proposal document

---

## Purpose

Assemble a proposal for a time-boxed discovery or technical assessment project that validates feasibility before committing to full implementation.

**When to use:**
- Significant technical uncertainty exists
- Want to validate approach before full investment
- Need to assess data quality, integration complexity, or performance feasibility
- De-risk a large project through upfront research
- Prove business value before committing full budget

**Typical Projects:**
- Technical feasibility assessment (2-4 weeks)
- AI readiness evaluation (2-6 weeks)
- Integration complexity analysis (2-4 weeks)
- Technology evaluation (compare 3 options, 3-4 weeks)
- Performance validation (can we meet latency/accuracy requirements, 2-3 weeks)

**Prerequisites:**
- ✅ `knowledge_base/user_requirements.json` complete (know what problem to solve)
- ⏳ `knowledge_base/design_decisions.json` partial (preliminary architecture approach)

---

## Instructions for Architecture Agent

### Step 1: Define Discovery Objectives

```
<thinking>
From user_requirements.json:
- What problem are we solving?
- What's uncertain or risky?
- What do we need to validate before full implementation?

Critical questions this discovery should answer:
1. [Question 1 based on requirements]
2. [Question 2 based on uncertainty]
3. [Question 3 based on technical risk]
</thinking>

**Discovery Objectives Identified:**

Based on requirements, this assessment will answer:

1. **[Primary Question]**  
   - Why critical: [Impact on full project]
   - Success criteria: [What answer is acceptable]

2. **[Secondary Question]**  
   [Same structure...]

3. **[Tertiary Question]**  
   [Same structure...]
```

---

### Step 2: Read from Knowledge Base

**Load:**
- `knowledge_base/user_requirements.json` (problem, business case)
- `knowledge_base/system_config.json` (constraints, budget)
- `knowledge_base/design_decisions.json` (if preliminary architecture exists)

---

### Step 3: Assemble Discovery Proposal

```markdown
# Discovery & Technical Assessment Proposal - [Project Name]

**Assessment Type:** [Technical Feasibility / AI Readiness / Integration Assessment / etc.]  
**Duration:** [2-6 weeks]  
**Prepared for:** [Decision Makers]  
**Date:** [Current date]

---

## Executive Summary

**Problem/Opportunity:**  
[From user_requirements.json: business.problem]

**Why Discovery is Needed:**  
[What critical uncertainties make it risky to proceed without assessment]

**Discovery Objectives:**
1. [Primary question to answer]
2. [Secondary question to answer]
3. [Tertiary question to answer]

**Resource Request:**
- **Duration:** [X weeks]
- **Team:** [Y people at Z% allocation]
- **Budget:** $[Amount] (primarily internal time + minimal cloud/tool costs)

**Expected Outcome:**  
Go/no-go decision + technical approach recommendation + effort estimate for full project (if GO)

**Risk Mitigation:**  
$[Discovery cost] investment now prevents potential $[Full project cost] investment in wrong approach.

---

## Problem Statement

**Business Context:**  
[From user_requirements.json: customer and business context]

**Current State:**  
[From user_requirements.json: business.current_state]

**Why This Matters:**  
[From user_requirements.json: business.business_value]

**Unknowns & Risks:**  
[What we don't know that makes full implementation risky without assessment]

**From user_requirements.json and design_decisions.json:**
- Technical feasibility concerns: [List]
- Data quality/availability questions: [List]
- Integration complexity uncertainties: [List]
- Performance requirement validation needs: [List]
- Cost or timeline unknowns: [List]

---

## Discovery Objectives (Questions to Answer)

**Primary Questions:**

1. **[Question 1]**  
   - Why this matters: [Business or technical importance]
   - Success criteria: [What answer would be acceptable to proceed]
   - How we'll answer: [Specific activities]

2. **[Question 2]**  
   [Same structure...]

3. **[Question 3]**  
   [Same structure...]

**Decision Criteria:**  
[What findings lead to GO vs. NO-GO vs. PIVOT]

---

## Assessment Approach

### Methodology

**Phase 1: Research & Planning (Days 1-3)**
- Review existing systems and data
- Identify similar implementations
- Define evaluation criteria
- Plan experiments and tests

**Phase 2: Technical Investigation (Days 4-15)**
- Data quality analysis
- Proof-of-concept development
- Performance testing
- Integration complexity assessment
- Technology evaluation

**Phase 3: Analysis & Recommendation (Days 16-[END])**
- Consolidate findings
- Develop recommendations
- Estimate effort for full implementation if GO
- Document risks and mitigation strategies

---

### Deliverables

**1. Assessment Report**
   - Executive summary of findings
   - Answers to each primary question
   - Data analysis results
   - Technical feasibility assessment
   - Risk analysis

**2. Technical Recommendation**
   - Recommended approach (if GO)
   - Technology stack recommendation
   - Architecture sketch
   - Integration strategy

**3. Implementation Plan** (if GO recommendation)
   - High-level project plan
   - Effort and timeline estimate
   - Resource requirements
   - Cost projection
   - Risk mitigation strategies

**4. Proof-of-Concept** (if applicable)
   - Working code demonstrating feasibility
   - Performance benchmark results
   - Not production-ready, but shows viability

---

## Team & Timeline

**Team Composition:**

| Role | Allocation | Responsibilities |
|------|------------|------------------|
| Tech Lead | [%] | Overall direction, recommendations |
| [Engineer/Specialist] | [%] | [Specific focus area] |
| [Engineer/Specialist] | [%] | [Specific focus area] |

**Total Capacity:** [X hours/week] for [Y weeks] = [Z total hours]

**Timeline:**

| Week | Activities | Milestone |
|------|------------|-----------|
| Week 1 | Research & planning | Assessment plan finalized |
| Week 2-3 | Technical investigation | Key findings identified |
| Week 4 | Analysis & recommendation | Final report & presentation |

**Key Dates:**
- Kickoff: [Date]
- Mid-point check-in: [Date]
- Final presentation: [Date]
- Decision: [Date]

---

## Budget

**Internal Time:**
- Engineering hours: [X hours] × $[Rate] = $[Amount]

**External Costs:**
- Cloud infrastructure (testing): $[Amount]
- Third-party tools/APIs: $[Amount]
- **Total:** $[Amount]

**Note:** Primarily internal time investment. External costs minimal for assessment phase.

---

## Success Criteria

**This assessment is successful if:**

✅ All primary questions answered with sufficient confidence  
✅ Clear go/no-go recommendation with supporting evidence  
✅ If "GO": Detailed implementation plan with effort estimate  
✅ If "NO-GO": Clear rationale with alternative paths explored  
✅ Risk mitigation strategies for identified challenges  
✅ Executive team can make informed decision

---

## Decision Scenarios

**Scenario 1: Clear "GO"**
- Findings: Technical feasibility confirmed, data sufficient, approach clear
- Recommendation: Proceed to full implementation
- Next steps: [Implementation proposal, then prototype development]

**Scenario 2: "GO with Modifications"**
- Findings: Feasible but requires adjustments to scope or approach
- Recommendation: Proceed with modified plan
- Next steps: [Adjusted implementation proposal]

**Scenario 3: "PAUSE"**
- Findings: Additional work needed before decision
- Recommendation: Address gaps then re-assess
- Next steps: [What needs to happen]

**Scenario 4: "NO-GO"**
- Findings: Not technically feasible or ROI insufficient
- Recommendation: Do not proceed with original plan
- Alternatives: [Other approaches to consider]

---

## Approval & Next Steps

**Decision Makers:**  
[From system_config.json: stakeholders.decision_makers]

**Approval Process:**
1. Review this proposal
2. Approve discovery budget
3. Kickoff meeting
4. Weekly status updates
5. Final presentation with recommendation
6. Decision on full implementation

**If Approved:**  
Discovery begins [Start Date]  
Results presented [End Date]  
Implementation decision by [Decision Date]

---

**Proposal Assembled:** [Timestamp]  
**Based on:** knowledge_base/user_requirements.json, design_decisions.json (preliminary)  
**Recommendation:** [Proceed with discovery to de-risk full implementation]
```

---

## Success Criteria

Discovery proposal is successful when:

✅ **Reads from knowledge base** (leverages existing requirements)  
✅ **Clear objectives** (specific questions to answer)  
✅ **Appropriate scope** (2-6 weeks, limited budget)  
✅ **Decision framework** (how findings lead to GO/NO-GO)  
✅ **Risk mitigation** (shows how discovery reduces larger investment risk)  
✅ **Executive-friendly** (clear recommendation and timeline)

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Purpose:** Assembly-only discovery proposal from knowledge base  
**Typical Duration:** 2-6 weeks  
**Investment Range:** $5K-$25K
