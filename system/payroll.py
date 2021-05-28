import sqlite3
from time import sleep
from system.register import employee_register, search_employee
from system.uteis import day, month, year, value_input, header, line


def month_salary():
    """
    Input of the employee's gross salary amount.
    :return: month_salary
    """
    while True:
        salary_value = input('Month salary:  ')
        if not salary_value.replace('.', '').isnumeric():
            print('Incorrect information! Enter the amount of the salary.')
        else:
            salary_value = round(float(salary_value), 2)
            return salary_value


def salary(gross_salary):
    """
    Using the input of the days worked, the gross salary of the month will be calculated. Always considering the basis
    for calculation of 30 days for the full salary, if the employee has absences in the months make the calculation
    (30 days - absences = total days worked).
    :param gross_salary: will be the value of month_salary.
    :return: salary
    """
    while True:
        worked_days = day('Number of days worked: ')
        if int(worked_days) < 30:
            salary = round(gross_salary / 30 * int(worked_days), 2)
            return salary
        elif int(worked_days) == 30:
            salary = round(gross_salary, 2)
            return salary
        elif int(worked_days) < 0:
            print('Incorrect information! The correct is 0 to 30 days.')
        elif int(worked_days) > 30:
            print('Incorrect information! The correct is 0 to 30 days')


def inss(salary, overtime_total):
    """
    This function calculates the discount amount on the employee's payroll for the INSS. The basis for calculation
    (gross salary of the month + overtime) with the base value result, a rate is established for the calculation of the
    discount. The consultation of the rate was justified through the link:https://tabeladoinss2019.com/tabela-inss-2021/
    :param salario: value corresponding to that informed in the salary function.
    :param overtime: the percentage of 50% was considered for the calculation of overtime.
    :return: inss_value
    """
    inss_salary = salary + overtime_total

    inss1_min = 0
    inss1_max = 1045.00
    inss2_min = 1045.01
    inss2_max = 2089.60
    inss3_min = 2089.61
    inss3_max = 3134.40
    inss4_min = 3134.41
    inss4_max = 6101.06

    if inss1_min <= inss_salary <= inss1_max:
        inss_rate = 7.5
        inss_value = round(float(inss_salary * inss_rate / 100), 2)
    elif inss2_min <= inss_salary <= inss2_max:
        inss_rate = 9
        inss_value = round(float(inss_salary * inss_rate / 100), 2)
    elif inss3_min <= inss_salary <= inss3_max:
        inss_rate = 12
        inss_value = round(float(inss_salary * inss_rate / 100), 2)
    elif inss4_min <= inss_salary <= inss4_max:
        inss_rate = 14
        inss_value = round(float(inss_salary * inss_rate / 100), 2)
    else:
        inss_value = round(float(713.09), 2)
    return inss_value


def irrf(salary, overtime_total, inss_value, bonus):
    """
    This function calculates the amount of the IRRF discount on the employee's payroll. The basis for the calculation
    will be (salary + overtime + bonus - INSS value) with the result of the base value a rate will be established for
    calculating the discount.
    The consultation of the rate was carried out through the link:http://www.portaltributario.com.br/guia/tabelairf.html
    :param salary: value corresponding to that informed in the salary function.
    :param overtime: the percentage of 50% was considered for the calculation of overtime.
    :param inss_value: value informed through the inss.
    :param bonus: value informed through the input requested in the function payroll_calculation.
    :return: irrf_value
    """
    irrf_salary = salary - inss_value + overtime_total + bonus

    irrf1_min = 0
    irrf1_max = 1903.98
    irrf2_min = 1903.99
    irrf2_max = 2826.65
    irrf3_min = 2826.66
    irrf3_max = 3751.05
    irrf4_min = 3751.06
    irrf4_max = 4664.68

    if irrf1_min <= irrf_salary <= irrf1_max:
        irrf_rate = 0
    elif irrf2_min <= irrf_salary <= irrf2_max:
        irrf_rate = 7.5
    elif irrf3_min <= irrf_salary <= irrf3_max:
        irrf_rate = 15
    elif irrf4_min <= irrf_salary <= irrf4_max:
        irrf_rate = 22.5
    else:
        irrf_rate = 27.5

    irrf_value = round(irrf_salary * irrf_rate / 100, 2)

    return irrf_value


def payroll_calculation():
    """
    This function performs the calculation of the payroll per employee. Earnings, discounts are calculated and resulting
    in employee's net salary.For discounts on: meal vouchers, medical assistance and dental assistance symbolic rates
    were used, considering that there is no mandatory provision foreseen in the law for such discounts. If provided for
    in a collective agreement, the employer must follow what is specified in the collective agreement, if Otherwise, it
    will be up to each employer to adopt or not the payroll deduction.
    For the discount of the transportation voucher, the rate of 6% was considered as provided by law. Calculations, the
    information will be saved in the salary table located in the database people_management.db.
    :return:
    """

    name = search_employee()
    if name == None:
        return
    accrual_month = month('Accrual month: ')
    accrual_year = year('Accrual year: ')
    accrual = f'{accrual_month}-{accrual_year}'
    salary_value = month_salary()
    base_salary = salary(salary_value)
    overtime = value_input('Overtime: ')
    absences = value_input('Absences: ')
    late = value_input('Late: ')
    bonus = value_input('Bonus: ')

    hourly_wage = round(salary_value / 220, 2)
    overtime_value = round(float(hourly_wage * 1.5), 2)
    overtime_total = round(overtime_value * overtime, 2)
    daily_wage = round(salary_value / 30, 2)
    absences_value = round(daily_wage * absences, 2)
    late_value = round(daily_wage * late / 60, 2)
    inss_value = inss(base_salary, overtime_total)
    irrf_value = irrf(base_salary, overtime_total, inss_value, bonus)
    sleep(2)



    header('EARNINGS')
    print(f'Salary:  {base_salary}')
    print(f'Bonus:  {bonus}')
    print(f'Overtime:  {overtime_total }')
    earnings_total = round(base_salary + overtime_total + bonus, 2)
    sleep(2)

    print(line())
    print(f'Earnings total:  {earnings_total}')
    print(line())
    sleep(2)

    header('DISCOUNTS')

    transportation_vouchers = round(base_salary * 6 / 100, 2)
    health_care = round(base_salary * 2 / 100, 2)
    dental_care = round(base_salary * 0.5 / 100, 2)
    meal_ticket = round(base_salary * 1 / 100, 2)

    print(f'absences: {absences_value}')
    print(f'late: {late_value}')
    print(f'transportation_vouchers: {transportation_vouchers}')
    print(f'health_care: {health_care}')
    print(f'dental_care: {dental_care}')
    print(f'meal_ticket: {meal_ticket}')
    print(f'inss_value: {inss_value}')
    print(f'irrf_value: {irrf_value}')

    discounts_total = round(absences_value + late_value + transportation_vouchers + health_care +
                            dental_care + meal_ticket + inss_value + irrf_value, 2)

    print(line())
    print(f'Discounts_total :  {discounts_total }')
    print(line())
    liquid_salary = round(earnings_total - discounts_total, 2)
    print(f'Liquid_salary:  {liquid_salary} ')
    print(line())

    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO salary (name,  salary ,bonus,  overtime, absences_value, late_value, 
    t_vouchers, health_care, dental_care, meal_ticket, inss, irrf, 
    earnings, discounts, liquid_salary, accrual)
    VALUES ('{name}',  '{base_salary}' ,'{bonus}',  '{overtime_total}', '{absences_value}', 
    '{late_value}',  '{transportation_vouchers}', '{health_care}', '{dental_care}', 
    '{meal_ticket}', '{inss_value}', '{irrf_value}', '{earnings_total}', '{discounts_total}', 
    '{liquid_salary}', '{accrual}')
    """)
    conn.commit()
    conn.close()
