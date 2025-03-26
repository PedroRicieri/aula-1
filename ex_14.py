num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
num3 = int(input("Insira o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"O numero maior é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O numero maior é: {num2}")
else:
    print(f"O numero maior é: {num3}")