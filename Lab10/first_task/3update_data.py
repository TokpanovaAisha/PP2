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


changing = int(input("What do you want to change?: \n1.name \n2.phone \nEnter tne choice number: "))

if changing == 1:
    name_before = input("What is the current name?: ")
    name_after = input("New name: ")
    cur.execute("UPDATE notebook SET name = %s WHERE name = %s;", (name_after, name_before))
    if cur.rowcount == 0:
        print("Name is not found")
    else:
        print("Name is updated")
elif changing == 2:
    phone_before = int(input("What is the current phone?: "))
    phone_after = int(input("New phone: "))
    cur.execute("UPDATE notebook SET phone = %s WHERE phone = %s;", (phone_after, phone_before))
    if cur.rowcount == 0:
        print("Phone is not found")
    else:
        print("Phone is updated")


conn.commit()
cur.execute("SELECT * FROM notebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()