from fastapi import APIRouter
from .hello import router as hello
from .model import router as model

router = APIRouter()

router.include_router(hello, prefix="/hello")
router.include_router(model, prefix="/model")
