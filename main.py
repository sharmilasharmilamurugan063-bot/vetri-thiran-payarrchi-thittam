from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/home", response_class=HTMLResponse)
async def home_planner(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )


@app.get("/party", response_class=HTMLResponse)
async def party_planner(request: Request):
    return templates.TemplateResponse(
        "party.html",
        {"request": request}
    )


@app.get("/jewelry", response_class=HTMLResponse)
async def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        "jewelry.html",
        {"request": request}
    )