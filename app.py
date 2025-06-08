import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv("BOT_TOKEN") or "7281967575:AAHCXsMmKwiGNNEBvRxCj30LBzfi2TrMnL0"
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Basic signal handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! You'll start receiving signals here.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"📡 Signal received: {message.text}")

# Webhook endpoint
@app.route(f"/{API_TOKEN}", methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

# Home route to confirm server is running
@app.route("/", methods=["GET"])
def index():
    return "🟢 Bot is live!", 200

# Run Flask on the dynamic port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
