from typing import Any
from sqlmodel import create_engine, SQLModel, Session
import config
from functools import lru_cache
from posts.models import Posts
from user.models import User
from auth.models import Auth

class Database:
    engine: Any
    SQLMODEL: Any

    def __init__(self):
        envsettings = config.Settings()
        dbtypenameprefix = envsettings.db_name_type_prefix
        database_url_connect = f"{dbtypenameprefix}{envsettings.postgres_user}:{envsettings.postgres_password}@{envsettings.postgres_server}:{envsettings.postgres_port}/{envsettings.postgres_db}"
        DATABASE_URL = database_url_connect
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.SQLMODEL = SQLModel

    def create_tb(self):
        Posts()
        User()
        Auth()

    def init_db(self):
        self.create_tb()
        self.SQLMODEL.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session
