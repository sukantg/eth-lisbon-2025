# First Audit – Autonomous Smart Contract Auditor

First Audit is an AI-powered Mech tool built to perform autonomous security audits on Solidity smart contracts. Leveraging OpenAI's GPT models, it analyzes contract code, detects vulnerabilities, suggests gas optimizations, and outputs a comprehensive Markdown-formatted audit report.

---

## Features

- **Vulnerability Detection** – Identifies common attack vectors (reentrancy, tx.origin, unsafe delegatecall, etc.)
- **Gas Optimization Tips** – Offers suggestions to reduce gas consumption
- **Best Practices Review** – Highlights deviations from Solidity security standards
- **Powered by OpenAI** – Uses GPT-4o for natural language contract analysis
- **Markdown Audit Reports** – Outputs readable reports with recommendations
- **Mech Compatible** – Built to run as a Valory Mech tool or agent

## Set Up Your Environment

Follow these instructions to prepare your local environment to run the demo below or build your own AI Mech.

---

### 1. Create a Poetry Virtual Environment and Install Dependencies

```bash
poetry install && poetry shell
```

### 2. Fetch Required Packages via Open Autonomy CLI

Run the following command to download necessary packages from the remote registry:

```bash
autonomy packages sync --update-packages
```
