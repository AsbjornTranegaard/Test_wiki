import psycopg2


class Sql:

    def __init__(self):
        self.connection = psycopg2.connect(user="postgres", password="Andersen84", host="localhost", port="5432", database="postgres")
        self.cursor = self.connection.cursor()

    def insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def __exit__(self):
        self.connection.commit()
        self.connection.close()


database = Sql()


#g = """DROP TABLE test"""
#database.insert(g)


z = """CREATE TABLE IF NOT EXISTS test (Id int PRIMARY KEY, Comment INT)"""
database.insert(z)


b = """INSERT INTO test VALUES (1, 4)"""
database.insert(b)


d = """SELECT * FROM test"""
database.insert(d)

