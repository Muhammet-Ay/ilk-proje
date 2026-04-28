from fastapi import FastAPI

app = FastAPI()
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

