from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    user_id: str | None = None


class MessagePayload(BaseModel):
    message: str
    answer: str
