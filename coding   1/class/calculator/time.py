import time as t
s=int(input('enter the time in seconds  : ')) 
for x in range(s,00,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours =int (x / 3600)
    print(f' {hours:02} : {minutes:02} : {seconds:02}') 
    t.sleep(1)
print('the time is up   @ bye')