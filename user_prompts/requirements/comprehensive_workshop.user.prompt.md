# Comprehensive Workshop - User Prompt (90 Minutes)

**Phase:** Requirements Discovery  
**Duration:** 90 minutes  
**Best for:** Complex multi-stakeholder AI systems, enterprise, high-stakes projects  
**Agent:** Requirements Agent  
**Output:** `knowledge_base/user_requirements.json`

---

## Purpose

Conduct deep-dive requirements workshop for complex AI projects with multiple stakeholders, intricate workflows, or enterprise requirements.

**Best for:**
- Large organizations (20+ people)
- Multi-agent systems with complex coordination
- Multiple stakeholder groups
- High-stakes projects (>$100K investment)
- Competing priorities need alignment
- Compliance or regulatory requirements

**Use Standard Discovery instead if:** Single stakeholder, straightforward workflows, <$75K budget  
**Use Quick Discovery instead if:** Solo-entrepreneur, simple problem, need speed

---

## Pre-Workshop Preparation (30-60 minutes before session)

### Tasks for Requirements Agent:

1. **Review available context:**
   - Any prior discovery notes or documentation
   - Industry/domain research
   - Stakeholder backgrounds (if known)

2. **Prepare customized questions:**
   - Tailor questions to their industry
   - Prepare 3-5 relevant AI examples from their domain

3. **Set up tools:**
   - Screen sharing for collaborative notes
   - Diagramming capability (for workflow mapping)
   - Recording software (with stakeholder permission)

---

## Workshop Structure (6 Sections)

### Opening (5 minutes)

**Set expectations:**

*"[STAKEHOLDER NAMES], thanks for this time. Over the next 90 minutes, we'll map your operations in detail. This will feel thorough—that's intentional. The more I understand how you work, the better I can design AI agents that fit your process rather than fighting it.*

*I'll ask specific questions and take detailed notes. There are no wrong answers—I need your operational reality, not an idealized version.*

*We'll cover six areas: (1) market positioning, (2) brand voice, (3) go-to-market, (4) core workflows, (5) business objectives, and (6) technology stack. The bulk of our time will be on workflows because that's where AI has the most impact."*

---

### Section 1: Industry & Market Positioning (15 minutes)

**Questions:**
1. "What industry are you in, and what industries do you serve?"
2. "How do you describe your work to others?"
3. "What makes your approach different from competitors?"
4. "Who are your primary users/customers?"
5. "What problems do you typically solve for them?"

**Capture:**
- Primary industry vertical
- Target customer/user profile
- Unique value proposition
- Competitive differentiation
- Common customer pain points

**Why it matters:** Understanding market context helps design agents that use appropriate terminology and address real market problems.

---

### Section 2: Brand Voice & Communication Style (15 minutes)

**Questions:**
1. "How would you describe your mission and core values?"
2. "How do you communicate with users/customers? What tone?"
3. "Does your communication style change by audience? (executives vs. technical vs. end-users)"
4. "Are there specific phrases you use or avoid?"
5. "Can you share examples of your typical communication?" (emails, proposals, marketing)

**Capture:**
- Mission statement (exact wording)
- Core values
- Communication style by audience
- Tone preferences (formal/casual/technical/accessible)
- Specific terminology to use or avoid
- Brand voice examples (request they share samples)

**Why it matters:** **This determines how AI agents communicate.** If you build a formal agent for a casual brand, it will feel wrong. Capture exact language patterns.

**Action:** Request stakeholder share example emails, proposals, or marketing materials for reference.

---

### Section 3: Go-to-Market Strategy (15 minutes)

**Questions:**
1. "How do you currently acquire new customers/users?"
2. "Walk through your process from initial engagement to commitment."
3. "How are services scoped or priced?"
4. "What's your biggest growth opportunity?"
5. "What prevents you from scaling faster?"

**Capture:**
- Customer acquisition channels
- Sales/engagement process stages and duration
- Pricing model
- Growth constraints
- Scaling bottlenecks

**AI Opportunities to listen for:**
- Lead qualification processes → Coordinator/Router agent
- Proposal generation workflows → Document Generator agent
- Customer onboarding steps → Workflow Agent
- Sales collateral creation → Document Generator agent
- Follow-up communication → Specialist Agent

---

### Section 4: Core Service Delivery Workflows (25 minutes) ⭐ MOST CRITICAL

**Process for each major service/workflow:**

For stakeholder's top 2-3 services, ask:

1. **Service overview:** "Describe [PROCESS] from the user's perspective. What are they getting?"

2. **Workflow walkthrough:** "Walk me through this step-by-step, from start to completion."

3. **Digital work:** "For each step, what digital work is involved? What gets created on a computer?"

4. **Judgment vs. routine:** "Which parts require your expert judgment? Which are rule-based?"

5. **Bottlenecks:** "Where does this slow down? What takes longer than you'd like?"

6. **Delegation candidates:** "If you had a perfect assistant who followed instructions exactly, what could you delegate?"

7. **Tools & templates:** "What tools do you use? Do you have templates or frameworks?"

**Example Deep Dive: Financial Modeling Service**

Q: "Walk me through creating one financial model from scratch."
- "What specific models do you create most often?"
- "What data sources do you pull from?"
- "What parts are formulaic? What requires your judgment?"
- "How long does a typical model take?"
- "Do you use a template or start fresh?"
- "What software do you use?"
- "What would I see you doing in the first hour of building a model?"

**For each service, capture:**
- Complete workflow diagram (step-by-step with time estimates)
- Input requirements (data, documents, information needed)
- Output deliverables (reports, models, presentations, etc.)
- Time requirements (per step and total)
- Decision points requiring expertise
- Routine or repetitive tasks (automation candidates)
- Bottlenecks and delays
- Tools used with specific features
- Templates or frameworks
- Quality control processes

**Time allocation:**
- 1 service: Full 25 minutes deep dive
- 2 services: 12-13 minutes each
- 3+ services: Focus on top 2, brief overview of others

---

### Section 5: Business Objectives & Concerns (10 minutes)

**Questions:**
1. "What are your objectives for the next quarter or year?"
2. "What are your biggest operational challenges right now?"
3. "Where do you imagine AI could help most?"
4. "What would success look like six months from now?"
5. "What concerns do you have about implementing AI?"

**Capture:**
- Quarterly/annual objectives with metrics
- Current operational challenges
- Stakeholder's AI opportunity ideas
- Success vision and metrics
- Concerns or hesitations about AI

**Handle concerns proactively:**
- "Data security" → Address in technical architecture
- "Losing personal touch" → Position as augmentation, not replacement
- "Cost" → Show ROI calculation
- "Complexity" → Emphasize gradual implementation
- "Reliability" → Discuss human oversight and quality control

---

### Section 6: Technology Stack & Integration Points (10 minutes)

**Questions:**
1. "What tools do you use for customer/user-facing work?"
2. "What tools do you use for internal operations?"
3. "Where do you manually transfer data between tools?"
4. "Where do your current tools frustrate you?"
5. "How would you rate your team's technical capabilities? (1-10)"

**Capture:**
- Complete tool inventory:
  - Tool name and version
  - Primary use case
  - Frequency of use
  - Integration points (or gaps)
  - API availability (note: research later if unknown)
  - Data export/import capabilities
- Manual data transfer points (🔴 FLAG these as HIGH priority integration opportunities)
- Technology adoption score (influences design complexity)

**Integration Opportunity Signals:**
- Manual data entry across systems
- Copy-paste workflows
- Tools that don't communicate
- Duplicated data in multiple places

---

## Workshop Wrap-Up (5 minutes)

**Summarize top opportunities:**

*"[STAKEHOLDER], this has been incredibly valuable. Let me summarize the highest-priority opportunities:*

*1. **[Agent Type]** to handle [Specific Task], reducing your [X]-hour process to [Y] hours of expert review*

*2. **[Agent Type]** to [Specific Task], cutting [Process] time by [Z]%*

*3. **[Agent Type]** to [Specific Task], freeing you from [Routine Work]*

*Does that align with your priorities? Am I missing anything?"*

**Confirm next steps:**

*"Here's what happens next:*

*1. I'll create a detailed requirements document within 48 hours*
*2. You'll review it for accuracy*
*3. Once confirmed, I'll design the complete system architecture (2-3 hours)*
*4. Then I'll build a working prototype (typically 4-8 weeks)*
*5. We'll meet for you to test the prototype with real work*

*Let's schedule the prototype review for [DATE_6-8_WEEKS]. Does that work?"*

---

## Requirements Output

**Write to:** `knowledge_base/user_requirements.json`

**Completeness score:** Should be COMPLETE (all critical sections populated)

**Deliver to stakeholder within 48 hours:**

```markdown
# Requirements Document - [Project Name]

[Complete structured requirements following user_requirements.json schema]

## Executive Summary
[For leadership - business case, expected impact, investment]

## Technical Details  
[For engineering - workflows, integrations, requirements]

## AI Opportunities Prioritized
1. [Opportunity 1] - HIGH Priority
2. [Opportunity 2] - HIGH Priority
3. [Opportunity 3] - MEDIUM Priority

## Recommended Architecture
[Preliminary multi-agent architecture based on patterns]

## Next Steps
[Architecture design → Prototype → Review meeting]
```

---

## Success Criteria

Comprehensive Workshop is successful when:

✅ **Complete in 90 minutes**  
✅ **All 6 sections covered**  
✅ **2-3 service workflows documented step-by-step**  
✅ **Complete technology stack** (80%+ tools captured)  
✅ **5+ specific AI opportunities identified**  
✅ **Stakeholders validate top 3 priorities**  
✅ **Prototype review meeting scheduled**  
✅ **Requirements document delivered within 48 hours**

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Estimated Duration:** 90 minutes  
**Completeness:** Executive-ready, comprehensive requirements
