import datetime

from pyrogram import Client, filters, types


api_id = '12828688'
api_hash = '9913a7b069b10a421077d01519773293'
session_name = ''


app = Client(session_name, api_id, api_hash, parse_mode='HTML')


@app.on_message(filters.command('start'))
def start_message_handler(client: Client, message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(['➕ Добавить канал',
                                          '✖️ Удалить канал'])
    text = '🛠 Меню'
    client.send_message(message.chat.id, text,
                        reply_markup=keyboard)


@app.on_message()
def message_handler(client, message: types.Message):
    pass


app.run()
