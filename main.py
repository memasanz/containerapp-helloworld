from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

# Simple GET endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello, welcome to FastAPI!"}

