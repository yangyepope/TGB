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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me")
    print(update.effective_chat)
    print(update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Your message is This")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="My name is <NAME>")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please, tell me your name")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_chat.id)
    print(update.effective_chat)
    print(update)
    print(update.message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.args)
    text_caps = ' '.join(context.args).upper()
    print(text_caps)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# 设置内联
async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    query = update.inline_query.query
    print(query)
    if not query:
        return

    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    print(results)
    await context.bot.answer_inline_query(update.inline_query.id, results)


# 未知命令过滤
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")




if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()

    # 创建handler
    start_handler = CommandHandler('start', start)
    # 过滤命令
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)

    # 内联handler
    inline_caps_handler = InlineQueryHandler(inline_caps)

    # 未知命令
    unknown_handler = MessageHandler(filters.COMMAND, unknown)



    # 添加handler
    application.add_handler(echo_handler)
    application.add_handler(start_handler)
    application.add_handler(caps_handler)

    application.add_handler(inline_caps_handler)

    application.add_handler(unknown_handler)

    application.run_polling()
