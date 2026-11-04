from sqlalchemy.orm import sessionmaker

from database.session import db


# criar seção no banco de dados
def take_section():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session  # retorna o valor sem parar a execução da função

    finally:
        session.close()
