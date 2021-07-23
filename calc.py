select = int(input("Please select your operation of choice from 1, 2, 3 or 4: "))
num1 = int(input("What is your first number of choice? " ))
num2 = int(input("What is your second number of choice? " ))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        " 1. Add\n" \
        " 2. Subtract\n" \
        " 3. Multiply\n" \
        " 4. Divide\n")

def calc(select, num1, num2):
    
    if select == 1:
        return num1, "+", num2, "=", add(num1, num2)

    elif select == 2:
        return num1, "-", num2, "=", subtract(num1, num2)

    elif select == 3:
        return num1, "*", num2, "=",multiply(num1, num2)

    elif select == 4:
        return num1, "/", num2, "=", divide(num1, num2)

    else:
        return "Invalid input"

output = calc(select, num1, num2)
print(output)
  