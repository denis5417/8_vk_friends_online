# Кто онлайн вк

Скрипт принимает на вход путь к файлу с app_id, логином и паролем и выводит имена и фамилии друзей онлайн

# Установка и использование

Python 3 должен быть заранее установлен. Используйте pip3, чтобы установить зависимости:

```bash
pip3 install -r requirements.txt 
```

Использование:

```bash
$ python3 vk_friends_online.py <path_to_file_with_credentials>
Roct Bb
Юлия Рожанская
Влада Ларина
Яна Бутримайте
Макс Колганов
Алексей Наумов
Артемий Быков
Никита Сикорский
Павел Никулин
Элина Риянова
Saveliy Dedkov
Юлия Молчанова
Вова Кузнецов
Даша Орехова
Артём Ксеневич
Диана Веснянцева
Леонид Крупнов
Дмитрий Кукушкин
Адам Шевченко
Алексей Колесников
Анастасия Русова
Alexander Ghost
Даниил Мажурин
```

Файл должен выглядеть следующим образом:
```
<app_id>
<login>
<password>
```
[Пример файла](https://pastebin.com/raw/SshzM8yi)

Рекомендовано использовать [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для лучшей изоляции.

# Цели проекта

Этот код написан в образовательных целях. Обучающий курс для веб-девелоперов - [DEVMAN.org](https://devman.org)
