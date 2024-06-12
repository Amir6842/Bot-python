import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from requests import get
from random import choice

async def shat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private':
        text = update.message.text
        
        response = get(f"http://api-free.ir/api/img.php?text={text}&v=3.5").json()
        image_urls = response['result']
        
        selected_image_url = choice(image_urls)
        
        await update.message.reply_photo(selected_image_url)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! متن خود را ارسال کنید تا تصویر آن را دریافت کنید.")

app = ApplicationBuilder().token("7356929818:AAE_RlusSkDlJl-DK4idH3H--SyGYi_JLmU").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shat))

app.run_polling()