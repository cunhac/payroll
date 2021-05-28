import sqlite3
from time import sleep
from system.uteis import day, month, year, text_input, header

def employee_register():
    """
    Through the inputs of the employees' registration information, this function will make it active in the system,
    storing the information in the database: people management.db.
    :return:
    """

    full_name = input('Full name: ').upper().strip()
    birth_day = day('Birth day: ')
    birth_month = month('Birth month: ')
    birth_year = year('Birth year: ')
    birth_date = f'{birth_year}-{birth_month}-{birth_year}'
    document_number = input('Document number: ')
    office = text_input('Office: ')
    departament = text_input('Department: ')
    hiring_day = day('Hiring day: ')
    hiring_month = month('Hiring month: ')
    hiring_year = year('Hiring year: ')
    hiring_date = f'{hiring_day}-{hiring_month }-{hiring_year}'
    dismissal_date = 'NULL'
    status = 'ACTIVE'
    sleep(2)

    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO employees (full_name, birth_date, document_number, hiring_date, office, departament,
                              dismissal_date, status )
    VALUES ('{full_name}', '{birth_date}','{document_number}', '{hiring_date}', '{office}', '{departament}',
            {dismissal_date}, '{status}')
    """)
    conn.commit()
    conn.close()

    header('REGISTER SUCCESSFULLY COMPLETED!')
    sleep(2)


def search_employee():
    """
    Through the name input, this function will check in the database if the employee is registered. Being registered -
    entered, it will return with the employee's name and then direct to the function payment_calculation. Otherwise,
    you will have the option to perform the register by being directed to the employee_register function.
    :return: name
    """

    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()

    while True:
        name = input('Full name: ').upper()
        cursor.execute("""
        SELECT * FROM employees WHERE full_name=?
        """, (name,))

        lines = cursor.fetchall()
        # foi criada a variavel linhas para nao perder o historico fetchall que é registrado uma vez.
        if len(lines) == 0:
            print('Unregistered employee.')
            print('Do you want to register an employee?')
            while True:
                option = input('Y/N: ').upper()
                if option == 'Y':
                    sleep(2)
                    header('EMPLOYEE_REGISTER')
                    employee_register()
                    break

                elif option == 'N':
                    sleep(2)
                    print('FINISHED SYSTEM!')
                    break

                else:
                    print('Invalid option. Type Y or N:')
            break
        else:
            for line in lines:
                if name in line[1]:
                    print(f'{name} found!')
                    conn.close()
                    return name
        break
