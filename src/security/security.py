import bcrypt

# converter a senha em hash


# para o cadastro - transformar a senha em senha criptografada
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# para o login - pega a senha digitada e o hash guardado e devolve true ou false
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
