import datetime
import requests
import json

from app.db.models import PriceBTC
from app.schemas import BasePrice


def fetch_btc_usd_price() -> BasePrice:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    timestamp = datetime.datetime.utcnow()
    item = PriceBTC(
        price=price,
        timestamp=timestamp
    )
    return item
