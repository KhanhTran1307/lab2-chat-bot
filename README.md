# 🤖 GreenMind AI — Đồ án ChatBot AI

Đồ án xây dựng ứng dụng ChatBot thông minh tích hợp trí tuệ nhân tạo, sử dụng mô hình ngôn ngữ lớn (LLM) để tương tác và hỗ trợ người dùng. Hệ thống được xây dựng với kiến trúc client-server hiện đại, đảm bảo hiệu năng và khả năng mở rộng.

---

## 👨‍🎓 Thông tin sinh viên
- **Họ và tên:** Trần Nguyễn Quốc Khánh
- **Mã số sinh viên:** 24120192
- **Môn học/Đồ án:** Tư duy tính toán / Lab 2
- **Giảng viên hướng dẫn:** Lê Đức Khoan

---

## 🎯 Mục tiêu và Mô tả dự án

**GreenMind AI** là một trợ lý ảo thông minh giúp người dùng giải đáp các câu hỏi đa lĩnh vực. Ứng dụng cung cấp một giao diện thân thiện, hiện đại (glassmorphism UI) kết hợp cùng backend mạnh mẽ xử lý dữ liệu theo thời gian thực.

**Điểm nổi bật của hệ thống:**
- Tích hợp **Google Gemini AI** xử lý ngôn ngữ tự nhiên mượt mà.
- Xác thực người dùng an toàn thông qua **Google OAuth (Firebase Authentication)**.
- Quản lý lịch sử hội thoại cá nhân hóa lưu trữ trên **Cloud Firestore**, cho phép đồng bộ trên nhiều phiên làm việc.

---

## 🛠️ Kiến trúc và Công nghệ sử dụng

Dự án được phân chia thành 2 phần độc lập (Frontend và Backend) giao tiếp qua RESTful API.

| Thành phần | Công nghệ / Framework | Vai trò |
|---|---|---|
| **Frontend** | HTML5, CSS3 (Custom UI), Vanilla JavaScript | Giao diện người dùng, xử lý logic client-side |
| **Backend** | Python, FastAPI | REST API Server, xử lý logic nghiệp vụ |
| **Authentication** | Firebase Authentication | Đăng nhập/Đăng xuất bằng tài khoản Google |
| **Database** | Firebase Cloud Firestore | Lưu trữ lịch sử tin nhắn dạng NoSQL |
| **AI Model** | Google Gemini API (`gemini-pro`) | Sinh nội dung, xử lý truy vấn của người dùng |

---

## 📁 Cấu trúc thư mục

```text
chatbot-app/
├── backend/
│   ├── main.py              # Entry point của FastAPI Server
│   ├── models.py            # Định nghĩa các model Pydantic/Data
│   ├── routers/             # Phân chia các API Routes (chat.py, messages.py)
│   ├── requirements.txt     # Danh sách thư viện Python
│   ├── .env                 # (Bỏ qua trên git) Chứa GEMINI_API_KEY
│   └── firebase-key.json    # (Bỏ qua trên git) Chứa Service Account Key
├── frontend/
│   └── index.html           # File giao diện chính của ứng dụng
├── .gitignore               # Cấu hình bỏ qua file nhạy cảm/không cần thiết
└── README.md                # Tài liệu dự án
```

---

## ⚙️ Hướng dẫn cài đặt và Chạy ứng dụng

### 1. Yêu cầu hệ thống
- **Python:** Phiên bản 3.10 trở lên.
- **Trình duyệt:** Chrome, Edge, Firefox (phiên bản mới nhất).
- **Tài khoản:** Google (để lấy Gemini API key và thiết lập Firebase).

### 2. Thiết lập Backend

Mở terminal và di chuyển vào thư mục `backend`:

```bash
cd backend
```

Tạo và kích hoạt môi trường ảo (Virtual Environment):
```bash
# Trên Windows
python -m venv .venv
.venv\Scripts\activate

# Trên macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

Cài đặt các thư viện cần thiết (Requirements):
```bash
# Vì file requirements.txt nằm ở thư mục ngoài, dùng lệnh sau:
pip install -r ../requirements.txt
```

Cấu hình các biến môi trường:
1. Tạo file `.env` tại thư mục `backend/` và thêm key của Gemini:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
2. Thêm file `firebase-key.json` (Service Account Key lấy từ Firebase Console) vào thư mục `backend/`.

Khởi động Server:
```bash
uvicorn main:app --reload
```
*Server sẽ chạy tại: `http://localhost:8000` (Truy cập `http://localhost:8000/docs` để xem tài liệu API).*

### 3. Thiết lập Frontend

- Ứng dụng Frontend không cần cài đặt node_modules hay build tool phức tạp.
- Bạn chỉ cần mở file `frontend/index.html` bằng **Live Server** (Extention của VS Code) hoặc mở trực tiếp trên trình duyệt.
- Đảm bảo Backend đang chạy để Frontend có thể gọi API thành công.

---

## 📡 Danh sách API Endpoints chính

- `GET /` : Kiểm tra trạng thái hoạt động của server.
- `GET /health` : API Health check.
- `POST /chat` : Nhận tin nhắn từ người dùng, gửi cho Gemini AI và lưu lịch sử vào Firestore.
- `GET /messages/{user_id}` : Trích xuất lịch sử trò chuyện của một người dùng cụ thể.

---

## 🎬 Demo 

https://drive.google.com/file/d/1x6wxAgwRnCIL9GdD29Xx0a2jCDnmP0WE/view?usp=sharing

---

## ⚠️ Lưu ý Bảo mật
Các file chứa thông tin nhạy cảm đã được cấu hình trong `.gitignore` và tuyệt đối **không được commit** lên GitHub:
- `backend/.env`
- `backend/firebase-key.json`
- Thư mục `.venv/`

---
*Đồ án được thực hiện phục vụ mục đích học tập và nghiên cứu.*
