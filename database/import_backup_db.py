import io
import sqlite3

conn = sqlite3.connect('../data/people_management.db')

cursor = conn.cursor()

with io.open('management_dump.sql', 'r') as f:
    sql = f.read()

cursor.executescript(sql)