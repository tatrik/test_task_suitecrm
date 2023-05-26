from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.schemas import PriceOut
from app.db.session import get_db
from app.crud.btc import fetch_btc_usd_price


router = APIRouter(prefix="/price", tags=['BTC'])


@router.post('/', response_model=PriceOut)
def create_price(
        db: Session = Depends(get_db),
):
    price = fetch_btc_usd_price()
    db.add(price)
    db.commit()
    db.refresh(price)
    return price
