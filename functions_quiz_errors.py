import os
import random

import data_quiz_errors as d

def opening_msg():
    os.system('cls')
    print("What is the outcome of the following code?")


def options_msg():
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'A' ,d.errors['A'], 'B', d.errors['B']))
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'C' ,d.errors['C'], 'D', d.errors['D']))
    print("{: >4s}{}: {}\t\t\t{}: {}".format("", 'E' ,d.errors['E'], 'F', d.errors['F']))
    print("{: >4s}{}: {}\t{}: {}".format("",     'G' ,d.errors['G'], 'H', d.errors['H']))


def get_user_choice(): 
    bad_input = True
    while (bad_input):
        try:
            choice = input('Your Choice ? ')
            if choice[0].upper() not in d.errors.keys():
                raise ValueError('Invalid Choice')
            bad_input=False
        except ValueError as e:
            print(e)

    return choice[0].upper()


def analyze_choice(fn,choice): 
    answer =fn()[1][0]
    while(choice != answer):
        print(f"No, the answer is not {d.errors[choice]}") 
        print('Have another go')
        choice=get_user_choice()
    print()
    print("YOU ARE RIGHT!")
    # print("{: >4s}{}".format("",'You are right!'))
    print()
    print("{: >4s}{}".format("",fn()[1]))
    print()
    print("{: >4s}{}".format("",fn()[2]))
    print()

def choose_problem():
    sample = random.sample(problem_list,1)
    return sample

def display_problem(problem): 
    opening_msg()
    print(problem()[0]) 
    options_msg()
    print()
    choice=get_user_choice()
    analyze_choice(problem,choice)

# continue_choice=True        

def continue_choice():
    continue_choice=True        
    user_choice = input("{: >4s}Continue or [Q/q]? > ".format(""))
    if (user_choice == '' or user_choice[0].upper() == "Y") and continue_choice:
        return continue_choice
    else:
        continue_choice=False
        print('Bye')
        return continue_choice


