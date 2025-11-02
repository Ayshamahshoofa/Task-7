import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# sample rows
sales_data = [
    ("Shampoo", 10, 150),
    ("Face Wash", 5, 200),
    ("Moisturizer", 8, 250),
    ("Shampoo", 7, 150),
    ("Face Wash", 6, 200)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

conn.commit()
conn.close()

print("Database created and sample data inserted ✅")
