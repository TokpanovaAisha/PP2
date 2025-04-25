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
cur.execute("""
    CREATE OR REPLACE PROCEDURE deleting(user_name TEXT, user_surname TEXT, user_phone BIGINT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF user_name IS NOT NULL AND  user_surname IS NOT NULL THEN 
            DELETE FROM myphonebook WHERE name = user_name AND surname = user_surname;
        ELSIF user_phone IS NOT NULL THEN
            DELETE FROM myphonebook WHERE phone = user_phone;
        END IF; 
    END;
    $$;
""")
cur.execute("SELECT * FROM myphonebook;")
rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

print("Enter name, surname or phone to delete the record in table")
choice = int(input("Delete by:\n1.Name and surname\n2.Phone\nYour choice: "))

name = surname = phone = None

if choice == 1:
    name = input("Name: ")
    surname = input("Surname: ")
    cur.execute("SELECT * FROM myphonebook WHERE name = %s AND surname = %s;", (name, surname))
    r = cur.fetchone()
    if r:
        cur.execute("CALL deleting(%s, %s, %s);", (name, surname, phone))
        print(f"You have successfully deleted the record by name {name} and surname {surname}!")
    else:
        print("There is no such a user")
elif choice == 2:
    phone = int(input("Phone: "))
    cur.execute("SELECT * FROM myphonebook WHERE phone = %s;", (phone,))
    r = cur.fetchone()
    if r:
        cur.execute("CALL deleting(%s, %s, %s);", (name, surname, phone))
        print(f"You have successfully deleted the record by phone {phone}!")     
    else:
        print("There is no such a phone number")
else:
    print("Invalid choice.")
    conn.close()
    exit()


conn.commit()


cur.execute("SELECT * FROM myphonebook;")
rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()
