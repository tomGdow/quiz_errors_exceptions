import data_quiz_errors as d
def problem_one():
    """ print an undefined identifier"""
    problem="""
   
   {: >4s}{}
   
   """.format("","print(x)")
    answer=("N", d.errors['N'])
    answer_explanation = "NameError: name 'x' is not defined"
    return(problem, answer, answer_explanation)

def problem_two():
    """ Call a function of two parameters with three parameters """
    problem = """{: >4s}
    def fn(a,b):
        return a + b

    fn(1,2,3) 
    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: fn() takes 2 positional arguments but 3 were given"
    return(problem, answer, answer_explanation)

def problem_three():
    """ Request a non-existent attribute from an object """
    problem = """{: >4s}

    "mystring".getTime()


    """.format("")

    answer = ("A",d.errors['A'])
    answer_explanation = "AttributeError: 'str' object has no attribute 'getTime'"
    return(problem, answer, answer_explanation)

def problem_four():
    """ call print function without parentheses """
    problem = """{: >4s}

    print "hello"

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?"
    return(problem, answer, answer_explanation)


def problem_five():
    """ add the sum of two integers to a string """
    problem = """{: >4s}

    1 + 2 + "three" 

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    return(problem, answer, answer_explanation)


def problem_six():
    """ Attempt to open a non-existent file """
    problem = """{: >4s}

    # file 'my_missing_file' does not exist!
    
    with open('my_missing_file.txt') as f:
        f.read()

    """.format("")

    answer = ("F", d.errors['F'])
    answer_explanation = "FileNotFoundError: [Errno 2] No such file or directory: 'my_missing_file.txt'"
    return(problem, answer, answer_explanation)

def problem_seven():
    """ Divide an integer by a string """
    problem = """{: >4s}

      3 / "two"  

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for /: 'int' and 'str' "
    return(problem, answer, answer_explanation)
