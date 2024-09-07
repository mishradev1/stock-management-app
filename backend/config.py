import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mongodb+srv://dev:YE5HhR9PbZZtPFXz@cluster0.ebtn2fd.mongodb.net/_stocks")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
