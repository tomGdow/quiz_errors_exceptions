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
    """ Remove item from dictionary with .pop() (no argument)"""

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
       
      mydict.get('c', 'Not There')  

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
    answer_explanation = "No Error. Returns None, but myset updated to {40, 10, 20, 30}"
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
    import random
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
    import random
    mylist = [1,2,3]
    random.sample(mylist,4)
    

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Sample larger than population or is negative"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_five():         
    """ Call undefined attribute on file object 

    """

    problem = """{: >4s}
    
    # 'abc.txt' is a file in the working directory

    f=open('abc.txt')
    f.readall()

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: '_io.TextIOWrapper' object has no attribute 'readall'"
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_six():         
    """ If block with indentation error 

    """

    problem = """{: >4s}

        a=10
        if a >= 10:
...         a+=2
...             print(a)

    """.format("")

    answer = ("D", d.errors['D'])
    answer_explanation = "IndentationError: unexpected indent"
    error_hierarchy = d.hierarchy['D']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_twenty_seven():         
    """ attempt to remove a non-existent element from a set with .remove() 

    """

    problem = """{: >4s}

    myset=set(['tom','dick', 'harry'])

    myset.remove('dave')
    

    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = """keyerror: 'dave'
    .remove() removes an element from a set; it must be a member.
    If the element is not a member, a KeyError is raised
    """
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)
     
def problem_twenty_eight():         
    """ attempt to remove a non-existent element from a set with .discard() 

    """

    problem = """{: >4s}

    myset=set(['tom','dick', 'harry'])

    myset.discard('dave')
    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. type(myset.discard('dave')) gives <class 'NoneType'>"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_twenty_nine():         
    """ attempt to remove a non-existent element from a set 
    using .discard() with two arguments 

    """

    problem = """{: >4s}

    myset=set(['tom','dick', 'harry'])

    myset.discard('dave', 'not there')
    

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: discard() takes exactly one argument (2 given)"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_thirty():         
    """ Call try-else-finally code block without an except clause 
       
    """

    problem = """{: >4s}

    try:                     
        x = int(input("Enter the denominator" ))
        y = 1 / x
    else:
        print('Cannot divide by Zero')
    finally:
        print('I always print')
    
    print('j', end = ' ')

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = """SyntaxError: invalid syntax.
    ('else' clause must be preceded by 'except' clause)"""
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)



def problem_thirty_one():         
    """ Use .popitem() without an argument to remove last item from dictionary
    """

    problem = """{: >4s}
    
    mydict = {{'a': 'alpha', 'b' : 'beta'}}

    mydict.popitem() 

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """Removes last item and returns it. mydict.popitem() (* ('b', 'beta') *)"""
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)



def problem_thirty_two():         
    """Call .add() to add element to empty dictionary ('{{}}')
    """

    problem = """{: >4s}
    
    x = {{}}
    x.add('tom')

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: 'dict' object has no attribute 'add' "
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_thirty_three():         
    """Call .add() to add element to emtpty set 

    """

    problem = """{: >4s}
    
    x = set()
    x.add('tom')
    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No error. type(x.add('tom')) (* <class 'NoneType'> *) 
    type(x)  (* <class 'set'> *)"""
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_thirty_four():         
    """ Re-import a module where name of module is no longer defined 

    """

    problem = """{: >4s}

    # 'greetings.py' is a valid module in the working directory

    import greetings as gr

    import importlib
    importlib.reload(greetings)
    

    """.format("")

    answer = ("N", d.errors['N'])
    answer_explanation = "NameError: name 'greetings' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)

  
def problem_thirty_five():         
    """ Call .format() method on a string with too many arguments

    """

    problem = """{: >4s}

    print("{{}},{{}},{{}}".format(2,3,4,5))    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error: returns '2,3,4' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_thirty_six():         
    """ Call .format() method on a string with too many arguments 

    """

    problem = """{: >4s}

    print("{{}},{{}},{{}}".format(2,3))    

    """.format("")

    answer = ("I", d.errors['I'])
    answer_explanation = "IndexError: Replacement index 2 out of range for positional args tuple"
    error_hierarchy = d.hierarchy['I']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_thirty_seven():         
    """ Call the builtin function any() with too many arguments

    """

    problem = """{: >4s}

    any(0,1,0,0,1)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: any() takes exactly one argument (5 given)"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_thirty_eight():         
    """ Call the builtin function any() with a single tuple as argument

    """

    problem = """{: >4s}

    any((0,1,0,0,1)) 

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """True 
    (any() returns True if bool(x) is True for any x in the iterable)"""
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_thirty_nine():         
    """call .now() method on datetime.date object 

    """

    problem = """{: >4s}

    import datetime
    now = datetime.date.now()
    

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: type object 'datetime.date' has no attribute 'now' "
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty():         
    """ DOCSTRING HERE 

    """

    problem = """{: >4s}
    import datetime
    today=datetime.datetime.now()
    april_fools= datetime.date(today.year, 4, 1)
    (today - april_fools).days

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'datetime.date'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_one():         
    """ subtract two date objects

    """

    problem = """{: >4s}
    import datetime
    today=datetime.date.today()
    april_fools= datetime.date(today.year, 4, 1)
    (today - april_fools).days    

    """.format("")
                             
    answer = ("X", d.errors['X'])
    answer_explanation = "No Error // 173 "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_two():         
    """ call deltatime constructor with months keyword argument 

    """

    problem = """{: >4s}
    
    delta_t = datetime.timedelta(months=1)

    """.format("")
                             
    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'months' is an invalid keyword argument for __new__()"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_three():         
    """ call deltatime constructor with weeks keyword argument 

    """

    problem = """{: >4s}
    
    delta_t = datetime.timedelta(weeks=4)          

    """.format("")
                             
    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. print(delta_t)  // 28 days, 0:00:00"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_four():         
    """ Call min function on array with element of different types

    """

    problem = """{: >4s}

    min(['tom', 'dick', 'harry',1])
    

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = " TypeError: '\u003C' not supported between instances of 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_five():         
    """ Call random.choises() on list with key value greater than length of list 

    """

    problem = """{: >4s}
    import random
    random.choices([1,2,3],k=4)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error: example output is '[2, 3, 3, 1]' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_forty_six():         
    """ Call random.choises() on list with key value greater than length of list 

    """

    problem = """{: >4s}
    import random
    random.choices([1,2,3],4)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'int' object is not iterable"            
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_seven():         
    """ Use strptime method of datetime object to correctly format date 

    """

    problem = """{: >4s}
    datetime.datetime.strptime('17/2000/3', "%d/%Y/%m")
    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error: datetime.datetime(2000, 3, 17, 0, 0)"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_eight():         
    """ Use strptime method of datetime object to format date with unconverted data

    """

    problem = """{: >4s}
          datetime.datetime.strptime('17/2000/3/', "%d/%Y/%m")

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: unconverted data remains: /"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_forty_nine():         
    """ Use strptime method of datetime object to format date where month value 
    is out of range

    """

    problem = """{: >4s}

    datetime.datetime.strptime('3/2000/17', "%d/%Y/%m")
    

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: unconverted data remains: 7"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty():         
    """ Delete from dictionary using del and non-existant key 

    """

    problem = """{: >4s}

    mydict = {{'fname': 'tom', 'lname': 'doe'}}
    del mydict['firstname']

    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = "KeyError: 'firstname'"
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_fifty_one():         
    """ Delete from dictionary using .pop and non-existant key 

    """

    problem = """{: >4s}
                                                     
    mydict = {{'fname': 'tom', 'lname': 'doe'}}
    mydict.pop('firstname')
                                                    

    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = "KeyError: 'firstname' "
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_two():         
    """ assert with false inequality 

    """

    problem = """{: >4s}
    
    a = 4
    b = 5
    assert a > b

    """.format("")

    answer = ("R", d.errors['R'])
    answer_explanation = "AssertionError"
    error_hierarchy = d.hierarchy['R']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_three():         
    """ Add None to integer 

    """

    problem = """{: >4s}

    None + 1    

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_four():         
    """ Add boolean to integer 

    """

    problem = """{: >4s}

    True + 1
    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error.  // output is 2"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_five():         
    """ Use del statement to delete tuple item 

    """

    problem = """{: >4s}

    my_tuple= (1,2,3)

    del my_tuple[0]
    

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'tuple' object doesn't support item deletion"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_six():         
    """ Use 'break' within if statement without enclosing loop 

    """

    problem = """{: >4s}

    a = 2
    if a < 5:
        print('hello')
        a += 1
        break
    else:
        print('goodbye')

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: 'break' not properly in loop"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_fifty_seven():         
    """ Use 'break' within if statement with enclosing loop

    """

    problem = """{: >4s}

    for i in range(3):
        if i:
            print('hello')
            break
        else:
            print('goodbye')

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No Error. Output:
    goodbye
    hello
    """
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_fifty_eight():         
    """ Format an integer with number type 'n' with comma as thousands separator 

    """

    problem = """{: >4s}
    
    "{{:,n}}".format(1000)

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Cannot specify ',' with 'n' "
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_fifty_nine():         
    """  Format a string with number type 'n' 
    """

    problem = """{: >4s}

    "{{:n}}".format('string')

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Unknown format code 'n' for object of type 'str' "
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)
