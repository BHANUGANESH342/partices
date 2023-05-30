cal=input('enter the operator( +,-,*,/ )')
num1=float(input('enter num 1 : '))
num2=float(input('enter num 2 : '))

if cal=='+':
    print('addition : ',num1+num2)
elif cal=='-': 
    print('subtraction : ',num1-num2)
elif cal=='*':
    print('multipilication : ',num1*num2)
elif cal=='/':
    print('division : ',num1/num2)
else: 
    print(f'{cal} not a oprator founded')