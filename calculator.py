def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "error division by zero not defined"
    return a/b

def exponent(a,b):
    return a**b

def floor_division(a,b):
    if b==0:
        print('error zero cant be in denominator')
    return a//b    

print("select operation")
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.division')
print('5.exponent')
print('6.floor_division')

while True:

    choice = input ("enter the choice=(1/2/3/4/5/6 or 'q'to quit):")

    if choice == 'q':
        print('exiting calculator goodbye!')
        break

    if choice in ('1','2','3','4','5','6'):
        num1= int(input('enter the 1 number='))
        num2= int(input('enter the 2 number='))


    if choice == '1':

        print("result:",add(num1,num2))

    if choice == '2':

        print("result:",subtract(num1,num2))

    if choice == '3':

        print("result:",multiply(num1,num2))
    
    if choice == '4':

        print("result:",division(num1,num2))

    if choice == '5':

        print("result:",exponent(num1,num2))

    if choice == '6':

        print("result:",floor_division(num1,num2))
        break
    
   

    else:
        print("invalid choicve! please select 1,2 ,3,4 or 'q' ")