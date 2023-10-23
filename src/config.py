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

useProxyForSend = True # True/False - использование прокси для отправки сообщений