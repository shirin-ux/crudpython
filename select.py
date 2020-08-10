import psycopg2

def selectCustom():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="localhost",
            database="learning",
            port="5432"
        )
        cursor = connection.cursor()

        pg_select = """ select * from public."customer" """
        cursor.execute(pg_select)

        print("selected rows from customer table")
        customer_records = cursor.fetchall()

        print("records of customer in the table")

        for row in customer_records:
            print("id = " , row[0])
            print("customerfname = " , row[1])
            print("customerlname = " , row[2])
            print("melicode = " , row[3])
            print("--------------*****----------- ", "\n")


    except(Exception, psycopg2.Error) as error:
        print("Error selecting data from customer table",error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("THE POSTGRESQL CONNECTION IS NOW CLOSED")

