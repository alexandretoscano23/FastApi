from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


# criar base do banco de dados
class Base(DeclarativeBase):
    pass


# criar as classes/tabelas do banco


# Tabela usuário
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))  # sempre o hash
    active: Mapped[bool] = mapped_column(default=True)
    admin: Mapped[bool] = mapped_column(default=False)

    orders: Mapped[list["Order"]] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="PENDENTE")
    price: Mapped[float] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int]
    taste: Mapped[str] = mapped_column(String(50))
    size: Mapped[str] = mapped_column(String(20))
    unit_price: Mapped[float]
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    order: Mapped["Order"] = relationship(back_populates="items")


# executa a criação dos metadados
