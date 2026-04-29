from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class KullaniciOlustur(BaseModel):
    isim: str
    email: str
    yas: int

@app.get("/") #Ana sayfa için GET isteği
def ana_sayfa():
    return {"message": "Merhaba, FastAPI!"} #Ana sayfaya erişildiğinde bu mesajı döndürür

@app.get("/kullanici/{isim}") #Kullanıcı bilgisi almak için GET isteği, URL'de kullanıcı adını alır
def kullanici(isim:str):
    return {"Kullanici": isim, "durum":"Aktif"}#Kullanıcı adını ve durumunu döndürür

@app.get("/Merhaba/{dil}") #Merhaba mesajı almak için GET isteği, URL'de dil alır
def merhaba(dil:str):
    selamlar = {
        "tr": "Merhaba!",
        "en": "Hello!",
        "es": "¡Hola!",
        "fr": "Bonjour!"
    }
    return {"dil": dil, "selam": selamlar.get(dil, "Dil bulunmadı")} #Dil bulunmazsa varsayılan mesaj döndürür

@app.post("/kullanici-olustur")
def yeni_kullanici(kullanici: KullaniciOlustur):
    return {
        "mesaj": "Kullanıcı başarıyla oluşturuldu!",
        "kullanici": {
            "isim": kullanici.isim,
            "email": kullanici.email,
            "yas": kullanici.yas
        }
    }