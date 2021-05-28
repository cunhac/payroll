from time import sleep
from system.uteis import header, line
from system.register import employee_register
from system.print import print_payholl
from system.dismissal import dismissal
from system.payroll import payroll_calculation


def payment_menu():
    """
    This is the function responsible for directing the information in the system. It contains 5 input options that are:

    1 - New register  (directs to the file: register.py);
    2 - Print payroll (directs to the file: print.py);
    3 - Dismissal     (directs to the file: dismissal.py);
    4 - Salary        (directs to the file: payroll.py);
    5 - Leave         (responsible for finalizing the system).
    :return: the function of the chosen option.
    """
    while True:
        header('PAYROLL MANAGEMENT')
        print('1 - New register')
        print('2 - Salary')
        print('3 - Dismissal')
        print('4 - Print payroll')
        print('5 - Leave ')
        print(line())
        option = input('Type the option: ')
        if not option.isnumeric():
            print('Invalid option!')
        elif option.isnumeric():
            option = int(option)
            if option == 1:
                header('NEW REGISTER')
                employee_register()
            elif option == 2:
                header('SALARY')
                payroll_calculation()
            elif option == 3:
                header('DISMISSAL')
                dismissal()
            elif option == 4:
                header('PRINT PAYROLL')
                print_payholl()
            elif option == 5:
                header('LEAVE')
                sleep(2)
                print('FINISHED SYSTEM!')
                break



payment_menu()