from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine("sqlite:///database/base.db")
SessionLocal = sessionmaker(bind=db)


def get_db():
    with SessionLocal() as session:
        yield session
