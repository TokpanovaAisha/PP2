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

cur.execute("SELECT * FROM notebook;")
rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

deleting = int(input("What do you want to delete?: \n1.name \n2.phone \nEnter tne choice number: "))

if deleting == 1:
    name_del = input("What name do you want to delete?: ")
    cur.execute("DELETE FROM notebook WHERE name = %s;", (name_del,))
    if cur.rowcount == 0:
        print("Name is not found")
    else:
        print("Name is deleted")
elif deleting == 2:
    phone_del = int(input("What phone do you want to delete?: "))
    cur.execute("DELETE FROM notebook WHERE phone = %s;", (phone_del,))
    if cur.rowcount == 0:
        print("Phone is not found")
    else:
        print("Phone is deleted")


conn.commit()
cur.execute("SELECT * FROM notebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()