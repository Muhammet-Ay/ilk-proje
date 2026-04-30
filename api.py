from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, engine, KullaniciDB, Base

app = FastAPI()
# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

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
@app.post("/kullanici-olustur")
def yeni_kullanici(kullanici: KullaniciOlustur):
    # Veritabanı oturumu başlat
    db = SessionLocal()
    
    # Yeni kullanıcı oluştur
    yeni_kullanici_db = KullaniciDB(
        isim=kullanici.isim,
        email=kullanici.email,
        yas=kullanici.yas
    )
    
    # Veritabanına ekle ve kaydet
    db.add(yeni_kullanici_db)
    db.commit()
    db.refresh(yeni_kullanici_db)
    db.close()
    
    return {
        "mesaj": "Kullanıcı veritabanına kaydedildi!",
        "kullanici": {
            "id": yeni_kullanici_db.id,
            "isim": yeni_kullanici_db.isim,
            "email": yeni_kullanici_db.email,
            "yas": yeni_kullanici_db.yas
        }
    }
@app.get("/kullanicilar")
def tum_kullanicilar():
    db = SessionLocal()
    kullanicilar = db.query(KullaniciDB).all()
    db.close()
    return {"kullanicilar": kullanicilar}