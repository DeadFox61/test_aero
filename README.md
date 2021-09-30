Инструкция запуска:

Установить зависимости: 
pip install -r requirements.txt
Выполнить миграции:
python manage.py migrate
Загрузить данные в БД из тестового json файла:
python load_data.py
Создать суперпользователя:
python manage.py createsuperuser
Запустить сервер:
python manage.py runserver
