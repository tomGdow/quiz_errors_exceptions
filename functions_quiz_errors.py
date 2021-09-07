import os
import random

import data_quiz_errors as d
import problems_quiz_errors as p

def opening_msg():
    os.system('cls')
    print("What error type, if any, is produced by the following code?")

def options_msg():
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'N' ,d.errors['N'], 'V', d.errors['V']))
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'T' ,d.errors['T'], 'I', d.errors['I']))
    print("{: >4s}{}: {}\t\t\t{}: {}".format("", 'K' ,d.errors['K'], 'S', d.errors['S']))
    print("{: >4s}{}: {}\t{}: {}".format("",     'Z' ,d.errors['Z'], 'A', d.errors['A']))
    print("{: >4s}{}: {}\t{}: {}".format("",     'F' ,d.errors['F'], 'X', d.errors['X']))
    print("{: >4s}{}: {}\t\t{}: {}".format("",     'D' ,d.errors['D'], 'B', d.errors['B']))


def get_user_choice(): 
    bad_input = True
    while (bad_input):
        try:
            choice = input('Your Choice ? ')
            if choice != '':
                choice = choice[0].upper()
            if choice not in d.errors.keys():
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
    print("{: >4s}{}".format("",fn()[3]))

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
    user_choice = input("CONTINUE or [Q/q]? > ")
    if (user_choice == '' or user_choice[0].upper() == "Y") and continue_choice:
        return continue_choice
    else:
        continue_choice=False
        print('Bye')
        return continue_choice

def next_question(problem, choice_fn):
    user_continue_choice = choice_fn()
    if user_continue_choice:
        display_problem(problem)
    return user_continue_choice # here
    
