import requests
import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=300):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler("882852026:AAHDbszLGh7pWRVJlzbh6q-HRlky_KbjcOc")
greetings = ('хай', 'привет', 'ку', 'здорово')
degree = ('покедова', 'давай', 'иди нахуй')
drink = ('го пить', 'го бухать', 'го по пиву')
boobs = ('скинь сиськи', 'скинь фотку', 'сиси')
sex = ('го ебаться', 'хочу тебя', 'потрахаемся?')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Спи псина, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрейший денечек, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Вечер в хату, {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in drink:
            greet_bot.send_message(last_chat_id, 'го.когда?')
        elif last_chat_text.lower() in boobs:
            greet_bot.send_message(last_chat_id, 'пусть шлюхи твои кинут')
        elif last_chat_text.lower() in sex:
            greet_bot.send_message(last_chat_id, 'ты в зеркало сначала посмотри')
        elif last_chat_text.lower() in degree:
            greet_bot.send_message(last_chat_id, 'Ну и пиздуй')
            break

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()