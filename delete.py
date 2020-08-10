import psycopg2


def delete(melicode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            database="learning",
            port="5432"
        )
        cursor = connection.cursor()
        pg_delete = """DELETE FROM public."customer" WHERE "melicode"=%s """
        cursor.execute(pg_delete, (melicode,))
        connection.commit()
        count = cursor.rowcount
        print("successfully deleted", count, "row")
    except(Exception, psycopg2.Error) as error:
        connection = None

    finally:
        if (connection) != None:
            cursor.close()
            connection.close()
            print("THE POSTGRESQL CONNECTION IS NOW CLOSED")
