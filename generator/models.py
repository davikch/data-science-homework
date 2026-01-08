from sqlalchemy import String
from sqlalchemy import DECIMAL as Decimal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Ride(Base):
    __tablename__ = "ride"
    id: Mapped[int] = mapped_column(primary_key=True)
    client: Mapped[str] = mapped_column(String)
    driver: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    price: Mapped[Decimal] = mapped_column(Decimal(precision=8, scale=2))

    def __init__(self, client, driver, destination, price):
        self.client = client
        self.driver = driver
        self.destination = destination
        self.price = price


# class Driver(Base):
#     __tablename__ = "driver"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     rating: Mapped[decimal.Decimal] = mapped_column(
#         decimal.Decimal, CheckConstraint("rating>=1.0 AND rating<=5.0")
#     )
#
#
# class Client(Base):
#     __tablename__ = "client"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String)
#     rating: Mapped[decimal.Decimal] = mapped_column(
#         decimal.Decimal, CheckConstraint("rating>=1.0 AND rating<=5.0")
#     )
