import data_quiz_errors as d
def problem_one():
    """ print an undefined identifier"""
    problem="""
   
   {: >4s}{}
   
   """.format("","print(x)")
    answer=("A", d.errors['A'])
    answer_explanation = "NameError: name 'x' is not defined"
    return(problem, answer, answer_explanation)

def problem_two():
    """ Call a function of two parameters with three parameters """
    problem = """{: >4s}
    def fn(a,b):
        return a + b

    fn(1,2,3) 
    """.format("")

    answer = ("C", d.errors['C'])
    answer_explanation = "TypeError: fn() takes 2 positional arguments but 3 were given"
    return(problem, answer, answer_explanation)

def problem_three():
    """ Request a non-existent attribute from an object """
    problem = """{: >4s}

    "mystring".getTime()


    """.format("")

    answer = ("H",d.errors['H'])
    answer_explanation = "AttributeError: 'str' object has no attribute 'getTime'"
    return(problem, answer, answer_explanation)

def problem_four():
    """ call print function without parentheses """
    problem = """{: >4s}

    print "hello"

    """.format("")

    answer = ("F", d.errors['F'])
    answer_explanation = "SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?"
    return(problem, answer, answer_explanation)
