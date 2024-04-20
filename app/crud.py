from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError, StatementError
from sqlalchemy.orm import Session

from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = pwd_context.hash(user.password)
    print(hashed_password)
    db_user = models.User(
        email=user.email,
        password=hashed_password,
        username=user.username,
        role=user.role
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered or other database integrity issue.")
    except StatementError as e:
        db.rollback()
        if 'invalid input value for enum' in str(e.orig):
            raise HTTPException(status_code=400, detail=f"Invalid role: {user.role}")
        raise HTTPException(status_code=400, detail="Invalid input or database error.")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user
