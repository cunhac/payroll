import sqlite3
import io

conn = sqlite3.connect('../data/people_management.db')

with io.open('management_dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n'% line)
print('successful backup!')
print('Except as an employees_dump.sql')

conn.close()