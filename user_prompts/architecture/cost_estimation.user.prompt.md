# Project Cost Estimation User Prompt

**Phase:** Solution Architecture  
**Purpose:** Calculate development costs, infrastructure expenses, and resource allocation for realistic budgeting and investor presentations  
**Agent:** cost-estimation-agent  

---

## Prompt Template

I need a comprehensive cost estimation for my AI-driven product development. Here are the project details:

**Product Specifications:**
- Product type: [WEB_APP / MOBILE_APP / API / DESKTOP_APP]
- AI capabilities: [AI_FEATURES_TO_IMPLEMENT]
- Technology stack: [SELECTED_TECH_STACK]
- Target launch: [LAUNCH_DATE]
- Expected users: [TARGET_USER_COUNT]

**Team Composition:**
- [ROLE]: [NUMBER] people × [SALARY] × [DURATION]
- [ROLE]: [NUMBER] people × [SALARY] × [DURATION]
- [ROLE]: [NUMBER] people × [SALARY] × [DURATION]

**Infrastructure Requirements:**
- Cloud provider: [AWS / GCP / AZURE / OTHER]
- Expected traffic: [USERS_PER_MONTH]
- Data storage: [EXPECTED_DATA_SIZE]
- AI model usage: [EXPECTED_API_CALLS]

**Business Context:**
- Company stage: [STARTUP / GROWTH / ENTERPRISE]
- Funding: [BOOTSTRAP / SEED / SERIES_A / LATER]
- Revenue model: [SUBSCRIPTION / FREEMIUM / ONE_TIME / USAGE_BASED]
- Target market: [B2B / B2C / B2B2C]

Please provide:
1. Detailed development cost breakdown
2. Infrastructure and operational costs
3. Third-party service costs
4. Total cost of ownership (TCO)
5. ROI analysis and break-even timeline

---

## Expected Outputs

The cost-estimation-agent should deliver:

1. **Development Costs**
   - **Personnel (70-80%):** [TOTAL_COST]
     - Salaries and benefits
     - Contractor costs
     - Equity compensation
   - **Tools and Software (5-10%):** [TOTAL_COST]
     - Development tools
     - Design software
     - Project management tools
   - **Infrastructure (10-15%):** [TOTAL_COST]
     - Cloud services
     - Development environments
     - Testing infrastructure

2. **Operational Costs (Monthly)**
   - **Cloud Infrastructure:** [MONTHLY_COST]
     - Compute instances
     - Database hosting
     - CDN and storage
     - AI/ML services
   - **Third-party Services:** [MONTHLY_COST]
     - LLM API costs
     - Vector database
     - Authentication services
     - Analytics and monitoring
   - **Team Costs:** [MONTHLY_COST]
     - Ongoing salaries
     - Benefits and taxes
     - Office and equipment

3. **AI-Specific Costs**
   - **LLM API Usage:** [MONTHLY_COST]
     - OpenAI/Anthropic API calls
     - Model fine-tuning
     - Embedding generation
   - **Vector Database:** [MONTHLY_COST]
     - Pinecone/Weaviate hosting
     - Data storage and queries
   - **AI Infrastructure:** [MONTHLY_COST]
     - GPU instances
     - Model hosting
     - Data processing

4. **Total Cost of Ownership (TCO)**
   - **Year 1:** [TOTAL_COST]
   - **Year 2:** [TOTAL_COST]
   - **Year 3:** [TOTAL_COST]
   - **3-Year TCO:** [TOTAL_COST]

5. **ROI Analysis**
   - **Break-even point:** [MONTHS]
   - **Revenue projections:** [YEARLY_REVENUE]
   - **Profit margins:** [PERCENTAGE]
   - **Payback period:** [MONTHS]

---

## Cost Categories Breakdown

### Development Phase Costs

#### Personnel Costs (70-80% of total)
**Core Team:**
- AI/ML Engineer: $150k × 12 months = $180k
- Full-Stack Developer: $120k × 12 months = $144k
- Backend Developer: $130k × 12 months = $156k
- Product Manager: $140k × 12 months = $168k
- Designer: $100k × 12 months = $120k

**Supporting Team:**
- DevOps Engineer: $140k × 6 months = $70k
- QA Engineer: $90k × 6 months = $45k
- Data Engineer: $130k × 3 months = $32.5k

**Total Personnel:** $915.5k

#### Tools and Software (5-10% of total)
**Development Tools:**
- GitHub Enterprise: $21/user/month × 8 users × 12 months = $2k
- Figma Professional: $12/user/month × 3 users × 12 months = $432
- JetBrains IDEs: $200/user/year × 5 users = $1k
- Design tools: $500/month × 12 months = $6k

**AI/ML Tools:**
- Weights & Biases: $50/month × 12 months = $600
- Hugging Face Pro: $9/user/month × 2 users × 12 months = $216
- MLOps platform: $200/month × 12 months = $2.4k

**Total Tools:** $12.2k

#### Infrastructure (10-15% of total)
**Development Infrastructure:**
- AWS/GCP development: $500/month × 12 months = $6k
- CI/CD services: $200/month × 12 months = $2.4k
- Testing environments: $300/month × 12 months = $3.6k
- Security tools: $100/month × 12 months = $1.2k

**Total Infrastructure:** $13.2k

### Operational Phase Costs

#### Cloud Infrastructure (Monthly)
**Compute:**
- Application servers: $200/month
- Database instances: $150/month
- AI/ML inference: $300/month
- Background jobs: $100/month

**Storage:**
- Database storage: $50/month
- File storage: $30/month
- Vector database: $200/month
- Backup storage: $20/month

**Networking:**
- Load balancer: $25/month
- CDN: $40/month
- Data transfer: $30/month

**Total Cloud Infrastructure:** $1,145/month

#### AI/ML Services (Monthly)
**LLM APIs:**
- OpenAI GPT-4: $2,000/month (based on usage)
- Anthropic Claude: $500/month
- Embedding models: $200/month

**Vector Database:**
- Pinecone: $200/month
- Weaviate: $150/month

**AI Infrastructure:**
- Model hosting: $300/month
- Data processing: $100/month

**Total AI/ML Services:** $3,450/month

#### Third-party Services (Monthly)
**Authentication:**
- Auth0: $23/month
- Firebase Auth: $0/month (free tier)

**Analytics:**
- Google Analytics: $0/month (free)
- Mixpanel: $25/month
- DataDog: $100/month

**Communication:**
- SendGrid: $15/month
- Twilio: $50/month

**Total Third-party Services:** $213/month

### Total Monthly Operational Costs
- Cloud Infrastructure: $1,145
- AI/ML Services: $3,450
- Third-party Services: $213
- **Total:** $4,808/month

---

## Cost Optimization Strategies

### Development Phase
1. **Remote Team:** 30% cost reduction through global talent
2. **Contractors:** 20% cost reduction for specialized roles
3. **Open Source:** Use free tools where possible
4. **Cloud Credits:** Leverage startup programs (AWS Activate, GCP for Startups)

### Operational Phase
1. **Auto-scaling:** Reduce costs during low usage
2. **Reserved Instances:** 30-50% savings on predictable workloads
3. **Spot Instances:** 60-90% savings on batch processing
4. **Caching:** Reduce API calls and database queries

### AI-Specific Optimizations
1. **Model Selection:** Use smaller, cheaper models where appropriate
2. **Caching:** Cache common AI responses
3. **Batch Processing:** Process requests in batches
4. **Fine-tuning:** Reduce API calls with custom models

---

## Revenue Projections

### B2B SaaS Model
**Pricing Tiers:**
- Starter: $99/month (100 users)
- Professional: $299/month (1,000 users)
- Enterprise: $999/month (unlimited)

**Year 1 Projections:**
- Month 6: 10 customers × $299 = $2,990/month
- Month 12: 50 customers × $299 = $14,950/month
- Annual Revenue: $107,400

**Year 2 Projections:**
- Month 18: 100 customers × $299 = $29,900/month
- Month 24: 200 customers × $299 = $59,800/month
- Annual Revenue: $538,200

### B2C Freemium Model
**Pricing:**
- Free: $0/month (limited features)
- Premium: $19/month (full features)

**Year 1 Projections:**
- Month 6: 1,000 free + 50 premium = $950/month
- Month 12: 5,000 free + 500 premium = $9,500/month
- Annual Revenue: $62,700

---

## Break-even Analysis

### B2B SaaS Scenario
**Monthly Costs:** $4,808
**Average Revenue per Customer:** $299
**Break-even Customers:** 16 customers
**Break-even Timeline:** Month 8-10

### B2C Freemium Scenario
**Monthly Costs:** $4,808
**Average Revenue per Premium User:** $19
**Break-even Premium Users:** 253 users
**Break-even Timeline:** Month 12-15

---

## Risk Factors

### Cost Overruns
- **AI API costs:** 50-100% higher than estimated
- **Infrastructure scaling:** 30-50% higher than estimated
- **Team expansion:** 20-30% higher than estimated

### Revenue Shortfalls
- **Slower adoption:** 30-50% lower than projected
- **Lower conversion:** 20-40% lower than projected
- **Competition:** 20-30% impact on pricing

### Mitigation Strategies
- **Conservative estimates:** Build 20% buffer
- **Phased approach:** Start with MVP, scale based on revenue
- **Flexible contracts:** Use month-to-month where possible
- **Regular monitoring:** Track costs and revenue weekly

---

## Success Metrics

A successful cost estimation should result in:

- ✅ Realistic development and operational costs
- ✅ Clear understanding of AI-specific expenses
- ✅ Achievable break-even timeline
- ✅ Cost optimization strategies
- ✅ Risk mitigation plans

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Purpose:** Calculate AI system development costs, infrastructure expenses, TCO, and ROI  
**Category:** Architecture Design  
**Agent:** Architecture Agent

---

This prompt ensures comprehensive cost analysis that supports realistic budgeting and investor presentations for AI-driven products.

