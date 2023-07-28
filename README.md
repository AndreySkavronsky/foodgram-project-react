![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Описание проекта

Foodgram - «Продуктовый помощник». Сервис на котором пользователи могут публиковать кулинарные рецепты, подписываться на других авторов и добавлять рецепты в избранное. Функция «Список покупок» позволяет пользователям скачать весь список ингредиентов, из понравившегося рецепта, в формате txt. 

## Сервис доступен по адресам (на время работы над проектом):
https://foodgrammy.sytes.net/                           Главная страница<br>
https://foodgrammy.sytes.net/admin/                     Административная страница<br>
https://foodgrammy.sytes.net/api/                       API сайта<br>
https://foodgrammy.sytes.net/signup                     Регистрация нового пользователя<br>
https://foodgrammy.sytes.net/recipes                    Список рецептов сервиса<br>
https://foodgrammy.sytes.net/subscriptions              Подписки пользователя на авторов<br>
https://foodgrammy.sytes.net/recipes/create             Создание нового рецепта<br>
https://foodgrammy.sytes.net/recipes/<user_name>/edit   Редактирование рецепта (индивидуальная страница для каждого пользователя)<br>
https://foodgrammy.sytes.net/favorites                  Избранные рецепты пользователя<br>
https://foodgrammy.sytes.net/cart                       Список покупок<br>
https://foodgrammy.sytes.net/change-password            Смена пароля<br>

## Тестовые учётные записи:

**Superuser**:<br>
__ADMIN#1__
login: `4foodgram@gmail.com` <br>
Password: `LimeLight` <br>

**Пользователи**

__USER#1__
login: `12@rambler.ru` <br>
Password: `ONETWOTHREE` <br>

__USER#2__
login: `23@rambler.ru` <br>
Password: `TWOTHREEFOUR` <br>

__USER#3__
login: `34@rambler.ru` <br>
Password: `THREEFOURFIVE` <br>

## Размещение на удалённом сервере:
- Создаём директорию проекта, например: foodgram.<br>
```bash
mkdir foodgram
cd foodgram
```
- Копируем в директорию файл docker-compose.production.yml из проекта.<br>
- Создаём в директории файл .env, прописываем в файле константы:<br>
```
POSTGRES_USER=<логин для базы данных>
POSTGRES_PASSWORD=<пароль для базы данных>
POSTGRES_DB=<имя базы данных>
DEBUG=<режим разработчика:True/False>
SECRET_KEY=<секретный ключ джанго>
ALLOWED_HOSTS=<разрешенные хосты>
DB_HOST=<название контейнера>
DB_PORT=<порт для подключения к БД>
FOODGRAM_PORT=<порт проекта на сервере>
DOCKER_NAME=<логин на Dockerhub>
```
- Запускаем сборку проекта из образов:<br>
```sudo docker compose -f docker-compose.production.yml up -d```
- Заходим в backend контейнер:<br>
```sudo docker exec -it foodgram_backend bash```
- Выполняем команды настройки проекта:<br>
_*(Данные команды настроены на автоматическое выполнение при сборке проекта из образов_<br>
_ниже приведены примеры для ручного ввода команд)_<br>
```python manage.py collectstatic --noinput```
```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py csv_import```
- Команда создания Superuser:<br>
```python manage.py createsuperuser```

## Размещение на локальном хосте:

Запуск установки контейнеров проекта:
```docker compose up -d```

После запуска проект готов к работе по адресу в браузере:

`localhost`                  - главная страница

`localhost/admin/`            - страница администратора



Реализованы базовые команды при запуске проекта:
```
docker-compose exec backend python manage.py collectstatic --noinput
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py import_csv
```

(docker-compose exec backend - варианты выполнения через терминал).

Создание суперюзера:
```docker-compose exec backend python manage.py createsuperuser```

Остановка тестового проекта и удаление контейнеров:
```docker compose down -v```

Проверка запуска контейнеров:
```docker ps```
```docker ps -a```

Образы контейнеров:
```docker images```

Удаление ненужных образов:
```docker rmi <ID container>```

Примеры API

```
Recipe List
GET /api/recipes/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "tags": [
                {
                    "id": 1,
                    "name": "Завтрак",
                    "color": "#FF69B4",
                    "slug": "breakfast"
                }
            ],
            "author": {
                "id": 2,
                "email": "12@rambler.ru",
                "username": "12",
                "first_name": "1",
                "last_name": "2",
                "is_subscribed": false
            },
            "ingredients": [
                {
                    "id": 703,
                    "name": "кофе растворимый",
                    "measurement_unit": "г",
                    "amount": 5
                },
                {
                    "id": 1032,
                    "name": "молоко",
                    "measurement_unit": "г",
                    "amount": 50
                },
                {
                    "id": 252,
                    "name": "вода",
                    "measurement_unit": "г",
                    "amount": 150
                },
                {
                    "id": 1547,
                    "name": "сахар",
                    "measurement_unit": "г",
                    "amount": 5
                }
            ],
            "is_favorited": false,
            "is_in_shopping_cart": false,
            "name": "Кофе с молоком",
            "image": "http://localhost/media/recipes/file_d9MAwE5.png",
            "text": "Вскипятить воду, заварить кофе, добавить молока.",
            "cooking_time": 2
        },
        {
            "id": 1,
            "tags": [
                {
                    "id": 1,
                    "name": "Завтрак",
                    "color": "#FF69B4",
                    "slug": "breakfast"
                },
                {
                    "id": 4,
                    "name": "Перекус",
                    "color": "#9ACD32",
                    "slug": "snack"
                }
            ],
            "author": {
                "id": 1,
                "email": "21@rambler.ru",
                "username": "21",
                "first_name": "2",
                "last_name": "1",
                "is_subscribed": false
            },
            "ingredients": [
                {
                    "id": 594,
                    "name": "кефир 3,2%",
                    "measurement_unit": "г",
                    "amount": 100
                }
            ],
            "is_favorited": false,
            "is_in_shopping_cart": true,
            "name": "Кефир",
            "image": "http://localhost/media/recipes/file.png",
            "text": "Налить кефир в стакан",
            "cooking_time": 1
        }
    ]
}
```
API/USERS/

```
User List
GET /api/users/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "email": "21@rambler.ru",
            "username": "21",
            "first_name": "2",
            "last_name": "1",
            "is_subscribed": false
        },
        {
            "id": 2,
            "email": "12@rambler.ru",
            "username": "12",
            "first_name": "1",
            "last_name": "2",
            "is_subscribed": false
        }
    ]
}
```

## Автор
Андрей Скавронский https://github.com/AndreySkavronsky