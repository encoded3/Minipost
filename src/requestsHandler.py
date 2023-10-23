import config
import requests
from bs4 import BeautifulSoup
try:
    str(config.minimail["address"])

    str(config.minimail["login"])
    str(config.minimail["password"])

    if not type(config.minimail["useproxy"]) == bool:
        raise ValueError("minimail.useproxy")


except Exception as e:
    raise ValueError("Invalid config value")


address = config.minimail["address"]
if address.endswith("/"):
    address = address[:len(address)-1]

login = config.minimail["login"]
password = config.minimail["password"]
proxy = {"http":config.proxy}
    

def getMessages():
    data = {
        "name": config.minimail["login"],
        "password": config.minimail["password"]
    }

    r = None

    try:
        if config.minimail["useproxy"]:
            r = requests.post(
                                address+"/login", 
                                data=data, 
                                proxies=proxy
                            )
        else:
            r = requests.post(
                                address+"/login", 
                                data=data
                            )
    except:
        return ["Не удалось загрузить сообщения :/"]

    soup = BeautifulSoup(r.text, "html.parser")

    parsedMessages = soup.find_all("li")
    
    messages = []
    for message in parsedMessages:
        Text = message.find_all("div")[0].text
        By = message.find_all("div")[1].text

        messages.append(Text + "\n\n"+By)
    
    return messages


def sendMessage(username:str, message:str, address:str):
    if address in config.mails.keys():
        address = config.mails[address]

    if address.endswith("/"):
        address = address[:len(address)-1]

    data = {
        "username": username,
        "message": message
    }

    r = None
    try:
        if config.useProxyForSend:
            r = requests.post(
                                address+"/send", 
                                data=data, 
                                proxies=proxy
                            )
        else:
            r = requests.post(
                                address+"/send", 
                                data=data
                            )
    except:
        return
    
    return r.status_code