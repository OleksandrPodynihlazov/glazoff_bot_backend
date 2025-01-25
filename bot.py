from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters,
)
from config import BOT_TOKEN, BOT_USERNAME, SUPPORT_CONTACT
import json


# mini app
async def launch_web_ui(update: Update, callback: CallbackContext):
    # display our web-app!
    kb = [
        [
            KeyboardButton(
                "Відкрити міні-додаток",
                web_app=WebAppInfo(
                    "https://front-deploy-8r81.onrender.com/"
                ),  # obviously, set yours here.
            )
        ]
    ]
    await update.message.reply_text(reply_markup=ReplyKeyboardMarkup(kb))


async def web_app_data(update: Update, context: CallbackContext):
    if update.message.web_app_data:
        try:
            # Отримуємо дані з WebApp
            raw_data = update.message.web_app_data.data
            print(f"Received WebApp Data: {raw_data}")

            # Парсимо JSON-дані
            data = json.loads(raw_data)

            await context.bot.send_message(
                chat_id=SUPPORT_CONTACT, text=f"Нове замовлення: {data}"
            )
            # Відповідаємо користувачеві
            await update.message.reply_text(f"Дані отримано: {data}")
        except Exception as e:
            # Лог помилки, якщо щось пішло не так
            print(f"Помилка обробки WebApp Data: {e}")
            await update.message.reply_text("Виникла помилка при обробці даних.")
    else:
        print("No WebApp data received.")
        await update.message.reply_text("Дані з WebApp не отримано.")


if __name__ == "__main__":
    # when we run the script we want to first create the bot from the token:
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    # we are listening for web app data
    application.add_handler(CommandHandler("start", launch_web_ui))

    application.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data)
    )

    # and send the bot on its way!
    print(
        f"Your bot is listening! Navigate to https://t.me/{BOT_USERNAME} to interact with it!"
    )
    application.run_polling()
