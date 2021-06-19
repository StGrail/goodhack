# Goodhack
Проект для online hackathon [хакатондобра.рф](хакатондобра.рф).
Рабочая версия сайта расположена [тут](https://musora-net.herokuapp.com)

Сайт помогает собирать заявки на проведение викторин, выставок и составлять отчеты по проведённым мероприятиям.

## Установка / Использование 
### Скачайте и установите зависимости
Выполните в консоли:
```
https://github.com/StGrail/goodhack.git
cd goodhack
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Выполните настройку
Переименуйте файл env.example в .env и замените  следующие данные:
```
DJANGO_SECRET_KEY = DJANGO_SECRET_KEY

DB_NAME = Название базы данных
DB_USER = Пользователь базы данных
DB_PASSWORD = Пароль базы данных

ADMIN_EMAIL = email для получения писем о новых заявках
```
### Наполните базу данных и создайте админа
```
python manage.py migrate
python manage.py createsuperuser
```

### Запустите сервер
```
python manage.py runserver
```
### Перейдите на [локальный сервер](http://127.0.0.1:8000)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)