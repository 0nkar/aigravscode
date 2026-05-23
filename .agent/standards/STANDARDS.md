# System Design Standards for Vibe Coding (Antigravity x Claude Ecosystem)

# Version: 2.1.0 (Production-Grade)

# Status: Enforced

## 1. Architectural Context Boundaries & Isolation

To prevent token bleeding and chaotic, unpredictable code insertion, all vibe-coded system components must adhere to strict boundary rules.

### 1.1 Core vs. Volatile Layering

- **The Core Layer**: Database schemas, authentication paths, cryptography, and core business models are strictly read-only for AI agents. They cannot be modified without human PR approval.
- **The Volatile Layer**: Frontend UI scaffolds, automated cron utilities, tracking pipelines, and simple reporting scripts (e.g., `.agent/workflows/`) can be generated and refactored autonomously by the agent.

### 1.2 The Interface Principle

- AI-generated features must be hidden behind explicit interface definitions or API gateways.
- If an agent generates an analytics utility, it must implement a pre-defined interface:
  ```typescript
  interface ISystemAnalyticAgent {
    initializeContext(): Promise<boolean>;
    executeTelemetryQuery(queryStr: string): Promise<AnalyticsPayload>;
    syncToGoogleEcosystem(targetSheetId: string): Promise<void>;
  }
  ```
- This ensures an entire AI-generated module can be dropped and regenerated from scratch without breaking downstream system dependencies.

---

## 2. Agent Initialization Rules & System Prompts

Every workspace running Antigravity or Claude Code must implement these root environment rules (`.cursorrules` / `.agent/rules/global.md`) to minimize architectural hallucination.

### 2.1 Zero Hardcoding Enforcement

- **Strict Prohibition**: Agents are strictly forbidden from hardcoding environment states, tokens, URLs, or Sheet IDs into code files.
- **Dynamic Mapping**: All system configurations must use dynamic variables mapped via standard environment configurations (`process.env` or system environment bindings).
- **Default Check**: Code matching regex `/(AI_KEY|SHEET_ID|GCP_TOKEN)\s*=\s*['"][a-zA-Z0-9]{10,}['"]/` will fail the automated pre-commit hook.

### 2.2 Framework Pinning

- Agents must explicitly use pinned structural versions:
  - Runtime: **Node.js v22.x** or **Python 3.12**
  - Cloud Interface: **Google Cloud SDK v480.0.0+**
- Agents are blocked from upgrading dependencies or introducing new package architectures without an isolated, explicit prompt tracking ticket.

---

## 3. Spec-Driven Handoff Pipeline

Vibe coding without validation produces untracked system debt. Every structural task must move through a structured four-stage system pipeline.
