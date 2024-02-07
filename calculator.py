print('''
      + addition
      - subtract
      * multiply
      / divide''')
num1=int(input("enter the value1:-"))
num2=int(input("enter the value2:-"))
opr=(input("enter the opr:-"))
if opr=="+":
    print(num1+num2)     #Addition
elif opr=="-":
    print(num1-num2)     #subtraction
elif opr=="*":
    print(num1*num2)     #mulplication
elif opr=="/":
    print(num1//num2)    #divide
elif opr=="%":           
    print(num1%num2)     #modulus/reminder
elif opr=="**":
    print(num1**num2)    #exponential
else:
    print("invalid opr....")
