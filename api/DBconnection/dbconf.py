import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database = "hospital",
                                          user = "postgres",
                                          password = "system",
                                          host = "localhost",
                                          port = "5432")

    def getConnection(self):
        print("successfully connected to database")
        return self.connection
