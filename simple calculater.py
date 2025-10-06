print("Simple Calculater")
print("Select an Opation")
print("1. Addion")
print("2. Substraction")
print("3. Multipication")
print("4. Division")
print("0. End the program")

while True:
    operation = int(input("Enter  choice(1/2/3/4/0) >> "))
    num1 = float(input("Enter num1 >> "))
    num2 = float(input("Enter num2 >> "))

    if operation == 1:
        print(num1+num2)
    elif operation == 2:
        print(num1-num2)
    elif operation == 3:
        print(num1*num2)
    elif operation == 4:
        print(num1/num2)
    elif operation == 0:
        break
    else:
        print("Invaild option Please Try Again")