## Backend Setup (FastAPI)
```
cd backend
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Mac/Linux)

pip install -r requirements.txt
uvicorn main:app --reload
```
Backend runs at: http://127.0.0.1:8000
Swagger docs at: http://127.0.0.1:8000/docs

## Frontend Setup (React)
```
cd frontend
npm install
npm run dev
```
Frontend runs at: http://localhost:5173

