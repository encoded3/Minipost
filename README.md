# Minipost
Minipost - это простой клиент для [Minimail](https://github.com/Grisshink/minimail/) I2P, который поддерживает просмотр и отправку писем.

## Установка и запуск

Для исправной работы клиента должны быть установлены [Python](https://www.python.org/downloads/) и [Git](https://git-scm.com/downloads). После чего склонируйте репозиторий.

### Установка

Для установки в UNIX-подобных системах:
```bash
git clone https://github.com/encoded3/Minipost.git
cd minipost
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Для установки в Windows:
```bash
git clone https://github.com/encoded3/Minipost.git
cd minipost
python -m venv env
.\Scripts\activate.bat
pip install -r requirements.txt
```

### Запуск
Для UNIX-подобных систем используйте bash-скрипт `minipost.sh`

Для Windows используйте `minipost.bat`


## Конфигурация
Для конфигурации клиента используйте файл `config.py`, который располагается в папке  `src`

```python
proxy = "http://127.0.0.1:4444" # Прокси-сервер

minimail = {
    "address": "http://127.0.0.1:3000", # URL для просомтра входящих сообщений
    "useproxy": False, # True/False - использование прокси для просмотра входящих сообщений

    "login": "admin",
    "password": "superstrongpassword"
}

mails = { # Названия почт, которые автоматически заменяются на b32 ссылку
    "mail1": "b32link",
    "mail2": "b32link"
}

nickname = "unknown" # Имя пользователя, которое применяется при отправки сообщений
```
