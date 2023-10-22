from textual.app import App, ComposeResult
from textual.containers import Container, ScrollableContainer
from textual.screen import Screen
from textual.widgets import *
from styles import *
from requestsHandler import getMessages, sendMessage
from config import nickname

SCENE = None

mainScene = None


class SendPost(Screen):
    CSS_PATH = "styles.tcss"
    BINDINGS = [("q", "pop_screen", "Выйти в главное меню")]

    def compose(self):
        self.messageArea = TextArea("Сообщение", theme="vscode_dark")
        self.recipient = Input(placeholder="Название почты из конфига Minipost или b32 ссылка на почту minimail")
        self.useproxy = Checkbox("Использовать прокси")

        yield Header(show_clock=True)

        yield self.recipient
        yield self.messageArea
        yield self.useproxy
        yield Button("Отправить", id="send")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "send":
            if self.recipient.value != "":
                status = sendMessage(nickname, self.messageArea.text, self.recipient.value, self.useproxy.value)
                
                if status == 200:
                    self.notify("Отправлено!", title="MiniPost")
                else:
                    self.notify("Не удалось отправить сообщение :(", title="MiniPost", severity='error')


class CheckMail(Screen):
    messages = getMessages()

    CSS_PATH = "styles.tcss"
    BINDINGS = [("q", "pop_screen", "Выйти в главное меню")]

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "exit":
            pass

    def compose(self):
        yield Header(show_clock=True)
        yield Title("Входящие\n")

        text = ""
        for message in self.messages:
            separatorLength = 0
            for line in message.split("\n"):
                if len(line) > separatorLength:
                    separatorLength = len(line)

            try:
                Label(message)
            except:
                message = "Не удалось вывести сообщение :/"

            text += "-"*separatorLength + "\n\n"
            text += message + "\n\n"
            text += "-"*separatorLength + "\n\n\n"


        yield ScrollableContainer( Label(text) )
        
        yield Footer()


class Main(App):
    CSS_PATH = "styles.tcss"
    BINDINGS = [("q", "pop_screen", "Выйти")]

    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "checkmail":
                self.push_screen(CheckMail())
            
            case "sendpost":
                self.push_screen(SendPost())

    def compose(self):
        yield Header(show_clock=True)
        yield Title("Добро пожаловать в Minipost!\n")

        yield Button("Отправить письмо", id="sendpost")
        yield Button("Просмотреть входящие", id="checkmail")

        yield Footer()


mainScene = Main

if __name__ == "__main__":
    SCENE = "Main"
    app = Main()

    app.title = "Minipost"
    app.run()
