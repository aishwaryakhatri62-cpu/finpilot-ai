def calculate_salary(base, overtime, bonus, deductions):
    overtime_pay = overtime * 500
    gross = base + overtime_pay + bonus
    tax = gross * 0.1
    net = gross - tax - deductions
    return gross, tax, net
