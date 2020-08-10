import psycopg2


def insert(customerfname, customerlname, melicode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            database="learning",
            port="5432"
        )
        cursor = connection.cursor()
        pg_insert = """INSERT INTO public."customer"("customerfname","customerlname","melicode") 
                     VALUES (%s,%s,%s)"""
        insert_values = (customerfname, customerlname, melicode)
        cursor.execute(pg_insert, insert_values)
        connection.commit()
        count = cursor.rowcount
        print("successfully inserted", count, "records")
    except(Exception,psycopg2.Error) as error:
        print("error connection to postgreSQL database",error)
        connection = None

    finally:
        if (connection):
           cursor.close()
           connection.close()
           print("THE POSTGRESQL CONNECTION IS NOW CLOSED")
