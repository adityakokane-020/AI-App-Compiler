def handle_failures(prompt, intent):

    warnings = []
    assumptions = []

    # Check vague prompt
    if len(prompt.split()) < 3:
        warnings.append(
            "Prompt is too short or vague"
        )

        assumptions.append(
            "Assuming a generic web application"
        )


    # Check no features detected
    if len(intent["features"]) == 0:

        warnings.append(
            "No known features detected"
        )

        assumptions.append(
            "Using default application configuration"
        )


    return {
        "warnings": warnings,
        "assumptions": assumptions,
        "status": "failure_checked"
    }