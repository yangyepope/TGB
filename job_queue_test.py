from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler
from format_test import Style

Token = "7123034213:AAG8PiN5v_yUayDwqUhROZVvI1XYq5EBtiA"


# chat_id = 5415202864
# chat_id = -1002073339732


# async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=chat_id, text='One message every minute')


# async def callback_30(context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=chat_id, text='A single message with 30s delay')


async def callback_alarm(context: ContextTypes.DEFAULT_TYPE):
    # Beep the person who called this alarm:
    print(context.job)
    await context.bot.send_message(chat_id=context.job.chat_id,
                                   text='<b>BEEP</b><code>' + context.job.data + '</code>!', parse_mode='HTML')


async def callback_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(chat_id=chat_id, text='Setting a timer for 1 minute!')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, 10, data=name, chat_id=chat_id)


application = Application.builder().token(Token).build()
# job_queue = application.job_queue

timer_handler = CommandHandler('timer', callback_timer)
application.add_handler(timer_handler)

# 定时任务
# job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

# job_minute.enabled = False  # Temporarily disable this job
# job_minute.schedule_removal()  # Remove this job completely

# job_queue.run_once(callback_30, 30)


application.run_polling()
