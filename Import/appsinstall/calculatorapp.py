def init():
    print("Calculator ...")
    a = int(input("input number one : "))
    b = int(input("input number two : "))
    operation = input("input operation : ")
    if operation == "/":
        print(a/b)
    if operation == "*":
        print(a*b)
    if operation == "+":
        print(a+b)
    if operation == "-":
        print(a-b)