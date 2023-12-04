from aiopg.sa import create_engine
from aiopg.sa import SAConnection
from fastapi import FastAPI
import uvicorn

from settings import Settings


class Application:
    def __init__(self, settings: Settings):
        self.settings = settings

    def _get_db_uri(self, db_settings) -> str:
        db_settings = self.settings.repository_settings
        return f"postgresql://{db_settings.user}:{db_settings.passw}" +\
               f"@{db_settings.host}:db_settings.db_port" +\
               f"/{db_settings.name}"

    def run(self, transport: FastAPI):
        settings = self.settings.transport_settings
        uvicorn.run(
                transport,
                host=settings.host,
                port=settings.port,
                timeout_keep_alive=0
                )


    async def db_engine(self):
        db_settings = self.settings.repository_settings
        async with create_engine(
                                user=db_settings.user,
                                database=db_settings.name,
                                host=db_settings.host,
                                password=db_settings.passw
                                ) as engine:
            self.engine = engine

    async def get_db_connection(self) -> SAConnection:
        async with self.engine.acquire() as conn:
            return conn

    def db_disconnect(self):
        self.engine.close()


settings: Settings = Settings()
application = Application(settings)

#application.run(transport)
