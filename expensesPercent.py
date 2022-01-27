# Calculating expenses with percentage

salary = input ("What is your salary? R$: ")
expenses = input ("What are your expenses? R$: ")

percent = (int(expenses)*100)/int(salary)

print('You spend {:.2f}''% ' 'of your salary in expenses'.format(percent))