from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LedgerLite"
    debug: bool = True
    database_name: str = "ledgerlite.db"

settings = Settings()

