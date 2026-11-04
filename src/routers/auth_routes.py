# endpoints de autenticação
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.models import User
from dependencies.dependencies import take_section
from schemas.schemas import UserSchema
from security.security import hash_password

auth_router = APIRouter(prefix="/auth", tags=["auth"])


# criar uma rota
# toda função no fast é async
@auth_router.get("/")
async def home():
    """
    Rota padrão de autenticações
    """
    return {"mensagem": "Vocẽ acessou a rota de autenticação", "authenticated": False}


@auth_router.post("/create_account")
async def create_account(
    user_schema: UserSchema, session: Session = Depends(take_section)
):
    # busca dentro da tabela usuário
    user = session.query(User).filter(User.email == user_schema.email).first()
    if user:
        # se já existe usuário com esse email
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
    # raise - dispara um error
    else:
        encrypted_password = hash_password(user_schema.password)
        new_user = User(
            name=user_schema.name,
            email=user_schema.email,
            password=encrypted_password,
            active=user_schema.active,
            admin=user_schema.admin,
        )
        session.add(new_user)
        session.commit()
        return {"message": "usuário cadastrado com sucesso {user_schema.email}"}
