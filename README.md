Тестовый проект

Инструкция запуска:

Установить зависимости: <br>
pip install -r requirements.txt <br>
Выполнить миграции: <br>
python manage.py migrate <br>
Загрузить данные в БД из тестового json файла: <br>
python load_data.py <br>
Создать суперпользователя: <br>
python manage.py createsuperuser <br>
Запустить сервер: <br>
python manage.py runserver
