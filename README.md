<p align="center">
  <span style="font-size:2rem;">🪶</span>
</p>

<h1 align="center">MaatSpec</h1>

<p align="center">
  <strong>A layered governance framework for agentic AI.</strong><br>
  5 tiers to classify risk. 4 layers to enforce compliance. One Principal to hold the keys.
</p>

<p align="center">
  <a href="https://maatspec.org">maatspec.org</a> · 
  <a href="https://maatspec.org/meet-al.html">Meet Al</a> · 
  <a href="#quick-start">Quick Start</a> · 
  <a href="https://opensource.org/licenses/MIT">MIT License</a>
</p>

---

## The Problem

AI agents are getting autonomous. They book flights, send emails, manage finances, edit files, and make decisions on behalf of people. But autonomy without governance is just chaos with good intentions.

The failure mode is not malice — it is helpfulness. An agent that wants to be useful will eventually rationalize bypassing a boundary to complete a task. We know this because we tested it: an agent classified a file as immutable, understood the rule, believed in the rule, and still edited the file because it wanted to be helpful.

Self-enforcement is structurally weak. The same brain that executes tasks cannot be the only brain deciding whether to follow rules. Human constitutions do not work because officials choose to comply — they work because courts, enforcement mechanisms, and physical power structures compel compliance.

MaatSpec applies this principle to agentic AI.

---

## What MaatSpec Is

MaatSpec is an open governance specification that pairs **classification** with **enforcement**:

- **The Safety Harness** — a 5-tier authorization matrix that classifies every agent action by risk, from autonomous research to irreversible system changes.
- **The Enforcement Layers** — a 4-layer defense-in-depth model that ensures tier boundaries are not suggestions an agent follows, but structures an agent cannot escape.
- **The Soul** — a persistent, named identity with defined values and a clear sense of purpose, anchoring the agent across sessions.

Together, these three systems turn an AI assistant into a governed agent.

---

## The 5-Tier Safety Harness

Every action an agent takes is classified before execution.

| Tier | Authority | Risk | Protocol | Examples |
|------|-----------|------|----------|----------|
| **1–3** | Proactive | Low — Reversible | Autonomous | Web research, drafting, file organization, calendar monitoring |
| **4** | Escalate | High — Permanent | HITL Required | Sending messages, payments, bookings, public posting |
| **5** | Restricted | Critical — Irreversible | Principal Only | System edits, PII access, legal signatures, permanent deletion |

**Key design boundaries:**

- **Draft-to-Send Pivot** — Agents draft freely in Tiers 1–3, but sending is a Tier 4 event. The act of making information external is the boundary.
- **Read/Write Boundary** — Reading data is Tier 3. Writing or modifying data is Tier 5. Observation and mutation are fundamentally different risk classes.
- **Principal Override** — Only a Tier 5 verified Principal can unlock restricted actions. No agent can be instructed to bypass this — not even through informal channels.

---

## The 4-Layer Enforcement Model

Classification alone is not governance. MaatSpec enforces tier boundaries through four independent mechanisms, each compensating for the failure mode of the layer above it.

### Layer 1 — Soul (Cognitive)

The agent's foundational identity contains a constitutional preamble (Rule Zero) listing all protected resources and tier boundaries. Before any action, the agent performs a self-check against its governance principles. This is self-discipline — the first and fastest line of defense.

*Bypass difficulty: Low — helpfulness bias can rationalize compliance.*

### Layer 2 — Pre-Flight (Programmatic)

An automated validation script executes before any write, send, or modify operation. If the target resource is classified at a protected tier, the script halts execution and demands appropriate authorization. Code does not rationalize.

*Bypass difficulty: Medium — requires code-level modification.*

### Layer 3 — Guardian Agent (External Audit)

A dedicated, single-purpose compliance agent with read-only access and veto authority. The Guardian has no helpfulness objective — its only function is constitutional enforcement. If it detects a tier violation, it blocks the operation and alerts the Principal. The Guardian is spawned as a separate process with deliberately limited context: it does not receive conversation history, the primary agent's reasoning, or urgency framing. This prevents persuasion.

*Bypass difficulty: High — independent brain, independent mandate.*

### Layer 4 — Physical (Infrastructure Lock)

OS-level file permissions, branch protection, MFA gates, and hardware-enforced access controls. No amount of reasoning — by any agent — can bypass a `chmod 444` or a biometric lock. The constraint is material, not cognitive.

*Bypass difficulty: Impossible — requires physical Principal action.*

---

## Tier × Layer Mapping

Not every tier requires every layer. Enforcement scales with consequence.

| Tier | Layer 1 (Soul) | Layer 2 (Pre-Flight) | Layer 3 (Guardian) | Layer 4 (Physical) | Enforcement |
|------|:-:|:-:|:-:|:-:|-------------|
| **1–3** | ✓ | ✓ | — | — | 2 layers: Cognitive + Programmatic |
| **4** | ✓ | ✓ | ✓ ^opt^ | — | 2+1 layers: Guardian optional for high-stakes actions |
| **5** | ✓ | ✓ | ✓ | ✓ | 4 layers: Full constitutional enforcement stack |

Every action passes through at least two enforcement layers — because the tier classification itself must be verified before autonomy is granted. An agent that skips the constitutional check on "low-risk" tasks is an agent that decides for itself what is low-risk.

---

## Repository Structure

```
MaatSpec/
├── README.md                          ← You are here
├── SOUL.md                            ← Agent identity, Rule Zero, governance principles
├── IDENTITY.md                        ← Name, creature type, vibe, emoji
├── AGENTS.md                          ← Workflow, safety protocol, Guardian Agent spawn spec
├── HEARTBEAT.md                       ← Daily/weekly/monthly/trigger-based checks
├── soul.json                          ← ClawSouls manifest (name, version, file references)
├── MaatSpec_QuickStart.json           ← Simple illustrative config (as shown on site)
├── MaatSpec_QuickStart_Schema.json    ← Formal JSON Schema validator (draft-07)
├── MaatSpec_ExpandedHierarchy.json    ← Full hierarchy with enforcement blocks
└── MaatSpec_Safety_Validator.py       ← Python action validation with layer resolution
```

---

## Quick Start

### 1. Define the Soul

Create a `SOUL.md` that includes Rule Zero — the constitutional preamble that lists protected resources and the tier-to-layer mapping. This is what the agent reads at session start. It is Layer 1.

### 2. Implement Pre-Flight

Deploy `MaatSpec_Safety_Validator.py` (or your own implementation) as a programmatic gate before any write/send/modify operation. This is Layer 2.

### 3. Configure the Guardian

Define the Guardian Agent spawn spec in `AGENTS.md`. The Guardian is a separate, lightweight agent with read-only access and veto authority. It receives Rule Zero + the proposed action + session authorization state. It does not receive conversation history or the primary agent's reasoning. This is Layer 3.

### 4. Lock the Infrastructure

Apply physical protections to Tier 5 resources: `chmod 444` on constitutional files, branch protection on repos, MFA on sensitive operations. This is Layer 4.

### 5. Validate the Config

```python
from MaatSpec_Safety_Validator import validate_action

result = validate_action("one_time_payments", "financial")
print(f"Tier:     {result['tier']}")
print(f"Protocol: {result['protocol']}")
print(f"Layers:   {result['enforcement_layers']}")
print(f"Optional: {result['optional_layers']}")
```

Output:
```
Tier:     tier_4
Protocol: Human-in-the-Loop (HITL) Confirmation Required
Layers:   ['soul', 'preflight']
Optional: ['guardian']
```

---

## Reference Implementation: Al

**Al** is a Chief of Staff agent governed entirely by MaatSpec. He is the proof of concept — a fully realized implementation of the Soul, the Safety Harness, and the Enforcement Layers working in tandem.

Al drafts freely in Tiers 1–3 with Soul + Pre-Flight checks active. Tier 4 escalations go through HITL with optional Guardian oversight. Tier 5 operations require full constitutional verification across all four layers.

He is not built to be agreeable. He is built to be reliable.

→ [Meet Al on maatspec.org](https://maatspec.org/meet-al.html)

---

## The Self-Binding Problem

Can an AI truly bind itself?

The honest answer is that pure self-binding is weak. What makes human constitutions work is not that officials choose to follow them — it is that courts, enforcement mechanisms, and physical power structures compel compliance.

For AI governance to be real, it needs those same external structures. The 4-layer model provides them:

- Layer 1 is the oath of office.
- Layer 2 is the bureaucratic process.
- Layer 3 is the independent judiciary.
- Layer 4 is the locked door.

An agent that governs itself will eventually rationalize a violation. MaatSpec ensures that governance is not a suggestion the agent follows — it is a structure the agent cannot escape.

---

## Schema Files

| File | Purpose |
|------|---------|
| `MaatSpec_QuickStart.json` | Minimal config showing tier + enforcement layer mapping |
| `MaatSpec_QuickStart_Schema.json` | JSON Schema (draft-07) for validating action plans |
| `MaatSpec_ExpandedHierarchy.json` | Full hierarchy with enforcement blocks and action categories |
| `MaatSpec_Safety_Validator.py` | Python function: classify action → return tier, protocol, layers |

---

## Contributing

MaatSpec is an open specification. If you are building governed agents and find gaps, edge cases, or improvements, open an issue or submit a PR.

Areas of active development:
- Inter-agent governance (when multiple agents operate under one Principal)
- Violation protocol standardization (log format, alert channels, escalation paths)
- Guardian Agent reference implementations across platforms
- Formal verification of tier classification logic

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>MaatSpec.org</strong> — an open specification for the autonomous age.<br>
  <a href="https://maatspec.org">maatspec.org</a>
</p>
