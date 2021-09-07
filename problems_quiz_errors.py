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

def problem_thirteen():
    """ Attempt to retrieve dictionary value with non-existent key"""

    problem = """{: >4s}

      mydict = {{'a': 'alpha', 'b' : 'beta'}}
       
      mydict.get('c', 'Not There)  

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "There is no error and  type(mydict.get('c')) gives <class 'str'>"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fourteen():         
    """ Add a string to the sum of two integers """

    problem = """{: >4s}

    a = 10
    b = 20
    c = '30'
    result = a + b + c 

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_fifteen():         
    """ Add a string to an integer (zero) 

    error: The problem occurs with sum += mark (TypeError) 

    """

    problem = """{: >4s}

    data=[]
    def get_data():
    	for i in range(1,5):
    		marks=input('Enter Marks:')
    		data.append(marks)

    def get_avg():
    	sum=0
    	for mark in data:
    		sum += mark     
    	return sum/len(data)
    get_data()
    print(get_avg())

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +=: 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_sixteen():         
    """ call an undefined function 

    """

    problem = """{: >4s}
    
    def calc_sum(x,y):
        op = x + y
        return(op)

    ss = calc_su(5,10)
    print(ss)

    """.format("")

    answer = ("N", d.errors['N'])
    answer_explanation = "NameError: name 'calc_su' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventeen():         
    """ Call .add() on a list  

    """

    problem = """{: >4s}
    
    l=[10,20,30]         
    l.add(30)

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: 'list' object has no attribute 'add'"
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighteen():         
    """ Call .add() on a set 

    """

    problem = """{: >4s}

    myset = {{10, 20, 30}}
    myset.add(40)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_nineteen():         
    """ call print() on undefined identifier

    """

    problem = """{: >4s}
    
    title ="python in easy steps"
    print titel

    """.format("")

    answer = ("N", d.errors['N'])
    answer_explanation = "NameError: name 'titel' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)
                     

def problem_twenty():         
    """ Multiply an undefined identifier

    """

    problem = """{: >4s}
    
    4 + spam * 3

    """.format("")

    answer = ("N", d.errors['N'])                          
    answer_explanation = "NameError: name 'spam' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_one():         
    """ Call int() on a string

    """

    problem = """{: >4s}
    
    ab = int('hi') 

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: invalid literal for int() with base 10: 'hi'"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_two():         
    """ Call random.choice() on an empty sequence

    """

    problem = """{: >4s}
    
    import random
    random.choice([])

    """.format("")

    answer = ("I", d.errors['I'])
    answer_explanation = "IndexError: Cannot choose from an empty sequence"
    error_hierarchy = d.hierarchy['I']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_three():         
    """ Call random.sample() on list with key value equal to length of list 

    """

    problem = """{: >4s}
    mylist = [1,2,3]
    random.sample(mylist,3)
    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error: output is '[2, 1, 3]' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_twenty_four():         
    """ Call random.sample() on list with key value greater than length of list 

    """

    problem = """{: >4s}
    mylist = [1,2,3]
    random.sample(mylist,4)
    

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Sample larger than population or is negative"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)
