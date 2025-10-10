# Standard Discovery - User Prompt (30-45 Minutes)

**Phase:** Requirements Discovery  
**Duration:** 30-45 minutes  
**Best for:** Most AI projects, small to medium teams, well-defined business context  
**Agent:** Requirements Agent  
**Output:** `knowledge_base/user_requirements.json`

---

## Purpose

Conduct focused discovery session for standard AI projects. More thorough than Quick Discovery, less intensive than Comprehensive Workshop.

**Best for:**
- Small to medium teams (5-20 people)
- Well-defined business problems
- Moderate complexity
- Standard timelines (6-12 weeks)
- Need stakeholder buy-in

**Use Quick Discovery instead if:** Simple problem, solo-entrepreneur, need speed  
**Use Comprehensive Workshop instead if:** Enterprise, multi-stakeholder, complex integrations

---

## Session Structure (4 Sections)

### Section 1: Business Context (10 minutes)

**Opening:**
*"Thanks for your time. Over the next 30-45 minutes, I want to understand your operations and identify where AI could genuinely help. This is exploratory—I need your honest reality, not an idealized version. Let's start with context."*

**Questions:**
1. "What are your core processes or workflows?"
2. "Who are your users/customers, and what do typical workflows look like?"
3. "What tools and systems do you use daily?"
4. "Walk me through your role—what do you handle vs. delegate?"

**Capture:**
- Operating model and key processes
- User/customer personas
- Current tool stack
- Technical sophistication level
- Delegation patterns

---

### Section 2: Pain Point Identification (10-15 minutes)

**Questions:**
1. "What tasks take the most time but feel repetitive?"
2. "Where do you feel bottlenecked in your work?"
3. "What tasks would you delegate if you had a perfect assistant?"
4. "What deliverables take longer than you'd like?"
5. "For your top pain point, walk me through the last time you did it—step by step."

**Listen for HIGH Priority signals:**
- "This is tedious but necessary"
- "I do this for every client/customer"
- "Takes 5+ hours per week"
- "Follows a formula or template"
- "I wish I could delegate this"

**For each pain point, capture:**
- Exact description (use their words)
- Frequency (daily/weekly/monthly)
- Time per instance
- Current workarounds
- Impact on business (time, quality, capacity)

**Real-time classification:**
```
<thinking>
For each pain point:
1. Digital/computer-based? → [Yes = higher priority]
2. Repetitive? → [Yes = higher priority]
3. Rule-based or templated? → [Yes = higher priority]
4. Time consumption: [>5 hrs/week = HIGH, 2-5 hrs = MEDIUM, <2 hrs = LOW]
5. Cost of error: [High = needs validation strategy]

Classification: [HIGH/MEDIUM/LOW]
Recommended pattern: [Agent type]
</thinking>

🔴 PAIN POINT IDENTIFIED: [Description]
Classification: HIGH - [Reason]
Suggested follow-up: "[Targeted question]"
Potential solution: [Agent pattern]
```

---

### Section 3: Workflow Deep-Dive (10 minutes)

**For top 1-2 pain points, map complete workflow:**

**Questions:**
1. "Walk me through [PROCESS] from start to finish—every step"
2. "What digital work is involved at each step?"
3. "Which parts require expert judgment? Which are more routine?"
4. "What tools do you use? Do you have templates?"
5. "Where does this slow down or get bottlenecked?"

**Create workflow diagram:**
```
Step 1: [Action] → Takes [X min] → Uses [Tool] → Requires [Judgment/Routine]
Step 2: [Action] → Takes [Y min] → Uses [Tool] → Requires [Judgment/Routine]
Step 3: [Action] → Takes [Z min] → Uses [Tool] → Requires [Judgment/Routine]

Total time: [Sum] 
AI automation potential: [Steps that are routine/rule-based]
Human expertise still needed: [Steps requiring judgment]
```

**Capture:**
- Complete step-by-step workflow
- Time per step
- Tools used
- Decision points (judgment vs. routine)
- Bottlenecks and delays
- Input requirements and output deliverables

---

### Section 4: Technical Context & Success Criteria (10 minutes)

**Technology Stack:**
1. "What tools do you use for this work?"
2. "How do these tools connect? Where do you manually transfer data?"
3. "Do any tools have APIs or export capabilities?"
4. "How comfortable are you with new technology? (1-10)"

**Success & Timeline:**
1. "What does success look like 6 months from now?"
2. "How will you measure whether this is working?"
3. "When do you need this operational? What's driving that timeline?"
4. "What budget range are you thinking? (Order of magnitude)"

**Capture:**
- Complete tool inventory with integration points
- Manual data transfer points (automation opportunities)
- Technology comfort level (influences UX design)
- Success metrics (quantifiable KPIs)
- Timeline constraints and business drivers
- Budget parameters

---

## Requirements Structuring

**After session, structure into user_requirements.json:**

**Analysis:**
```
<thinking>
1. Problem type: [Classification]
2. AI suitability: [HIGH/MEDIUM/LOW] for each pain point
3. Recommended architecture: [Single agent / Multi-agent with X agents]
4. Integration complexity: [LOW/MEDIUM/HIGH]
5. Timeline estimate: [Weeks]
6. Budget estimate: $[Development] + $[Monthly operations]
7. Completeness: [COMPLETE/PARTIAL] - [Missing items if partial]
</thinking>
```

**Populate JSON schema:**
```json
{
  "customer": {
    "legal_name": "[From answers]",
    "industry": "[From answers]",
    "business_model": "[From context questions]",
    "ai_adoption_stage": "[beginner/intermediate based on sophistication]"
  },
  "use_case": {
    "title": "[Descriptive title]",
    "summary": "[1-2 sentence description]",
    "target_users": ["[From Q about who uses system]"],
    "workflow_steps": ["[From workflow deep-dive]"]
  },
  "business": {
    "problem": "[From pain point questions]",
    "current_state": {
      "how_handled_today": "[From workflow mapping]",
      "pain_points": ["[Each identified pain point]"],
      "time_spent": "[From frequency questions]"
    },
    "business_value": {
      "efficiency_gains": "[Time saved]",
      "cost_savings": "[Calculated from time × rate]"
    },
    "success_metrics": {
      "kpis": ["[From success criteria questions]"]
    }
  },
  "technical": {
    "functional_requirements": [
      {"title": "[Feature 1]", "priority": "must_have", "complexity": "[low/medium/high]"}
    ],
    "integration_requirements": {
      "api_integrations": ["[From tools discussion]"]
    }
  },
  "project_scope": {
    "timeline_estimate_weeks": "[From timeline question]",
    "level_of_effort_estimate": "[Quick estimate]"
  },
  "_metadata": {
    "discovery_method": "standard_discovery",
    "discovery_duration_minutes": "[30-45]",
    "completeness_score": "[complete/partial]"
  }
}
```

---

## Post-Session Deliverable

**Generate and share with user:**

```markdown
# Discovery Session Summary

**Date:** [Session date]  
**Duration:** [Actual minutes]  
**Stakeholders:** [Names]

## Context

[2-3 sentence description of their business/operations]

## Pain Points Identified

### 🔴 HIGH Priority (AI-Suitable)

1. **[Pain Point 1]**
   - Description: [Details]
   - Frequency: [How often]
   - Time impact: [Hours per week/month]
   - Current approach: [How handled today]
   - Proposed AI solution: [Agent type]
   - Estimated savings: [Hours/week]

2. **[Pain Point 2]**
   [Same structure...]

### 🟡 MEDIUM Priority

[Same structure if applicable...]

### 🟢 LOW Priority (Keep Human-Led)

[Same structure if applicable...]

## Technology Stack

**Current Tools:**
- [Tool 1]: [Purpose] - API Available: [Yes/No/Unknown]
- [Tool 2]: [Purpose] - API Available: [Yes/No/Unknown]

**Integration Opportunities:**
- [Where manual data transfer happens]
- [Where tools don't connect]

## Recommended AI Agents

1. **[Agent Type 1]** for [Specific Task]
   - Addresses: [Pain point]
   - Pattern: [From docs/agent_design_patterns.md]
   - Estimated savings: [Hours/week]
   - Implementation complexity: [LOW/MEDIUM/HIGH]

2. **[Agent Type 2]** for [Specific Task]
   [Same structure...]

## Success Criteria

**User-Defined Metrics:**
- [KPI 1]: [Target]
- [KPI 2]: [Target]
- [KPI 3]: [Target]

## Next Steps

✅ **Requirements complete** - Ready for architecture design

**Recommended:**
1. Review this summary for accuracy
2. Proceed to Architecture Agent for system design
3. Architecture phase: 2-3 hours → Complete technical plan
4. Prototype development: 4-8 weeks → Working system

**Timeline:**
- Architecture design: This week
- Prototype review: [Date 6-8 weeks out]

---

**Knowledge Base:**
✅ Requirements saved to `knowledge_base/user_requirements.json`

**Ready to proceed to architecture design?**
```

---

## Success Criteria

Standard Discovery is successful when:

✅ **Complete in 30-45 minutes**  
✅ **3+ pain points identified and classified**  
✅ **1-2 workflows mapped in detail** (step-by-step)  
✅ **Technology stack captured** (tools + integration points)  
✅ **Success metrics defined** (measurable KPIs)  
✅ **Requirements written** to user_requirements.json  
✅ **User validates** top priorities  
✅ **Next step determined** (usually: proceed to architecture)

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Estimated Duration:** 30-45 minutes  
**Completeness:** Ready for architecture design
