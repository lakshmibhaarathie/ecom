from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from api.config.api_config import settings
from api.exception.api_exception import EcommException
from api.logger.api_logging import logging



logging.info(f"{10*'>'} {10*' '} DATABASE {10*' '} {10*'<'}")
#url = "postgressql://<username>:<password>@<host-ip-address>/<databasename>"

DATABASE_URL = f"{settings.DATABASE}://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}"

engine = create_engine(url=DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine, autocommit=False,autoflush=False
)

Base = declarative_base()

def get_db():
    """
    Description:
        This function prepares a connection with database.
    Returns:
        Database object
    """
    db = SessionLocal()
    logging.info("Succesfully Connected to DataBase...!")
    try:
        yield db
    finally:
        db.close()


