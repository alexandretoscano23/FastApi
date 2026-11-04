# endpoints de autenticação
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.models import Order
from dependencies.dependencies import take_section
from schemas.schemas import OrderSchema

order_router = APIRouter(prefix="/orders", tags=["orders"])


# criar uma rota
# toda função no fast é async
@order_router.get("/")
async def orders():
    """
    Rota padrão de pedidos
    """
    return {"mensagem": "Vocẽ acessou a rota de pedidos"}


@order_router.post("/pedido")
async def create_order(
    order_schema: OrderSchema, session: Session = Depends(take_section)
):
    new_order = Order(user=OrderSchema.user)
    session.add(new_order)
    session.commit()
    return {"message": f"Pedido criado com sucesso. ID do pedido: {new_order.id}"}
