# # salary in three years, if it was increased to 10% every X years.
# from math import sqrt 

class Calculator:
    def __init__(self, sal, perc, months, total, calcfim):
        self.sal = sal
        self.perc = perc
        self.months = months
        self.calcfim = calcfim
    
    def Calculation(self):
        calc = sal*(perc/100)
        totalSal = calc+sal
    
        
sal = int(input('What is the employees monthly salary? US$'))
perc = int(input('How many percent quarterly increase?: '))
months = int(input('How many months should this calculation take?: '))

if months == 1:
    totalSal = Calculator.totalSal
elif months == 2:
    totalSal = Calculator.totalSal*2

Calculator()

print('The employees old salary was US${:.2f}, now with {}% of quarterly increase during {} years, will start to win US${:.2f} a month.\nWith an increase of US${:.2f} after 3 months'.format
      (sal,perc,months,totalSal,Calculator.calcfim,Calculator.totalSal))
