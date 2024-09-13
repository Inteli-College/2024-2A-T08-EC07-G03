from fastapi import APIRouter
from .hello import router as hello
from .model import router as model
from .crud import router as crud
from .datalake import router as datalake

router = APIRouter()

router.include_router(hello, prefix="/hello")
router.include_router(model, prefix="/model")
router.include_router(crud, prefix="/crud")
router.include_router(datalake, prefix="/datalake")
