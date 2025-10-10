# Tech Stack Generation User Prompt

**Phase:** Solution Architecture  
**Purpose:** Select optimal AI frameworks, cloud platforms, and development tools aligned with requirements and team capabilities  
**Agent:** tech-stack-architect-agent  

---

## Prompt Template

I need to select the optimal technology stack for my AI-driven MVP. Here are the project details:

**Product Requirements:**
- Product type: [WEB_APP / MOBILE_APP / API / DESKTOP_APP]
- Core functionality: [MAIN_FEATURES]
- AI capabilities needed: [AI_USE_CASES]
- Expected user load: [CONCURRENT_USERS / DAILY_USERS]

**Team Capabilities:**
- Team size: [NUMBER_OF_DEVELOPERS]
- Primary languages: [PROGRAMMING_LANGUAGES]
- AI/ML experience: [NOVICE / INTERMEDIATE / EXPERT]
- Cloud experience: [NOVICE / INTERMEDIATE / EXPERT]
- DevOps experience: [NOVICE / INTERMEDIATE / EXPERT]

**Constraints:**
- Budget: [MONTHLY_BUDGET_RANGE or ANNUAL_BUDGET]
- Timeline: [DEVELOPMENT_TIMELINE - weeks/months]
- Compliance requirements: [GDPR / HIPAA / SOC2 / NONE]
- Integration needs: [EXTERNAL_APIS / SERVICES]
- Existing infrastructure: [CURRENT_TECH_STACK if replacing/extending]

**Performance Requirements:**
- Response time: [TARGET_RESPONSE_TIME - e.g., <2 seconds]
- Availability: [UPTIME_REQUIREMENT - e.g., 99.9%]
- Scalability: [EXPECTED_GROWTH_RATE - e.g., 10x in 6 months]
- Data volume: [EXPECTED_DATA_SIZE - e.g., 1TB, 10M records]
- Concurrent users: [EXPECTED_CONCURRENT_USERS]

**Additional Context:**
- Project type: [New system | Feature addition | Integration | Migration]
- Technical complexity: [Low | Medium | High | Very High]
- Strategic importance: [Experimental | Important | Critical]
- Desired tech stack maturity: [Cutting-edge | Modern | Battle-tested]

**Decision Criteria (prioritize):**
1. [e.g., Time to market - must launch quickly]
2. [e.g., Team familiarity - minimize learning curve]
3. [e.g., Cost optimization - minimize infrastructure costs]
4. [e.g., Scalability - prepare for rapid growth]
5. [e.g., Maintainability - long-term support]

Please provide:
1. **Recommended technology stack** with detailed rationale for each choice
2. **Alternative options** with trade-offs analysis (pros/cons)
3. **Cost breakdown** for each stack option (development + infrastructure)
4. **Team readiness assessment** - learning curve and training needs
5. **Risk analysis** - technical risks for each option
6. **Migration/scaling path** - how to evolve from MVP to production scale
7. **Decision matrix** - comparison table across key criteria

---

## Expected Outputs

The tech-stack-architect-agent should deliver:

1. **Primary Technology Stack**
   - **Frontend:** Framework, libraries, build tools
   - **Backend:** Language, framework, API design
   - **AI/ML Platform:** LLM provider, model selection, orchestration
   - **Database:** Primary DB, caching, vector DB (if needed)
   - **Infrastructure:** Cloud provider, deployment, monitoring
   - **DevOps:** CI/CD, containerization, orchestration

2. **Alternative Options**
   - **Option A:** [TECH_STACK] - Pros/Cons
   - **Option B:** [TECH_STACK] - Pros/Cons
   - **Option C:** [TECH_STACK] - Pros/Cons

3. **Cost Analysis**
   - **Development costs:** [ESTIMATED_COST]
   - **Infrastructure costs:** [MONTHLY_COST]
   - **Third-party services:** [MONTHLY_COST]
   - **Total first year:** [TOTAL_COST]

4. **Learning Curve Assessment**
   - **Easy adoption:** [TECHNOLOGIES]
   - **Moderate learning:** [TECHNOLOGIES]
   - **Significant learning:** [TECHNOLOGIES]
   - **Training recommendations:** [RESOURCES]

5. **Implementation Roadmap**
   - **Phase 1 (MVP):** [TECHNOLOGIES_AND_TIMELINE]
   - **Phase 2 (Scale):** [ADDITIONAL_TECHNOLOGIES]
   - **Phase 3 (Production):** [ENTERPRISE_FEATURES]

---

## Technology Categories to Consider

### AI/ML Platforms
- **LLM Providers:** OpenAI, Anthropic, Google, Azure OpenAI
- **Vector Databases:** Pinecone, Weaviate, Chroma, Qdrant
- **ML Frameworks:** LangChain, LlamaIndex, Haystack
- **Model Hosting:** Hugging Face, Replicate, AWS Bedrock

### Backend Technologies
- **Languages:** Python, Node.js, Go, Rust, Java
- **Frameworks:** FastAPI, Django, Express.js, Spring Boot
- **Databases:** PostgreSQL, MongoDB, Redis, Supabase
- **APIs:** REST, GraphQL, gRPC

### Frontend Technologies
- **Frameworks:** React, Vue.js, Angular, Svelte
- **Mobile:** React Native, Flutter, Native iOS/Android
- **Desktop:** Electron, Tauri, Qt

### Cloud Platforms
- **Providers:** AWS, Google Cloud, Azure, Vercel, Railway
- **Services:** Compute, storage, databases, AI services
- **Deployment:** Docker, Kubernetes, Serverless

### DevOps & Monitoring
- **CI/CD:** GitHub Actions, GitLab CI, Jenkins
- **Monitoring:** DataDog, New Relic, Sentry, Grafana
- **Logging:** ELK Stack, Splunk, CloudWatch

---

## Success Criteria

A successful tech stack recommendation should result in:

- ✅ Technologies aligned with team capabilities
- ✅ Cost-effective solution within budget
- ✅ Scalable architecture for future growth
- ✅ Clear implementation roadmap
- ✅ Risk mitigation for technology choices

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Purpose:** AI system technology stack selection with Well-Architected alignment  
**Category:** Architecture Design  
**Agent:** Architecture Agent

---

This prompt ensures technology selection that balances capability, cost, and team expertise for AI-driven products.


