# SubscribeService

SubscribeService - это веб-сервис, построенный с использованием Django и PostgreSQL, который предоставляет RESTful API для управления лентой статей для пользователей с различными ролями.

## Оглавление
- [Установка](#установка)
- [Настройка](#настройка)
- [Использование](#использование)
- [API эндпоинты](#api-эндпоинты)
- [Тестирование](#тестирование)
- [Автор](#автор)

## Установка

### Используемый стек
- Python 3.12+
- PostgreSQL
- Virtualenv

### Шаги установки
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/asdzog/SubscribeService.git
    cd SubscribeService
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source myenv/bin/activate  # для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корневой директории проекта со следующим содержимым:
    ```env
    SECRET_KEY='your_secret_key'
    DEBUG='True'  # или 'False'
    POSTGRES_DB='your_db_name'
    POSTGRES_USER='your_db_username'
    POSTGRES_PASSWORD='your_db_password'
    POSTGRES_PORT='your_db_port'
    ADM_PSW='your_admin_password'
    ADM_EMAIL='your_admin_email'
    ```

5. Настройте `settings.py` для использования переменных окружения:
    ```python
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()

    # Базовая директория проекта
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG') == 'True'
    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }
    ```

6. Примените миграции и создайте суперпользователя:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

7. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Использование

### Регистрация пользователя
Используйте следующий запрос для регистрации нового пользователя:
```bash
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "Password123"}'
   ```
## API эндпоинты

### Публичные статьи
* `GET /api/articles/public/` - Получить все публичные статьи

### Пользователи
* `POST /api/users/` - Регистрация нового пользователя

### Статьи
* `GET /api/articles/` - Получить все статьи (публичные для неавторизованных, все для авторов)
* `POST /api/articles/` - Создать новую статью (только для авторов)
* `GET /api/articles/{id}/` - Получить статью по ID
* `PUT /api/articles/{id}/` - Обновить статью (только автор)
* `DELETE /api/articles/{id}/` - Удалить статью (только автор)

## Тестирование

Для тестирования API вы можете использовать такие инструменты, как Postman или curl. Примеры curl запросов приведены выше.

## Автор

* **Aleksey Dzogiy**
* Telegram: [click here to contact me](https://t.me/aleksey_dz)
* Email: asdzog@mail.ru

