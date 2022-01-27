# Calculation of salary with annual increase based on X years

Sal = (float(input("What is your current salary? R$: ")))
Inc = (float(input("What is the percentage of annual increase?: ")))
Term = (int(input("In how many years do you intend to do this calculation?: ")))
Year = 0

while Year < Term:
    Sal += Sal * Inc / 100
    Sal = round (Sal, 2)
    Year += 1
    print ("Year:", Year, ";   Monthly Salary: $", Sal)