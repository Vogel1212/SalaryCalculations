# salary adjustment according to salary height

# salaries up to BRL 800.00 (including): 20% increase
# salaries between BRL 800.00 and BRL 1000.00: 15% increase
# salaries between BRL 1000.00 and BRL 1500.00: 10% increase
# salaries from BRL 1500.00 onwards: 5% increase

current_wage = float(input('What is the employees monthly salary? US$: '))
readjust1 = 20/100
readjust2 = 15/100
readjust3 = 10/100
readjust4 = 5/100

if current_wage <= 800:
    salary_new = current_wage + ( current_wage * readjust1)
    value_increase = current_wage - salary_new
    print(f'Current salary is: {current_wage}')
    print(f'The percentage increase is: {readjust1*100:.2f} %')
    print(f'The value of the increase is: {value_increase}')
    print(f'The new salary is: {salary_new}')


elif current_wage > 800 and current_wage <=1000:
    salary_new = current_wage + (current_wage * readjust2)
    value_increase = current_wage - salary_new
    print(f'Current salary is: {current_wage}')
    print(f'The percentage increase is: {readjust2*100:.2f} %')
    print(f'The value of the increase is: {value_increase}')
    print(f'The new salary is: {salary_new}')


elif current_wage > 1000 and current_wage <= 1500:
    salary_new = current_wage + (current_wage * readjust3)
    value_increase = salary_new - current_wage
    print(f'Current salary is: {current_wage}')
    print(f'The percentage increase is: {readjust3*100:.2f} %')
    print(f'The value of the increase is: {value_increase}')
    print(f'The new salary is: {salary_new}')

elif current_wage > 1500:
    salary_new = current_wage + (current_wage * readjust4)
    value_increase = current_wage - salary_new
    print(f'Current salary is: {current_wage}')
    print(f'The percentage increase is: {readjust4*100:.2f} %')
    print(f'The value of the increase is: {value_increase}')
    print(f'The new salary is: {salary_new}')

else:
    print('Unable to calculate your salary adjustment, please re-enter your salary')