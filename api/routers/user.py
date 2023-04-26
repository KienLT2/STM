from fastapi import APIRouter
from models.user import User

from peewee import fn
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel

router = APIRouter()


class Users(BaseModel):
    name: str
    phonenumber: str
    email: str
    password: str
    fund: int
    role: int


@router.get("/api/users")
def get_all_users():
    """Get all users"""
    users = User.select()
    users = [model_to_dict(user) for user in users]
    return users


@router.get("/api/users/{id}")
def get_user_by_id(id):
    """Get user by id"""
    user = User.get(User.id == id)
    return user


@router.post("/api/users")
def create_user(payload_: Users):
    """Create a new user"""
    payload = payload_.dict()
    User.create(**payload)


@router.patch("/api/users/{id}")
def edit_user(id: int, payload_: Users):
    """Update user info"""
    payload = payload_.dict()
    user = (
        User.update(
            name=payload["name"],
            phonenumber=payload["phonenumber"],
            email=payload["email"],
            password=payload["password"],
            fund=payload["fund"],
            role=payload["role"]
        )
        .where(User.id == id)
        .execute()
    )
    # number of changed rows
    return user


@router.delete("/api/users/{id}")
def delete_user(id: int):
    """Delete user"""
    user = User.get_by_id(id)
    user.delete_instance()
