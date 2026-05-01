# AI Database Query Engine (AI SQL Assistant)

## Overview
This system is an AI-powered SQL assistant built with **Streamlit**, **Google Gemini**, and **Oracle Database**. It allows users to ask questions about a medical database (MediLink & MediStore) using natural language. The system securely translates these natural language queries into Oracle SQL, validates them for safety (preventing destructive operations), and executes them directly against the database to return results.

## Features
- **Natural Language to SQL**: Uses Google Gemini (`gemini-3-flash-preview`) to intelligently generate SQL queries based on a provided database schema.
- **Safety First**: Includes a built-in query validator (`validator.py`) that actively blocks potentially harmful SQL commands (e.g., `DROP`, `DELETE`, `UPDATE`, `TRUNCATE`).
- **Oracle DB Integration**: Connects and executes queries directly against an Oracle Database using `oracledb`.
- **Interactive UI**: A clean, intuitive web interface powered by Streamlit.
- **Fallback Mechanism**: Provides a safe demo query if the AI service becomes unavailable or fails to generate a query.

## Prerequisites
- **Python 3.8+**
- An active **Oracle Database** instance (configured in `database.py`)
- **Google Gemini API Key**

## Setup & Installation

1. **Clone the repository** (if applicable) and navigate to the project directory:
   ```bash
   cd ai-database-query-engine
   ```

2. **Create and activate a virtual environment** (Recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**:
   The application uses environment variables for configuration. Create a `.env` file in the project root by copying the provided example:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and fill in your actual credentials:
   ```env
   # Google Gemini API
   GEMINI_API_KEY=your_gemini_api_key_here

   # Oracle Database Configuration
   DB_USER=SYSTEM
   DB_PASSWORD=your_oracle_password_here
   DB_DSN=192.168.1.199:1521/SYSTEM
   ```

## Running the Application

Once everything is set up, start the Streamlit application by running:

```bash
streamlit run app.py
```

The application will launch in your default web browser (typically accessible at `http://localhost:8501`).

## System Architecture / File Structure
- `app.py`: The main entry point. Sets up the Streamlit UI, defines the hardcoded database schemas, and orchestrates the flow from user input to query execution.
- `llm.py`: Handles communication with the Google Gemini API. It injects the database schema and rules into the prompt to ensure accurate SQL generation.
- `validator.py`: A security layer that ensures only safe, read-only (`SELECT`) operations are processed.
- `database.py`: Manages the connection to the Oracle database and handles the execution of the final validated SQL query.
- `requirements.txt`: Contains the direct Python dependencies (`streamlit`, `oracledb`, `google-genai`).
