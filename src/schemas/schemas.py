from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    active: bool | None
    admin: bool | None

    # indicar que a classe vai ser interpretada como uma classe que vai ser transformada em sql
    class Config:
        from_attributes = True


class OrderSchema(BaseModel):
    user: int

    class Config:
        from_attributes = True
