def repair_schema(schema, validation):

    if validation["valid"]:
        return {
            "repaired": False,
            "schema": schema,
            "message": "No repair needed"
        }


    errors = validation["errors"]


    # Fix missing UI
    if "UI pages are missing" in errors:
        schema["ui_schema"] = {
            "pages": ["Default Page"]
        }


    # Fix missing API
    if "API endpoints are missing" in errors:
        schema["api_schema"] = {
            "endpoints": ["/default"]
        }


    # Fix missing Database
    if "Database tables are missing" in errors:
        schema["database_schema"] = {
            "tables": ["DefaultTable"]
        }


    return {
        "repaired": True,
        "schema": schema,
        "message": "Schema repaired successfully"
    }