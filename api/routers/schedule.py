from fastapi import APIRouter
from models.schedule import Schedule
from datetime import date, time

from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel

router = APIRouter()
class Schedules(BaseModel):
    id: int
    date: date
    time: time
    fieldfee: int
    participants: []


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


@router.post("/api/schedule")
def create_schedule(payload_: Schedule):
    """Create new schedule"""
    payload = payload_.dict()
    Schedule.create(**payload)


@router.patch("/api/schedule/{id}")
def update_schedule(id: int, payload_: Schedules):
    """Update schedule"""
    payload = payload_.dict()
    schedule = (
        Schedule.update(**payload)
        .where(Schedule.id == id)
        .execute()
    )
    # number of changed rows
    return schedule


@router.delete("/api/schedule/{id}")
def delete_schedule(id: int):
    """Delete schedule"""
    schedule = Schedule.get_by_id(id)
    schedule.delete_instance()
