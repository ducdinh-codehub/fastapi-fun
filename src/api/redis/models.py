from typing import Any
from redis import StrictRedis
import config
import json

def is_json(json_string):
    """
    Checks if a given string is a valid JSON.

    Args:
        json_string: The string to check.

    Returns:
        True if the string is valid JSON, False otherwise.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

class Redis:
    redis_manager: Any
    redis_cache: Any
    redis_host: str
    redis_port: int
    redis_db: int
    redis_username: str
    redis_password: str

    def __init__(self):
        self.redis_host = config.Settings().redis_server
        self.redis_port = config.Settings().redis_port
        self.redis_db = config.Settings().redis_db
        self.redis_username = config.Settings().redis_username
        self.redis_password = config.Settings().redis_password
        a = "asdasd"
        self.redis_manager = StrictRedis(host=self.redis_host, port=self.redis_port, db=self.redis_db, username=config.Settings().redis_username, password=config.Settings().redis_password)
        self.redis_cache = self.redis_manager.get_cache()
        
    def getItemRedisCache(self, key):
        value = self.redis_manager.get(key)
        return value
    
    def setItemRedisCache(self, key, value):
        isJson = is_json(value)
        if isJson:
            self.redis_manager.set(key, json.dumps(value))
        else:
            self.redis_manager.set(key, value)
    
    def setBitItemRedisCache(self, key, offset, value):
        self.redis_manager.setbit(key, offset, value)

    def getBitItemRedisCache(self, key, offset):
        value = self.redis_manager.getbit(key, offset)
        return value
    
    def getAllKeysInRedisCache(self):
        all_keys = []
        for key in self.redis_manager.scan_iter(match='*'):
            all_keys.append(key.decode('utf-8'))
        return all_keys
            
    def delItemsInRedisCache(self, keyList: list):
        # Keylist the list of keys
        self.redis_cache.delete_by_redis_keys(keyList)

    def flushAllRedisCache(self):
        self.redis_cache.flush()

    def closeRedisCache(self):
        self.redis_manager.close()        

