from time import sleep
import sqlite3
from system.uteis import day, month, year


def dismissal():
    """
    Through the name input, this function will check in the database if the employee's registration is counted. Being
    registered, it will request the inputs of some information and conclude making it inactive in the system. If not,
    river, you will have the option to try the name input again or exit the system.
    :return: name
    """
    name = input('name: ').upper()

    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM employees WHERE full_name=?
        """, (name,))

    lines = cursor.fetchall()
    if len(lines) == 0:
        print('Unregistered employee.')
        print('Do you want to try again?')
        while True:
            option = input('Y/N: ').upper()
            if option == 'Y':
                sleep(2)
                return name

            elif option == 'N':
                sleep(1)
                print('FINISHED SYSTEM!')
                sleep(2)
                return
            else:
                print('Invalid option. Type it again:')
                return
    else:
        for line in lines:
            if name in line[1]:
                print(f'{name} found!')
                conn.close()
            # return name
            break

    dismissal_day = day('Day of dismissal: ')
    dismissal_month = month('Month of dismissal: ')
    dismissal_year = year('Year of dismissal: ')
    dismissal_date = f'{dismissal_day}-{dismissal_month}-{dismissal_year}'
    status = 'INACTIVE'
    print(f'{name}[31m INACTIVE\033[m')

    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()
    cursor.execute(f"""
        UPDATE  employees 
        SET  dismissal_date = ?, status = ?
        WHERE full_name = ?
        """, (dismissal_date, status, name))
    conn.commit()
    conn.close()
