# AutoDoc — Context-aware Automated Documentation Generator for Microservices

## Purpose
AutoDoc generates living documentation for microservices by combining static code analysis, runtime traces (PII redacted), and LLM synthesis to produce endpoint docs, example requests/responses, and sequence diagrams.

## Workflow
1. Static analysis extracts endpoints, types, and signatures.
2. Runtime instrumentation collects example requests/responses and traces; PII is redacted.
3. An LLM synthesizes human-friendly documentation and diagrams from code + traces.
4. CI integration regenerates docs on merges; diffs are surfaced in PRs for review.

## Impact
- Keeps documentation current and synchronized with code.
- Reduces onboarding time and documentation drift.
- Improves API discoverability and reduces bugs from stale docs.

## Privacy & Security
- PII redaction on traces.
- Controlled generation environment; secrets excluded.
- Opt-out per team for trace collection.
