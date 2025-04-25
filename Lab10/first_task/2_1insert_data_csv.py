import psycopg2
from tabulate import tabulate
import csv


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

with open('my_friends_csv.txt', 'r') as f:
    reader = csv.reader(f)
    next(reader)  

    for row in reader:
        cur.execute(
            """INSERT INTO notebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (name, phone) DO NOTHING;""",
                row)


conn.commit()
cur.execute("SELECT * FROM notebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()