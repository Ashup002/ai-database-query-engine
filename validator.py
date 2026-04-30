FORBIDDEN = ["DROP", "DELETE", "TRUNCATE", "UPDATE"]


def validate_query(query):
    query_upper = query.upper()

    for word in FORBIDDEN:
        if word in query_upper:
            return False, f"❌ Unsafe query detected: {word}"

    return True, "✅ Query is safe"