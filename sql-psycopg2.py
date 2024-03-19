import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "artist"')
# cursor.execute('SELECT "name" FROM "artist"')
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])
cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Amy Winehouse"])

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)