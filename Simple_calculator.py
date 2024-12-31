num1=float(input("enter the 1st number : "))
num2=float(input("enter the 2nd number : "))
operator=input("enter operator(+,-,*,/) : " )
validity=1  #validity check of operator:  assuming if 1 than valid
if operator=='+':
    answer=num1+num2
elif operator=='-':
    answer=num1-num2
elif operator=='*':
    answer=num1*num2
elif operator=='/':
    answer=num1/num2
else:
    validity=0 # 0 for invalid

if validity==1 :
    print(f"The final answer is {round(answer,6)}")
else :
    print(f"'{operator}' is an invalid operator!")
