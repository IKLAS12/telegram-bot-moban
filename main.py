from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import asyncio

BOT_TOKEN = '8135651413:AAEqBTxiQEfrSaxpFcgqHX4IT5Rb50o3BOE'

# Data 7 grup: chat_id, 2 username target (tanpa @), dan 8 mention tag
GRUP_DATA = {
    -4749637563: {
        'usernames': ['from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import asyncio

BOT_TOKEN = '8135651413:AAEqBTxiQEfrSaxpFcgqHX4IT5Rb50o3BOE'

# Data 7 grup: chat_id, 2 username target (tanpa @), dan 8 mention tag
GRUP_DATA = {
    -4749637563: {
        'usernames': ['@Rangers_Abing'],
        'tags': ['@budi_black_assistant_bot', '@Rizki_Adi']
    },
    -4657513726: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@tag1b', '@tag2b', '@tag3b', '@tag4b', '@tag5b', '@tag6b', '@tag7b', '@tag8b']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    # Tambahkan hingga 7 grup
}

REPLAY_TEXT = (
    "Mas-mas moban di cek pastikan pelanggan sudah di amankan ya 🦾🦾\n"
    "Tolong fast respon, OJO LUPUT!!!"
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    chat_id = message.chat_id
    chat_title = message.chat.title
    sender_username = message.from_user.username
    sender_text = message.text

    # Tampilkan info ke terminal
    print(f"[📩] Grup: {chat_title}")
    print(f"🆔 Chat ID: {chat_id}")
    print(f"👤 Pengirim: @{sender_username}")
    print(f"💬 Pesan: {sender_text}\n")

    if chat_id in GRUP_DATA:
        target_data = GRUP_DATA[chat_id]
        if sender_username and sender_username.lower() in [u.lower() for u in target_data['usernames']]:
            tags = ' '.join(target_data['tags'])
            response = f"{REPLAY_TEXT}\n{tags}"
            await message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("🤖 Bot aktif... Menunggu pesan masuk.")
    app.run_polling()
', 'user1b'],
        'tags': ['@budi_black_assistant_bot', '@tag2a', '@tag3a', '@tag4a', '@tag5a', '@tag6a', '@tag7a', '@tag8a']
    },
    -4657513726: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@tag1b', '@tag2b', '@tag3b', '@tag4b', '@tag5b', '@tag6b', '@tag7b', '@tag8b']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    -4797747371: {
        'usernames': ['budi_black_assistant_bot', 'user2b'],
        'tags': ['@budi_black_assistant_bot', '@tag2c', '@tag3c', '@tag4c', '@tag5c', '@tag6c', '@tag7c', '@tag8d']
    },
    # Tambahkan hingga 7 grup
}

REPLAY_TEXT = (
    "Mas-mas moban di cek pastikan pelanggan sudah di amankan ya 🦾🦾\n"
    "Tolong fast respon, OJO LUPUT!!!"
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    chat_id = message.chat_id
    chat_title = message.chat.title
    sender_username = message.from_user.username
    sender_text = message.text

    # Tampilkan info ke terminal
    print(f"[📩] Grup: {chat_title}")
    print(f"🆔 Chat ID: {chat_id}")
    print(f"👤 Pengirim: @{sender_username}")
    print(f"💬 Pesan: {sender_text}\n")

    if chat_id in GRUP_DATA:
        target_data = GRUP_DATA[chat_id]
        if sender_username and sender_username.lower() in [u.lower() for u in target_data['usernames']]:
            tags = ' '.join(target_data['tags'])
            response = f"{REPLAY_TEXT}\n{tags}"
            await message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("🤖 Bot aktif... Menunggu pesan masuk.")
    app.run_polling()
