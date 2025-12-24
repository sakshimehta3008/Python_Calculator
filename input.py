print("Hello to Python Calculator!")
print("Choose any one of the operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exit")
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
input= int(input("Enter your choice: "))

if(input==6):
    print("Calculator closed!")
elif(input==1):
    print("Sum of two numbers is: ",num1+num2)
elif(input==2):
    print("Difference of two numbers is: ",num1-num2)
elif(input==3):
    print("Product of two numbers is: ",num1*num2)
elif(input==4):
    if(num2==0):
        print("Divison by 0 not possible!")
    else:
        print("Quotient of two numbers is: ",num1/num2)
elif(input==5):
    print("Remainder of two numbers is: ",num1%num2)
else:
    print("Not a valid choice")