from db import connectionclass


def delete(melicode):
  with connectionclass() as cursor:
        pg_delete = """DELETE FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_delete, (melicode,))

        count = cursor.rowcount
        print("successfully deleted", count, "row")
