# Week 4 Assignment — AI in Software Engineering
Theme: Building Intelligent Software Solutions

## Submission contents
- Code: `code/*`
- Report: this document (convert to PDF)
- Presentation: demo (not included)

---

## Part 1 — Theoretical Analysis (30%)

### Q1: How AI-driven code generation tools reduce development time and limitations
AI code-completion tools (e.g., GitHub Copilot) speed development by suggesting boilerplate and idiomatic patterns, reducing time spent searching for APIs and writing repetitive code. They accelerate prototyping and help surface common error-handling patterns. Limitations include: incorrect or insecure suggestions, hallucinations, licensing/provenance concerns, over-reliance that may erode deep knowledge, and inability to fully capture project-specific semantics.

### Q2: Supervised vs. unsupervised learning in automated bug detection
Supervised learning uses labeled buggy/non-buggy examples and predicts known bug types effectively when labels are representative. Unsupervised learning (anomaly detection, clustering) surfaces novel or rare issues without labels but often has higher false positive rates and needs human validation.

### Q3: Why bias mitigation is critical for personalization
Personalization affects user experiences. If training data over- or under-represents groups, models can deliver unequal experiences, erode trust, and cause harm. Bias mitigation ensures fairness, legal compliance, and equitable UX.

### Case Study: AIOps in deployment pipelines — Two examples
1. Predictive anomaly detection: ML models analyze deployment metrics to predict rollout failures, enabling proactive halts or checks that reduce downtime.  
2. Intelligent remediation automation: AIOps suggests or auto-executes remediation steps (auto-scaling, rollbacks) based on historical incidents, decreasing MTTR.

---

## Part 2 — Practical Implementation (60%)

### Task 1: AI-Powered Code Completion
Files: `code/task1_sorting.py` (AI-suggested) and `code/task1_sorting_manual.py` (manual).

**200-word analysis**  
The AI-suggested implementation uses Python's built-in `sorted()` with a lambda key. This leverages Timsort (O(n log n)) implemented in C for performance and stability; it's concise and readable. The manual implementation constructs tuples `(missing_flag, value, index, dict)` and sorts them explicitly; this is educational but introduces Python-level overhead (tuple allocation and extra loops), making it less efficient in practice. For production, prefer the built-in `sorted()` for clarity and performance, and add tests to verify behavior with missing keys and mixed types.

### Task 2: Automated Testing with AI
File: `code/task2_selenium_login.py`. Update `LOGIN_URL`, selectors, and credentials before running. The script saves a screenshot to `report/figures/login_test_result.png`.

**150-word summary**  
Automated testing with AI-enhanced tools increases coverage and repeatability. Scripting login scenarios with Selenium validates authentication flows across browsers and environments. AI-powered test platforms accelerate authoring by suggesting robust selectors, auto-healing locators, and proposing negative/edge test cases, which reduces maintenance. Running tests in CI catches regressions earlier and improves confidence. The script included runs valid and invalid scenarios and saves a screenshot for reporting.

### Task 3: Predictive Analytics for Resource Allocation
File: `code/task3_predictive.py`. Uses sklearn's breast cancer dataset and a synthetic mapping to a 3-class "priority" label for demonstration.

Process:
1. Load data and compute a synthetic `risk_score`.
2. Map `risk_score` to `low`, `medium`, `high`.
3. Scale features and split data with stratification.
4. Train RandomForest (class_weight='balanced').
5. Evaluate with accuracy and macro F1; save confusion matrix.

Example outputs (your run may differ):
- Accuracy: 0.75  
- F1 (macro): 0.70

---

## Part 3 — Ethical Reflection (10%)
Potential biases:
- Underrepresentation: teams or platforms may be underrepresented, causing mis-prioritization.
- Label bias: historical priority labels reflect human subjectivity.
- Feature bias: features correlated with team, region, or customer tier could introduce unfairness.

Mitigation:
- Use fairness toolkits (e.g., IBM AI Fairness 360) to measure disparities and apply reweighing or post-processing.
- Maintain human-in-the-loop for high-impact decisions.
- Provide explainability (feature importance, SHAP) and continuous monitoring.

---

## Bonus — Innovation Proposal (1-page)
**Title:** AutoDoc — Context-aware Automated Documentation Generator for Microservices

**Purpose:** Generate living documentation combining static analysis, runtime traces (PII redacted), and LLM synthesis to produce endpoint docs, example payloads, and diagrams.

**Workflow:**
1. Static analysis extracts endpoints and signatures.
2. Runtime instrumentation collects example requests/responses.
3. LLM synthesizes docs and diagrams.
4. CI integration regenerates docs on merge; diffs reviewed in PRs.

**Impact:** Keeps docs current, reduces onboarding time, and prevents bugs from stale documentation.

---

## Appendix — Produce PDF & submission checklist
1. Place screenshots in `report/figures/`.  
2. Convert this markdown to PDF (Print-to-PDF or `pandoc report/week4_report.md -o report/week4_report.pdf`).  
3. Commit & push repo with the PDF and figures.  
4. Share repo link and paste report summary into the Community article.
