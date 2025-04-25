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
    CREATE TABLE IF NOT EXISTS notebook(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone BIGINT,
        UNIQUE (name, phone)
    );
""")

people = [
    ('Aisha', 870173645),
    ('Ivan', 877712381),
    ('Aiman', 870712345)
]

for name, phone in people:
    cur.execute("""
        INSERT INTO notebook(name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name, phone) DO NOTHING;
    """, (name, phone))


conn.commit()
cur.execute("SELECT * FROM notebook;")

rows = cur.fetchall()
headers = [x[0] for x in cur.description]
print(tabulate(rows, headers=headers, tablefmt="pretty"))

cur.close()
conn.close()
