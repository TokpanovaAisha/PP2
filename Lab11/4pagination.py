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
def show(query, p = None):
    cur.execute(query, p)
    rows = cur.fetchall()
    headers = [x[0] for x in cur.description]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))
    
show("SELECT * FROM myphonebook;")

cur.execute("""
    CREATE OR REPLACE FUNCTION pagination(lim INT, off INT)
    RETURNS TABLE(id INT, name TEXT, surname TEXT, phone BIGINT) AS $$
    BEGIN
        RETURN QUERY
        SELECT myphonebook.id, myphonebook.name, myphonebook.surname, myphonebook.phone
        FROM myphonebook 
        LIMIT lim OFFSET off;
    END;
    $$ LANGUAGE plpgsql;
""")

print("Enter how many records you want to output and how many to skip:")
lim = int(input("Records to output: "))
off = int(input("Skip: "))
show("SELECT * FROM pagination(%s, %s);", (lim, off))

cur.close()
conn.close()