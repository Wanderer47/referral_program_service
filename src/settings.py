from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class RepositorySettings(BaseSettings):
    host: str = Field(default="localhost")
    port: str = Field(default="5432")
    user: str = Field(default="postgr")
    passw: str = Field(default="postgr")
    name: str = Field(default="postgr")


class TransportSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 5000


class Settings(BaseSettings):
    repository_settings: RepositorySettings = RepositorySettings()
    transport_settings: TransportSettings = TransportSettings()
