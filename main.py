import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from service import check_text

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")


@app.get("/check_text/{text}")
def foo(text: str):
    key_words = [
        'наркотики', 'вещество', 'наркотическое', 'прекурсор', 'психотропный', 'психоактивный', 'взрывчатый', 'бомба',
        'взрыв', 'орган', 'ткань', 'табак', 'сигареты', 'вейп', 'вэйп', 'пар', 'курить', 'реферат', 'курсовая',
        'аттестация', 'иноагент', 'инагент', 'агент', 'биткоин', 'валюта'
    ]
    return {
        "text_quality": check_text(text, key_words),
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
