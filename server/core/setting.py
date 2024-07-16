from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "crud"
    VERSION: str = "1.0.0"
    API_V1_STR: str = ""
    DATABASE_URL: str = "mysql+pymysql://test:Testtest12@localhost:3306/board?charset=utf8mb4"
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    bucket_name: str = "#"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
