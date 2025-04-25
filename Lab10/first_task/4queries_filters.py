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

def show(query):
    cur.execute(query)
    rows = cur.fetchall()
    headers = [x[0] for x in cur.description]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

show("SELECT * FROM notebook;")

filters = int(input("Choose the filter: \n1.Names in descending order\n2.Names in the ascending order\n3.Where name is 'Anya'\n4.Phones that begin with 8701\nYour choice: "))

if filters == 1:
    show("SELECT * FROM notebook ORDER BY name DESC;")
elif filters == 2:
    show("SELECT * FROM notebook ORDER BY name ASC;")
elif filters == 3:
    show("SELECT * FROM notebook WHERE name = 'Anya';")
elif filters == 4:
    show("SELECT * FROM notebook WHERE phone::TEXT LIKE '8701%';")


cur.execute("SELECT * FROM notebook;")

cur.close()
conn.close()