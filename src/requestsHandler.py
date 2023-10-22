import config
import requests

import AdvancedHTMLParser
HTML = AdvancedHTMLParser.AdvancedHTMLParser()

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

    HTML.parseStr(r.text)

    parsedMessages = HTML.getElementsByTagName("a")
    
    messages = []
    for message in parsedMessages:
        #message = AdvancedHTMLParser.Tags.AdvancedTag
        
        #Text = message[0].textContent
        Nodes = message.getAllNodes()

        Text = Nodes[1].textContent
        By = Nodes[3].textContent

        messages.append(Text + "\n\n"+By)
    
    return messages


def sendMessage(username:str, message:str, address:str, useproxy:bool):
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
        if useproxy:
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
        return None
    
    return r.status_code