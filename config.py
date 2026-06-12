import os

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

class Config:

    database_url = os.getenv(
        "DATABASE_URL"
    )

    if database_url:
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret-key"
    )