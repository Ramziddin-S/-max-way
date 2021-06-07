from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from way_category""")
        categories = dictfetchall(cursor)
    return categories

def get_categories_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select way_category.name as category, count(way_product.id) as count from way_category
            left join way_product on way_category.id = way_product.category_id 
            group by way_category.name"""
        )
        categories = dictfetchall(cursor)
    return categories


def get_product_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select id, title, description, image, price from way_product where id = %s """,
            [product_id]
        )
        product = dictfetchone(cursor)
        return product


def get_product():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from way_product""")
        product = dictfetchall(cursor)
    return product


def get_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from way_user""")
        user = dictfetchall(cursor)
    return user


def get_order():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from way_order""")
        order = dictfetchall(cursor)
    return order


def get_status_info(status):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select way_user.*, way_order.status as status from way_user left join way_order 
        on way_user.id = way_order.id where status in ({str(status).strip("[]")})"""
                       )
        status = dictfetchall(cursor)
    return status





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















