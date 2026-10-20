from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.api import health, meetings, schedule
from backend.ws.endpoint import router as websocket_router

app = FastAPI(title="Orbit Meet", version="1.0.0")

BASE = Path(__file__).resolve().parent.parent
FRONTEND = BASE / "frontend"
ADMIN = BASE / "admin"

# Static assets used by the frontend.
app.mount("/static", StaticFiles(directory=FRONTEND), name="static")
# Serve the small admin interface and its CSS/JS files.
app.mount("/admin", StaticFiles(directory=ADMIN, html=True), name="admin")

app.include_router(health.router)
app.include_router(meetings.router)
app.include_router(schedule.router)
app.include_router(websocket_router)


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(FRONTEND / "html" / "index.html")
