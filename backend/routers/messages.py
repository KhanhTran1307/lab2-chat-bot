from fastapi import APIRouter
from models import MessagePayload

router = APIRouter()

# Lưu lịch sử chat trong bộ nhớ (reset khi server restart)
# Nếu muốn lưu lâu dài, thay bằng Firestore hoặc SQLite
chat_history: dict[str, list] = {}


@router.get("/messages/{user_id}")
async def get_messages(user_id: str):
    history = chat_history.get(user_id, [])
    return {"history": history}


@router.post("/messages/{user_id}")
async def save_message(user_id: str, payload: MessagePayload):
    if user_id not in chat_history:
        chat_history[user_id] = []
    chat_history[user_id].append({
        "message": payload.message,
        "answer": payload.answer,
    })
    return {"status": "ok"}
