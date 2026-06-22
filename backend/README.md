# AI App Compiler

## Overview

AI App Compiler is a system that converts natural language application ideas into structured and executable application configurations.

Example Input:

Build a CRM with login, dashboard, contacts, role-based access and premium payments.


Generated Output includes:

- Intent extraction
- System architecture
- UI schema
- API schema
- Database schema
- Authentication rules
- Business logic


---

## Architecture

User Prompt
        |
        v
Intent Extraction
        |
        v
System Design Layer
        |
        v
Schema Generation
        |
        v
Validation Engine
        |
        v
Repair Engine
        |
        v
Runtime Execution
        |
        v
Final JSON Output


---

## Features

- Multi-stage AI compiler pipeline
- Deterministic output generation
- Schema validation
- Automatic repair system
- Failure handling
- Runtime execution simulation
- Evaluation framework
- Frontend interface

---

## Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn


### Frontend

- HTML
- JavaScript


---

## Project Structure

AI-App-Compiler/

backend/
- agents
- models
- validators
- runtime
- evaluation
- main.py


frontend/
- index.html


---

## Installation

Clone repository:

git clone <repository-url>


Move into project:

cd AI-App-Compiler


Create virtual environment:

python -m venv venv


Activate environment:

Windows:
venv\Scripts\activate


Install dependencies:

cd backend

pip install -r requirements.txt


---

## Run Backend

cd backend

uvicorn main:app --reload


---

## Run Frontend

Open frontend/index.html using Live Server.

---

## Evaluation

The system was evaluated using:

- 10 real-world product prompts
- 10 edge cases

Metrics tracked:

- Success rate
- Failure types
- Latency
- Reliability


---

## Future Improvements

- Integrate real LLM APIs
- Generate actual applications from JSON
- Add database deployment support
- Improve UI generation


---

## Author

Aditya Kokane
