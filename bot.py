import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("8386231124:AAEgLiSpQlfAlPUCIwRfLSUBEKTQHCNQBAM")  # Railway ENV me add karna
ADMIN_ID = 6556890316

# 🟢 START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    # 👉 USER SAVE (offer ke liye)
    context.application.user_data[user_id] = True

    keyboard = [
        [InlineKeyboardButton("💎 1 Month - $3.99", url="https://rzp.io/rzp/Oa0lD2k")],
        [InlineKeyboardButton("🔥 2 Months - $6.99", url="https://rzp.io/rzp/Oa0lD2k")],
        [InlineKeyboardButton("👑 3 Months - $12.99", url="https://rzp.io/rzp/Oa0lD2k")],
        [InlineKeyboardButton("🎁 Offer: 3 Months 30% OFF ($10.99)", url="https://rzp.io/rzp/Oa0lD2k")],
        [InlineKeyboardButton("✅ I Paid", callback_data="paid")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.ibb.co/LDTNZfnw",
        caption="🔥 Choose your plan & unlock premium content 😏",
        reply_markup=reply_markup
    )

# 🟢 BUTTON CLICK
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    # 👉 ADMIN KO NOTIFICATION
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"💰 New Payment Request!\nUser ID: {user_id}"
    )

    await query.message.reply_text(
        f"⏳ Payment checking...\nYour ID: {user_id}"
    )

# 🟢 ADMIN ACCESS COMMAND
async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:

        if len(context.args) == 0:
            await update.message.reply_text("❌ Use: /access USER_ID")
            return

        user_id = int(context.args[0])

        await context.bot.send_message(
            chat_id=user_id,
            text="🔥 Payment successful! Welcome to premium 😏"
        )

        # 📸 PHOTO
        await context.bot.send_photo(
            chat_id=user_id,
            photo="https://i.ibb.co/LDTNZfnw"
        )

        # 🔗 PRIVATE CHANNEL
        await context.bot.send_message(
            chat_id=user_id,
            text="🔒 Join Private Channel:\nhttps://t.me/+1R4StxEOBEQ5YmNl"
        )

# 🟢 OFFER BROADCAST
async def offer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == ADMIN_ID:

        offer_text = """🎁 LIMITED OFFER!

🔥 3 Months Plan 30% OFF
Now Only $10.99 😍

💳 Buy Now:
https://rzp.io/rzp/Oa0lD2k
"""

        for user_id in context.application.user_data:
            try:
                await context.bot.send_message(chat_id=user_id, text=offer_text)
            except:
                pass

        await update.message.reply_text("✅ Offer sent to all users!")

# 🟢 MAIN APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("access", access))
app.add_handler(CommandHandler("offer", offer))

print("Bot is running...")
app.run_polling()
