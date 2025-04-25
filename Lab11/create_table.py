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
#в этой таблице уникальные номера, имя+фамилия не повторяются
cur.execute("""
    CREATE TABLE IF NOT EXISTS myphonebook(
        id SERIAL PRIMARY KEY,
        name TEXT,
        surname TEXT,
        phone BIGINT UNIQUE,
        UNIQUE (name, surname)
    );
""")


people = [
    ('Aisha', 'Tokpanova', 87017364500),
    ('Aisha', 'Mukhametova', 87017364501),
    ('Ivan', 'Ivanov', 87771238111),
    ('Ivan', 'Petrov', 87771238112),
    ('Aiman', 'Ospanova', 87071234567),
    ('Aiman', 'Tokpanova', 87071234568),
    ('Sasha', 'Tokpanova', 87071234569),
    ('Aliya', 'Saparova', 87079998877),
    ('Aliya', 'Kurmangali', 87079998878),
    ('Dana', 'Akhmetova', 87015556677),
    ('Dana', 'Baideldinova', 87015556678),
    ('Rustem', 'Zhaksylykov', 87778889990),
    ('Askar', 'Nurgaliyev', 87778889991)
]

for name, surname, phone in people:
    cur.execute("""
        INSERT INTO myphonebook(name, surname, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, (name, surname, phone))

conn.commit()

cur.execute("SELECT * FROM myphonebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()
