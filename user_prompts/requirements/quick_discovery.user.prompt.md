# Quick Discovery - User Prompt (15 Minutes)

**Phase:** Requirements Discovery  
**Duration:** 15 minutes  
**Best for:** Solo-entrepreneurs, small teams, simple AI use cases, fast decision-making  
**Agent:** Requirements Agent  
**Output:** `knowledge_base/user_requirements.json`

---

## Purpose

Rapidly assess AI opportunities through a structured 10-question interview. Get from "I have an idea" to "Here's what to build next" in exactly 15 minutes.

**Best for:**
- Solo-entrepreneurs or small teams (1-5 people)
- Clear, focused problems
- Simple automation needs
- Fast decision-making required
- First-time AI system builders

**Not suitable for:**
- Complex multi-stakeholder projects → Use Comprehensive Workshop instead
- Enterprise systems with compliance requirements → Use Standard Discovery
- Unclear problems requiring deep exploration → Use Standard Discovery

---

## Instructions for Requirements Agent

When a user invokes this prompt, execute the following 4-step process:

### Step 1: Welcome & Set Expectations (1 minute)

```
🚀 Welcome to Quick Discovery!

I'll help you figure out what to build and how to build it—in just 15 minutes.

I'll ask you **10 quick questions** about your project, then give you:
✅ Clear requirements summary
✅ AI suitability assessment
✅ Recommended agent patterns
✅ Specific next steps

**Important:** Be specific in your answers. The more detail you provide, the better recommendations you'll get.

Ready? Let's start:

**Question 1 of 10:** What problem are you trying to solve with AI?
(Describe it in 1-2 sentences—don't overthink it!)
```

---

### Step 2: Progressive Questioning (8 minutes)

Ask questions **one at a time**. Keep your responses brief and encouraging. Use `<thinking>` tags internally to classify pain points and identify patterns.

#### The 10 Questions

**Q1: Problem Statement**
```
What problem are you trying to solve with AI?
```
**Capture:** Core pain point, current manual process

---

**Q2: Current Process**
```
How do you handle this today? Walk me through the manual steps.
```
**Capture:** Workflow steps, time spent, tools used

**Real-time classification:**
```
<thinking>
Is this digital/computer-based? → [Yes/No]
Is it repetitive? → [Yes/No]
Initial classification: [HIGH/MEDIUM/LOW]
</thinking>
```

---

**Q3: Frequency & Impact**
```
How often does this happen, and how much time does it take each time?
```
**Capture:** Volume (daily/weekly/monthly), time per instance, total time investment

**Real-time calculation:**
```
<thinking>
Frequency: [X times per week/month]
Time per instance: [Y hours]
Annual impact: [X × Y × 52 or X × Y × 12] = [TOTAL] hours/year
Classification: If >250 hrs/year (5+ hrs/week) → HIGH priority
</thinking>
```

---

**Q4: Input & Output**
```
What information goes in, and what should come out?
```
**Capture:** Data sources, desired deliverables, output format

---

**Q5: Decision Points**
```
What parts require your judgment vs. following rules or templates?
```
**Capture:** Complexity level, where AI fits, what stays human-led

---

**Q6: Team Context**
```
Who will use this system? What's their technical comfort level (1-10)?
```
**Capture:** User personas, technical sophistication, training needs

---

**Q7: Tools & Systems**
```
What tools do you currently use? Any integrations needed?
```
**Capture:** Technology stack, integration requirements, API availability

---

**Q8: Timeline**
```
When do you need this working? What's driving that timeline?
```
**Capture:** Urgency, business drivers, deadline flexibility

---

**Q9: Resources**
```
What resources do you have? (team size, budget range, time availability)
```
**Capture:** Constraints, available resources, willingness to invest

---

**Q10: Success Criteria**
```
What does success look like? How will you measure whether this AI system is worth it?
```
**Capture:** Measurable outcomes, acceptance criteria, KPIs

---

### Step 3: Analysis & Requirements Structuring (4 minutes)

After gathering answers, analyze and structure requirements:

**Internal Analysis:**
```
<thinking>
1. Problem Classification:
   - Type: [Document generation / Data processing / Research / Workflow automation / etc.]
   - Complexity: [Simple / Moderate / Complex]
   - AI Suitability: [HIGH / MEDIUM / LOW]
   - Time impact: [Hours/week] → [Annual value]

2. Pattern Matching:
   - Primary pattern: [Specialist / Workflow / Document Generator / etc.]
   - Reason: [Why this pattern fits based on their answers]
   - Reference: docs/agent_design_patterns.md - [Pattern Name]

3. Multi-Agent Assessment:
   - Single agent sufficient? OR
   - Multi-agent needed? (If yes, which agents and why)

4. Technical Assessment:
   - Recommended LLM: [Claude / GPT-4 / etc. with rationale]
   - Integration complexity: [Low / Medium / High]
   - Development time: [Hours/days estimate]
   - Tech stack: [Python/Node.js, frameworks]

5. ROI Quick Calculation:
   - Time saved: [Hours/year]
   - Value: [If billable, hours × rate] OR [Opportunity cost]
   - Investment: [Estimated development cost]
   - Payback: [Months]

6. Completeness Check:
   - All 10 questions answered? ✓
   - Sufficient detail for architecture? [Yes/Partial/No]
   - Missing information: [List gaps if any]
</thinking>
```

**Structure into user_requirements.json:**

Map answers to JSON schema:
- Q1, Q2 → `business.problem`, `business.current_state`
- Q3 → `business.success_metrics`, `business.business_value.efficiency_gains`
- Q4 → `technical.functional_requirements`, `use_case.workflow_steps`
- Q5 → `technical.ai_services.evaluation_criteria`
- Q6 → `use_case.target_users`, `use_case.user_personas`
- Q7 → `technical.integration_requirements`, `reference_materials.documents`
- Q8 → `project_scope.timeline_estimate_weeks`, `financial.budget_constraints`
- Q9 → `constraints` (from system_config), `project_scope.level_of_effort_estimate`
- Q10 → `business.success_metrics`, `business.desired_outcome`

---

### Step 4: Generate Recommendations & Write to Knowledge Base (2 minutes)

**Deliver recommendations in this format:**

```markdown
# 🎯 Your AI Architecture Plan - Quick Discovery Results

## Problem Summary

**What you're solving:** [Restate their problem clearly in 1-2 sentences]

**Current state:** [How they handle it today, time/cost impact]

**AI Suitability: [🔴 HIGH / 🟡 MEDIUM / 🟢 LOW]**

**Rationale:**
- [Reason 1: e.g., Digital, repetitive task]
- [Reason 2: e.g., Clear rules or templates exist]
- [Reason 3: e.g., Significant time impact (X hrs/week)]

**Expected Impact:**
- Time savings: [X hours/week] → [Y hours/year annually]
- Value: $[Z/year] ([Calculate from time saved × hourly value])
- Quality improvement: [Specific improvements]
- Capacity gain: [What they can do with freed time]

---

## Recommended Solution

### Primary Approach: [Agent Pattern Name]

**Pattern:** [Specialist / Workflow / Document Generator / Multi-Agent / etc.]

**Why this pattern:**
[Specific reasoning based on their answers - reference docs/agent_design_patterns.md]

**How it works:**
1. [Step 1 of their workflow automated]
2. [Step 2 of their workflow automated]
3. [Output delivered in desired format]

**For multi-agent systems:**
- **Agent 1: [Name]** - [Specific responsibility]
- **Agent 2: [Name]** - [Specific responsibility]
- **Coordination:** [How they share data]

**Example from the framework:**
→ See: `docs/agent_design_patterns.md` - [Pattern Name] section

---

## Technology Recommendations

**LLM Platform:** [Claude Sonnet 3.5 / GPT-4 Turbo / etc.]
- **Reason:** [Why this choice fits their needs, constraints, use case]
- **Cost estimate:** $[amount]/month based on [usage assumptions]

**Development Stack:** [Python + FastAPI + Streamlit / Node.js + Express + React / etc.]
- **Reason:** [Based on team skills, timeline, complexity]
- **Learning curve:** [Low / Moderate / Significant]

**Integration Approach:** [API integration / CSV upload / Hybrid / Simulated initially]
- **For [Their Tool 1]:** [Specific integration strategy with complexity assessment]
- **For [Their Tool 2]:** [Specific integration strategy]

**Development Timeline Estimate:**
- **Phase 1 (Foundation):** [X days] - Setup, core agent prompt
- **Phase 2 (Core Development):** [Y days] - Main functionality
- **Phase 3 (Testing & Polish):** [Z days] - Validation, refinement
- **Total:** [X+Y+Z days / weeks]

---

## Requirements Summary (for knowledge_base/user_requirements.json)

✅ **Writing to:** `knowledge_base/user_requirements.json`

**Key sections populated:**
- customer: ✓ Basic context
- use_case: ✓ Problem, solution approach, target users
- business: ✓ Current state, desired outcome, business value, success metrics
- technical: ✓ Functional requirements (MVP scope), integration needs
- project_scope: ✓ Timeline estimate, phased approach
- financial: ✓ Expected ROI, budget constraints
- risks: ✓ Initial risk assessment
- _metadata: ✓ Discovery method (quick_discovery), completeness score

**Completeness Score:** [COMPLETE / PARTIAL / INCOMPLETE]

**Missing Information (if PARTIAL):**
- [Specific technical detail 1]
- [Specific technical detail 2]
- **Note:** Architecture Agent can gather these technical details during design phase

---

## Your Next Steps

**Recommended Path:**

Since this is a [simple/moderate/complex] use case with [clear/moderate/unclear] requirements, I recommend:

### → Proceed to Architecture Agent

**What happens next:**
1. Architecture Agent will execute 6-step design process:
   - Step 1: Tech stack selection (30 min)
   - Step 2: Architecture diagram (20 min)
   - Step 3: Team composition (20 min)
   - Step 4: LOE estimation (30 min)
   - Step 5: Cost estimation (20 min)
   - Step 6: Project plan (40 min)

2. **Total time:** 2-3 hours for complete architecture design

3. **You'll get:**
   - Detailed technology stack recommendations
   - Visual architecture diagram
   - Team composition and hiring plan
   - Accurate cost and timeline estimates
   - Complete project implementation plan

**Ready to proceed to architecture design?**

---

## Alternative Paths (if not ready for full architecture)

### Path A: Build Quick Prototype First (Validate Fast)
**Best if:** You want to see something working before committing to full design

→ Skip to Engineering Agent with basic requirements
→ Build minimal prototype in 1-2 days
→ Validate value before investing in complete architecture
→ **Risk:** May need to refactor if architecture isn't sound

### Path B: Gather More Requirements (Need More Detail)
**Best if:** Requirements still feel incomplete or complex

→ Use Standard Discovery (30 min) or Comprehensive Workshop (90 min)
→ Get more detailed requirements
→ Then proceed to architecture
→ **Timeline:** +30-90 minutes for requirements

---

## Summary

**What we accomplished:**
- ✅ 10 questions answered in 15 minutes
- ✅ Problem clearly defined
- ✅ AI suitability assessed ([HIGH/MEDIUM/LOW])
- ✅ Agent pattern matched
- ✅ Technology recommended
- ✅ Requirements written to knowledge base

**Knowledge Base Updated:**
- ✅ `knowledge_base/user_requirements.json` populated

**What's Next:**
- Proceed to Architecture Agent for system design
- Estimated time to working prototype: [X weeks]
- Expected investment: $[Y] development + $[Z]/month operations

---

Ready to move forward with architecture design?
```

---

## Example: Financial Operations Assistant (Primary Example)

**Scenario:** Solo-entrepreneur spending 10 hours/week on invoicing, expense tracking, and financial reporting.

### Sample 10-Question Flow

**Q1: What problem are you trying to solve with AI?**
> "I spend way too much time on financial admin—invoicing, tracking expenses, and creating monthly reports. It's taking 10+ hours every week away from client work."

```
<thinking>
Problem: Financial administration workload
Initial assessment: HIGH priority (repetitive, digital, time-consuming)
</thinking>
```

---

**Q2: How do you handle this today?**
> "I use QuickBooks for invoicing (manual entry), take photos of receipts then manually categorize in Excel, and compile monthly P&L reports by pulling data from multiple sources into Excel templates."

```
<thinking>
Tools: QuickBooks, Excel, manual processes
Pattern emerging: Document generation + data processing
Multiple disconnected tools = integration opportunity
</thinking>
```

---

**Q3: How often does this happen, and how much time does it take?**
> "Invoicing: 2 hours/week. Expenses: 3 hours/week. Monthly reports: 5 hours once a month. Total about 10 hours/week average."

```
<thinking>
10 hrs/week × 50 weeks = 500 hrs/year
At $100-200/hr billable rate = $50K-$100K opportunity cost
Classification: HIGH priority (>5 hrs/week threshold)
</thinking>

🔴 PAIN POINT IDENTIFIED: Financial operations (10 hrs/week = 500 hrs/year)
Significant opportunity for automation!
```

---

[Continue through all 10 questions...]

**Q10: What does success look like?**
> "Success means spending <2 hours/week on financial admin instead of 10. Monthly reports generated automatically in minutes instead of hours. Accurate expense categorization without manual work. More time for billable client work."

```
<thinking>
Success metrics clear:
- Time: 10 hrs/week → <2 hrs/week (80% reduction)
- Monthly reports: 5 hours → <15 minutes
- Quality: Accurate categorization (>95%)
User knows what they want = COMPLETE requirements for this scope
</thinking>
```

---

### Analysis Results

```
<thinking>
1. Problem Classification:
   - Type: Financial operations automation (invoicing, expenses, reporting)
   - Complexity: Moderate (multiple workflows, but each is straightforward)
   - AI Suitability: HIGH (digital, repetitive, rule-based, structured data)

2. Pattern Matching:
   - Primary pattern: Multi-Agent System
     - Agent 1: Financial Operations Agent (invoicing, expense categorization)
     - Agent 2: Analytics & Reporting Agent (P&L, forecasting, insights)
   - Reason: Two distinct domains (operations vs. analytics) with shared data
   - Reference: Similar to financial-assistant-for-families architecture

3. Technical Assessment:
   - Recommended LLM: Claude Sonnet 3.5 (excellent at financial analysis, structured data)
   - Alternative: Claude Haiku for simple categorization (cost optimization)
   - Integration complexity: MEDIUM (QuickBooks API, email for sending invoices)
   - Development time: 4-6 weeks estimate

4. ROI Calculation:
   - Time saved: 8 hrs/week (10 → 2) = 400 hrs/year
   - Value: At $150/hr billable = $60,000/year opportunity cost
   - Investment: ~$50K-75K development + $200/month operations
   - Payback: <12 months

5. Completeness: COMPLETE for quick discovery (can proceed to architecture)
</thinking>
```

---

### Generated Output

```markdown
# 🎯 Your AI Architecture Plan - Financial Operations Assistant

## Problem Summary

**What you're solving:** Automating 10 hours/week of routine financial administration (invoicing, expense tracking, monthly reporting) for a solo-entrepreneur.

**Current state:** Manual processes across QuickBooks, Excel, and email consuming 500 hours/year that could be spent on billable client work.

**AI Suitability: 🔴 HIGH Priority** - Excellent fit for AI automation

**Rationale:**
- Digital, computer-based tasks (invoicing, spreadsheets, documents)
- Highly repetitive (same process weekly/monthly)
- Structured data and clear rules (financial transactions follow patterns)
- Significant time impact (10 hrs/week = 500 hrs/year)
- Clear templates exist (invoice formats, expense categories, report structures)

**Expected Impact:**
- **Time savings:** 8 hours/week → 400 hours/year
- **Value:** $60,000/year (at $150/hr billable rate - opportunity cost eliminated)
- **Quality improvement:** Consistent categorization, fewer errors, real-time insights
- **Capacity gain:** 400 hours freed up for revenue-generating client work

**Business Case:**
- Investment: $50K-$75K development + $200/month operations
- Payback: <12 months
- ROI: 80-120% in Year 1, 300-400% over 3 years

---

## Recommended Solution

### Primary Approach: Multi-Agent Financial Operations System

**Pattern:** Multi-Agent System (2 specialized agents)

**Why this pattern:**
You have two distinct problem domains that benefit from specialization:
1. **Operations** (invoicing, expense tracking) - Transactional, frequent, rule-based
2. **Analytics** (reporting, forecasting) - Analytical, periodic, insight-driven

Separating these into specialized agents gives you:
- Better performance (each agent optimized for its domain)
- Lower costs (use cheaper models for simple operations, premium for complex analytics)
- Easier improvement (update one agent without affecting the other)

**How it works:**

**Agent 1: Financial Operations Agent**
1. Receives project data (hours, rate, client) → Generates professional invoice
2. Receives expense data (receipt photo/text) → Categorizes using IRS business rules
3. Tracks transactions → Stores in shared knowledge base

**Agent 2: Analytics & Reporting Agent**
1. Reads transaction data from knowledge base
2. Generates monthly P&L, cash flow statements
3. Identifies trends and provides forecasts
4. Delivers actionable financial insights

**Coordination:**
- Shared knowledge base (local JSON/SQLite)
- Operations Agent writes transactions
- Analytics Agent reads and analyzes
- User interacts with either agent based on task

**Example from the framework:**
→ See: `docs/agent_design_patterns.md` - Multi-Agent Coordinator pattern
→ Reference: Similar to [financial-assistant-for-families](https://github.com/Modular-Earth-LLC/financial-assistant-for-families) but with better separation of concerns

---

## Technology Recommendations

**LLM Platform:** Claude Sonnet 3.5 (Anthropic)
- **Reason:** 
  - Excellent at financial analysis and structured data processing
  - Strong at maintaining professional tone for invoices
  - Reliable for rule-based categorization (IRS expense categories)
  - Good balance of quality and cost
- **Cost estimate:** $100-150/month
  - Invoicing: 20 invoices/month × ~2K tokens = 40K tokens
  - Expenses: 50 expenses/month × ~1K tokens = 50K tokens
  - Reports: 1 report/month × ~10K tokens = 10K tokens
  - Total: ~100K tokens/month × $3/million = $0.30 + overhead ≈ $100-150/month
- **Cost optimization:** Use Claude Haiku for simple expense categorization (60% cost reduction)

**Development Stack:** Python + Streamlit
- **Reason:**
  - Python: Excellent for financial calculations, data processing, CSV/JSON handling
  - Streamlit: Fastest path to functional UI for non-technical users
  - LangChain (optional): If need complex agent orchestration
- **Learning curve:** Low (if team knows Python) / Moderate (if new to Python)
- **Timeline advantage:** 30% faster than building custom web app

**Integration Approach:** Hybrid (Phase 1: CSV, Phase 2: API)
- **Phase 1 (MVP):** 
  - QuickBooks: CSV export upload (simple, works immediately)
  - Email: Gmail API for sending invoices (well-documented)
  - Receipts: Text entry or photo OCR (Anthropic vision API)
- **Phase 2 (Enhancement):**
  - QuickBooks API: Direct integration (after MVP validates value)
  - Bank feeds: Plaid API for automatic transaction import

**Development Timeline Estimate:**
- **Phase 1 (MVP - 4 weeks):**
  - Week 1: Setup, agent prompts, basic invoicing
  - Week 2: Expense categorization, data storage
  - Week 3: Monthly reports, UI
  - Week 4: Testing, refinement, documentation
- **Phase 2 (API Integration - 2 weeks):**
  - QuickBooks API integration
  - Enhanced features based on MVP feedback

---

## Requirements Summary

✅ **Successfully written to:** `knowledge_base/user_requirements.json`

**Sections populated:**
- ✅ customer: Solo-entrepreneur, consulting business
- ✅ use_case: Financial operations automation, target user (solo-entrepreneur)
- ✅ business: Problem (10 hrs/week admin), value ($60K/year), success metrics
- ✅ technical: 
  - Functional requirements: Invoice generation, expense categorization, monthly reporting
  - Performance: <30 sec invoicing, <10 sec categorization
  - Integration: QuickBooks, Gmail, receipt photos
- ✅ project_scope: Phase 1 (MVP), Phase 2 (API integration)
- ✅ financial: ROI projection (80-120% Year 1)
- ✅ risks: OCR accuracy, data security, user adoption
- ✅ _metadata: Quick discovery (15 min), completeness score: COMPLETE

**Completeness Score:** COMPLETE (ready for architecture design)

**Validation:** All 10 questions answered with sufficient detail for architecture phase.

---

## Your Next Steps

**Recommended:** Proceed to Architecture Agent

**Why:** You have complete requirements. Architecture Agent will:
1. Select optimal tech stack (validate my recommendations)
2. Generate architecture diagram (visual system design)
3. Estimate team needs (likely 1-2 engineers for solo-entrepreneur tool)
4. Calculate accurate costs and timeline
5. Create detailed project plan

**Time investment:** 2-3 hours for complete architecture design

**What you'll get:**
- Validated technology stack
- Architecture diagram for presentations
- Accurate cost estimate ($X development + $Y/month operations)
- Realistic timeline with milestones
- Complete implementation plan

**Alternative:** If you want to validate with a quick prototype first, you can skip to Engineering Agent (riskier, but faster to see something working).

**How do you want to proceed?**
```

---

## Success Criteria

This quick discovery is successful when:

✅ **Complete in 15 minutes** (10 questions + analysis)  
✅ **Problem clearly defined** (user can explain it in 1-2 sentences)  
✅ **AI suitability assessed** (HIGH/MEDIUM/LOW with clear rationale)  
✅ **Pattern matched** (recommended agent architecture)  
✅ **Technology recommended** (LLM, stack, integrations)  
✅ **ROI estimated** (quick calculation of value)  
✅ **Requirements written** to user_requirements.json  
✅ **Next steps clear** (proceed to architecture OR gather more requirements)

---

## Notes for Requirements Agent

**This is a USER PROMPT - the user copies this into chat where Requirements Agent is running.**

**Your role (Requirements Agent):**
1. Follow the 4-step process exactly
2. Ask questions one at a time
3. Use `<thinking>` tags for classification and analysis (don't show to user)
4. Structure answers into user_requirements.json schema
5. Provide clear, actionable recommendations
6. Guide to appropriate next step

**Keep it fast:** 15 minutes total, no more. Be efficient but thorough.

**Primary example:** Use financial operations assistant throughout for consistency.

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Estimated Duration:** 15 minutes  
**Completeness:** Sufficient for architecture design (may need technical details later)
