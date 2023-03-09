# THIS PROGRAM IS FOR A SIMPLE CALCULATOR IN PYTHON                                                                                                                                 
# "BIRRA MUNIR"                                                                                                                                                                                           # "08.03.2023"                                                                                                                                                                                             


# IMPORT LINRARIES
import operator
import math
import numpy as np
import time


op_dict = {'1': operator.add, '2': operator.sub, '3':operator.mul,
           '4':operator.truediv, '5':'Second Power', '6':'Square Root', '7':'Exit'}
sym_dict = {'1.': 'Addition', '2.': 'Subtraction', '3.': 'Multiplication', '4.': 'Division',
            '5.':'Second Power', '6.': 'Square Root', '7.': 'Exit'}

def calculator(op):
    global op_dict

    def num_input():
        return input('Give the number here: ')

    def nums_input():
        a = input('Give the first number here: ')
        b = input('Give the second number here: ')
        return a,b
    if op == '7':
        print('Thank you for using the calculator')
        exit()
    elif op == '6':
        a = num_input()
        ans = math.sqrt(int(a))
        time.sleep(1)
        print('The answer is: {}'.format(ans))
    elif op == '5':
        a = num_input()
        time.sleep(1)
        ans = np.square(int(a))
        print('The answer is: {}'.format(ans))

    else:
        a,b = nums_input()
        ans = op_dict[op](int(a),int(b))
        time.sleep(1)
        print('The answer is: {}'.format(ans))

def op_input():
    user_inp = input('Give the number for the operation to perform: ')
    return user_inp
def menu(sym_dict):
    for num,op in sym_dict.items():
        print(num,op)


while True:
    time.sleep(1)
    print('Choose number for the operation to perform')
    menu(sym_dict)
    operation = op_input()
    time.sleep(1)
    print('You chose: {}'.format(sym_dict[operation+'.']))
    time.sleep(1)
    calculator(operation)
