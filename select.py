from db import connectionclass

def selectCustom():
    with connectionclass() as cursor:

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

