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
    CREATE OR REPLACE FUNCTION pattern_1(pattern TEXT, filters INT)
    RETURNS TABLE(id INT, name TEXT, surname TEXT, phone BIGINT) AS $$
    BEGIN
        RETURN QUERY
        SELECT myphonebook.id, myphonebook.name, myphonebook.surname, myphonebook.phone
        FROM myphonebook 
        WHERE 
            CASE
                WHEN filters = 1 THEN myphonebook.name LIKE pattern || '%'
                WHEN filters = 2 THEN myphonebook.phone::TEXT LIKE pattern || '%'
                WHEN filters = 3 THEN myphonebook.name LIKE '%' || pattern
                WHEN filters = 4 THEN myphonebook.phone::TEXT LIKE '%' || pattern
                WHEN filters = 5 THEN myphonebook.surname LIKE '%' || pattern
                WHEN filters = 6 THEN myphonebook.surname LIKE pattern || '%'
                ELSE FALSE
            END;
    END;
    $$ LANGUAGE plpgsql;
""")
filters = input("Choose the pattern: \n1.Names starting with the entered letter" \
                                        "\n2.Phones starting with the entered digit" \
                                        "\n3.Names ending with the entered letter" \
                                        "\n4.Phones ending with the entered digit" \
                                        "\n5.Surname ending with the entered letter"\
                                        "\n6.Surname starting with the entered letter"\
                                        "\nYour choice: ")


if filters == '1':
    pattern = input("Enter the letter with which the names will begin: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
elif filters == '2':
    pattern = input("Enter the digit with which the phones will begin: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
elif filters == '3':
    pattern = input("Enter the letter with which the names will end: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
elif filters == '4':
    pattern = input("Enter the digit with which the phones will end: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
elif filters == '5':
    pattern = input("Enter the letter with which the surname will end: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
elif filters == '6':
    pattern = input("Enter the letter with which the surname will begin: ")
    show("SELECT * FROM pattern_1(%s, %s);", (pattern, filters))
else:
    print("Enter the number between 1 and 6")

cur.close()
conn.close()