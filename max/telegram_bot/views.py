from django.shortcuts import render
from telegram.ext import Updater, CallbackContext, MessageHandler, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from . import button
from . import database
from datetime import datetime


def check_user_data(func):
    def inner(update, context):
        chat_id = update.message.from_user.id
        user = database.git_user_chat_id(chat_id)
        state = context.user_data.get('state', 0)
        if state == 0 or state == 4:
            if user:
                if not user["first_name"]:
                    update.message.reply_text(
                        text='Ismingizni kirting!', reply_markup=ReplyKeyboardRemove()
                    )
                    context.user_data['state'] = 1
                    return False
                elif not user['last_name']:
                    update.message.reply_text(
                        text='Famiylangizni kirting!', reply_markup=ReplyKeyboardRemove()
                    )
                    context.user_data['state'] = 2
                    return False
                elif not user['contact']:
                    bottun = [[KeyboardButton(text='Yuborish', request_contact=True)]]
                    update.message.reply_text(
                        text="Telifon nameriz kirting", reply_markup=ReplyKeyboardMarkup(bottun, resize_keyboard=True)
                    )
                    context.user_data['state'] = 3
                    return False
                else:

                    return func(update, context)
            else:
                created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                database.create_user(chat_id, created_at)
                context.user_data['state'] = 1
                update.message.reply_text(
                    text="Ismingizni kirting"
                )
                return False

        else:
            return func(update, context)

    return inner


def check_user_state(update, context):
    chat_id = update.message.from_user.id
    user = database.git_user_chat_id(chat_id)

    if user:
        if not user['first_name']:
            update.message.reply_text(text="Ismingizni kirting!")
            context.user_data['state'] = 1
        elif not user['last_name']:
            update.message.reply_text(text="Familangizni kirting")
            context.user_data['state'] = 2
        elif not user['contact']:
            update.message.reply_text(
                text="Telfon raqamni kirting")

            context.user_data['state'] = 3
        else:
            button.menu(update, context)
            context.user_data['state'] = 4
    else:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        database.create_user(chat_id, created_at)
        update.message.reply_text(text="Telefon raqamingizni kiriting!",
                                  reply_markup=ReplyKeyboardRemove())
        return False


@check_user_data
def start_handler(update: Updater, context: CallbackContext):
    button.menu(update, context)


@check_user_data
def message_handler(update: Updater, context: CallbackContext):
    msg = update.message.text
    chat_id = update.message.from_user.id
    message_id = update.message.message_id
    state = context.user_data.get("state", 0)
    if state == 1:
        database.update_user(state, chat_id, msg)
        check_user_state(update, context)
    elif state == 2:
        database.update_user(state, chat_id, msg)
        check_user_state(update, context)
    elif state == 3:
        database.update_user(state, chat_id, msg)
        check_user_state(update, context)

    else:
        if msg == '🛍 Buyurtma berish':
            categories = database.get_all_category()
            button.categorys(update, context, categories, chat_id, message_id)

        elif msg == '🎉 Aksiya':
            update.message.reply_text(text="Xozirda aksiyalarmiz tugagan")
        elif msg == "📞 Biz bilan bog'laning":
            update.message.reply_text(text="+998942400150")
        else:
            update.message.reply_text(text="Asslom alaykum")


def inline_handler(update, context):
    global product
    query = update.callback_query
    data_split = query.data.split("_")
    chat_id = query.from_user.id
    message_id = query.message.message_id

    if data_split[0] == "category":
        if data_split[1] == "back":
            categories = database.get_all_category()
            button.categorys(update, context, categories, chat_id, message_id)

        elif data_split[1] == "product":
            if data_split[2] == "back":
                products = database.get_products(int(data_split[3]))
                context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                button.back_to_products(update, context, products, chat_id, message_id)
            elif data_split[2] == "card":
                if len(data_split) > 4:
                    context.user_data["text"] = ""
                    if data_split[4] == "minus":
                        count = int(data_split[5])
                        if count > 1:
                            count -= 1
                            text = context.user_data.get("text")
                            product = database.get_products_dictfetchone(int(data_split[3]))
                            cart = context.user_data.get("cart", {})
                            cart[data_split[3]] = cart.get(data_split[3], 0) - 1
                            context.user_data['cart'] = cart
                            total_price = context.user_data.get("total_price", 0)
                            for i, j in cart.items():
                                product = database.get_products_dictfetchone(int(i))
                                price = int(product['price'])
                                total_price += price * int(j)
                                text += f"{product['title']} ⏩ {j}\n"
                            context.user_data['total_price'] = total_price
                            context.user_data['text'] = text
                            button.sent_product(update, context, product, chat_id, message_id, count)

                    elif data_split[4] == "plus":
                        text = context.user_data.get("text")
                        count = int(data_split[5])
                        count += 1
                        product = database.get_products_dictfetchone(int(data_split[3]))
                        cart = context.user_data.get("cart", {})
                        cart[data_split[3]] = cart.get(data_split[3], 0) + 1
                        context.user_data['cart'] = cart
                        total_price = context.user_data.get("total_price", 0)
                        for i, j in cart.items():
                            product = database.get_products_dictfetchone(int(i))
                            price = int(product['price'])
                            total_price += price * int(j)
                            text += f"{product['title']} ⏩ {j}\n"
                        context.user_data['total_price'] = total_price
                        context.user_data['text'] = text
                        button.sent_product(update, context, product, chat_id, message_id, count)

                    elif data_split[4] == "basket":
                        text = context.user_data.get("text")
                        cart = context.user_data.get("cart", {})
                        total_price = context.user_data.get("total_price", 0)
                        if int(data_split[5]) == 1:
                            product = database.get_products_dictfetchone(int(data_split[3]))
                            text += f"{product['title']} ⏩ 1\n"
                            # total_price += int(product['price'])
                            context.user_data['text'] = text
                            cart[data_split[3]] = 1
                        context.user_data["text"] = text
                        context.user_data['cart'] = cart
                        context.user_data["total_price"] = total_price
                        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                        button.sent_product(update, context, product, chat_id, message_id,  text)

                elif data_split[4] == "back":
                    category_id = database.get_products_dictfetchone(int(data_split[3]))['category_id']
                    products = database.get_products(category_id)
                    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                    button.back_to_products(update, context, products, chat_id, message_id)

                elif data_split[4] == "submit":
                    cart = context.user_data.get("cart", {})
                    total_price = context.user_data.get("total_price", 0)
                    database.update_order(total_price, datetime.now().strftime("%d-%m-%Y %H:%M:%S"), cart, chat_id)
                    context.user_data['cart'] = {}
                    context.user_data['total_price'] = 0
                    context.user_data['text'] = ""
                    context.user_data['order_id'] = database.get_max_id(chat_id)
                    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                    context.bot.send_message(
                        text="Ismingizni kiriting",
                        chat_id=chat_id,
                        reply_markup=ReplyKeyboardRemove()
                    )
                    context.user_data["state"] = 5

                else:
                    product = database.get_products(int(data_split[2]))
                    button.sent_product(update, context, product, chat_id, message_id, int(data_split[3]))

            else:
                product = database.get_products_dictfetchone(int(data_split[2]))
                button.sent_product(update, context, product, chat_id, message_id, count=1)

        else:
            product = database.get_products(int(data_split[1]))
            button.get_products(update, context, product, chat_id, message_id)


def image_handler(update: Updater, context: CallbackContext):
    pass


def contact_handler(update: Updater, context: CallbackContext):
    pass
