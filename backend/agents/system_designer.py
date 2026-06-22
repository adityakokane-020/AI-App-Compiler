def design_system(intent):

    features = intent.get("features", [])

    entities = ["User"]
    modules = []
    roles = ["User"]

    if "login" in features:
        modules.append("Authentication")

    if "dashboard" in features:
        modules.append("Dashboard")

    if "payment" in features or "payments" in features:
        entities.append("Subscription")
        modules.append("Payment System")

    if "analytics" in features:
        roles.append("Admin")
        modules.append("Analytics")

    entities = sorted(entities)
    roles = sorted(roles)
    modules = sorted(modules)

    return {
        "entities": entities,
        "roles": roles,
        "modules": modules,
        "status": "system_designed"
    }