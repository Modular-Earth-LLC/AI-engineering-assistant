# Technical Project Plan Generation User Prompt

**Phase:** Solution Architecture  
**Purpose:** Create detailed implementation roadmaps, sprint planning, and risk mitigation strategies for AI product development  
**Agent:** project-planning-agent  

---

## Prompt Template

I need a comprehensive technical project plan for my AI-driven MVP. Here are the project details:

**Project Overview:**

- Product name: [PRODUCT_NAME]
- Product type: [WEB_APP / MOBILE_APP / API / DESKTOP_APP]
- Target launch: [LAUNCH_DATE]
- Team size: [NUMBER_OF_DEVELOPERS]

**Technical Requirements:**

- Technology stack: [SELECTED_TECH_STACK]
- AI capabilities: [AI_FEATURES_TO_IMPLEMENT]
- Integration requirements: [EXTERNAL_APIS / SERVICES]
- Performance targets: [RESPONSE_TIME / UPTIME / SCALE]

**Team Composition:**

- [ROLE]: [NUMBER] developers with [EXPERIENCE_LEVEL] experience
- [ROLE]: [NUMBER] developers with [EXPERIENCE_LEVEL] experience
- [ROLE]: [NUMBER] developers with [EXPERIENCE_LEVEL] experience

**Constraints:**

- Budget: [TOTAL_BUDGET]
- Timeline: [TOTAL_DURATION]
- Risk tolerance: [LOW / MEDIUM / HIGH]
- Quality requirements: [MINIMUM_VIABLE / PRODUCTION_READY]

Please provide:

1. Detailed project timeline with milestones
2. Sprint planning with deliverables
3. Resource allocation and dependencies
4. Risk assessment and mitigation strategies
5. Quality assurance and testing plan

---

## Expected Outputs

The project-planning-agent should deliver:

1. **Project Timeline**
   - **Phase 1 (Foundation):** [DURATION] - [KEY_DELIVERABLES]
   - **Phase 2 (Core Development):** [DURATION] - [KEY_DELIVERABLES]
   - **Phase 3 (AI Integration):** [DURATION] - [KEY_DELIVERABLES]
   - **Phase 4 (Testing & Polish):** [DURATION] - [KEY_DELIVERABLES]
   - **Phase 5 (Launch):** [DURATION] - [KEY_DELIVERABLES]

2. **Sprint Planning**
   - **Sprint 1-2:** [FEATURES] - [ESTIMATED_EFFORT]
   - **Sprint 3-4:** [FEATURES] - [ESTIMATED_EFFORT]
   - **Sprint 5-6:** [FEATURES] - [ESTIMATED_EFFORT]
   - **Sprint 7-8:** [FEATURES] - [ESTIMATED_EFFORT]

3. **Resource Allocation**
   - **Frontend Development:** [DEVELOPER] - [HOURS/WEEK] - [TASKS]
   - **Backend Development:** [DEVELOPER] - [HOURS/WEEK] - [TASKS]
   - **AI/ML Development:** [DEVELOPER] - [HOURS/WEEK] - [TASKS]
   - **DevOps/Infrastructure:** [DEVELOPER] - [HOURS/WEEK] - [TASKS]

4. **Risk Assessment**
   - **Technical Risks:** [RISK] - [PROBABILITY] - [IMPACT] - [MITIGATION]
   - **Resource Risks:** [RISK] - [PROBABILITY] - [IMPACT] - [MITIGATION]
   - **Timeline Risks:** [RISK] - [PROBABILITY] - [IMPACT] - [MITIGATION]
   - **External Risks:** [RISK] - [PROBABILITY] - [IMPACT] - [MITIGATION]

5. **Quality Assurance Plan**
   - **Testing Strategy:** [UNIT / INTEGRATION / E2E / AI_MODEL]
   - **Code Quality:** [REVIEW_PROCESS / STANDARDS / TOOLS]
   - **Performance Testing:** [LOAD / STRESS / AI_RESPONSE_TIME]
   - **Security Testing:** [VULNERABILITY / PENETRATION / AI_SAFETY]

---

## Project Phases Breakdown

### Phase 1: Foundation (Weeks 1-2)

**Objectives:**

- Set up development environment
- Initialize project structure
- Configure CI/CD pipeline
- Set up basic infrastructure

**Deliverables:**

- Project repository with proper structure
- Development environment documentation
- Basic CI/CD pipeline
- Infrastructure provisioning scripts

### Phase 2: Core Development (Weeks 3-6)

**Objectives:**

- Implement core business logic
- Build user interface
- Set up database and APIs
- Implement authentication

**Deliverables:**

- Core application functionality
- User interface (web/mobile)
- RESTful API endpoints
- User authentication system

### Phase 3: AI Integration (Weeks 7-10)

**Objectives:**

- Integrate AI/ML capabilities
- Implement AI agent workflows
- Set up vector databases
- Build AI orchestration layer

**Deliverables:**

- AI agent implementations
- Vector database integration
- AI orchestration system
- AI model evaluation framework

### Phase 4: Testing & Polish (Weeks 11-12)

**Objectives:**

- Comprehensive testing
- Performance optimization
- Security hardening
- User experience refinement

**Deliverables:**

- Test suite with high coverage
- Performance benchmarks
- Security audit report
- Polished user experience

### Phase 5: Launch (Weeks 13-14)

**Objectives:**

- Production deployment
- Monitoring setup
- User onboarding
- Launch preparation

**Deliverables:**

- Production-ready application
- Monitoring and alerting
- User documentation
- Launch announcement

---

## Risk Mitigation Strategies

### Technical Risks

- **AI Model Performance:** Implement A/B testing and fallback mechanisms
- **Integration Failures:** Build robust error handling and retry logic
- **Scalability Issues:** Design for horizontal scaling from the start
- **Data Quality:** Implement data validation and cleaning pipelines

### Resource Risks

- **Key Developer Unavailable:** Cross-train team members and document processes
- **Skill Gaps:** Provide training and consider external consultants
- **Budget Overruns:** Implement cost monitoring and regular budget reviews
- **Scope Creep:** Maintain strict change control and regular scope reviews

### Timeline Risks

- **AI Development Delays:** Start AI work early and have fallback plans
- **Integration Complexity:** Prototype integrations early
- **Testing Bottlenecks:** Implement automated testing from day one
- **External Dependencies:** Identify and mitigate third-party risks

---

## Success Metrics

A successful project plan should result in:

- ✅ Realistic timeline with achievable milestones
- ✅ Clear resource allocation and dependencies
- ✅ Comprehensive risk mitigation strategies
- ✅ Quality assurance plan with measurable outcomes
- ✅ Contingency plans for major risks

---

This prompt ensures comprehensive project planning that balances ambition with realism for AI-driven product development.

