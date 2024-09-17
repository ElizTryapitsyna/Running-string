# Running-string
Test case with running string on python and django

установить виртуальное окружение:
   `python -m venv venv`
установить  необходимые библиотеки: (cv2, numpy, transliterate, movis)\
провести миграции
    `python manage.py migrate`
запустить приложение
    `python manage.py runserver`

Работа с приложением:

Создание суперпользователя:
   python manage.py createsuperuser
Пример создания видео:
    http://127.0.0.1:8000?message=Привет, мир
