num1=float(input("Enter the First Number:"))
num2=float(input("Enter the Second Number:"))
operation=input("Choose the Operation (+,-,*,/,^):")
if operation=='+':
           result=num1+num2
elif operation=='-':
           result=num1-num2
elif operation=='*':
           result=num1*num2
elif operation=='/':
           result=num1/num2
elif operation=='^':
           result=num1**num2
else:
    print("Invalid Input")
print(f"The result is {result}")           
           
           
           
           
           
           
