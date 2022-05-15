from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from sqlalchemy_utils.functions.database import create_database

if __name__ == "__main__":
    raise Exception("This script should not be executed directly")

# https://fastapi.tiangolo.com/tutorial/sql-databases/#import-the-sqlalchemy-parts

env = dict(dotenv_values(".env"))

# DB_CONNECTION_STRING = env.get("DB_CONNECTION_STRING")
DB_CONNECTION_STRING = "sqlite:///./sql_app.db"

if not DB_CONNECTION_STRING:
    raise Exception("Could not load environment variable 'DB_CONNECTION_STRING'.")

engine = create_engine(DB_CONNECTION_STRING, connect_args={"check_same_thread": False})

if not database_exists(engine.url):
    print(f"Created database '{env.get('DB_DATABASE_NAME')}'")
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()


# dependency
def get_db():
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

