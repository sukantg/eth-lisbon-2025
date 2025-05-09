# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2025 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

import os
import sys
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI, APIStatusError

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_contract(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def audit_with_openai(contract_code):
    prompt = f"""
You are a senior smart contract auditor. Analyze the following Solidity contract and return:
- A brief summary of what it does
- Security vulnerabilities
- Gas optimization tips
- Best practices it violates
- An overall security rating from 1 to 10
- All output should be in Markdown format

Solidity Contract:{contract_code}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a security-focused Solidity expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500,
        )
        return response.choices[0].message.content.strip()

    except APIStatusError as e:
        print(f"OpenAI API returned error {e.status_code}: {e.response}")
        return f"Error: {e}"

def save_report(content, filename="audit_report.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"{filename.replace('.md', '')}_{timestamp}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Audit report saved to {path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python auditagent.py path/to/contract.sol")
        return

    contract_path = sys.argv[1]

    try:
        contract = read_contract(contract_path)
        print("Auditing contract with GPT-4o...")
        report = audit_with_openai(contract)
        print("\nAudit Report:\n")
        print(report)
        save_report(report)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
