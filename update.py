from db import connectionclass


def update(customerfname, melicode):

    with connectionclass() as cursor:
        print("customer table befor updating")
        pg_select = """SELECT * FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_select, (melicode,))
        customer_record = cursor.fetchone()
        print(customer_record)

        pg_update = """update public "customer" set "customerfname"=%s WHERE "melicode"=%s """
        cursor.execute(pg_update, (customerfname, melicode))

        count = cursor.rowcount
        print(count, "successfully updating")

        print("customer table affter updating")

        pg_select = """ SELECT * FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_select, (melicode,))
        customer_record = cursor.fetchone()
        print(customer_record)
