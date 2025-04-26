AI Agent Technical Test
Repository
GitHub Repo
Setup Instructions

Clone the repository: git clone https://github.com/your-username/ai_agent_test.git
Install dependencies: pip install -r requirements.txt
Create a .env file with GEMINI_API_KEY=your_api_key_here
Ensure data/tax_policies.csv exists in the data folder
Run: python3 main.py

Approach Summary

Input: CLI for natural language questions
Retrieval: Keyword-based search on CSV dataset
LLM: gemini-2.0-flash-lite generates context-based answers
Data: CSV with tax policy information

Future Improvements

Use vector similarity search
Support multi-source datasets
Add conversational memory
Improve error handling and logging and architecture sepparating the LLM code from the agent

