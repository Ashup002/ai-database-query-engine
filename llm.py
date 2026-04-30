from google import genai
import os

# Configure API key securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use correct free model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_sql(user_query, schema):
    prompt = f"""
You are an expert Oracle SQL developer.

Database Schema:
{schema}

Rules:
- Use correct table names and columns
- Use JOIN when columns end with _KEY
- Prefer SELECT queries only
- Avoid DELETE, DROP, UPDATE
- Return ONLY SQL query

User Query:
{user_query}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("LLM Error:", e)
        return None