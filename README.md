# Brendwall project

## Установка и запуск

### Шаг 1: Клонирование репозитория

```
git clone git@github.com:d1g-1t/brendwall-project.git
cd brendwall-project
```

### Шаг 2: Создание виртуального окружения

```
python3.10 -m venv venv
source venv/Scripts/activate  # Для Windows
# source venv/bin/activate    # Для Unix/MacOS
```

### Шаг 3: Установка зависимостей

```
python -m pip install --upgrade pip && pip install -r requirements.txt
```

### Шаг 4: Применение миграций

```
python manage.py makemigrations
python manage.py migrate
```

### Шаг 5: Запуск сервера разработки

```
python manage.py runserver
```

После запуска проект будет доступен по ссылке: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Павел Охрим. [t.me/](https://t.me/d1g_it)

