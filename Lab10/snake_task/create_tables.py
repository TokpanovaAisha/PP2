import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="AlIyA2015",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(100) UNIQUE NOT NULL,
        state VARCHAR(100) 
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score(
        user_id INTEGER PRIMARY KEY REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        direction VARCHAR(100),
        snake_head_x INTEGER,
        snake_head_y INTEGER,
        snake_body TEXT,
        velocity INTEGER
    );
""")

conn.commit()

cur.execute("SELECT * FROM user_score;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT * FROM users;")
rows = cur.fetchall()
for row in rows:
    print(row)

print("Таблицы созданы.")
cur.close()
conn.close()
