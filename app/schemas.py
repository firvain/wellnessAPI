from datetime import datetime

from pydantic import BaseModel
from enum import Enum


class Role(Enum):
    admin = 'admin'
    rancher = 'rancher'
    cheesemaker = 'cheesemaker'
    vet = 'vet'


class UserBase(BaseModel):
    username: str
    email: str
    role: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class Login(BaseModel):
    email: str
    password: str


