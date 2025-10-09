# Testing Strategy - User Prompt

**Phase:** Deployment / Quality Assurance  
**Purpose:** Create comprehensive testing approach for AI system prototypes  
**Agent:** Deployment Agent  
**Input:** `outputs/prototypes/[project-name]/`, `knowledge_base/user_requirements.json`  
**Output:** Test plans, test cases, UAT scenarios  
**Duration:** 2-4 hours

---

## Purpose

Develop systematic testing strategies that validate AI system functionality, performance, and user experience. This ensures prototypes are ready for stakeholder evaluation and identifies issues before production deployment.

---

## When to Use This Prompt

**Prerequisites:**
- ✅ Prototype development complete
- ✅ Functional requirements documented in `user_requirements.json`
- ✅ Demo scenarios identified

**Best for:**
- Pre-deployment validation
- User acceptance testing (UAT) preparation
- Regression testing after changes
- Performance benchmarking

---

## Instructions for Deployment Agent

### Phase 1: Test Coverage Analysis (30 minutes)

```
<thinking>
1. Read user_requirements.json → functional_requirements
2. Read prototype README → implemented features
3. Identify test coverage needs:
   - Functional requirements: [COUNT] to test
   - Integration points: [COUNT] to test
   - User workflows: [COUNT] to test
   - Edge cases: [IDENTIFIED]
   
4. Determine test types needed:
   - Unit tests: [YES/NO, COUNT]
   - Integration tests: [YES/NO, COUNT]
   - End-to-end tests: [YES/NO, COUNT]
   - Performance tests: [YES/NO]
   - UAT scenarios: [YES/NO, COUNT]
</thinking>

✅ **Test Coverage Analysis Complete**

**Requirements to Test:** [COUNT] functional requirements  
**User Workflows:** [COUNT] workflows to validate  
**Integration Points:** [COUNT] external integrations  
**Edge Cases Identified:** [COUNT]

**Test Types Needed:**
- ✅ Unit Tests: [COUNT] tests
- ✅ Integration Tests: [COUNT] tests
- ✅ End-to-End Tests: [COUNT] workflows
- ✅ UAT Scenarios: [COUNT] stakeholder test cases
- ✅ Performance Tests: [Latency, throughput benchmarks]

Beginning test plan generation...
```

---

### Phase 2: Unit Test Plan (30 minutes)

For code-based prototypes, generate unit test specifications:

```
✅ **Unit Test Plan Generated**

**File:** `outputs/prototypes/[project-name]/tests/TEST_PLAN_UNIT.md`

## Unit Tests - [Project Name]

### Purpose
Validate individual components and functions work correctly in isolation.

### Test Framework
- **Language:** [Python / Node.js / etc.]
- **Framework:** [pytest / jest / etc.]
- **Coverage Target:** 70%+ (80%+ for critical paths)

### Tests by Component

#### Component: LLM Integration (`src/utils/llm_client`)

**Test 1: API Connection**
- Test ID: UT-001
- Description: Verify LLM API connection and authentication
- Input: Valid API key
- Expected: Successful connection, no errors
- Priority: Critical

**Test 2: Prompt Submission**
- Test ID: UT-002
- Description: Verify prompts are sent correctly
- Input: Sample prompt text
- Expected: Response received, proper format
- Priority: Critical

**Test 3: Error Handling - Invalid API Key**
- Test ID: UT-003
- Description: Verify graceful handling of auth errors
- Input: Invalid API key
- Expected: Clear error message, no crash
- Priority: High

**Test 4: Error Handling - Rate Limiting**
- Test ID: UT-004
- Description: Verify retry logic on rate limits
- Input: Rapid consecutive requests
- Expected: Exponential backoff, eventual success
- Priority: Medium

#### Component: Agent Orchestration (`src/agents/supervisor`)

**Test 5: Agent Routing**
- Test ID: UT-005
- Description: Verify correct agent selection based on input
- Input: Various user queries
- Expected: Correct agent invoked for each query type
- Priority: Critical

[... more tests per component]

### Running Unit Tests

**Commands:**
- Run test suite with verbose output
- Generate coverage reports (HTML format)
- Target specific test directories

### Coverage Requirements
- **Critical paths:** 90%+ coverage
- **Integration logic:** 80%+ coverage
- **Utility functions:** 70%+ coverage
- **Overall:** 75%+ coverage
```

---

### Phase 3: Integration Test Plan (45 minutes)

Test how components work together:

```
✅ **Integration Test Plan Generated**

**File:** `outputs/prototypes/[project-name]/tests/TEST_PLAN_INTEGRATION.md`

## Integration Tests - [Project Name]

### Purpose
Validate that system components interact correctly and data flows as expected.

### Test Scenarios

#### Scenario 1: Agent-to-LLM Communication

**Test ID:** IT-001  
**Description:** Verify agent can successfully communicate with LLM API  
**Components:** Agent → LLM Client → External API  
**Priority:** Critical

**Steps:**
1. Initialize agent with configuration
2. Send test prompt through agent
3. Verify prompt reaches LLM API
4. Verify response returns to agent
5. Verify response is processed correctly

**Input:**
```
User query: "Generate a financial report"
```

**Expected Output:**
- LLM API called with correct parameters
- Response received within 5 seconds
- Response formatted appropriately
- Agent state updated

**Pass Criteria:**
- ✅ No errors or exceptions
- ✅ Response time < 5 seconds
- ✅ Response format matches schema
- ✅ Agent state persisted correctly

---

#### Scenario 2: Knowledge Base Access

**Test ID:** IT-002  
**Description:** Verify agents can read from and write to knowledge base  
**Components:** Agent → Knowledge Base → File System / Database  
**Priority:** Critical

**Steps:**
1. Agent reads existing knowledge base data
2. Agent processes user query using KB data
3. Agent writes results back to KB
4. Verify data integrity maintained

**Input:**
```
Query requiring KB data: "What is the current budget?"
```

**Expected Output:**
- KB data successfully retrieved
- Data used in LLM prompt context
- New data written to KB
- JSON schema maintained

**Pass Criteria:**
- ✅ Read operations successful
- ✅ Data correctly incorporated in prompt
- ✅ Write operations successful
- ✅ No data corruption

---

#### Scenario 3: Multi-Agent Coordination

**Test ID:** IT-003  
**Description:** Verify supervisor agent correctly routes to worker agents  
**Components:** Supervisor → Worker Agents → LLM API  
**Priority:** High

**Steps:**
1. User submits query requiring multiple agents
2. Supervisor analyzes intent
3. Supervisor routes to appropriate worker agent(s)
4. Worker agents execute and return results
5. Supervisor aggregates and presents results

**Input:**
```
Complex query: "Analyze expenses and generate invoice"
```

**Expected Output:**
- Supervisor correctly identifies need for 2 agents
- Analytics agent processes expense analysis
- Operations agent generates invoice
- Results combined coherently

**Pass Criteria:**
- ✅ Correct agents invoked
- ✅ Proper execution order
- ✅ Context maintained between agents
- ✅ Results aggregated correctly

---

#### Scenario 4: Error Recovery

**Test ID:** IT-004  
**Description:** Verify system handles errors gracefully across components  
**Components:** All components  
**Priority:** High

**Steps:**
1. Simulate LLM API failure
2. Verify agent error handling
3. Verify user receives clear error message
4. Verify system state remains stable

**Input:**
```
Normal query: "Help me with budgeting"
Injected error: LLM API timeout
```

**Expected Output:**
- Error detected at LLM client level
- Retry logic attempted (3 retries)
- Graceful failure after retries exhausted
- Clear error message to user
- System remains operational

**Pass Criteria:**
- ✅ No system crashes
- ✅ Retry logic executes
- ✅ User-friendly error message
- ✅ System recoverable for next request

[... more integration scenarios]

### Running Integration Tests

**Commands:**
- Run integration test suite
- Include slow tests (marked appropriately)
- Use integration-specific test runners

---

### Phase 4: End-to-End Test Plan (1 hour)

Test complete user workflows:

```
✅ **End-to-End Test Plan Generated**

**File:** `outputs/prototypes/[project-name]/tests/TEST_PLAN_E2E.md`

## End-to-End Tests - [Project Name]

### Purpose
Validate complete user workflows from start to finish, simulating real user interactions.

### E2E Test Scenarios

#### Workflow 1: [Primary Use Case - Example: Generate Financial Report]

**Test ID:** E2E-001  
**User Persona:** [Primary user type]  
**Workflow:** Complete financial report generation  
**Duration:** ~5 minutes  
**Priority:** Critical

**Prerequisites:**
- System deployed and accessible
- Knowledge base populated with sample data
- User authenticated (if applicable)

**Steps:**

1. **User accesses system**
   - Action: Open application URL or launch CLI
   - Expected: Welcome screen displayed, system ready
   - Validation: ✅ UI/CLI loads without errors

2. **User initiates request**
   - Action: Enter "Generate monthly financial report for October"
   - Expected: System acknowledges request, begins processing
   - Validation: ✅ Loading indicator shown

3. **System processes request**
   - Action: Agent analyzes intent
   - Expected: Correct agent(s) invoked
   - Validation: ✅ (Internal) Correct routing logic

4. **System retrieves data**
   - Action: Agent queries knowledge base for October data
   - Expected: Relevant financial data retrieved
   - Validation: ✅ Data displayed or mentioned in response

5. **System generates report**
   - Action: LLM generates report based on data
   - Expected: Comprehensive financial report created
   - Validation: ✅ Report contains expected sections:
     - Income summary
     - Expense breakdown
     - Net cash flow
     - Insights and recommendations

6. **User reviews report**
   - Action: Report displayed to user
   - Expected: Well-formatted, readable report
   - Validation: ✅ Format is clear and professional

7. **User requests modification**
   - Action: "Can you add a comparison to September?"
   - Expected: Report updated with comparison
   - Validation: ✅ Context maintained, comparison added

8. **User saves report**
   - Action: Click "Save" or "Export"
   - Expected: Report saved as PDF/MD/TXT
   - Validation: ✅ File saved successfully, downloadable

**Success Criteria:**
- ✅ Workflow completes without errors
- ✅ Response time < 30 seconds (excluding LLM generation)
- ✅ Report quality meets requirements
- ✅ Context maintained throughout conversation
- ✅ Export functionality works

**Failure Scenarios to Test:**
- Missing data for requested month
- User interrupts mid-generation
- Export fails due to permissions

---

#### Workflow 2: [Secondary Use Case - Example: Budget Planning]

**Test ID:** E2E-002  
**User Persona:** [Secondary user type]  
**Workflow:** Create budget plan for next quarter  
**Duration:** ~10 minutes  
**Priority:** High

[Similar detailed structure...]

---

#### Workflow 3: [Error Recovery Workflow]

**Test ID:** E2E-003  
**User Persona:** Any user  
**Workflow:** Recover from LLM API failure mid-session  
**Duration:** ~3 minutes  
**Priority:** High

**Steps:**
1. User initiates normal request
2. System begins processing
3. **Inject error:** Simulate LLM API timeout
4. System detects error and attempts retry
5. Retry succeeds or fails gracefully
6. User receives appropriate feedback
7. User can continue with new request

**Success Criteria:**
- ✅ Error doesn't crash system
- ✅ User informed of issue clearly
- ✅ System recovers and remains usable
- ✅ No data loss

### Running E2E Tests

**Manual Testing:**
1. Follow test scripts step-by-step
2. Record observations for each validation point
3. Note any deviations from expected behavior
4. Log screenshots or screen recordings

**Automated (if applicable):**
```bash
# Playwright (Node.js)
npx playwright test tests/e2e/

# Selenium (Python)
pytest tests/e2e/ --headed
```
```

---

### Phase 5: User Acceptance Test (UAT) Scenarios (1 hour)

Create stakeholder-friendly test scenarios:

```
✅ **UAT Scenarios Generated**

**File:** `outputs/prototypes/[project-name]/tests/UAT_SCENARIOS.md`

## User Acceptance Testing - [Project Name]

### Purpose
Enable stakeholders to validate that the system meets business requirements and provides expected value.

### How to Use This Document
1. Stakeholders should attempt each scenario
2. Rate experience: ✅ Pass | ⚠️ Acceptable | ❌ Fail
3. Provide feedback comments
4. Note any unexpected behavior

---

## UAT Scenario 1: [Primary Business Value]

**Business Goal:** [What business need this addresses]  
**User Role:** [Who would do this in real life]  
**Difficulty:** Easy  
**Duration:** 5 minutes

### Story
> As a [USER_ROLE], I need to [ACTION] so that I can [BUSINESS_OUTCOME].

### Instructions

**Step 1:** [User-friendly instruction]
- What to do: [Clear action]
- What you should see: [Expected result in plain language]

**Step 2:** [Next instruction]
- What to do: [Clear action]
- What you should see: [Expected result]

[... more steps]

### Success Looks Like
- [ ] I was able to complete the task without help
- [ ] The system responded quickly (< 30 seconds)
- [ ] The output met my expectations
- [ ] I would use this feature regularly

### Feedback
**Rating:** [ ] Pass | [ ] Acceptable | [ ] Fail

**Comments:**
[Stakeholder writes feedback here]

**Suggestions for Improvement:**
[Stakeholder writes suggestions]

---

## UAT Scenario 2: [Secondary Business Value]

[Similar structure...]

---

## UAT Scenario 3: [Edge Case or Error Handling]

**Business Goal:** Verify system handles problems gracefully  
**User Role:** Any user  
**Difficulty:** Medium  
**Duration:** 3 minutes

### Story
> As a user, when something goes wrong, I need clear information about what happened and how to proceed.

### Instructions

**Step 1:** Try to [ACTION THAT MIGHT FAIL]
- What to do: [Intentionally problematic request]
- What you should see: [Error message, not crash]

**Step 2:** Follow any recovery instructions
- What to do: [Follow system guidance]
- What you should see: [Successful recovery]

### Success Looks Like
- [ ] System didn't crash or freeze
- [ ] Error message was understandable (not technical jargon)
- [ ] I knew what to do next
- [ ] I could continue using the system after the error

[More scenarios...]

---

## Summary Sheet

**Tester Name:** ________________  
**Date:** ________________  
**Overall Impression:** [ ] Excellent | [ ] Good | [ ] Needs Work | [ ] Not Ready

| Scenario | Pass/Fail | Priority Issues |
|----------|-----------|-----------------|
| 1. [Name] | [ ] | |
| 2. [Name] | [ ] | |
| 3. [Name] | [ ] | |

**Would you use this system in your daily work?**  
[ ] Definitely | [ ] Probably | [ ] Maybe | [ ] Probably Not | [ ] Definitely Not

**Most Important Improvements:**
1. ___________________
2. ___________________
3. ___________________
```

---

### Phase 6: Performance Test Plan (30 minutes)

Define performance benchmarks:

```
✅ **Performance Test Plan Generated**

**File:** `outputs/prototypes/[project-name]/tests/TEST_PLAN_PERFORMANCE.md`

## Performance Tests - [Project Name]

### Purpose
Validate system meets performance requirements and identify bottlenecks.

### Performance Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Response Time** | < 5 seconds | Time from user input to first response token |
| **LLM Latency** | < 3 seconds | Time for LLM API to return response |
| **Knowledge Base Query** | < 500ms | Time to read from knowledge base |
| **Throughput** | 10 req/min | Requests processed per minute (single user) |
| **Concurrent Users** | 5 users | Number of simultaneous users supported |
| **Memory Usage** | < 2GB | RAM consumption during operation |
| **Startup Time** | < 10 seconds | Time from launch to ready state |

### Performance Test Scenarios

#### Test 1: Response Time Under Normal Load

**Objective:** Measure typical response times  
**Method:** Send 20 representative queries, record response times

**Queries:**
1. "Generate an invoice for $1500"
2. "Analyze last month's expenses"
3. [... 18 more typical queries]

**Measurements:**
- Min response time: _______
- Max response time: _______
- Average response time: _______
- 95th percentile: _______

**Pass Criteria:** Average < 5 seconds, 95th percentile < 10 seconds

---

#### Test 2: Throughput

**Objective:** Measure requests per minute  
**Method:** Send continuous requests for 5 minutes

**Pass Criteria:** >= 10 requests per minute sustained

---

#### Test 3: Concurrent Users

**Objective:** Test multiple simultaneous users  
**Method:** Simulate 2, 5, 10 concurrent users

**Measurements:**
- 2 users: Avg response time _______
- 5 users: Avg response time _______
- 10 users: Avg response time _______

**Pass Criteria:** 
- 5 concurrent users: < 10 second average response
- Graceful degradation beyond 5 users

---

#### Test 4: Large Data Handling

**Objective:** Test with complex/large inputs  
**Method:** Process large documents, complex queries

**Pass Criteria:** Completes without out-of-memory errors

### Running Performance Tests

**Tools:**
- Apache JMeter (load testing)
- Locust (Python-based load testing)
- `time` command (basic measurement)
- Browser DevTools (network timing)

**Example (simple):**
```bash
# Time a single request
time curl -X POST http://localhost:8000/chat \
  -d '{"message": "Generate report"}'

# Run load test
locust -f tests/performance/load_test.py --host=http://localhost:8000
```
```

---

### Phase 7: Test Documentation Summary (15 minutes)

Create master test summary:

```
✅ **Test Documentation Complete**

**File:** `outputs/prototypes/[project-name]/tests/README.md`

# Testing Guide - [Project Name]

## Overview

This directory contains comprehensive testing documentation for the AI system prototype.

## Test Plans

| Test Type | File | Purpose | Priority |
|-----------|------|---------|----------|
| **Unit Tests** | `TEST_PLAN_UNIT.md` | Component-level validation | Medium |
| **Integration Tests** | `TEST_PLAN_INTEGRATION.md` | Component interaction validation | High |
| **End-to-End Tests** | `TEST_PLAN_E2E.md` | Complete workflow validation | Critical |
| **UAT Scenarios** | `UAT_SCENARIOS.md` | Stakeholder acceptance testing | Critical |
| **Performance Tests** | `TEST_PLAN_PERFORMANCE.md` | Performance benchmarking | Medium |

## Quick Start

### For Developers
```bash
# Run all unit tests
pytest tests/unit/ -v --cov

# Run integration tests
pytest tests/integration/ -v

# Run E2E tests
pytest tests/e2e/ --headed
```

### For Stakeholders
1. Open `UAT_SCENARIOS.md`
2. Follow each scenario step-by-step
3. Rate your experience
4. Provide feedback in document

## Test Coverage

**Current Coverage:** [To be measured]
- Unit tests: [%]
- Integration tests: [%]
- E2E tests: [COUNT] workflows

**Target Coverage:**
- Unit: 75%+
- Integration: 80%+ of integration points
- E2E: All critical user workflows

## Reporting Issues

Found a bug? Document it here:
- **Issue:** [What went wrong]
- **Steps to reproduce:** [How to recreate]
- **Expected:** [What should happen]
- **Actual:** [What actually happened]
- **Priority:** [Critical / High / Medium / Low]

---

**Testing Status:** [READY FOR TESTING / IN PROGRESS / COMPLETE]
```

---

## Success Criteria

Testing strategy is complete when:

✅ **Comprehensive Coverage**
- Unit tests cover key components
- Integration tests cover component interactions
- E2E tests cover critical workflows
- UAT scenarios enable stakeholder validation
- Performance benchmarks defined

✅ **Executable**
- Test plans are clear and actionable
- Stakeholders can run UAT scenarios independently
- Developers can run automated tests easily
- Results are measurable

✅ **Documented**
- All test types documented
- Success criteria defined
- Running instructions provided
- Issue reporting process clear

---

## Next Steps

After creating test strategy:

1. **Execute tests** - Run through each test plan
2. **Document results** - Record pass/fail for each test
3. **Address failures** - Fix bugs identified during testing
4. **Re-test** - Verify fixes work
5. **Stakeholder UAT** - Schedule UAT sessions with stakeholders
6. **Production readiness** - Use test results to assess readiness

---

**Version:** 0.1  
**Last Updated:** 2025-10-04  
**Agent:** Deployment Agent  
**Duration:** 2-4 hours to create comprehensive testing strategy
