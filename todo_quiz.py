
    """ problems

>>> "{:,n}".format(1e4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Cannot specify ',' with 'n'.
>>>

>>> "{:n}".format("tom")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Unknown format code 'n' for object of type 'str'


      
    """
def problem_fifty_two():         
    """ Print a float with 'd' format code 

    """

    problem = """{: >4s}

    import math
    val= math.sqrt(2)
    print("{{:d}}".format(val))

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Unknown format code 'd' for object of type 'float' "
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_three():         
    """ Print a float with 'f' format code 

    """

    problem = """{: >4s}
    
    print("{{:.0f}}".format(math.sqrt(4)))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. math.sqrt(4) is a float. Output is 2"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_four():         
    """ Print a float with 'd' format code 

    """

    problem = """{: >4s}
    
    import math
    print("{{:d}}".format(math.pow(2,3)))

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Unknown format code 'd' for object of type 'float'"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_five():         
    """ Print an integer with 'd' format code 

    """

    problem = """{: >4s}
    
    print("{{:d}}".format(pow(2,3)))
    """.format("")

    answer = ("X", d.errors['X'])         
    answer_explanation = "No error. Output is 8"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_six():         
    """ Print an integer with 'd' format code

    """

    problem = """{: >4s}
                                             
    print("{{:d}}".format(2**3))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 8"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_seven():         
    """ Missing semi-colon in for statement 

    """

    problem = """{: >4s}

    for i in range(4)
        print(i)

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: invalid syntax"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)
