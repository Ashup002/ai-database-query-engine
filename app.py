import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from llm import generate_sql
from validator import validate_query
from database import run_query

st.set_page_config(page_title="AI SQL Assistant", layout="wide")

st.title("🚀 AI SQL Assistant (Safe Mode)")
st.write("Ask database in natural language")

# 👉 Replace this with your REAL schema later
schema = """
System: MediLink

Table: MDB_PATIENTS
Columns: PATIENT_DBID, NAME_FAMILY, NAME_GIVEN, BIRTH_DATETIME, SEX

Table: MDB_ORDERS
Columns: ORDER_DBID, PATIENT_DBID, VISIT_DBID, ORDER_ID

Table: MDB_REPORTS
Columns: REPORT_DBID, ORDER_DBID, REPORT_TEXT, RESULT_STATUS


System: MediStore

Table: DIDB_PATIENTS
Columns: PATIENT_DB_UID, FIRST_NAME, LAST_NAME, BIRTH_DATE

Table: DIDB_STUDIES
Columns: STUDY_DB_UID, PATIENT_DB_UID, STUDY_DATE, MODALITY

Table: DIDB_SERIES
Columns: SERIES_DB_UID, STUDY_DB_UID, SERIES_NUMBER

Relationships:
- MDB_PATIENTS.PATIENT_DBID ↔ DIDB_PATIENTS.PATIENT_DB_UID
- DIDB_PATIENTS.PATIENT_DB_UID ↔ DIDB_STUDIES.PATIENT_DB_UID
- DIDB_STUDIES.STUDY_DB_UID ↔ DIDB_SERIES.STUDY_DB_UID

Rules:
- Columns ending with _DBID or _UID are keys
- Use JOINs when connecting tables
"""

user_input = st.text_input("Ask your query:")

if user_input:

    # Step 1: Generate SQL
    sql_query = generate_sql(user_input, schema)

    # Step 2: Fallback if AI fails
    if not sql_query:
        st.warning("AI unavailable, using demo query")
        sql_query = "SELECT * FROM ADDRESS"
    
    st.code(sql_query, language="sql")

    # Step 3: Validate
    valid, message = validate_query(sql_query)

    if valid:
        st.success(message)

        if st.button("Execute Query"):
            result = run_query(sql_query)
            st.write(result)
    else:
        st.error(message)