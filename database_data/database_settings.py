from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:str
    DB_NAME:str
    DB_USER:str
    DB_PASSWORD:str 
    # postgresql+psycopg://user_name:password@host:port/db_name
    # postgresql+psycopg2://user:password@localhost/dbname
    @property
    def DATABASE_URL_asyncpg(self)-> str:
        """Async url"""
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def DATABASE_URL_psycopg(self)-> str:
        """Sync url"""
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='..env') #env_file='..env'

settings = Settings()