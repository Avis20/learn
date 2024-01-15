from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Настройки PostgreSQL
class PostgresConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='postgres_')

    echo_log: bool = Field(default=False)

    host: str = Field(default='localhost')
    port: int = Field(default=5432)
    db: str = Field(default='billing_database')
    user: str = Field(default='billing')
    password: str = Field(default='billing')

    @property
    def database_url(self):
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

