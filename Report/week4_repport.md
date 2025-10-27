### Week 4 Assignment — AI in Software Engineering
Theme: Building Intelligent Software Solutions

#### Submission contents
- Code: code/* (see repository)
- Report: this document (convert to PDF)
- Presentation: demo (not included as requested)

---

#### Part 1 — Theoretical Analysis (30%)

##### Q1: How AI-driven code generation tools reduce development time and limitations
AI code-completion tools (e.g., GitHub Copilot) speed development by suggesting boilerplate and idiomatic patterns, reducing the time spent searching for APIs and writing repetitive code. They accelerate prototyping, help enforce consistent style, and surface common error-handling patterns drawn from large code corpora. Limitations include: (1) suggestions can be incorrect, insecure, or suboptimal and still look plausible; (2) hallucinations or nondeterministic outputs require careful human review; (3) code provenance and licensing concerns; (4) over-reliance can erode developers' deep understanding; (5) inability to fully capture project-specific semantics and architectural constraints.

##### Q2: Supervised vs. unsupervised learning in automated bug detection
Supervised learning uses labeled examples (buggy vs. non-buggy) and is suitable for predicting known bug classes with high accuracy when labels are abundant and representative. Unsupervised learning (anomaly detection, clustering) finds unusual patterns without labels and is useful for discovering new or rare failure modes when labeled data is scarce. Supervised models excel for targeted detection; unsupervised approaches are valuable for exploratory detection but typically produce more false positives and need human validation.

##### Q3: Why bias mitigation is critical for personalization
Personalization models tailor user experiences, and if training data over- or under-represents user subgroups, some users may receive degraded or biased experiences. This leads to exclusion, harms trust, and can violate fairness and legal requirements. Bias mitigation ensures equitable UX, fosters trust, and prevents systematic disadvantages to underrepresented groups.

##### Case Study: AIOps in deployment pipelines — Two examples
1. Predictive anomaly detection: ML models trained on monitoring and deployment metrics predict potential rollout failures (e.g., spike in error rates), enabling proactive checks or halts that reduce downtime.
2. Intelligent remediation automation: AIOps systems suggest or enact remediation steps (auto-scaling, rolling back a release, or restarting services) based on historical runbooks and incident data, thereby reducing MTTR.

---

#### Part 2 — Practical Implementation (60%)

##### Task 1: AI-Powered Code Completion
- Files: code/task1_sorting.py (AI-suggested) and code/task1_sorting_manual.py (manual)
- Demo test: code/task1_tests.py

200-word analysis:
The AI-suggested implementation uses Python's built-in `sorted()` with a lambda key extractor. This leverages Timsort (O(n log n)) implemented in C, offering both performance and stability; it's concise and readable. The manual implementation constructs tuples `(missing_flag, value, index, dict)` and sorts them to preserve stability and control missing values. While the manual approach is educational and explicit, it adds Python-level overhead (tuple packing/unpacking and list construction) and uses more memory. In practice, the AI-suggested `sorted()` approach is more efficient because it avoids extra Python loops and relies on optimized internals; it is also less error-prone. The manual version is helpful for learning or when custom fallback logic is necessary. For production, prefer `sorted()` combined with unit tests.

##### Task 2: Automated Testing with AI
- File: code/task2_selenium_login.py
- Screenshot: report/figures/login_test_result.png (saved by script)

150-word summary:
Automated testing with AI-enhanced tools improves coverage, repeatability, and maintenance. Scripting login tests with Selenium validates authentication flows across environments. AI-powered test platforms (e.g., Testim.io or AI plugins for Selenium IDE) accelerate authoring by suggesting robust element selectors, auto-healing locators when DOM changes, and proposing negative/edge test cases. This reduces brittle tests and maintenance overhead. In our run, the script executed valid and invalid credential scenarios and produced pass/fail outcomes plus a screenshot. The main advantages compared to manual testing are speed, consistency, and the ability to run tests continuously in CI. AI assists in generating broader test permutations automatically, increasing coverage and catching regressions earlier.

##### Task 3: Predictive Analytics for Resource Allocation
- File: code/task3_predictive.py
- Note: This uses sklearn's breast cancer dataset and constructs a synthetic 3-class priority label for demonstration. Documented in the notebook/script.

Process summary:
1. Load dataset and construct a synthetic `risk_score` from selected features.
2. Map `risk_score` into `low`, `medium`, `high` labels.
3. Preprocess with StandardScaler, stratified train/test split.
4. Train RandomForest (class_weight='balanced').
5. Evaluate with accuracy and macro F1; save confusion matrix and model.

Example outputs (your run may differ):
- Accuracy: 0.75
- F1 (macro): 0.70
Attach confusion matrix image saved at `report/figures/confusion_matrix.png`.

---

#### Part 3 — Ethical Reflection (10%)
When deploying the predictive model:
- Potential biases:
  - Underrepresentation: certain teams/platforms may be scarce in historical data causing mis-prioritization.
  - Labeling bias: priority labels might reflect manager subjectivity rather than objective severity.
  - Feature bias: features correlated with team, location, or customer tier could produce unfair outcomes.
- Mitigation:
  - Use fairness toolkits (e.g., IBM AI Fairness 360) to measure disparate impact and apply reweighing, adversarial debiasing, or post-processing (equalized odds).
  - Maintain human-in-the-loop for review of high-impact decisions.
  - Provide explainability (feature importance, SHAP) and continuous monitoring.

---

#### Bonus — Innovation Proposal (1-page)
Title: AutoDoc — Context-aware Automated Documentation Generator for Microservices

Purpose:
AutoDoc generates living documentation using static code analysis, runtime traces, and LLM synthesis to produce endpoint docs, example payloads, and sequence diagrams.

Workflow:
1. Static analysis to extract endpoints, types, and function signatures.
2. Runtime instrumentation to gather example requests/responses (PII redaction).
3. LLM synthesizes human-friendly docs and usage examples; generates diagrams.
4. CI integration: docs updated on merge; diffs reviewed during PR.

Impact:
Improves onboarding, reduces bugs from stale docs, and maintains synchronization between code and documentation. Privacy: PII redaction; opt-out per team. Security: docs generation runs in controlled environment; no secrets exported.

---

#### Appendix — How to produce PDF and submission checklist
1. Convert `report/week4_report.md` to PDF:
   - Option A: Open in VSCode/Markdown editor and Print -> Save as PDF.
   - Option B (pandoc): `pandoc report/week4_report.md -o report/week4_report.pdf`
2. Place screenshots into `report/figures/`.
3. Commit & push to GitHub.
4. Share repo link and article (copy report text into Community article).

---

### Part 2 deliverables (copyable snippets already included in code/)
