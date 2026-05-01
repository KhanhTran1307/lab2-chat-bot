from fastapi import APIRouter, HTTPException
from google import genai
from models import ChatRequest
from routers.messages import chat_history
import os

router = APIRouter()

API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)


@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        user_msg = request.message
        user_id = request.user_id

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg
        )

        answer = response.text

        # Lưu lịch sử vào bộ nhớ
        if user_id:
            if user_id not in chat_history:
                chat_history[user_id] = []
            chat_history[user_id].append({"message": user_msg, "answer": answer})

        return {"answer": answer}

    except Exception as e:
        print("LỖI:", e)
        err_str = str(e)
        if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
            raise HTTPException(
                status_code=429,
                detail="API Gemini đã hết quota miễn phí. Vui lòng thử lại sau vài phút hoặc kiểm tra billing tại https://ai.dev/rate-limit"
            )
        raise HTTPException(status_code=500, detail=err_str)