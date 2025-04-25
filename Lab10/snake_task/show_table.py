import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT * FROM user_score;")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\n")

cur.execute("SELECT * FROM users;")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()
