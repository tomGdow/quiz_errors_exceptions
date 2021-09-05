import os
import random


choice = ''
def opening_msg():
    os.system('cls')
    print("What is the outcome of the following code?")

errors = {"A": 'NameError', "B": 'ValueError', "C": "TypeError", "D": "IndexError",
        "E": "KeyError", "F":"SyntaxError", "G": "ZeroDivisionError", "H": "AttributeError"}

def options_msg():
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'A' ,errors['A'], 'B', errors['B']))
    print("{: >4s}{}: {}\t\t{}: {}".format("",   'C' ,errors['C'], 'D', errors['D']))
    print("{: >4s}{}: {}\t\t\t{}: {}".format("", 'E' ,errors['E'], 'F', errors['F']))
    print("{: >4s}{}: {}\t{}: {}".format("",     'G' ,errors['G'], 'H', errors['H']))


def problem_one():
    """ print an undefined identifier"""
    problem="""
   
   {: >4s}{}
   
   """.format("","print(x)")
    answer=("A", errors['A'])
    answer_explanation = "NameError: name 'x' is not defined"
    return(problem, answer, answer_explanation)

def problem_two():
    """ Call a function of two parameters with three parameters """
    problem = """{: >4s}
    def fn(a,b):
        return a + b

    fn(1,2,3) 
    """.format("")

    answer = ("C", errors['C'])
    answer_explanation = "TypeError: fn() takes 2 positional arguments but 3 were given"
    return(problem, answer, answer_explanation)

def problem_three():
    """ Request a non-existent attribute from an object """
    problem = """{: >4s}

    "mystring".getTime()


    """.format("")

    answer = ("H",errors['H'])
    answer_explanation = "AttributeError: 'str' object has no attribute 'getTime'"
    return(problem, answer, answer_explanation)

def problem_four():
    """ call print function without parentheses """
    problem = """{: >4s}

    print "hello"

    """.format("")

    answer = ("F", errors['F'])
    answer_explanation = "SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?"
    return(problem, answer, answer_explanation)


def get_user_choice(): 
    bad_input = True
    while (bad_input):
        try:
            choice = input('Your Choice ? ')
            if choice[0].upper() not in errors.keys():
                raise ValueError('Invalid Choice')
            bad_input=False
        except ValueError as e:
            print(e)

    return choice[0].upper()


def analyze_choice(fn,choice): 
    answer =fn()[1][0]
    while(choice != answer):
        print(f"No, the answer is not {errors[choice]}") 
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

continue_choice=True        

def continue_choice():
    continue_choice=True        
    user_choice = input("{: >4s}Continue or [Q/q]? > ".format(""))
    if (user_choice == '' or user_choice[0].upper() == "Y") and continue_choice:
        return continue_choice
    else:
        continue_choice=False
        print('Bye')
        return continue_choice


if __name__ == '__main__':
    display_problem(problem_one)
    user_continue_choice=continue_choice()
    if user_continue_choice:
        display_problem(problem_two)
    user_continue_choice=continue_choice()
    if user_continue_choice:
        display_problem(problem_three)
    user_continue_choice=continue_choice()
    if user_continue_choice:
        display_problem(problem_four)
