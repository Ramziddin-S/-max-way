from django.db import connection
from contextlib import closing


def git_user_chat_id(chat_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from bot_user where chat_id = %s """,
                       [chat_id]
                       )
        user = dictfetchone(cursor)
    return user


def create_user(chat_id, created_at):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""INSERT INTO  bot_user (chat_id, created_at) VALUES (%s, %s)""",
                       [chat_id, created_at]
                       )


def update_user(state, chat_id, data):
    with closing(connection.cursor()) as cursor:
        if state == 1:
            cursor.execute(
                """update bot_user set first_name = %s where chat_id = %s """,
                [data, chat_id]
            )
        elif state == 2:
            cursor.execute(
                """update bot_user set last_name = %s where chat_id = %s """,
                [data, chat_id]
            )
        elif state == 3:
            cursor.execute(
                """update bot_user set contact = %s where chat_id = %s """,
                [data, chat_id]
            )


def get_all_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from way_category"""
        )
        categorys = dictfetchall(cursor)
        return categorys


def get_products(data):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            f"""select * from way_product where category_id={data}"""
        )
        categorys = dictfetchall(cursor)
        return categorys


def get_products_dictfetchone(data):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            f"""select * from way_product where id=%s""",
            [data]
        )
        categorys = dictfetchone(cursor)
        return categorys

def get_products_category_id(data):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            f"""select * from way_product where id=%s""",
            [data]
        )
        pk = dictfetchone(cursor)['category_id']
        return pk


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
