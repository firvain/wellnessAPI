from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum as SQLAlchemyEnum
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from app.database import Base
from enum import Enum


class Role(Enum):
    admin = 'admin'
    rancher = 'rancher'
    cheesemaker = 'cheesemaker'
    vet = 'vet'


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    # Use SQLEnum and specify the Enum class created above
    role = Column(String)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)
