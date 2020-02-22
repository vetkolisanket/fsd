import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute("""
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
""")

cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);'

DATA = {
    'id':2,
    'completed': False
}

cursor.execute(SQL, DATA)

cursor.execute('SELECT * FROM table1')

result = cursor.fetchall()
# print(result)

for k,v in result:
    print(k, v)

connection.commit()

cursor.close()
connection.close()
