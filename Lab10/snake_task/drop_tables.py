import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS user_score CASCADE;")
conn.commit()
cur.execute("DROP TABLE IF EXISTS users CASCADE;")
conn.commit()
print("Таблицы очищены.")

cur.close()
conn.close()
