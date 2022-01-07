
# Calculator for final salary with hours worked, with income tax deductions showing net salary.

######

ganho = int(input('Value earned per hour worked: US$'))
horas = int(input('How many hours did you work this month: US$'))
bruto = horas*ganho
ir = bruto*(11/100)
inss = bruto*(8/100)
sind = bruto*(5/100)
liq = bruto-ir-inss-sind


print('Gross salary: US${}'.format(bruto))
print('IR (11%): US${}'.format(ir))
print('INSS (8%): US${}'.format(inss))
print('Sindicato (5%): US${}'.format(sind))
print('Liquid Salary: US${}'.format(liq))