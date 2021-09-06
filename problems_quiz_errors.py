import data_quiz_errors as d
def problem_one():
    """ print an undefined identifier"""
    problem="""
   
   {: >4s}{}
   
   """.format("","print(x)")
    answer=("N", d.errors['N'])
    answer_explanation = "NameError: name 'x' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_two():
    """ Call a function of two parameters with three parameters """
    problem = """{: >4s}
    def fn(a,b):
        return a + b

    fn(1,2,3) 
    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: fn() takes 2 positional arguments but 3 were given"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_three():
    """ Request a non-existent attribute from an object """
    problem = """{: >4s}

    "mystring".getTime()


    """.format("")

    answer = ("A",d.errors['A'])
    answer_explanation = "AttributeError: 'str' object has no attribute 'getTime'"
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_four():
    """ call print function without parentheses """
    problem = """{: >4s}

    print "hello"

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_five():
    """ add the sum of two integers to a string """
    problem = """{: >4s}

    1 + 2 + "three" 

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_six():
    """ Attempt to open a non-existent file """
    problem = """{: >4s}

    # file 'my_missing_file' does not exist!
    
    with open('my_missing_file.txt') as f:
        f.read()

    """.format("")

    answer = ("F", d.errors['F'])
    answer_explanation = "FileNotFoundError: [Errno 2] No such file or directory: 'my_missing_file.txt'"
    error_hierarchy = d.hierarchy['F']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_seven():
    """ Divide an integer by a string """
    problem = """{: >4s}

      3 / "two"  

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for /: 'int' and 'str' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eight():
    """ Take the Square Root of -1"""
    problem = """{: >4s}

      import math
      math.sqrt(-1)

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: math domain error "
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_nine():
    """ Attempt to remove item from dictionary with .pop() (no argument)"""

    problem = """{: >4s}

      mydict = {{'a': 'alpha', 'b' : 'beta'}}
       
      mydict.pop() 

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: pop expected at least 1 argument, got 0"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)



def problem_ten():
    """ call print function with invalid quotation marks"""

    problem = """{: >4s}

      print('Simon's millions')

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: invalid syntax"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eleven():
    """ Attempt to retrieve dictionary value with non-existent key"""

    problem = """{: >4s}

      mydict = {{'a': 'alpha', 'b' : 'beta'}}
       
      mydict['c']  

    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = "KeyError: 'c'"
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_twelve():
    """ Attempt to retrieve dictionary value with non-existent key"""

    problem = """{: >4s}

      mydict = {{'a': 'alpha', 'b' : 'beta'}}
       
      mydict.get('c')  

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "There is no error and  type(mydict.get('c')) gives <class 'NoneType'>"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)
