from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class RepositorySettings(BaseSettings):
    db_host: str = Field(default="localhost")
    db_port: str = Field(default="5432")
    db_user: str = Field(default="postgr")
    db_pass: str = Field(default="postgr")
    db_name: str = Field(default="postgr")


class Settings(BaseSettings):
    repository_settings: RepositorySettings = RepositorySettings()


settings: Settings = Settings()

#print(settings.repository_settings.db_user)
