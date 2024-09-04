from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import well

app = FastAPI()

# Подключение шаблонов
templates = Jinja2Templates(directory="templates")

# Подключение маршрутов из файла well.py
app.include_router(well.router)

# Настройка CORS (опционально, если нужно)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно ограничить до нужных доменов
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
