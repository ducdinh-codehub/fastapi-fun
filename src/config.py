from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    app_version: str
    database_url: str
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding='utf-8')


    
    

