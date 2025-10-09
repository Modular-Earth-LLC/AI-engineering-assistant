# Team Composition Generation User Prompt

**Phase:** Solution Architecture  
**Purpose:** Determine ideal team structure, skill requirements, and hiring priorities for AI startup or product team  
**Agent:** team-architect-agent  

---

## Prompt Template

I need to build the right team for my AI-driven product. Here are the project details:

**Product Requirements:**
- Product type: [WEB_APP / MOBILE_APP / API / DESKTOP_APP]
- AI capabilities: [AI_FEATURES_TO_IMPLEMENT]
- Technology stack: [SELECTED_TECH_STACK]
- Target launch: [LAUNCH_DATE]

**Current Team:**
- [ROLE]: [NUMBER] people - [CURRENT_SKILLS]
- [ROLE]: [NUMBER] people - [CURRENT_SKILLS]
- [ROLE]: [NUMBER] people - [CURRENT_SKILLS]

**Constraints:**
- Budget: [MONTHLY_TEAM_BUDGET]
- Timeline: [HIRING_TIMELINE]
- Location: [REMOTE / HYBRID / ONSITE]
- Company stage: [STARTUP / GROWTH / ENTERPRISE]

**Business Context:**
- Company size: [NUMBER_OF_EMPLOYEES]
- Funding stage: [BOOTSTRAP / SEED / SERIES_A / LATER]
- Growth stage: [MVP / PRODUCT_MARKET_FIT / SCALING]
- Market: [B2B / B2C / B2B2C]

Please provide:
1. Ideal team structure and roles
2. Required skills for each role
3. Hiring priorities and timeline
4. Budget allocation recommendations
5. Team scaling strategy

---

## Expected Outputs

The team-architect-agent should deliver:

1. **Team Structure**
   - **Core Team (MVP):** [ROLES_AND_COUNT]
   - **Extended Team (Growth):** [ROLES_AND_COUNT]
   - **Future Team (Scale):** [ROLES_AND_COUNT]

2. **Role Specifications**
   - **Role:** [TITLE]
     - **Responsibilities:** [KEY_TASKS]
     - **Required Skills:** [TECHNICAL_SKILLS]
     - **Preferred Experience:** [YEARS_AND_BACKGROUND]
     - **Salary Range:** [COMPENSATION_RANGE]
     - **Hiring Priority:** [HIGH / MEDIUM / LOW]

3. **Hiring Timeline**
   - **Month 1:** [ROLES_TO_HIRE]
   - **Month 2:** [ROLES_TO_HIRE]
   - **Month 3:** [ROLES_TO_HIRE]
   - **Month 6:** [ROLES_TO_HIRE]

4. **Budget Allocation**
   - **Engineering (70%):** [BUDGET_AMOUNT]
   - **Product (15%):** [BUDGET_AMOUNT]
   - **Design (10%):** [BUDGET_AMOUNT]
   - **DevOps (5%):** [BUDGET_AMOUNT]

5. **Team Scaling Strategy**
   - **Phase 1 (0-6 months):** [TEAM_SIZE_AND_FOCUS]
   - **Phase 2 (6-18 months):** [TEAM_SIZE_AND_FOCUS]
   - **Phase 3 (18+ months):** [TEAM_SIZE_AND_FOCUS]

---

## Essential Roles for AI Products

### Core Engineering Team

#### AI/ML Engineer
**Responsibilities:**
- Design and implement AI models
- Integrate LLM APIs and vector databases
- Build AI agent orchestration systems
- Optimize model performance and costs

**Required Skills:**
- Python, LangChain, LlamaIndex
- Experience with OpenAI, Anthropic, or similar
- Vector databases (Pinecone, Weaviate)
- MLOps and model deployment

**Hiring Priority:** HIGH (Critical for AI products)

#### Full-Stack Developer
**Responsibilities:**
- Build user interfaces and APIs
- Integrate AI capabilities into applications
- Implement real-time features
- Optimize application performance

**Required Skills:**
- React/Vue.js, Node.js/Python
- RESTful APIs and GraphQL
- Database design (PostgreSQL, MongoDB)
- Cloud platforms (AWS, GCP, Azure)

**Hiring Priority:** HIGH (Core product development)

#### Backend Developer
**Responsibilities:**
- Design scalable backend architecture
- Implement data processing pipelines
- Build API integrations
- Ensure system reliability and security

**Required Skills:**
- Python/Node.js/Go
- Database optimization
- API design and microservices
- Cloud infrastructure

**Hiring Priority:** HIGH (System foundation)

### Specialized Roles

#### AI Product Manager
**Responsibilities:**
- Define AI product strategy
- Prioritize AI features and capabilities
- Coordinate between technical and business teams
- Measure AI product success metrics

**Required Skills:**
- AI/ML product experience
- Technical background
- User research and analytics
- Cross-functional collaboration

**Hiring Priority:** MEDIUM (After MVP)

#### DevOps Engineer
**Responsibilities:**
- Set up CI/CD pipelines
- Manage cloud infrastructure
- Implement monitoring and logging
- Ensure security and compliance

**Required Skills:**
- Docker, Kubernetes
- Cloud platforms (AWS/GCP/Azure)
- Infrastructure as Code
- Security best practices

**Hiring Priority:** MEDIUM (Before production)

#### Data Engineer
**Responsibilities:**
- Design data pipelines
- Implement data quality checks
- Build data warehouses
- Optimize data processing

**Required Skills:**
- Python, SQL
- Data pipeline tools (Airflow, dbt)
- Data warehouses (Snowflake, BigQuery)
- ETL/ELT processes

**Hiring Priority:** LOW (After significant data growth)

### Supporting Roles

#### UX/UI Designer
**Responsibilities:**
- Design AI-powered user interfaces
- Create intuitive AI interaction patterns
- Conduct user research
- Prototype and test designs

**Required Skills:**
- Figma, Sketch, Adobe Creative Suite
- User research methods
- AI/ML interface design experience
- Prototyping tools

**Hiring Priority:** MEDIUM (Early for user experience)

#### QA Engineer
**Responsibilities:**
- Test AI model accuracy and performance
- Implement automated testing
- Ensure product quality
- Test integrations and edge cases

**Required Skills:**
- Testing frameworks (Jest, Pytest)
- AI model testing experience
- API testing tools
- Performance testing

**Hiring Priority:** LOW (Before production)

---

## Team Composition by Company Stage

### Startup (0-10 employees)
**Core Team (4-6 people):**
- 1 AI/ML Engineer (Lead)
- 2 Full-Stack Developers
- 1 Product Manager (Founder/CEO)
- 1 Designer (Part-time/Contract)

**Focus:** MVP development, rapid iteration

### Growth (10-50 employees)
**Extended Team (8-15 people):**
- 2-3 AI/ML Engineers
- 3-4 Full-Stack Developers
- 1 Backend Developer
- 1 DevOps Engineer
- 1 AI Product Manager
- 1 Designer
- 1 QA Engineer

**Focus:** Product-market fit, scaling features

### Scale (50+ employees)
**Full Team (15+ people):**
- 4-6 AI/ML Engineers
- 6-8 Full-Stack Developers
- 2-3 Backend Developers
- 2 DevOps Engineers
- 1 Data Engineer
- 2 Product Managers
- 2 Designers
- 2 QA Engineers
- 1 AI Research Scientist

**Focus:** Market leadership, advanced AI features

---

## Hiring Strategies

### Immediate Hires (Month 1)
1. **Senior AI/ML Engineer** - Lead technical AI implementation
2. **Full-Stack Developer** - Build core product features
3. **Product Manager** - Define product strategy and roadmap

### Short-term Hires (Months 2-3)
1. **Backend Developer** - Scale system architecture
2. **DevOps Engineer** - Production infrastructure
3. **UX Designer** - User experience optimization

### Medium-term Hires (Months 4-6)
1. **Additional AI/ML Engineer** - Advanced AI features
2. **QA Engineer** - Quality assurance
3. **Data Engineer** - Data infrastructure

### Long-term Hires (6+ months)
1. **AI Research Scientist** - Cutting-edge AI capabilities
2. **Additional Product Manager** - Feature specialization
3. **Engineering Manager** - Team leadership

---

## Budget Considerations

### Salary Ranges (US Market)
- **AI/ML Engineer:** $120k-200k
- **Full-Stack Developer:** $80k-150k
- **Backend Developer:** $90k-160k
- **DevOps Engineer:** $100k-170k
- **Product Manager:** $100k-180k
- **Designer:** $70k-130k
- **QA Engineer:** $70k-120k

### Total Team Budget (Monthly)
- **Startup (6 people):** $50k-80k
- **Growth (12 people):** $100k-160k
- **Scale (20 people):** $180k-300k

### Cost Optimization Strategies
- **Remote-first hiring** - Access global talent pool
- **Contractors for specialized roles** - Reduce fixed costs
- **Equity compensation** - Align incentives
- **Internship programs** - Develop junior talent

---

## Success Metrics

A successful team composition should result in:

- ✅ Right mix of technical skills for AI product
- ✅ Realistic hiring timeline and budget
- ✅ Clear role definitions and responsibilities
- ✅ Scalable team structure for growth
- ✅ Strong culture and collaboration

---

This prompt ensures optimal team building that balances technical expertise, business needs, and resource constraints for AI-driven products.


