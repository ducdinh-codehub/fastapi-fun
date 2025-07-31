from pydantic_settings import BaseSettings

class CommonConfigs(BaseSettings):
    app_name: str
    admin_email: str
    app_version: str
    db_name_type_prefix: str
    postgres_server: str
    postgres_port: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    environment: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    backend_cors_origins: str
    smtp_host: str
    smtp_user: str
    smtp_password: str
    emails_from_email: str
    smtp_tls: bool
    smtp_ssl: bool
    smtp_port: int
    redis_server: str
    redis_port: int
    redis_db: int
    redis_username: str
    redis_password: str
    rabbitmq_user: str
    rabbitmq_password: str
    rabbitmq_host: str
    rabbitmq_port: int

    