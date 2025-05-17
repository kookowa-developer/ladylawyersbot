
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Telegram bot tokeningiz (ehtiyot bo‘ling, ochiq joyda ulashmang)
TOKEN = "7813923465:AAHgJMHRlTX7u8b5uMJ-mH3_m5Z2Cqqfgdw"
bot = telebot.TeleBot(TOKEN)

# /start komandasi uchun salomlashuv va raqam tugmalari
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("📞 Tezkor raqam: 1146", url="tel:1146"),
        InlineKeyboardButton("📞 Tezkor raqam: 102", url="tel:102")
    )
    bot.send_message(
        message.chat.id,
        "👋 Assalomu alaykum!\n\nMen ayollar huquqlari bo‘yicha O‘zbekiston Respublikasi qonunchiligiga asoslangan chatbotman.\nSavolingizni yozing.",
        reply_markup=markup
    )

# Foydalanuvchi xabarlarini qabul qilish va javob berish
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    # Admin bilan bog‘lanish uchun maxsus javob
    if "admin" in text or "bog‘lanish" in text or "aloqa" in text:
        bot.send_message(message.chat.id, "📩 Birozdan so‘ng sizga bog‘lanamiz.")
    else:
        bot.send_message(message.chat.id, "🤖 Iltimos, kuting... AI yordamida javob tayyorlanmoqda.")

        # Oddiy andoza javoblar (AI o‘rnini bosuvchi)
        if "mehnat" in text:
            bot.send_message(message.chat.id, "👩‍💼 Ayollarning mehnat huquqlari Mehnat kodeksi bilan himoyalangan.")
        elif "taʼlim" in text or "ta'lim" in text:
            bot.send_message(message.chat.id, "🎓 Ayollar taʼlim olish huquqiga ega. Bu huquq Konstitutsiya bilan kafolatlangan.")
        elif "huquq" in text:
            bot.send_message(message.chat.id, "📚 Ayollar umumiy inson huquqlaridan tashqari, maxsus ijtimoiy himoya huquqlariga ham egadir.")
        else:
            bot.send_message(message.chat.id, "❓ Savolingiz qabul qilindi. Tez orada javob beramiz.")

# Botni ishga tushurish
bot.polling()
