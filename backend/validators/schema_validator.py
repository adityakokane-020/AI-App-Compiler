def validate_schema(schema):

    errors = []

    ui = schema.get("ui_schema", {})
    api = schema.get("api_schema", {})
    db = schema.get("database_schema", {})

    # Check UI pages
    if not ui.get("pages"):
        errors.append("UI pages are missing")

    # Check API endpoints
    if not api.get("endpoints"):
        errors.append("API endpoints are missing")

    # Check Database tables
    if not db.get("tables"):
        errors.append("Database tables are missing")

    if len(errors) == 0:
        return {
            "valid": True,
            "errors": []
        }

    return {
        "valid": False,
        "errors": errors
    }