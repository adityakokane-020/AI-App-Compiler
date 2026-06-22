def execute_app(schema):

    ui_pages = schema["ui_schema"]["pages"]
    api_endpoints = schema["api_schema"]["endpoints"]
    db_tables = schema["database_schema"]["tables"]

    return {
        "application_status": "Executable",

        "generated_files": {
            "pages": [
                f"{page}.html" for page in ui_pages
            ],

            "apis": [
                f"{api}.py" for api in api_endpoints
            ],

            "database": [
                f"{table}.sql" for table in db_tables
            ]
        },

        "message":
        "Application can be generated successfully"
    }