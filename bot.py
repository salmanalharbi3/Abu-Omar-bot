from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# ===== الإعدادات =====
BOT_TOKEN = os.getenv("BOT_TOKEN")  # حط التوكن لاحقًا في الإعدادات
SECRET_WORD = "سر الليل"

# نخزّن المستخدمين المصرّح لهم
authorized_users = set()

# ===== الأوامر =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "حيّاك الله.\n"
        "الدخول له رمز.\n"
        "عجِّل علينا أكتب كلمة السر."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    # التحقق من كلمة السر
    if user_id not in authorized_users:
        if text == SECRET_WORD:
            authorized_users.add(user_id)
            await update.message.reply_text(
                "حيّاك الله يا مرحبا.\n"
                "تفضّل، وش طلبك؟"
            )
        else:
            await update.message.reply_text("الرمز موب صحيح .. أنا أقول أنك تفارقني بطريقة ودّية والقلب داعي لك...")
        return

    # ===== ردود البوت (لهجة نجدية قديمة – خدمات عامة) =====
    reply = (
        "يا مرحبا🌹.\n\n"
        " أبو عمر، بالخدمة باللي نقدر عليه💐،\n"
        "تدبير، تنسيق، سعي بالطيب، ومشاويرٍ تمشي الأمور🌷.\n\n"
        "قل وش خاطرك ونسمعك🌺."
    )
    await update.message.reply_text(reply)

# ===== التشغيل =====
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN غير موجود")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
add bot.py
