print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Cria a porcentagem que será usada
tipPercentage = tip / 100

# Calcula o valor total da gorjeta
totalTip = bill * tipPercentage

# Calcula o valor total da conta incluindo a gorjeta
totalBill = bill + totalTip

# Divide o valor total pelo número de pessoas
total = totalBill / people

# Arredonda o valor para 2 casas decimais
final = round(total, 2)

# Imprime o valor final por pessoa
print(f"Each person should pay: ${final}")
