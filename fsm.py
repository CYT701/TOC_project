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

    def is_going_to_state_lightroast(self, event):
        text = event.message.text
        return text.lower() == "淺焙"

    def is_going_to_state_mediumroast(self, event):
        text = event.message.text
        return text.lower() == "中焙"

    def is_going_to_state_cityroast(self, event):
        text = event.message.text
        return text.lower() == "深焙"

    def is_going_to_backstate1(self, event):
        text = event.message.text
        return text.lower() == "ok"

    def is_going_to_backuser(self, event):
        text = event.message.text
        return text.lower() == "離開"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入焙度:")
        #self.go_back()

    '''def on_exit_state1(self):
        print("Leaving state1")'''

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "生命樹咖啡:\nhttps://zh-tw.facebook.com/lifetreesilkroadcoffee/\n雷巴咖啡:\nhttps://www.rebacoffee.com/\n咖啡匙:\nhttps://www.facebook.com/cuppingspoon/")
        self.go_back()
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "輸入[沖煮技巧]或[台南咖啡推薦]以獲得更多資訊")
        self.go_back()
    
    def on_enter_state_lightroast(self, event):
        print("I'm entering state_lightroast")

        reply_token = event.reply_token
        send_text_message(reply_token, "咖啡豆16g\n水溫:92~94度\n研磨度:二砂糖粗細\n悶蒸:30~50秒(視排氣狀況)\n手法:中小水由中心向外慢繞至150cc，待濾杯中液體流下一半後再注水至240cc")
        #self.go_back()

    def on_enter_state_mediumroast(self, event):
        print("I'm entering state_lightroast")

        reply_token = event.reply_token
        send_text_message(reply_token, "咖啡豆16g\n水溫:88~90度\n研磨度:二砂糖粗細\n悶蒸:20~40秒\n手法:中水由中心向外慢繞至150cc，待濾杯中液體流下一半後再中心注大水至240cc")
        #self.go_back()

    def on_enter_state_cityroast(self, event):
        print("I'm entering state_cityroast")

        reply_token = event.reply_token
        send_text_message(reply_token, "咖啡豆16g\n水溫:85~88度\n研磨度:二砂糖粗細略粗\n悶蒸:20秒\n手法:中水由中心注水至150cc，待濾杯中液體流下一半後再中心中水往外繞圈至240cc")
        #self.go_back()

    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, "首頁，輸入[說明]以獲得更多資訊")
        self.go_back()



