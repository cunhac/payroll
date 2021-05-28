# http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
# https://www.youtube.com/c/RegisdoPython/playlists

import sqlite3
from sqlite3 import Cursor
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('../data/people_management.db')

cursor = conn.cursor()

sql = """create table employees (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        full_name TEXT , 
        birth_date TIMESTAMP,
        document_number TEXT ,
        hiring_date TIMESTAMP,
        dismissal_date TEXT,
        office TEXT ,
        departament TEXT,
        status TEXT
        )
"""
cursor.execute(sql)

sql = """create table salary(
        name TEXT ,
        salary FLOAT , 
        bonus FLOAT,
        overtime FLOAT ,
        absences_value FLOAT,
        late_value FLOAT,
        t_vouchers FLOAT,
        health_care FLOAT ,
        dental_care FLOAT,
        meal_ticket FLOAT,
        inss FLOAT,
        irrf FLOAT,
        earnings FLOAT,
        discounts FLOAT,
        liquid_salary FLOAT,
        accrual TEXT    
        )  
"""
cursor.execute(sql)
conn.close()

