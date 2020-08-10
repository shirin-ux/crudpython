from db import connectionclass


def insert(customerfname, customerlname, melicode):

    with connectionclass() as coursor:

        pg_insert = """INSERT INTO public."customer"
                       ("customerfname","customerlname","melicode") 
                        VALUES (%s,%s,%s) """

        insert_values = (customerfname, customerlname, melicode)

        coursor.execute(pg_insert,insert_values)
        count = coursor.rowcount
        print("successfully",count,"recordes.")

