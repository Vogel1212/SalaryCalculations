# # salary in three years, if it was increased to 10% every X years.
# from math import sqrt 
# ######
# sal = int(input('What is the employees monthly salary? US$'))
# perc = int(input('How many percent quarterly increase?: '))
# months = int(input('How many months should this calculation take?: '))
# calc = sal*(perc/100)
# num = sqrt()
# totalSal = calc+sal

# methodCalc = 

# while True:
#     if  months == 3:
#         sum1 = totalSal
#         sum2 = sum1*(perc/100)   

#         sum3 = sum2
#         sum4 = sum3*(perc/100) 

#         sum5 = sum4
#         sum6 = sum5*(perc/100)  
#         break

# total = sum6+sal
# calcfim = total-sal

# print('The employees old salary was US${:.2f}, now with {}% of quarterly increase during {} years, will start to win US${:.2f} a month.\nWith an increase of US${:.2f} after 3 months'.format
#       (sal,perc,months,total,calcfim))

class Calculator:
    def __init__(self, sal, perc, months, total, calcfim):
        self.sal = sal
        self.perc = perc
        self.months = months
    
    def Calculation(self):
        calc = sal*(perc/100)
        totalSal = calc+sal
    

        
sal = int(input('What is the employees monthly salary? US$'))
perc = int(input('How many percent quarterly increase?: '))
months = int(input('How many months should this calculation take?: '))

print('The employees old salary was US${:.2f}, now with {}% of quarterly increase during {} years, will start to win US${:.2f} a month.\nWith an increase of US${:.2f} after 3 months'.format
      (sal,perc,months,total,calcfim))