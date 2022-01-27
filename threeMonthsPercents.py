# # salary in three years, if it was increased to 10% every X years.
# from math import sqrt 

# class Calculator:
#     def __init__(self, sal, perc, months, total, calcfim, result):
#         self.sal = sal
#         self.perc = perc
#         self.months = months
#         self.calcfim = calcfim
#         self.result = result
    
#     # def Calculation(self):
#     #     calc = sal*(perc/100)
#     #     totalSal = calc+sal
    
#     def Calculation(self):
#         result = sal + (sal * 0.15)
        
# sal = int(input('What is the employees monthly salary? US$'))
# perc = int(input('How many percent quarterly increase?: '))
# months = int(input('How many months should this calculation take?: '))

# if months == 1:
#     totalSal = Calculator.result
# elif months == 2:
#     totalSal = Calculator.result*2

# Calculator()

# print('The employees old salary was US${:.2f}, now with {}% of quarterly increase during {} years, will start to win US${:.2f} a month.\nWith an increase of US${:.2f} after 3 months'.format
#       (sal,perc,months,totalSal,Calculator.calcfim,Calculator.result))


# sal = int(input('What is the employees monthly salary? US$: '))
# perc = int(input('How many percent quarterly increase?: '))
# percT = (1.0/perc*100)
# result = sal + (sal * percT)
# print('Salary plus {} percent is: {}'.format(perc,result))

current_wage = float(input('What is the employees monthly salary? US$: '))
readjust1 = 20/100
readjust2 = 15/100
readjust3 = 10/100
readjust4 = 5/100

if current_wage <= 280:
    salary_new = current_wage + ( current_wage * readjust1)
    value_increase = current_wage - salary_new
    print(f'O salário atual é: {current_wage}')
    print(f'O percentual de aumento é: {readjust1*100:.2f} %')
    print(f'O valor do aumento é: {value_increase}')
    print(f'O novo salário é: {salary_new}')


elif current_wage > 280 and current_wage <=700:
    salary_new = current_wage + (current_wage * readjust2)
    value_increase = current_wage - salary_new
    print(f'O salário atual é: {current_wage}')
    print(f'O percentual de aumento é: {readjust2*100:.2f} %')
    print(f'O valor do aumento é: {value_increase}')
    print(f'O novo salário é: {salary_new}')


elif current_wage > 700 and current_wage <= 1500:
    salary_new = current_wage + (current_wage * readjust3)
    value_increase = salary_new - current_wage
    print(f'O salário atual é: {current_wage}')
    print(f'O percentual de aumento é: {readjust3*100:.2f} %')
    print(f'O valor do aumento é: {value_increase}')
    print(f'O novo salário é: {salary_new}')

elif current_wage > 1500:
    salary_new = current_wage + (current_wage * readjust4)
    value_increase = current_wage - salary_new
    print(f'O salário atual é: {current_wage}')
    print(f'O percentual de aumento é: {readjust4*100:.2f} %')
    print(f'O valor do aumento é: {value_increase}')
    print(f'O novo salário é: {salary_new}')

else:
    print('Não foi possível calcular seu reajuste, digite novamente seu salário atual')