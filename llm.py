from google import genai
import os

# The SDK automatically picks up the GEMINI_API_KEY environment variable.
client = genai.Client()

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
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        print("LLM Error:", e)
        return None