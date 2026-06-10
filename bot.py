from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8145646747:AAHEWPad_dj_9vn2xgAHLwz4RW-_0ratEys"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti")


async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if not post:
        return

    chat = post.chat
    username = chat.username

    if not username:
        return

    link_text = f"\n\n@{username}"

    if post.text:
        if link_text not in post.text:
            await post.edit_text(post.text + link_text)

    elif post.caption:
        if link_text not in post.caption:
            await post.edit_caption(post.caption + link_text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # ✅ TO‘G‘RI CHANNEL HANDLER
    app.add_handler(
        MessageHandler(filters.UpdateType.CHANNEL_POST, handle_channel_post)
    )

    print("BOT ISHLAYAPTI")
    app.run_polling()


if __name__ == "__main__":
    main()
