from fastapi import FastAPI, Form, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import FileResponse
import database as db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext


app = FastAPI()

templ = Jinja2Templates(directory="html")


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)




@app.get('/')
async def get(request: Request):
    return templ.TemplateResponse(
        name="index.html",
        context={"request": request}
    )




@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{'user:'}: {data}")

@app.get('/reg')
async def reg_page(request: Request):
    return templ.TemplateResponse(
        name="reg.html",
        context={"request": request}
    )


@app.post("/reguser")
async def reguser(username = Form(), password=Form()):
    # создание jwt token
    await db.save(usermame=username, passw=password)
    return {"name": username, "password": password}

@app.get("/forusers")
async def chatusers(request: Request):
    return templ.TemplateResponse(
        name='chatforusers.html',
        context={"request": request}
    )

