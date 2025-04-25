import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS myphonebook CASCADE;")
conn.commit()
print("Таблица очищена.")

cur.close()
conn.close()
