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
    CREATE OR REPLACE PROCEDURE update_phone(user_name TEXT, user_surname TEXT, user_phone BIGINT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS(SELECT 1 FROM myphonebook WHERE name = user_name AND surname = user_surname AND phone = user_phone) THEN 
            RAISE NOTICE 'No changes were made. This name, surname, and phone combination is already exists.';
            RETURN; 
        END IF;
        
        IF EXISTS(SELECT 1 FROM myphonebook WHERE phone = user_phone AND NOT (name = user_name AND surname = user_surname)) THEN 
            RAISE NOTICE 'A user with this phone number is already exists.';
            RETURN;
        END IF;
        
        IF NOT EXISTS(SELECT 1 FROM myphonebook WHERE name = user_name AND surname = user_surname) THEN
            INSERT INTO myphonebook(name, surname, phone) 
            VALUES (user_name, user_surname, user_phone);
            RAISE NOTICE 'Your data has been successfully added!';
        ELSE
            UPDATE myphonebook
            SET phone = user_phone
            WHERE name = user_name AND surname = user_surname;
            RAISE NOTICE 'Your phone number has been successfully updated!';
        END IF;
    END;
    $$;
""")

print("Enter name, surname and phone to add in table")

name = input("Name: ")
surname = input("Surname: ")
phone = int(input("Phone: "))


cur.execute("CALL update_phone(%s, %s, %s);", (name, surname, phone))
conn.commit()

cur.execute("SELECT * FROM myphonebook;")
rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))
for notice in conn.notices:
    print(notice.strip())

cur.close()
conn.close()
