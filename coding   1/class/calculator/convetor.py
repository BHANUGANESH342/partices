x = float(input('enter the weight : ') )
weight= input('weight in kgs or pounds {K or P}')
if weight == 'K': 
    pounds = x * 2.205
    print(f'your  enter weight is {x}, weight in pounds {pounds} ')
elif weight == 'P':
    kgs = x /2.205
    print(f'your  enter weight is {x}, weight in pounds {kgs} ')
else: 
    print(f'your entered {x} is not founded')