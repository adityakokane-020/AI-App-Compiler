from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import PromptRequest, GenerateResponse
from agents.intent_extractor import extract_intent
from agents.system_designer import design_system
from agents.schema_generator import generate_schema
from validators.schema_validator import validate_schema
from agents.repair_engine import repair_schema
from runtime.executor import execute_app
from agents.failure_handler import handle_failures
app = FastAPI(
    title="AI App Compiler",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Backend Running Successfully"
    }
@app.post("/generate", response_model=GenerateResponse)
def generate_app(request: PromptRequest):

    # Stage 1: Intent Extraction
    intent = extract_intent(request.prompt)
    # Stage 2: Failure Handling
    failure_report = handle_failures(

    request.prompt,
    intent
)

    # Stage 2: System Design
    system_design = design_system(intent)

    # Stage 3: Schema Generation
    schema = generate_schema(system_design)
    # Stage 4: Validation
    validation = validate_schema(schema)
    # Stage 5: Repair
    repair = repair_schema(schema, validation)
    # Stage 6: Runtime Execution
    runtime = execute_app(repair["schema"])

    return {
        "status": "success",
        "message": "Application configuration generated successfully",
        "data": {
            "intent": intent,
            "failure_report": failure_report,
            "system_design": system_design,
            "schema": schema,
            "validation": validation,
            "repair": repair,
            "runtime": runtime
        }
    }