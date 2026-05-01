from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import chat, messages

# Load biến môi trường từ file .env (gọi 1 lần duy nhất ở đây)
load_dotenv()

app = FastAPI(
    title="Chatbot API",
    description="API backend cho ứng dụng chatbot sử dụng Gemini AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Các endpoint cơ bản ──────────────────────────────────────────


@app.get("/")
async def root():
    """Trang chủ – kiểm tra server đang chạy."""
    return {
        "message": "Chào mừng đến với Chatbot API!",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint – dùng để kiểm tra trạng thái server."""
    return {"status": "ok"}


# ── Đăng ký các router ───────────────────────────────────────────

app.include_router(chat.router)
app.include_router(messages.router)