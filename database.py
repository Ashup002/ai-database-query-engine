import oracledb
import os

def get_connection():
    return oracledb.connect(
        user=os.getenv("DB_USER", "SYSTEM"),
        password=os.getenv("DB_PASSWORD", "a1d2m7i4"),
        dsn=os.getenv("DB_DSN", "192.168.1.199:1521/SYSTEM")
    )


def run_query(query):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        result = [dict(zip(columns, row)) for row in rows]

        cursor.close()
        conn.close()

        return result

    except Exception as e:
        return str(e)