import logging
import os

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, MessageHandler, filters, \
    InlineQueryHandler

# 日志配置
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)',
#                     level=logging.INFO
#                     )

logging.getLogger('httpx').setLevel(logging.WARNING)

Token = '7123034213:AAG8PiN5v_yUayDwqUhROZVvI1XYq5EBtiA'


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_chat.id)
    print(update.effective_chat)
    print(type(update))
    print(update)
    print(context)
    print(update.message)
    if update.message.text == 'll':
        text = "微信汇率"
    else:
        text = "XXX宝汇率"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)




if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(echo_handler)
    application.run_polling()
