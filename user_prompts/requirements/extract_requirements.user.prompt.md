# Extract Requirements from Notes - User Prompt

**Phase:** Requirements Discovery  
**Duration:** 30-60 minutes  
**Best for:** Post-meeting requirements structuring  
**Agent:** Requirements Agent  
**Input:** Unstructured meeting notes, emails, transcripts  
**Output:** `knowledge_base/user_requirements.json`

---

## Purpose

Parse unstructured meeting notes, email threads, or conversation transcripts into structured requirements following the user_requirements.json schema.

**When to use:**
- After stakeholder discovery sessions or requirements meetings
- Have scattered notes that need organization
- Before creating project proposals or technical designs
- Transitioning from informal notes to formal requirements

**Prerequisites:** Meeting notes, email threads, Slack conversations, or transcripts

---

## Instructions for Requirements Agent

When a user provides unstructured notes, execute this extraction process:

### Step 1: Load and Review Notes

```
Thank you for sharing these notes. I'll parse them into a structured requirements document.

**What I'll do:**
1. Extract key information across all requirement categories
2. Structure according to user_requirements.json schema
3. Flag missing information with "[TO BE DETERMINED]"
4. Recommend follow-up questions

**This will take a few minutes. Processing...**
```

---

### Step 2: Systematic Extraction

**Parse notes and extract information for each category:**

**DO NOT fabricate information.** Only extract what is explicitly stated or clearly implied.

#### Extract: Customer/Organization Context

**Look for:**
- Company name, industry, size
- Business model
- Market position
- AI experience/maturity

**If found in notes:** Populate `customer` section  
**If not found:** Mark "[TO BE DETERMINED]"

---

#### Extract: Use Case & Problem Statement

**Look for:**
- What problem they're trying to solve
- Current pain points
- Desired outcomes
- Target users

**Map to:**
- `use_case.title`, `use_case.summary`, `use_case.problem_statement`
- `business.problem`
- `business.desired_outcome`

---

#### Extract: Current State & Workflows

**Look for:**
- How things work today
- Manual processes
- Time spent on tasks
- Tools being used
- Bottlenecks

**Map to:**
- `business.current_state.how_handled_today`
- `business.current_state.pain_points`
- `business.current_state.time_spent`
- `technical.integration_requirements`

---

#### Extract: Business Value & Success Metrics

**Look for:**
- Expected ROI or time savings
- Cost reduction opportunities
- Strategic importance
- Success criteria
- KPIs mentioned

**Map to:**
- `business.business_value` (all subsections)
- `business.success_metrics.kpis`
- `financial.expected_roi`

---

#### Extract: Technical Requirements

**Look for:**
- Specific features mentioned ("need to be able to X")
- Performance targets ("must be fast", "real-time")
- Integration needs ("connect to system Y")
- Security/compliance mentions
- Data sources

**Map to:**
- `technical.functional_requirements`
- `technical.non_functional_requirements`
- `technical.integration_requirements`
- `technical.data_requirements`

---

#### Extract: Project Scope & Timeline

**Look for:**
- Timeline mentions ("need by end of quarter")
- Budget constraints
- Phased approach mentions
- What's in/out of scope

**Map to:**
- `project_scope.timeline_estimate_weeks`
- `constraints.timeline.deadline` (in system_config)
- `project_scope.phased_approach`

---

#### Extract: Risks & Concerns

**Look for:**
- Stakeholder concerns about AI
- Technical risks mentioned
- Business risks
- Dependencies

**Map to:**
- `risks.business_risks`
- `risks.technical_risks`
- `risks.assumptions`

---

### Step 3: Identify Gaps

**After extraction, analyze completeness:**

```
<thinking>
Required for architecture design:
✓ Problem statement clear
✓ Current process documented
✗ Performance requirements missing
✗ Data volume unclear
✗ Integration details incomplete

Completeness score: PARTIAL

Critical gaps:
1. [Gap 1]
2. [Gap 2]

Optional gaps (can be gathered later):
1. [Gap 3]
</thinking>
```

**Generate gap analysis:**

```markdown
## Missing Information (Critical for Architecture)

**High Priority (need before architecture design):**
1. **[Missing Item 1]**
   - Why needed: [Impact on architecture]
   - Suggested question: "[Question to ask stakeholder]"

2. **[Missing Item 2]**
   - Why needed: [Impact on architecture]
   - Suggested question: "[Question to ask stakeholder]"

**Medium Priority (Architecture Agent can gather during design):**
1. **[Missing Item 3]**
   - Why needed: [Impact]
   - Can be determined during: [Which architecture step]

**Optional (Nice to have):**
1. **[Missing Item 4]**
   - Impact: [Low - won't block design]
```

---

### Step 4: Generate Structured Requirements Document

**Output format:**

```markdown
# Requirements Document - [Project Name]

**Extracted from:** [Meeting notes from DATE]  
**Stakeholders:** [Names from notes]  
**Completeness:** [COMPLETE / PARTIAL / INCOMPLETE]

---

## Executive Summary

**Problem:** [Concise problem statement extracted from notes]

**Proposed Solution:** [High-level AI approach based on pain points]

**Expected Impact:**
- [Business value extracted from notes]
- [Estimated based on pain points if not stated]

**AI Suitability:** [HIGH/MEDIUM/LOW based on pain point analysis]

---

## Customer Context

**Organization:** [Company name]  
**Industry:** [Industry]  
**Business Model:** [How they operate/make money]  
**AI Maturity:** [beginner/intermediate/advanced based on notes]

---

## Use Case

**Title:** [Descriptive title]

**Summary:** [1-2 paragraph description extracted from notes]

**Target Users:** [Who will use this system]

**Workflow Steps:** [High-level steps extracted or inferred]

---

## Business Requirements

### Current State
**How handled today:** [Extracted from notes]

**Pain Points:**
1. [Pain point 1 from notes]
2. [Pain point 2 from notes]

**Time/Cost Impact:** [Quantification if mentioned]

### Desired Outcome
**Success Definition:** [What success looks like, extracted from notes]

**Expected Improvements:** [Benefits mentioned in notes]

### Business Value
- **Revenue impact:** [Extracted or "[TO BE DETERMINED]"]
- **Cost savings:** [Extracted or estimated from time savings]
- **Strategic value:** [Competitive advantage mentioned]
- **Efficiency gains:** [Time saved, capacity unlocked]

### Success Metrics
**KPIs:** [Metrics mentioned in notes, or "[TO BE DETERMINED - suggest KPIs]"]

---

## Technical Requirements

### Functional Requirements

[For each feature mentioned in notes]

**FR-1: [Feature Title]**
- Description: [From notes]
- Priority: [MUST_HAVE / SHOULD_HAVE / NICE_TO_HAVE - infer from notes]
- Complexity: [LOW / MEDIUM / HIGH - initial estimate]

**FR-2: [Feature Title]**
[Same structure...]

### Non-Functional Requirements

**Performance:**
- Response time target: [Extracted or "[TO BE DETERMINED]"]
- Throughput: [Extracted or "[TO BE DETERMINED]"]
- Concurrent users: [Extracted or "[TO BE DETERMINED]"]

**Security & Compliance:**
- [Any compliance requirements mentioned: GDPR, HIPAA, etc.]
- [Security concerns mentioned]

### Integration Requirements

**Systems to integrate:**
1. **[System 1]:** [Purpose, mentioned in notes]
   - API available: [Yes/No/Unknown]
   - Integration complexity: [Estimate]

2. **[System 2]:** [Purpose]
   [Same structure...]

### Data Requirements

**Data Sources:** [Data sources mentioned]  
**Data Volume:** [Estimate if mentioned]  
**Data Quality:** [Concerns mentioned in notes]

---

## Project Scope

**In Scope (Phase 1):**
- [Features that seem critical from notes]

**Out of Scope (Phase 1):**
- [Features that seem secondary or "nice to have"]

**Assumptions:** [Assumptions being made based on notes]

**Constraints:** [Constraints mentioned: budget, timeline, technical]

---

## Risks

**Business Risks:**
1. [Risk mentioned in notes with mitigation if stated]

**Technical Risks:**
1. [Technical concern mentioned]

**Assumptions to Validate:**
- [Assumption 1 that needs confirmation]

---

## Missing Information Summary

### Critical (Need Before Architecture)
- [ ] [Missing item 1] - Suggested question: "[Question]"
- [ ] [Missing item 2] - Suggested question: "[Question]"

### Important (Can gather during architecture)
- [ ] [Missing item 3]
- [ ] [Missing item 4]

### Nice to Have
- [ ] [Missing item 5]

---

## Recommended Follow-Up Actions

1. **Immediate:**
   - [Action to fill critical gap]
   - [Action to confirm assumption]

2. **Before architecture design:**
   - [Clarification needed]

3. **During architecture:**
   - [Technical details Architecture Agent can gather]

---

**Knowledge Base Status:**
✅ Written to: `knowledge_base/user_requirements.json`

**Completeness Score:** [COMPLETE / PARTIAL / INCOMPLETE]

**Ready for architecture design?** [Yes, if COMPLETE] [No, need follow-up if PARTIAL/INCOMPLETE]
```

---

## Example: Extracting from Financial Operations Meeting Notes

**Input (sample notes):**

```
Meeting with John (solo entrepreneur, consulting business)
Date: 2025-10-01

Pain points:
- Spends WAY too much time on invoicing - about 2 hrs/week
- Manual expense tracking in Excel is killing him - 3 hrs/week
- Monthly financial reports take 5 hours to compile
- Uses QuickBooks for invoicing but it's manual entry
- Takes photos of receipts but then has to categorize manually
- Pulls data from QB, Excel, and email into monthly P&L reports

Tech level: Comfortable with basic software, not a developer (6/10)

Timeline: Would like this working in next quarter (Q1 2026)

Budget: Willing to invest $50K-75K if ROI is clear

Success = spending <2 hrs/week on financial admin instead of 10 hrs

Tools: QuickBooks Self-Employed, Excel, Gmail
```

**Extracted requirements:**

```markdown
# Requirements Document - Financial Operations AI Assistant

**Extracted from:** Meeting notes (2025-10-01)  
**Stakeholder:** John (Solo Entrepreneur)  
**Completeness:** COMPLETE

## Executive Summary

**Problem:** Solo-entrepreneur spending 10 hours/week on routine financial tasks (invoicing, expense tracking, monthly reporting).

**Proposed Solution:** Multi-agent AI system for financial operations automation.

**Expected Impact:**
- Time savings: 8 hours/week (80% reduction)
- Annual value: $60,000/year opportunity cost (at $150/hr billable rate)

**AI Suitability: 🔴 HIGH** - Repetitive, digital, rule-based tasks with clear ROI

---

## Customer Context

**Organization:** Solo consulting business  
**Industry:** Professional services / consulting  
**Business Model:** Billable hours  
**AI Maturity:** beginner (first AI project)

## Use Case

**Title:** Financial Operations AI Assistant for Solo-Entrepreneurs

**Summary:** Automate invoicing, expense tracking, and financial reporting to free up 8 hours/week for revenue-generating client work.

**Target Users:** Solo-entrepreneur (non-technical, comfortable with basic software)

**Workflow Steps:**
1. Generate invoices from project data
2. Categorize expenses from receipt photos
3. Compile monthly P&L reports from multiple data sources

## Business Requirements

### Current State
- Invoicing: QuickBooks (manual entry) - 2 hrs/week
- Expenses: Receipt photos + Excel categorization - 3 hrs/week  
- Reports: Manual compilation from QB + Excel - 5 hrs/month
- **Total:** 10 hrs/week average

### Desired Outcome
- Financial admin time: <2 hrs/week (from 10)
- Automated processes with expert review vs. manual execution

### Business Value
- Time savings: 400 hrs/year
- Value: $60,000/year opportunity cost
- Cost reduction: Eliminate manual processes

---

## Technical Requirements

**FR-1: Automated Invoice Generation** (Priority: MUST_HAVE)
**FR-2: Expense Categorization from Photos** (Priority: MUST_HAVE)
**FR-3: Monthly Financial Report Generation** (Priority: MUST_HAVE)

**Performance:** [TO BE DETERMINED - need during architecture]

**Integration:**
- QuickBooks Self-Employed
- Gmail
- Receipt photo processing

**Technology Comfort:** 6/10 (need simple UI)

---

## Project Scope

**Timeline:** Q1 2026 (next quarter)  
**Budget:** $50K-$75K

**Missing Information:**
- [ ] Specific performance requirements (response time targets)
- [ ] Data volume (number of invoices/expenses per month)
- [ ] Compliance requirements (if any)

**Recommended follow-up:** Quick 15-min call to clarify performance needs, or Architecture Agent can gather during design.

---

✅ **Written to:** `knowledge_base/user_requirements.json`
✅ **Completeness:** COMPLETE (ready for architecture)
✅ **Next Step:** Proceed to Architecture Agent
```

---

## Success Criteria

Requirements extraction is successful when:

✅ **All provided information extracted** (nothing missed from notes)  
✅ **Properly structured** into user_requirements.json schema  
✅ **Gaps clearly identified** with "[TO BE DETERMINED]"  
✅ **Follow-up questions suggested** for critical gaps  
✅ **Completeness score accurate** (COMPLETE/PARTIAL/INCOMPLETE)  
✅ **Ready for next phase** (architecture design or follow-up)

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Input:** Unstructured text (notes, emails, transcripts)  
**Output:** Structured user_requirements.json
