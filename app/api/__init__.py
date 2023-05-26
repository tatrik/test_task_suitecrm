from fastapi import APIRouter

from .leads import router as leads_router
from .btc import router as btc_router


router = APIRouter()
router.include_router(leads_router)
router.include_router(btc_router)
