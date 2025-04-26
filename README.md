AI Agent Technical Test
Setup Instructions

Clone the repository.
Install dependencies: pip install pandas python-dotenv google-generativeai.
Create a .env file with GEMINI_API_KEY=your_api_key_here.
Ensure data/tax_policies.csv exists with the provided dataset.
Run the script: python main.py.

Approach Summary

Input: CLI accepts natural language questions.
Retrieval: Keyword-based search matches question keywords to dataset text.
LLM: Gemini-1.5-flash generates answers using retrieved context.
Data: CSV with tax policy information.

Future Improvements

Implement vector similarity search with sentence-transformers.
Add multi-source dataset support.
Include conversational memory for follow-up questions.
Enhance error handling and logging.