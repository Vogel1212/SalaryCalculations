
# Calculator for final salary with hours worked, with income tax deductions showing net salary.

######

gain = float(input('Value earned per hour worked: US$'))
hours = float(input('How many hours did you work this month: US$'))
raw = hours*gain
ir = raw*(11/100)
inss = raw*(8/100)
sind = raw*(5/100)
liq = raw-ir-inss-sind


print('Raw salary: US${:.2f}'.format(raw))
print('IR (11%): US${:.2f}'.format(ir))
print('INSS (8%): US${:.2f}'.format(inss))
print('Sindicato (5%): US${:.2f}'.format(sind))
print('Liquid Salary: US${:.2f}'.format(liq))