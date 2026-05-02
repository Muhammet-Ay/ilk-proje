class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Merhaba, ben {self.name}! {self.age} yaşındayım.")


user1 = User("Muhammet", 20)
user1.introduce()

# create a function that adds two numbers
def add_numbers(a, b):
    return a + b


from fastapi import FastAPI, HTTPException
from database import SessionLocal, KullaniciDB

app = FastAPI()

# Verilen ID'ye göre tek bir kullanıcı getiren GET rotası
@app.get("/kullanicilar/{kullanici_id}")
def get_kullanici(kullanici_id: int):
    """
    Belirtilen ID'ye sahip kullanıcıyı veritabanından getir.
    Eğer kullanıcı yoksa 404 Not Found hatası döndür.
    """
    db = SessionLocal()
    try:
        # Veritabanından ID'ye göre kullanıcıyı sorgula
        kullanici = db.query(KullaniciDB).filter(KullaniciDB.id == kullanici_id).first()
        
        # Eğer kullanıcı bulunamazsa 404 hatası döndür
        if not kullanici:
            raise HTTPException(status_code=404, detail=f"Kullanıcı ID {kullanici_id} bulunamadı")
        
        # Kullanıcı verisini döndür
        return {
            "id": kullanici.id,
            "isim": kullanici.isim,
            "email": kullanici.email,
            "yas": kullanici.yas
        }
    finally:
        db.close()

