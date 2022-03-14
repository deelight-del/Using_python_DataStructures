#Two functions of armstrong number test definition

#Function definition 2
def armstrong():
    
    """
An armstrong number is any number of n digits which
is equal to the sum of nth power of digits in the number. 
Generally in most programming cases we consider numbers from 000 to 999 
that is 3 digit numbers. Thus, we also define armstrong number is 
any number of 3 digits as sum of cubes of digits in number.

For example:
3 digit armstrong number 153=(1*1*1)+(5*5*5)+(3*3*3)
4 digit armstrong number 1634=(1*1*1*1)+(6*6*6*6)+(3*3*3*3)+(4*4*4*4)

Functions take an input 'x' and rteurns whether digit is
an armstrong number or not
"""
    
    global x
    x = input('enter your armstrong number ')
    length = len(x)
    number = int(x)
    armstrong_test = 0
    for dig in x:
        armstrong_test = armstrong_test + (int(dig)**length)
    if armstrong_test == number:
        print(f'{x} is an armstrong number')
    else:
        print(f'{x} is  not an armstrong number')
        
        pass
    pass

def armstrong_():
    
   """
An armstrong number is any number of n digits which
is equal to the sum of nth power of digits in the number. 
Generally in most programming cases we consider numbers from 000 to 999 
that is 3 digit numbers. Thus, we also define armstrong number is 
any number of 3 digits as sum of cubes of digits in number.

For example:
3 digit armstrong number 153=(1*1*1)+(5*5*5)+(3*3*3)
4 digit armstrong number 1634=(1*1*1*1)+(6*6*6*6)+(3*3*3*3)+(4*4*4*4)

Functions take an input 'x' and rteurns whether digit is
an armstrong number or not
"""
    num = int(input('Enter your armstrong number: '))
    order = len(str(num))
    temp=num
    armstrong_test = 0
    while temp>0:
        unit = temp%10
        armstrong_test = armstrong_test + (unit**order)
        temp = temp//10
    if armstrong_test == num:
        print(f'{num} is an armstrong number')
    else:
        print(f'{num} is  not an armstrong number')
