from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def ana_sayfa():
    return {"message": "Merhaba, FastAPI!"}

@app.get("/kullanici/{isim}")
def kullanici(isim:str):
    return {"Kullanici": isim, "durum":"Aktif"}
