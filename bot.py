from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# 🔑 ADD YOUR BOT TOKEN HERE
TOKEN = "8386231124:AAHvhaVg-Z1L24pJ2CJNRxB3674gjPD_nHU"



# 👑 YOUR TELEGRAM USER ID
ADMIN_ID = 6556890316

# 🚀 START COMMAND (INLINE MENU)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Buy Now", url="https://rzp.io/rzp/Oa0lD2k")],
        [InlineKeyboardButton("📸 Demo", callback_data="demo")],
        [InlineKeyboardButton("📞 Support", callback_data="support")],
        [InlineKeyboardButton("✅ I Paid", callback_data="paid")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome!\n\nPlease choose an option:",
        reply_markup=reply_markup
    )

# 🔘 BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    username = query.from_user.username

    # 📸 DEMO
    if query.data == "demo":
        await query.message.reply_photo(
            photo="https://ibb.co/LDTNZfnw",
            caption="📸 This is a demo preview"
        )

    # 📞 SUPPORT
    elif query.data == "support":
        await query.message.reply_text(
            "📞 Contact support: @riyoraxsupport"
        )

    # 💰 I PAID
    elif query.data == "paid":
        await query.message.reply_text(
            f"⏳ Payment is being reviewed...\nYour ID: {user_id}\n\nSend this ID to admin"
        )

        # 🔥 NOTIFY ADMIN
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔥 New Payment Request\n\nUser ID: {user_id}\nUsername: @{username}"
        )

# 💳 BUY COMMAND (LEFT MENU)
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Payment link:\nhttps://rzp.io/rzp/Oa0lD2k"
    )

# 📸 DEMO COMMAND (LEFT MENU)
async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://ibb.co/LDTNZfnw",
        caption="📸 Demo preview"
    )

# 📞 SUPPORT COMMAND (LEFT MENU)
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Contact support: @riyoraxsupport"
    )

# 👑 ADMIN COMMAND (ACCESS)
async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:

        if len(context.args) == 0:
            await update.message.reply_text("Please provide a user ID")
            return

        user_id = int(context.args[0])

        # ✅ SEND ACCESS MESSAGE
        await context.bot.send_message(
            chat_id=user_id,
            text="🔥 Payment successful!\n\n👉 Join private access:\nhttps://t.me/+1R4StxEOBEQ5YmNl"
        )

        # 📸 SEND PREMIUM PHOTO
        await context.bot.send_photo(
            chat_id=user_id,
            photo="https://ibb.co/LDTNZfnw"
        )

# ⚙️ BOT START
app = ApplicationBuilder().token(TOKEN).build()

# COMMAND HANDLERS
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("demo", demo))
app.add_handler(CommandHandler("support", support))

# BUTTON HANDLER
app.add_handler(CallbackQueryHandler(button))

# ADMIN COMMAND
app.add_handler(CommandHandler("access", access))

print("Bot is running...")
app.run_polling()
