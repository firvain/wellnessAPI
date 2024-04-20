from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import User, UserCreate
from app.crud import create_user, get_user_by_email

router = APIRouter()


@router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Call the CRUD operation to create a user and handle exceptions in the CRUD function
    return create_user(db=db, user=user)

# @router.get("/users/me/", response_model=User)
# def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user