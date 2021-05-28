import sqlite3

conn = sqlite3.connect('../data/people_management.db.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM employees;
""")

for linha in cursor.fetchall():
    print(linha)

cursor.execute("""
SELECT * FROM salary;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()

