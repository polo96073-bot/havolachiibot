from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ChannelPostHandler,
    ContextTypes,
    filters,
)

TOKEN = "8145646747:AAHEWPad_dj_9vn2xgAHLwz4RW-_0ratEys"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\n"
        "Men kanaldagi postlarga @kanal_nomi qo‘shaman."
    )


async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if not post:
        return

    chat = post.chat
    username = chat.username

    # Public kanal bo‘lmasa chiqib ketadi
    if not username:
        return

    link_text = f"\n\n@{username}"

    # Matnli post
    if post.text:
        if link_text not in post.text:
            await post.edit_text(post.text + link_text)

    # Rasm
    elif post.photo:
        caption = post.caption or ""
        if link_text not in caption:
            await post.edit_caption(caption + link_text)

    # Video
    elif post.video:
        caption = post.caption or ""
        if link_text not in caption:
            await post.edit_caption(caption + link_text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChannelPostHandler(handle_channel_post))

    print("BOT ISHGA TUSHDI")
    app.run_polling()


if __name__ == "__main__":
    main()
