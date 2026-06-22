from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    status: str
    message: str
    data: dict