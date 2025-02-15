while True:
    n1 = float(input("Enter the first numbe: "))
    n2 = float(input("Enter the second number: "))
    operator = input("Enter operation add,sub,mul or div: ")

    if operator== "+":
        print("Result:", n1 + n2)
    elif operator == "-":
        print("Result:", n1 - n2)
    elif operator== "*":
        print("Result:", n1 * n2)
    elif operator == "/":
        print("Result:", n1 / n2 if n2 != 0 else "Error: Division by zero")
    else:
        print("Invalid operation enterd")