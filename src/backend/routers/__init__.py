from fastapi import APIRouter
from .hello import router as hello

router = APIRouter()

router.include_router(hello, prefix="/hello")
