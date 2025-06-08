from flask import Flask, request
import telegram

TOKEN = "7281967575:AAHCXsMmKwiGNNEBvRxCj30LBzfi2TrMnL0"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "DarrellScalpBot is Live"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text.lower() == "btc now":
        bot.send_message(chat_id=chat_id, text="Buy BTC/USD at 69,200. Stop loss at 68,800.")

    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
