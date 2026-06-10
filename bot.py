from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8145646747:AAHEWPad_dj_9vn2xgAHLwz4RW-_0ratEys"


# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\n"
        "Men kanal postlariga @username qo‘shib beraman.\n\n"
        "Shartlar:\n"
        "✔ Kanal public bo‘lishi\n"
        "✔ Bot admin bo‘lishi (edit rights)\n"
    )


# Kanal postlarini ushlash
async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if not post:
        return

    chat = post.chat
    username = chat.username

    if not username:
        return  # private kanal bo‘lsa ishlamaydi

    suffix = f"\n\n@{username}"

    try:
        # Text post
        if post.text:
            if suffix not in post.text:
                await post.edit_text(post.text + suffix)

        # Caption (photo/video/document)
        elif post.caption:
            if suffix not in post.caption:
                await post.edit_caption(post.caption + suffix)

    except Exception as e:
        print("Edit error:", e)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Kanal post handler (TO‘G‘RI FILTER)
    app.add_handler(
        MessageHandler(filters.UpdateType.CHANNEL_POST, handle_channel_post)
    )

    print("BOT ISHLAYAPTI 🚀")
    app.run_polling()


if name == "main":
    main()
