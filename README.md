# AI App Compiler

## Overview

AI App Compiler is a multi-stage AI-based application generation system that converts natural language application ideas into structured application configurations.

Example:

Input:
Build a CRM with login, dashboard, contacts, and payment system

Output:
A structured JSON containing features, system design, schema, validation, and execution details.

---

## Features

- Intent Extraction
- System Design Generation
- Schema Generation
- Schema Validation
- Auto Repair Engine
- Failure Handling
- Runtime Execution Simulation
- Evaluation Framework
- Frontend Interface using HTML and JavaScript
- FastAPI Backend

---

## Project Architecture

```
User Prompt
     |
     ↓
Intent Extractor
     |
     ↓
System Designer
     |
     ↓
Schema Generator
     |
     ↓
Schema Validator
     |
     ↓
Repair Engine
     |
     ↓
Runtime Executor
     |
     ↓
Final JSON Output
```

---

## Project Structure

```
AI-App-Compiler/
│
├── backend/
│   ├── agents/
│   ├── models/
│   ├── validators/
│   ├── runtime/
│   ├── evaluation/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── README.md
└── .gitignore
```

---

## Installation

1. Clone the repository

```bash
git clone <repository_url>
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

Windows:
```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Running Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend URL:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

---

## Running Frontend

Open `frontend/index.html` using Live Server.

---

## Evaluation

Run the evaluation system:

```bash
python -m backend.evaluation.evaluation_runner
```

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript
- Git & GitHub

---

## Author

Aditya Kokane
