from telegram import Update
from telegram.ext import Application, ContextTypes

Token = "7123034213:AAG8PiN5v_yUayDwqUhROZVvI1XYq5EBtiA"
chat_id = 5415202864


async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text='One message every minute')


async def callback_30(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text='A single message with 30s delay')


application = Application.builder().token(Token).build()
job_queue = application.job_queue

# 定时任务
# job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)
job_queue.run_once(callback_30, 30)

application.run_polling()
