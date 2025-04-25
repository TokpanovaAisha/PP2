import psycopg2
from tabulate import tabulate


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

quantity = int(input("How many people do you want to add?: "))
for i in range (quantity):
    entered_name = input("Name:")
    entered_phone = int(input("Phone: "))
    cur.execute(
            """INSERT INTO notebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (name, phone) DO NOTHING;""",
                (entered_name, entered_phone))
    if cur.rowcount == 0:
        print(f"Name: {entered_name} and phone: {entered_phone} have already exist. Enter another data.")
    else:
        print(f"You added {entered_name}, {entered_phone}")




conn.commit()
cur.execute("SELECT * FROM notebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()