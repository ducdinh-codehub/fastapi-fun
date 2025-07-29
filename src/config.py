from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    app_version: str
    db_name_type_prefix: str
    postgres_server: str
    postgres_port: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    environment: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding='utf-8')


    
    

