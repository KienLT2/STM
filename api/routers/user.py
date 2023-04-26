from fastapi import APIRouter
from models.user import User

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
    users = User.select().dicts()
    return list(users)


@router.get("/api/users/{id}")
def get_user_by_id(id):
    """Get user by id"""
    user = model_to_dict(User.get(User.id == id))
    return user
# Response model

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
        User.update(**payload)
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
