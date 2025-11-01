import asyncio
from listener import start_listener
from utils import log

async def main():
    log("🚀 Orange Call Bot started successfully!")
    await start_listener()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("🛑 Bot stopped manually.")

import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from listener import start_listener
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

app = Flask(__name__)

@app.route('/')
def home():
    return "Orange Bot is alive!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is online!")

def run_bot():
    app_telegram = ApplicationBuilder().token(BOT_TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    start_listener()
    app_telegram.run_polling()

if __name__ == '__main__':
    # Run bot in a background thread
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=PORT)
