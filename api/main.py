from fastapi import FastAPI

from routers import user
from routers import fund

router = FastAPI()


@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(user.router)
router.include_router(fund.router)
