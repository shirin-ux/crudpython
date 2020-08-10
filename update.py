import psycopg2


def update(customerfname, melicode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            database="learning",
            port="5432"
        )
        cursor = connection.cursor()
        pg_select = """SELECT * FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_select, (melicode,))
        customer_record = cursor.fetchone()
        print(customer_record)

        pg_update = """update public "customer" set "customerfname"=%s WHERE "melicode"=%s """
        cursor.execute(pg_update, (customerfname, melicode))
        connection.commit()
        count = cursor.rowcount
        print(count, "successfully updating")

        print("customer table affter updating")

        pg_select = """ SELECT * FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_select, (melicode,))
        customer_record = cursor.fetchone()
        print(customer_record)
    except(Exception, psycopg2.Error) as error:
        print("Error in updating the data", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("THE POSTGRESQL CONNECTION IS NOW CLOSED")
