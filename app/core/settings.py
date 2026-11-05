from pydantic import BaseModel, BaseSettings, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSetting(BaseModel):
    app_name: str = "Board API"
    debug: bool = False

class DatabaseSettings(BaseModel):
    url: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    database_url: str = Field(validation_alias="DATABASE_URL")
    
    @property
    def app(self) -> AppSetting:
        return AppSetting()
    
    @property
    def db(self) -> DatabaseSettings:
        return DatabaseSettings(url=self.database_url)