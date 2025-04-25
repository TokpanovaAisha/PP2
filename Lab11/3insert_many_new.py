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
# Create procedure to insert many new users by list of name and phone. 
# Use loop and if statement in stored procedure. 
# Check correctness of phone in procedure and return all incorrect data.

quantity = int(input("How many people do you want to add?: "))
name_list = []
surname_list = []
phone_list = []
inc_name_list = []
inc_surname_list = []
inc_phone_list = []
for i in range(quantity):
    name = input("Name:")
    surname = input("Surname: ")
    phone = int(input("Phone: "))
    name_list.append(name)
    surname_list.append(surname)
    phone_list.append(phone)



cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_many_new(name_list TEXT[], surname_list TEXT[], phone_list BIGINT[], num BIGINT)
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT:= 1;
        name TEXT;
        surname TEXT;
        phone BIGINT;
    BEGIN
        WHILE num >= i LOOP
            name := name_list[i];
            surname := surname_list[i];
            phone := phone_list[i];

            IF LENGTH(phone::TEXT) != 11 THEN
                RAISE NOTICE 'The invalid phone - % with name and surname - % and %', phone, name, surname;
            ELSE
                INSERT INTO myphonebook (name, surname, phone)
                VALUES (name, surname, phone);
                RAISE NOTICE 'Inserted: % % %', name, surname, phone;
            END IF;
            i := i + 1;
        END LOOP;
    END;
    $$;
""")
    

cur.execute("CALL insert_many_new(%s, %s, %s, %s);", (name_list, surname_list, phone_list, quantity))
conn.commit()

cur.execute("SELECT * FROM myphonebook;")
rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))
for notice in conn.notices:
    print(notice.strip())
cur.close()
conn.close()
