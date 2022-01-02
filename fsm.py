from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "沖煮技巧"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "台南咖啡推薦"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "說明"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入焙度:")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "生命樹咖啡:\nhttps://zh-tw.facebook.com/lifetreesilkroadcoffee/")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "輸入[沖煮技巧]或[台南咖啡推薦]以獲得更多資訊")
        self.go_back()
    
    def on_exit_state3(self):
        print("Leaving state3")
