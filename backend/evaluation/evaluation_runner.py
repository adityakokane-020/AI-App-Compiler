import time

from backend.evaluation.test_cases import test_prompts
from backend.agents.intent_extractor import extract_intent
from backend.agents.failure_handler import handle_failures
from backend.agents.system_designer import design_system
from backend.agents.schema_generator import generate_schema
from backend.validators.schema_validator import validate_schema
from backend.agents.repair_engine import repair_schema
from backend.runtime.executor import execute_app

success = 0
failure = 0
total_latency = 0


for prompt in test_prompts:

    start = time.time()

    try:

        intent = extract_intent(prompt)

        failure_report = handle_failures(
            prompt,
            intent
        )

        system = design_system(intent)

        schema = generate_schema(system)

        validation = validate_schema(schema)

        repair = repair_schema(
            schema,
            validation
        )

        runtime = execute_app(
            repair["schema"]
        )

        success += 1


    except Exception as e:

        print("FAILED:", prompt)
        print("ERROR:", e)

        failure += 1


    end = time.time()

    total_latency += (
        end - start
    )


print("\n========= Evaluation Result =========")

print(
    "Total Tests:",
    len(test_prompts)
)

print(
    "Success:",
    success
)

print(
    "Failures:",
    failure
)

print(
    "Success Rate:",
    (success / len(test_prompts)) * 100,
    "%"
)

print(
    "Average Latency:",
    total_latency / len(test_prompts),
    "seconds"
)