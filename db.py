from payscopg2 import pool

connection_pool = pool.SamlpilconnectionPool(1, 10,
                                             user="postgres",
                                             password="1234",
                                             host="localhost",
                                             database="learning",
                                             port="5432"
                                             )


class connectionclass:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor=self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None :
             self.connection.rollback()
        else    :
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)

