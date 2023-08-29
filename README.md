# Тестовое задание для Галиуллин А.М.

Создать файл .env в корне проекта, внести следующие переменные:

```
POSTGRES_HOST=test_task_pg

POSTGRES_PORT=5432

POSTGRES_DB=postgres

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

```

________________________________________________________________

Развернуть в докере:
docker-compose up -d --build

Сервер:
http://localhost:8000/

Чат-бот:
*Для взаимодействий с чат ботом необходимо передавать message и session_id, полученный при первом взаимодействии*
http://localhost:8000/chatbot/



Аутентификация по email и password:
http://localhost:8000/api-token-auth/

Получение данных о зарегистрированном пользователе по токену:
http://localhost:8000/user_data/