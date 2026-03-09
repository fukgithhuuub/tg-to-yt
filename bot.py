import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from youtube_utils import upload_video
from dotenv import load_dotenv

load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, send me a video and I will upload it to YouTube!")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    if not video:
        return

    # Send a waiting message
    status_message = await update.message.reply_text("Downloading video...")

    file = await context.bot.get_file(video.file_id)
    file_path = f"video_{video.file_id}.mp4"
    await file.download_to_drive(file_path)

    await status_message.edit_text("Uploading to YouTube...")

    try:
        title = update.message.caption if update.message.caption else "Uploaded from Telegram"
        description = "This video was uploaded via Telegram Bot"

        response = upload_video(file_path, title, description)

        video_id = response.get('id')
        await status_message.edit_text(f"Successfully uploaded! Video URL: https://www.youtube.com/watch?v={video_id}")
    except Exception as e:
        logging.error(f"Error uploading video: {e}")
        await status_message.edit_text(f"Failed to upload video: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    video_handler = MessageHandler(filters.VIDEO, handle_video)

    application.add_handler(start_handler)
    application.add_handler(video_handler)

    application.run_polling()
