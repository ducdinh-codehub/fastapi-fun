from pydantic_settings import SettingsConfigDict

from models import CommonConfigs
class Settings(CommonConfigs):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding='utf-8')


    
    

