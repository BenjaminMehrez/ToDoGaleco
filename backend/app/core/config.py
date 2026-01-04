from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class Settings(BaseSettings):

  APP_NAME: str = "ToDo"
  APP_VERSION: str = '1.0.0'

  ENVIRONMENT: str = "development"
  DATABASE_URL: str
  DEBUG: bool
  SECRET_KEY: str
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


  model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
  return Settings()
