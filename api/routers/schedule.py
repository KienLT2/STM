from fastapi import APIRouter
from models.schedule import Schedule
from datetime import date, time

from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel

router = APIRouter()
class Schedules(BaseModel):
    id : int
    date : date
    time : time
    fieldfee : int
    participants : int[]


@router.get("/api/schedule")
def get_all_schedule():
    """Get all schedule"""
    schedules = Schedule.select().dict()
    return schedules


@router.get("/api/schedule/{id}")
def get_schedule_by_id(id: int):
    """Get schedule by id"""
    schedule = model_to_dict(Schedule.get(Schedule.id == id))
    return schedule