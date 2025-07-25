from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
print(TOKEN)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ну привет что ли. Как тебя зовут?')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'Арина':
        await update.message.reply_text('Привет мандаринка!:3')
    if update.message.text == 'Никита':
        await update.message.reply_text('Мой создатель')
    if update.message.text == 'Петухов':
        await update.message.reply_text('))))))')


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()


if __name__ == '__main__':
    main()
