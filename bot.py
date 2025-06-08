from flask import Flask, request
import telegram
import os

TOKEN = "7281967575:AAHCXsMmKwiGNNEBvRxCj30LBzfi2TrMnL0"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "DarrellScalpBot is live."

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.lower()

    if "btc now" in text:
        bot.send_message(chat_id=chat_id, text="📈 Signal: Buy BTC/USD @ 69,200 | SL: 68,800")
    elif "gold now" in text:
        bot.send_message(chat_id=chat_id, text="📈 Signal: Buy XAU/USD @ 2,355 | SL: 2,342")

    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns the port
    app.run(host="0.0.0.0", port=port)

