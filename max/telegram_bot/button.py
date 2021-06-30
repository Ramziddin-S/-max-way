from telegram.ext import Updater, CallbackContext, MessageHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
from django.conf import settings


def menu(update, context):
    button = [
        [KeyboardButton(text='🛍 Buyurtma berish')],
        [KeyboardButton(text='🎉 Aksiya'), KeyboardButton(text='ℹ️ Biz haqimizda')],
        [KeyboardButton(text="📞 Biz bilan bog'laning"), KeyboardButton(text='⚙️ Sozlamalar')]
    ]
    update.message.reply_text(
        text='Asosiy menyu', reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True)
    )


def categorys(update, context, categories, chat_id, message_id):
    buttons = []
    row = []
    count = 0
    for category in categories:
        row.append(
            InlineKeyboardButton(
                text=f"{category['name']}",
                callback_data=f"category_{category['id']}"
            )
        )
        count += 1
        if count == 2:
            buttons.append(row)
            row = []
            count = 0
    if len(categories) % 2 == 1:
        buttons.append(row)

    try:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Kategoriyalarni tanglang!",
            reply_markup=InlineKeyboardMarkup(buttons)

        )
    except:
        context.bot.send_message(
            chat_id=chat_id,
            text="Kategoriyalarni tanglang!",
            reply_markup=InlineKeyboardMarkup(buttons))


def get_products(update, context, products, chat_id, message_id):
    buttons = []
    row = []
    count = 0
    for product in products:
        row.append(
            InlineKeyboardButton(
                text=f"{product['title']}",
                callback_data=f"category_product_{product['id']}"
            )

        )
        count += 1
        if count == 2:
            buttons.append(row)
            row = []
            count = 0
    if len(products) % 2 == 1:
        buttons.append(row)
    buttons.append(
        [
            InlineKeyboardButton(
                text="Orqaga",
                callback_data="category_back"
            )
        ]
    )

    context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="Kategoriyalarni tanglang!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def back_to_products(update, context, products, chat_id, message_id):
    buttons = []
    row = []
    count = 0
    for product in products:
        row.append(
            InlineKeyboardButton(
                text=f"{product['title']}",
                callback_data=f"category_product_{product['id']}"
            )

        )
        count += 1
        if count == 2:
            buttons.append(row)
            row = []
            count = 0
    if len(products) % 2 == 1:
        buttons.append(row)
    buttons.append(
        [
            InlineKeyboardButton(
                text="Orqaga",
                callback_data="category_back"
            )
        ]
    )

    context.bot.send_message(
        chat_id=chat_id,
        text="Kategoriyalarni tanglang!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def sent_product(update, context, product, chat_id, message_id, count=1):
    caption = f"<b>{product['title']}</b>\nNarxi:{product['price']}\n{product['description']}"
    buttons = [
        [
            InlineKeyboardButton(text="➖", callback_data=f"category_product_card_{product['id']}_minus_{count}"),
            InlineKeyboardButton(text=f"{count}", callback_data=f"category_product_card_{product['id']}_count"),
            InlineKeyboardButton(text="➕", callback_data=f"category_product_card_{product['id']}_plus_{count}")
        ],
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data=f"category_product_back_{product['category_id']}_"),
            InlineKeyboardButton(text="✅ Savatchaga qo'shish",
                                 callback_data=f"category_product_card_{product['id']}_basket_{count}")
        ]
    ]
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_photo(caption=caption, chat_id=chat_id,
                           photo=open(settings.MEDIA_ROOT / product['image'], "rb"),
                           parse_mode="HTML",
                           reply_markup=InlineKeyboardMarkup(buttons))
