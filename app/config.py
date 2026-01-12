import os

class Config:
    DATABASE_URL = (
        os.getenv("DATABASE_URL")
        or os.getenv("DATABASE_PUBLIC_URL")
    )
