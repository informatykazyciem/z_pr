from fastapi import FastAPI, Depends, File, UploadFile
from pydantic import BaseModel
from typing import Union
from PIL import Image, ImageOps
from datetime import datetime
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import math
import shutil

app = FastAPI()


@app.get("/")
async def root():
    return {
        " W celu sprawdzenia czy liczba jest pierwsza ależy wpisać np. /prime/7 "
        "- po prime wpisujemy wybrana przez nas liczbe którą chcemy sprawdzić" +
        " Dostęp do panelu z logowaniem odbywa się poprzez wstawienie: /login " +
        " W celu inwersji kolorów obrazka - /picture/invert"
    }


@app.get("/prime/{number}")
async def is_prime(number: float):
    response = {
        "Liczba": number,
        "Czy_pierwsza": is_prime(number)
    }
    return response


def is_prime(number: float):
    if number <= 1:
        return "Liczba nie jest pierwsza"
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return "Liczba nie jest pierwsza"
    return "Liczba  jest pierwsza"


@app.get("/login")
async def user(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    time = datetime.now().strftime("%H:%M:%S")
    return f"Czas teraz {time} "


@app.post("/picture/invert")
async def invert(image: UploadFile = File('monstera.jpg')):
    image = Image.open(image)
    im_invert = ImageOps.invert(image)
    im_invert.save('monster_invert.jpg', quality=95)
    return 'Kolory zmienione'
