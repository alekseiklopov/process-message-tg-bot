import os
import telebot

TG_TOKEN = os.environ.get("TG_TOKEN")
bot = telebot.TeleBot(TG_TOKEN)
my_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
my_keyboard.row("Информация")


@bot.message_handler(commands=["start"])
def start_message(msg):
    bot.send_message(msg.chat.id,
                     "Добро пожаловать! Пожалуйста, отправьте что-нибудь или нажмите на кнопку \"Информация\"",
                     reply_markup=my_keyboard)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "информация":
        bot.send_message(message.chat.id, """Что бот делает?
1. Сохранять аудиосообщения из диалогов в базу данных (СУБД или на диск) по идентификаторам пользователей.
2. Конвертировать все аудиосообщения в формат wav с частотой дискретизации 16kHz.
Формат записи: uid —> [audio_message_0, audio_message_1, ..., audio_message_N].
3. Определять, есть ли лицо на отправляемых фотографиях или нет, и сохранять только те, где оно есть.

Какие технологии использует?
Telebot, Docker, Tensorflow, Flask, AWS

Кто создал?
Алексей Клопов - @itsmealeksei - klopov.pw""")
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(content_types=["document"])
def handle_docs(message):
    bot.reply_to(message, "Отправьте фото/аудиосообщение, не файл!")


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    answer = ["type of downloaded file: {}.".format(type(downloaded_file)),
              "downloaded file: {}.".format(downloaded_file)]
    # answer = process_photo(downloaded_file)
    bot.reply_to(message, answer)


@bot.message_handler(content_types=["voice"])
def handle_audio(message):
    bot.reply_to(message, message)


bot.polling()
