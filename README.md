  # Репозиторий содержит файлы исходного кода сервиса для обмена книгами

## Userstory

- [x] Регистрация
- [x] Авторизация
- [x] Пользователь может опубликовать коллекцию книг
- [] Посмотреть коллекции других пользователей
- [] Отметить у себя экземпляры книг, отданных на прочтение
- [] Получать различные уведомления о состоянии коллекции книг

### Шаги:

```shell
git clone https://github.com/chuckis/bookya.git
cd bookya
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Проект в стадии разработки, stay tuned!
