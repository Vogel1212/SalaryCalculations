
# Calculator for final salary with hours worked, with income tax deductions showing net salary.

######

ganho = float(input('Value earned per hour worked: US$'))
horas = float(input('How many hours did you work this month: US$'))
bruto = horas*ganho
ir = bruto*(11/100)
inss = bruto*(8/100)
sind = bruto*(5/100)
liq = bruto-ir-inss-sind


print('Gross salary: US${:.2f}'.format(bruto))
print('IR (11%): US${:.2f}'.format(ir))
print('INSS (8%): US${:.2f}'.format(inss))
print('Sindicato (5%): US${:.2f}'.format(sind))
print('Liquid Salary: US${:.2f}'.format(liq))