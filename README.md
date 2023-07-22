# praktikum_new_diplom
Проект в разработке

Реализован тестовый вариант для размещения на локальном хосте.

Запуск установки контейнеров проекта:
```docker compose up -d```

После запуска проект готов к работе по адресу в браузере:

`localhost`                  - главная страница

`localhost/admin/`            - страница администратора



Реализованы базовые команды при запуске проекта:
`docker-compose exec backend python manage.py collectstatic --noinput`
`docker-compose exec backend python manage.py makemigrations`
`docker-compose exec backend python manage.py migrate`
`docker-compose exec backend python manage.py import_csv`

(docker-compose exec backend - варианты выполнения через терминал).

Создание суперюзера:
`docker-compose exec backend python manage.py createsuperuser`

Остановка тестового проекта и удаление контейнеров:
`docker compose down -v`

Проверка запуска контейнеров:
`docker ps`
`docker ps -a`

Образы контейнеров:
`docker images`

Удаление ненужных образов:
`docker rmi <ID container>`

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