import sqlite3


def print_payholl():
    """
    Through the competency date input, a query will be performed with the database returning the impression of the
    payroll referring to the competence requested with the following totals by departments: total
    earnings, total discounts and total net wages.
    :return:
    """
    accrual = input('Enter the accrual ? [MM-AAAA]:    ')
    print('-' * (28 * 7 + 13))
    conn = sqlite3.connect('data/people_management.db')
    cursor = conn.cursor()

    query_accrual = """
               SELECT s.accrual ,		
                       f.departament,
                       s.salary, 
                       s.bonus,
                       s.overtime,
                       s.late_value,
                       s.t_vouchers,
                       s.health_care,
                       s.dental_care,
                       s.meal_ticket,
                       s.inss,
                       s.irrf,
                       s.earnings,
                       s.discounts,
                       s.liquid_salary
                       FROM salary s
                            left join employees f
                             on s.name = f.full_name
                             WHERE accrual=?
                            """
    cursor.execute(query_accrual, (accrual,))
    lines = cursor.fetchall()
    columns = []

    for c in cursor.description:
        columns.append(c[0].upper().replace('_', ' '))
    columns.pop(0)
    columns.pop(0)

    for line in lines:
        values = line[2:]
        sector = lines[1]

    dic = {'DIRECTION': [0] * len(columns),
           'COMMERCIAL': [0] * len(columns),
           'CONTROLLERSHIP': [0] * len(columns),
           'PURCHASE': [0] * len(columns),
           'LOGISTICS': [0] * len(columns),
           }

    for line in lines:
        departament = line[1]
        values = line[2:]
        dic_values = dic[departament]
        for i, v in enumerate(values):
            dic_values[i] = dic_values[i] + v
        dic[departament] = dic_values
    print(f"{'COST CENTER':>10}", end=' ')

    for c in columns:
        print(f"{c:>14}", end=' ')
    print()
    print('-' * (28 * 7 + 13))

    for k, v in dic.items():
        print(f'{k:<22}', end=' ')
        for l in v:
            print(f"{round(l, 2):<13}", end=' ')
        print()

    total_list = [0] * len(columns)
    for k in dic.keys():
        departament_list = dic[k]
        for i, v in enumerate(departament_list):
            total_list[i] = total_list[i] + v
    print('-' * (28 * 7 + 13))
    print(f"{'TOTAL':<8}", end=' ')

    for t in total_list:
        print(f"{round(t, 2):>14}", end=' ')
    print()
