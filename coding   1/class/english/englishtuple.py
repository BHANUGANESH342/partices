print(f"Tell me if you ………A…….. any help.")
print(f"The first time I ……B………… him was at university.")
print(f"This is the garage …………C…….. they used to work.")
print(" I ………D………. a terrible experience yesterday.")
print('enter in small letters')
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
print('CORRECT ANSWERS ARE AS FLLOWS')
e=('need','met','where','had')
print(f"Tell me if you {e[0]}. any help. \n")
print(f"The first time I {e[1]} him was at university.\n")
print(f"This is the garage {e[2]} they used to work. \n")
print(f" I {e[3]} a terrible experience yesterday. \n")