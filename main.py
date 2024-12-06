from models import Model
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from pydantic import BaseModel
from music import Music

from fastapi.staticfiles import StaticFiles


# FastAPI의 인스턴스를 생성
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/imgs", StaticFiles(directory="images"), name="images")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# templates 폴더의 "index.html" 응답
@app.get("/Questions", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("question.html", {"request": request})



# 사용자가 폼을 통해 보낸 데이터(content)를 받아서 "result.html" 템플릿에 넘김
@app.post("/predict/")
async def post_result(  request : Request
                       ,a1 : int = Form(...)
                       ,a2 : int = Form(...)
                       ,a3 : int = Form(...)
                       ,a4 : int = Form(...)
                       ,a5 : int = Form(...)
                       ,a6 : int = Form(...)
                       ,a7 : int = Form(...)
                       ,a8 : int = Form(...)
                       ,a9 : int = Form(...)
                       ,a10 : int = Form(...)
                     ):
    values = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    
    #music = Music()
    #play = music.play()
    if prediction[0] == 0:
            content = 'Your Depression test result : No Depression'
    if prediction[0] == 1:
            content = 'Your Depression test result : Mild Depression'
    if prediction[0] == 2:
            content = 'Your Depression test result : Moderate Depression'
    if prediction[0] == 3:
            content = 'Your Depression test result : Moderately severe Depression'
    if prediction[0] == 4:
            content = 'Your Depression test result : Severe Depression'

    # return { "content": content }
    return templates.TemplateResponse("result.html", {"request": request, "content": content})

@app.post("/predict/music")
async def post_result():
    
        music = Music()
        play = music.play()
        stop = music.stop()
        return { "music": play, "stop" : stop}      

 
@app.get("/predict/coloring", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("coloring.html", {"request": request})






