from flask_vk_bot import *
from flask_vk_bot import flask_app


@bot_app.route('main')
def main(token):
    msg = Message(peer_id=token.user_id, text="Главное меню")
    msg.add_button(label='Главное меню', menu_id='main')
    msg.add_button(label='Второе меню', menu_id='menu2')
    msg.add_button(label='Третье меню', menu_id='menu3')
    return msg


@bot_app.route('menu2')
def main(token):
    text = '\n - '.join([m.text for m in token.prev_msg])
    msg = Message(peer_id=token.user_id, text="Второе меню\n" + text)
    msg.add_button(label='Главное меню', menu_id='main')
    return msg


@bot_app.route('menu3')
def main(token):
    msg = Message(peer_id=token.user_id, text="Третье меню")
    msg.add_button(label='Главное меню', menu_id='main')
    msg.add_button(label='Второе меню', menu_id='menu2')
    return msg


if __name__ == '__main__':
    flask_app.app.run()
