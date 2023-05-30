print(f"Tell me if you ………A…….. any help.")
print(f"  The first time I ……B………… him was at university.")
print(f"This is the garage …………C…….. they used to work.")
print(" I ………D………. a terrible experience yesterday.")
A=input('enter A answer   :')
B=input('enter B answer   :')
C=input('enter C answer   :')
D=input('enter D answer   :')
coun=0


def answers(A,B,C,D):
    if A=="need":
        print(True)
    else:
        print(False)
    if B=="met":
        print(True)
    else:
        print(False)
    if C=="where":
        print(True)
    else:
        print(False)
    if D=="had":
        print(True)
    else:
        print(False)


answers(A,B,C,D)
      
    
