def generate_schema(system_design):

    modules = system_design.get("modules", [])
    entities = system_design.get("entities", [])
    roles = system_design.get("roles", [])

    ui_pages = []
    api_endpoints = []
    database_tables = []
    auth_rules = []

    if "Authentication" in modules:
        ui_pages.append("Login Page")
        api_endpoints.append("/login")

    if "Dashboard" in modules:
        ui_pages.append("Dashboard Page")
        api_endpoints.append("/dashboard")

    if "Payment System" in modules:
        ui_pages.append("Payment Page")
        api_endpoints.append("/payments")

    for entity in entities:
        database_tables.append(entity)

    for role in roles:
        auth_rules.append({
            "role": role,
            "permissions": "basic_access"
        })

    return {
        "ui_schema": {
            "pages": ui_pages
        },

        "api_schema": {
            "endpoints": api_endpoints
        },

        "database_schema": {
            "tables": database_tables
        },

        "auth_schema": {
            "roles": auth_rules
        },

        "status": "schema_generated"
    }