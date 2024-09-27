import os
from dotenv import load_dotenv
import telebot
import qrcode
from io import BytesIO


load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


user_states = {}


@bot.message_handler(commands=['textqr'])
def textqr_command(message):
    bot.reply_to(message, "Write a link or text word to convert it to a QR code.")
    user_states[message.chat.id] = "waiting_for_input"


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.id in user_states and user_states[message.chat.id] == "waiting_for_input":
        text = message.text
        qr_image = generate_qr_code(text)
        bot.send_photo(message.chat.id, qr_image)
        del user_states[message.chat.id]
    else:
        response = (
            "Use the Following Command:\n"
            "/textqr - Convert Text to QR Code"
        )
        bot.reply_to(message, response)
        
    
def generate_qr_code(text):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0) 
    return img_byte_array
        

bot.infinity_polling()