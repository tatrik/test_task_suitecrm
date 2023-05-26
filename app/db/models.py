from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Leads(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_work = Column(String(32))
    first_name = Column(String(120))
    last_name = Column(String(120))


class PriceBTC(Base):
    __tablename__ = "price_btc_usd"

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    timestamp = Column(DateTime)
