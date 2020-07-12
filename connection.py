import MySQLdb

host = 'localhost'
user = 'root'
password = '123456'
db = 'escola_curso'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)


def select(fields, table, where=None):

    global c

    query = "SELECT " + fields + " FROM " + table
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()


def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()


# values = [
#     "default, 'Jeftar 1', '1986-09-18', 'Rua Nova Granada 13', 'Recife', 'PE', '123456789101'"]

# result = insert(values, "alunos")

# print(result)
