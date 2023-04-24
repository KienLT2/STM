from fastapi import FastAPI

from routers import user

router = FastAPI()


@router.get("/")
def root_access():
    return {"message": "Hello World"}


router.include_router(user.router)
