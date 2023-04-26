from fastapi import APIRouter
from models.fund import Fund

from pydantic import BaseModel

router = APIRouter()

class Funds(BaseModel):
    id: int
    fund: int



@router.get("/api/fund")
def get_fund():
    """Get fund"""
    fund = Fund.select().order_by(Fund.id.desc()).first()
    return fund


@router.post("/api/fund")
def create_fund(payload_: Funds):
    """Create new record of fund"""
    payload = payload_.dict()
    Fund.create(**payload)



