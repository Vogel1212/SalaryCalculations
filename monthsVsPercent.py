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

salary = input ("Insert the value of your salary ")
expenses = input ("insert the value of your expenses ")

percentage = (float(expenses)*100)/float(salary)

print("You spend ",percentage ,"%", "of your salary in your expenses.")