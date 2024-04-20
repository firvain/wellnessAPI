import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import environment

# Choose the database URL based on the environment
if environment.lower() == "prod":
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL_PROD")
else:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL_DEV")

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
