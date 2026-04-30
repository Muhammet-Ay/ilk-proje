from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./Kullanicilar.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class KullaniciDB(Base):
    __tablename__ = "Kullanicilar"

    id = Column(Integer, primary_key=True, index=True)
    isim = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    yas = Column(Integer)