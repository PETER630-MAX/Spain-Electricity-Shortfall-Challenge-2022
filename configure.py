'''
This is a code for a calculator, which only accepts operators such
as "+", "-", "*", "/"
'''

num1 = float(input("Enter First Number: "))
operator = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))

if operator=="+":
    print(num1 + num2)

elif operator=="-":
    print(num1 - num2)
elif operator=="*":
    print(num1 * num2)
elif operator=="/":
    print(num1 / num2)
else:
    print("invalid operator")