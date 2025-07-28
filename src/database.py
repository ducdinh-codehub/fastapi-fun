from sqlmodel import create_engine, SQLModel, Session
import config
from functools import lru_cache
from posts.models import Posts
from user.models import User
from auth.models import Auth

@lru_cache
def get_settings():
    return config.Settings()

DATABASE_URL = get_settings().database_url

engine = create_engine(DATABASE_URL, echo=True)
SQLMODEL = SQLModel

def create_tb():
    Posts()
    User()
    Auth()

def init_db():
    create_tb()
    SQLMODEL.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
