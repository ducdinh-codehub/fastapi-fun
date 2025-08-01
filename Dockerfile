FROM python:3.13-slim

WORKDIR /MYPRJ

COPY ./requirements/dev.txt /MYPRJ/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /MYPRJ/requirements.txt

COPY . .

CMD ["fastapi", "run", "./src/main.py", "--port", "8000"]

ENV APP_NAME="Smart Agricultural App" \
    ADMIN_EMAIL=dinhduc4work@gmail.com \
    APP_VERSION=1.0.0 \
    DB_NAME_TYPE_PREFIX=postgresql:// \
    ENVIRONMENT=local\
    SECRET_KEY=081874c919e144e387d37b4ce8542586f197301fbc82cd4a66278e324d8cfafa \
    ALGORITHM=HS256\
    ACCESS_TOKEN_EXPIRE_MINUTES=30\
    BACKEND_CORS_ORIGINS=http://localhost:3000,https://localhost:3000\
    SMTP_HOST=smtp.gmail.com\
    SMTP_USER=dinhduc4testing@gmail.com\
    SMTP_PASSWORD=hxkvunbtubytsdmq\
    EMAILS_FROM_EMAIL=clientservicebot@gmail.com\
    SMTP_TLS=True\
    SMTP_SSL=False\
    SMTP_PORT=465\
    POSTGRES_SERVER=localhost\
    POSTGRES_PORT=5432\
    POSTGRES_DB=agrismart\
    POSTGRES_USER=postgres\
    POSTGRES_PASSWORD=123456789\
    REDIS_SERVER=localhost\
    REDIS_PORT=6379\
    REDIS_DB=0\
    REDIS_USERNAME=dinhduc4testing\
    REDIS_PASSWORD=111111\
    RABBITMQ_USER=guest\
    RABBITMQ_PASSWORD=guest\
    RABBITMQ_HOST=localhost\
    RABBITMQ_PORT=5672\
    AMQP_URL=amqp://guest:guest@rabbitmq

EXPOSE 8000