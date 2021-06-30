from django.db import connection
from contextlib import closing
from collections import OrderedDict


def get_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from way_category """,
        )
        categors = dict_fetchall(cursor)
        return categors


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
