# Implementation Proposal Assembly - User Prompt

**Phase:** Post-Architecture (after design complete, before engineering)  
**Purpose:** Assemble executive proposal for POC/MVP implementation  
**Agent:** Architecture Agent  
**Inputs:** `knowledge_base/user_requirements.json`, `knowledge_base/design_decisions.json`  
**Output:** Executive proposal document

---

## Purpose

Assemble a comprehensive implementation proposal for executive approval by READING from the knowledge base (not redoing architecture work). This proposal enables business leaders to make go/no-go decisions on prototype development.

**When to use:**
- After Architecture Agent has completed all 6 design steps
- Before Engineering Agent begins prototype development
- Need executive/leadership approval for development investment
- Ready to present technical plan to decision-makers

**Prerequisites:**
- ✅ `knowledge_base/user_requirements.json` complete
- ✅ `knowledge_base/design_decisions.json` complete (all 6 steps)
- ✅ Architecture diagram generated
- ✅ Cost estimates calculated

---

## Instructions for Architecture Agent

When user requests implementation proposal, execute this assembly process:

### Step 1: Validate Prerequisites

```
<thinking>
Checking knowledge base completeness:
1. user_requirements.json exists? → [Yes/No]
2. design_decisions.json exists? → [Yes/No]
3. All 6 design steps complete? → [Check _metadata.steps_completed]
4. Executive summary populated? → [Yes/No]

If incomplete: Identify missing steps and recommend completing them first.
If complete: Proceed with assembly.
</thinking>

✅ Knowledge base validated - all prerequisites met.

Assembling implementation proposal...
```

**If incomplete:**
```
⚠️ Cannot assemble proposal - missing architecture decisions

**Missing:**
- [Step X not complete]: Run user_prompts/architecture/[prompt].user.prompt.md
- [Section Y missing]: Complete via Architecture Agent

**Required for proposal:**
- Complete tech stack selection
- Architecture diagram generated
- Team composition defined
- LOE estimates calculated
- Cost projections complete
- Project plan created

Please complete these steps, then return here for proposal assembly.
```

---

### Step 2: Read from Knowledge Base

**Load data from:**
- `knowledge_base/user_requirements.json`
- `knowledge_base/design_decisions.json`  
- `knowledge_base/system_config.json`

**Extract:**
```
<thinking>
From user_requirements.json:
- Problem statement
- Business value and ROI
- Success metrics
- Stakeholder information
- Risks

From design_decisions.json:
- Executive summary (go/no-go recommendation)
- Tech stack with rationale
- Architecture diagram
- Team composition
- LOE estimates (timeline, hours, complexity)
- Cost projections (development, infrastructure, TCO)
- Project plan (phased roadmap, milestones)
- Risks and mitigation strategies

From system_config.json:
- Decision makers (who needs to approve)
- Budget constraints
- Timeline constraints
- Strategic priority
</thinking>
```

---

### Step 3: Assemble Executive Proposal

**Generate proposal in this dual-audience format:**

```markdown
# Implementation Proposal - [Project Name]

**Project Type:** POC (4-8 weeks) / MVP (8-16 weeks)  
**Prepared for:** [Decision Makers from system_config.json]  
**Date:** [Current date]  
**Recommendation:** [GO / Conditional GO / NO-GO from design_decisions.json]

---

## Executive Summary (5-Minute Read)

**Problem:**  
[From user_requirements.json: business.problem]

**Proposed Solution:**  
[From design_decisions.json: executive_summary.recommended_approach]

**Investment Required:**
- **Development:** $[From design_decisions.json: costs.development_costs.total_development]
- **Infrastructure:** $[From design_decisions.json: costs.infrastructure_costs.total_infrastructure_first_year] (Year 1)
- **Ongoing:** $[Monthly operational costs] per month
- **Total Year 1:** $[From design_decisions.json: costs.total_cost_of_ownership.year_1_total]

**Timeline:**  
[From design_decisions.json: estimates.timeline.total_weeks] weeks  
**Target Completion:** [Calculate from start date + weeks]

**Expected ROI:**
- **Payback Period:** [From design_decisions.json: costs.roi_projections.payback_period_months] months
- **3-Year ROI:** [From design_decisions.json: costs.roi_projections.roi_percentage_3yr]%
- **Annual Value:** $[From user_requirements.json: business.business_value]

**Confidence Level:** [From design_decisions.json: executive_summary.confidence_level]

**Key Risks:**
[Top 3 from design_decisions.json: risks_and_mitigation with mitigations]

**Key Benefits:**
[From design_decisions.json: executive_summary.key_benefits]

**Recommendation:** [GO / Conditional GO / NO-GO]  
[From design_decisions.json: executive_summary.go_no_go_recommendation]

---

## Business Case

### Problem Statement

**Current Situation:**  
[From user_requirements.json: business.current_state]

**Pain Points:**
[From user_requirements.json: business.current_state.pain_points]

**Business Impact:**
- **Time Cost:** [From user_requirements.json: business.current_state.time_spent]
- **Financial Cost:** [From user_requirements.json: business.current_state.costs]
- **Opportunity Cost:** [Calculated business value loss]

**Impact of Inaction:**
- Continue spending [X hours/week] on manual processes
- Miss opportunity for $[Y/year] in savings/revenue
- [Other strategic impacts from requirements]

---

### Proposed Solution

**Solution Overview:**  
[From user_requirements.json: use_case.summary]

**How It Works:**  
[From user_requirements.json: use_case.workflow_steps]

**Core Capabilities:**  
[From user_requirements.json: technical.functional_requirements - must_have items]

**User Experience:**  
[From user_requirements.json: use_case.user_experience_goals]

**Multi-Agent Architecture (if applicable):**  
[From design_decisions.json: architecture_design - if multi-agent, describe each agent's role]

---

## Technical Approach

### Architecture Overview

**System Diagram:**  
[From design_decisions.json: architecture_design.diagram_code]

[Include the actual diagram in chosen format]

**Key Components:**  
[From design_decisions.json: architecture_design.key_components]

**Data Flows:**  
[From design_decisions.json: architecture_design.data_flows]

**Architecture Rationale:**  
[From design_decisions.json: architecture_design.diagram_description]

---

### Technology Stack

**Selected Technologies:**  
[From design_decisions.json: tech_stack.primary_stack]

**LLM Platform:**
- Provider: [tech_stack.llm_platform.provider]
- Models: [tech_stack.llm_platform.models]
- Rationale (Technical): [tech_stack.llm_platform.rationale_technical]
- Rationale (Business): [tech_stack.llm_platform.rationale_business]
- Cost: [tech_stack.llm_platform.cost_per_million_tokens]

**Backend:**
- Language: [tech_stack.backend.language]
- Framework: [tech_stack.backend.framework]
- Rationale: [tech_stack.backend.rationale]

**Frontend:**
- Framework: [tech_stack.frontend.framework]
- Type: [tech_stack.frontend.type]
- Rationale: [tech_stack.frontend.rationale]

**Infrastructure:**
- Cloud: [tech_stack.infrastructure.cloud_provider]
- Compute: [tech_stack.infrastructure.compute]
- Monitoring: [tech_stack.infrastructure.monitoring]
- Rationale: [tech_stack.infrastructure.rationale]

**Alternative Stacks Considered:**  
[From design_decisions.json: tech_stack.alternative_stacks]
- [Why not selected]

---

### AWS Well-Architected Alignment

[From design_decisions.json: tech_stack.well_architected_alignment]

**Operational Excellence:** [Description]  
**Security:** [Description]  
**Reliability:** [Description]  
**Performance Efficiency:** [Description]  
**Cost Optimization:** [Description]  
**Sustainability:** [Description]

**GenAI Lens Compliance:** [From architecture_design.genai_considerations]

---

## Project Plan

### Implementation Approach

**Methodology:** [From design_decisions.json: project_plan.implementation_approach]

### Phased Roadmap

**Phase 1: MVP** ([From design_decisions.json: project_plan.phased_roadmap.phase_1_mvp.duration_weeks] weeks)
- **Objectives:** [project_plan.phased_roadmap.phase_1_mvp.objectives]
- **Deliverables:** [project_plan.phased_roadmap.phase_1_mvp.deliverables]
- **Success Criteria:** [project_plan.phased_roadmap.phase_1_mvp.success_criteria]
- **Team Allocation:** [project_plan.phased_roadmap.phase_1_mvp.team_allocation]
- **Cost:** $[project_plan.phased_roadmap.phase_1_mvp.cost]

**Phase 2: Enhancement** (if approved after Phase 1)
[Same structure from phase_2_enhancement]

**Phase 3: Scale** (if approved after Phase 2)
[Same structure from phase_3_scale]

---

### Timeline & Milestones

**Total Duration:** [From design_decisions.json: estimates.timeline.total_weeks] weeks  
**Start Date:** [Proposed]  
**End Date:** [Calculated]

**Key Milestones:**  
[From design_decisions.json: estimates.timeline.milestones]

**Critical Path:**  
[From design_decisions.json: project_plan.critical_path]

---

### Team Composition

**Required Roles:**  
[From design_decisions.json: team_composition.required_roles]

| Role | Count | Skills | Allocation | Duration |
|------|-------|--------|------------|----------|
[For each role in team_composition.required_roles]

**Total Team Size:** [From design_decisions.json: team_composition.total_team_size]  
**Total FTEs:** [From design_decisions.json: team_composition.total_ftes]

**Hiring Needs:**  
[From design_decisions.json: team_composition.hiring_needs]

**Training Requirements:**  
[From design_decisions.json: team_composition.training_requirements]

---

## Financial Investment

### Cost Breakdown

**Development Costs:**
- Internal Team: $[From design_decisions.json: costs.development_costs.internal_team.total]
- External Contractors: $[costs.development_costs.external_contractors.total]
- Recruitment: $[costs.development_costs.recruitment_costs]
- Training: $[costs.development_costs.training_costs]
- **Total Development:** $[costs.development_costs.total_development]

**Infrastructure Costs (Year 1):**
- Cloud Compute: $[costs.infrastructure_costs.cloud_compute.first_year]
- LLM API Usage: $[costs.infrastructure_costs.llm_api_usage.first_year]
- Storage & Database: $[costs.infrastructure_costs.cloud_storage.first_year]
- Monitoring: $[costs.infrastructure_costs.monitoring_observability.first_year]
- **Total Infrastructure:** $[costs.infrastructure_costs.total_infrastructure_first_year]

**Third-Party Costs (Year 1):**
- Tools & Licenses: $[costs.third_party_costs.tools_licenses.first_year]
- SaaS Services: $[costs.third_party_costs.saas_services.first_year]
- **Total Third-Party:** $[costs.third_party_costs.total_third_party_first_year]

---

### Total Cost of Ownership (TCO)

| Year | Development | Infrastructure | Third-Party | Total |
|------|-------------|----------------|-------------|-------|
| Year 1 | $[Development one-time] | $[Infrastructure Y1] | $[Third-party Y1] | $[TCO Y1] |
| Year 2 | $0 | $[Infrastructure Y2] | $[Third-party Y2] | $[TCO Y2] |
| Year 3 | $0 | $[Infrastructure Y3] | $[Third-party Y3] | $[TCO Y3] |
| **3-Year Total** | | | | **$[3-year TCO]** |

[From design_decisions.json: costs.total_cost_of_ownership]

---

### ROI Projections

**Expected Benefits:**
- Annual Savings: $[From costs.roi_projections.expected_annual_savings]
- Revenue Increase: $[From costs.roi_projections.expected_annual_revenue_increase]
- Payback Period: [From costs.roi_projections.payback_period_months] months
- 3-Year ROI: [From costs.roi_projections.roi_percentage_3yr]%

**Cost Optimization Recommendations:**  
[From design_decisions.json: costs.cost_optimization_recommendations]

---

## Risk Assessment & Mitigation

### Technical Risks

[From design_decisions.json: risks_and_mitigation.technical_risks]

| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan |
|------|--------|-------------|---------------------|------------------|
[For each technical risk]

### Business Risks

[From design_decisions.json: risks_and_mitigation.business_risks]

| Risk | Impact | Probability | Mitigation Strategy | Contingency Plan |
|------|--------|-------------|---------------------|------------------|
[For each business risk]

### Overall Risk Rating

**Risk Level:** [From design_decisions.json: risks_and_mitigation.overall_risk_rating]

**Risk Management Approach:**  
[From design_decisions.json: risks_and_mitigation.risk_management_approach]

---

## Success Criteria

### Technical Success Metrics

[From user_requirements.json: business.success_metrics.kpis - technical]
[From design_decisions.json: project_plan.success_criteria_and_kpis.technical_kpis]

- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

### Business Success Metrics

[From user_requirements.json: business.success_metrics.kpis - business]
[From design_decisions.json: project_plan.success_criteria_and_kpis.business_kpis]

- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

### Measurement Approach

[From design_decisions.json: project_plan.success_criteria_and_kpis.measurement_approach]

---

## Decision Framework for Executives

### Approve if:
✅ ROI > 3x over 3 years ([Actual ROI]%)  
✅ Payback < 18 months ([Actual payback] months)  
✅ Costs fit budget ($[Total] vs. $[Budget from system_config])  
✅ Aligns with strategic priority ([From system_config: strategic_priority])  
✅ Risks mitigated ([From design_decisions: all HIGH risks have mitigations])  
✅ Team can deliver ([From team_composition: skills vs. gaps])

### Conditional Approval if:
⚠️ ROI 2-3x (recommend phased approach)  
⚠️ Payback 18-24 months (validate assumptions)  
⚠️ Budget stretch <20% (consider contingency)  
⚠️ Some skill gaps (hiring/training plan required)

### Reject if:
❌ ROI < 2x  
❌ Payback > 24 months  
❌ Costs exceed budget by >20%  
❌ Critical unmitigated risks  
❌ Strategic misalignment

---

## Recommendation

**[GO / Conditional GO / NO-GO]**

[From design_decisions.json: executive_summary.go_no_go_recommendation]

**Rationale:**  
[From executive_summary with supporting evidence from requirements and decisions]

**Conditions (if Conditional GO):**
- [Condition 1]
- [Condition 2]

**Next Steps (if approved):**
1. Executive approval and budget allocation
2. Team mobilization (hiring if needed)
3. Engineering Agent begins prototype development
4. Weekly status updates to [stakeholders from system_config]
5. Prototype demo in [X weeks]

---

## Approval Signatures

**Technical Approval:**  
[CTO/VP Engineering from system_config.stakeholders.decision_makers]

**Budget Approval:**  
[CFO/Finance from system_config.stakeholders.decision_makers]

**Business Approval:**  
[CEO/Business Leader from system_config.stakeholders.decision_makers]

**Date:** _______________

---

## Appendices

### Appendix A: Detailed Architecture
[Full architecture diagram and component descriptions from design_decisions.json]

### Appendix B: Complete Cost Breakdown
[Detailed cost calculations from design_decisions.json: costs section]

### Appendix C: Risk Registry
[Complete risk list with detailed mitigation from design_decisions.json]

### Appendix D: Project Plan Details
[Full project plan from design_decisions.json: project_plan]

---

**Proposal Generated:** [Timestamp]  
**Assembled by:** Architecture Agent  
**Knowledge Base Version:** [From _metadata in JSON files]
```

---

## Success Criteria

Implementation proposal is successful when:

✅ **Reads from knowledge base** (no manual architecture duplication)  
✅ **Dual-audience format** (executive summary + technical details)  
✅ **Clear recommendation** (GO/Conditional/NO-GO with rationale)  
✅ **Complete financial picture** (development + infrastructure + TCO + ROI)  
✅ **Risk mitigation** (all high-impact risks addressed)  
✅ **Actionable** (clear next steps if approved)  
✅ **Decision-ready** (executives have all information needed)

---

## Notes for Architecture Agent

**This is a USER PROMPT for assembly only. Do NOT:**
- Re-do tech stack selection (READ from design_decisions.json)
- Re-calculate costs (READ from design_decisions.json)
- Re-estimate timeline (READ from design_decisions.json)
- Redesign architecture (READ from design_decisions.json)

**Do:**
- READ all data from knowledge base
- ASSEMBLE into executive proposal format
- ADD proposal-specific content (approval section, decision framework)
- TRANSLATE technical details to business impact where needed
- FORMAT for dual-audience (executive summary + technical appendices)

**Focus:** Assembly, translation, and presentation—not re-analysis.

---

**Version:** 0.1  
**Last Updated:** 2025-10-03  
**Purpose:** Assembly-only proposal generation from knowledge base  
**Target Audience:** Executives (CEOs, CFOs, CTOs, VPs) + Technical Leaders
