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
    print(titel)

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

        a = 10
        if a >= 10:
            a += 2
                print(a)

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


def problem_sixty():         
    """Format an integer with 'd' and precision value 

    """

    problem = """{: >4s}

    "{{:.4d}}".format(1000)

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Precision not allowed in integer format specifier"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_sixty_one():         
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


def problem_sixty_two():         
    """ Print a float with 'f' format code 

    """

    problem = """{: >4s}

    print("{{:.0f}}".format(math.sqrt(4)))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. math.sqrt(4) is a float. Output is 2"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_sixty_three():         
    """Format a float with '%d' 

    """

    problem = """{: >4s}

    print("%d" % math.sqrt(2))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 1"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_sixty_four():         
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


def problem_sixty_five():         
    """ Print an integer with 'd' format code 

    """

    problem = """{: >4s}

    print("{{:d}}".format(pow(2,3)))
    """.format("")

    answer = ("X", d.errors['X'])         
    answer_explanation = "No error. Output is 8"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_sixty_six():         
    """ Print an integer with 'd' format code

    """

    problem = """{: >4s}

    print("{{:d}}".format(2**3))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 8"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_sixty_seven():         
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


def problem_sixty_eight():         
    """ Increment an unassigned variable within a function 

    """

    problem = """{: >4s}

    x=10
    def myfn(arg):
        x += arg
        return x    

    myfn(20)

    """.format("")

    answer = ("U", d.errors['U'])
    answer_explanation = "UnboundLocalError: local variable 'x' referenced before assignment"
    error_hierarchy = d.hierarchy['U']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_sixty_nine():         
    """ Add undefined variable to function argument 

    """

    problem = """{: >4s}

    def fn(arg):
        x + arg
        return arg

    fn(2)

    """.format("")

    answer = ("N", d.errors['N'])
    answer_explanation = "NameError: name 'x' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_seventy():                                                                     
    """ Increment local unassigned variable within function where variable of 
        the same name is defined in global scope

    """

    problem = """{: >4s}

    x=1
    def fn(arg):
        x += arg
        return x

    fn(2)

    """.format("")

    answer = ("U", d.errors['U'])
    answer_explanation = "UnboundLocalError: local variable 'x' referenced before assignment"
    error_hierarchy = d.hierarchy['U']
    return(problem, answer, answer_explanation, error_hierarchy)


def problem_seventy_one():         
    """ increment global variable from within function call 

    """

    problem = """{: >4s}

    x = 1
    def fn(arg):
        global x
        x+=10
        return x

    fn(10)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 11"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_seventy_two():         
    """ A function where non-default parameter follows default parameter

    """

    problem = """{: >4s}

    def fn(a=10, b=10, c):
        pass

    fn(c=10)    

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: non-default argument follows default argument"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_three():         
    """ A function that adds two arguments with default values to a keyword-only argument

    """

    problem = """{: >4s}

    def fn (a=10, b=10, *,c):
        return a + b + c

    fn(c=10)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is 30"
    error_hierarchy = d.hierarchy['X']         
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_four():         

    """ A function that adds an integer to a tuple

    """

    problem = """{: >4s}

    def fn(a,b, *args):
        return a + b + args

    fn(1,2,3,4,5) 


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'tuple' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_five():         
    """ A function that returns the sum of a list and a tuple  

    """

    problem = """{: >4s}

    def fn(a,b,*args):
        return [a,b] + args

    fn(1,2,3,4,5)

    """.format("")

    answer = ("T", d.errors['T'])                                 
    answer_explanation = "TypeError: can only concatenate list (not 'tuple') to list"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_six():         
    """ A function that sums the elements of a tuple and integers 

    """

    problem = """{: >4s}

     def fn(a,b, *args):
        for item in args:
            a+=item
        return a + b

     fn(1,2,3,4,5)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Returns 15"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_seven():         
    """ A function that adds a tuple to a tuple 

    """

    problem = """{: >4s}

    def fn(a,b, * args):
        return (a,b) + args

    fn(1,2,3,4,5)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Returns (1,2,3,4,5) - a tuple"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)                          


def problem_seventy_eight():         
    """ function where compulsory keyword parameters is executed with positional arguements only 

    """

    problem = """{: >4s}

    def fn(*a, b, c):
        return a,??b, c

    fn(1,2,3)


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: fn() missing 2 required keyword-only arguments: 'b' and 'c'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_seventy_nine():         
    """ function with compulsory keyword parameters is called with keyword arguments after positional argument 

    """

    problem = """{: >4s}

    def fn(*a, b, c):
        return a,??b, c

    fn(1,b=2,c=3)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is ((1,), 2, 3) "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty():         
    """ function call where positional argument follows keyword argument" 

    """

    problem = """{: >4s}

    def fn(*a, b, c):
        return a,??b, c

    fn(b=2,c=3,1)


    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: positional argument follows keyword argument"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_one():         
    """ Dictionary constructor with string as assignment value

    """

    problem = """{: >4s}

    mydict = dict('a' = 'tom')    

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = " SyntaxError: expression cannot contain assignment, perhaps you meant '=='? "
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_two():         
    """ Pass keyword arguments to function that returns a dictionary

    """

    problem = """{: >4s}

    def fn(**kwargs):
        return kwargs

    fn(a=10,b=20)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Returns {'a': 10, 'b': 20}"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_three():         
    """ Pass keyword arguments as string to function that returns a dictionary

    """

    problem = """{: >4s}

    def fn(**kwargs):
        return kwargs

    fn('a'=10, 'b'=20)

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: expression cannot contain assignment, perhaps you meant '=='? "
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_four():         
    """ Add an integer to a string 

    """

    problem = """{: >4s}

    2 + "3"

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_five():         
    """ Multiply a string by an integer 

    """

    problem = """{: >4s}

    2 * "3"

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is \"33\" "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_six():         
    """ Concatenate two strings using the '+' operator

    """

    problem = """{: >4s}

    '2' + '3'


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is 23"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_seven():         
    """ Multiply two strings with '*' operator 

    """

    problem = """{: >4s}

    '2' * '3'

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: can't multiply sequence by non-int of type 'str' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_eighty_eight():         
    """ Subtract two strings using the '-' operator

    """

    problem = """{: >4s}

    "2" - "1"

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for -: 'str' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_eighty_nine():         
    """ Divide a string by an integer using the "/" operator 

    """

    problem = """{: >4s}

    "2"/3

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for /: 'str' and 'int' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety():         
    """ A function with return statements in both try and finally blocks is called and the output is printed

    """

    problem = """{: >4s}

    def fn():
        try:
            return 1
        finally:
            return 2

    print("{{}}{{}}".format(fn()))

    """.format("")

    answer = ("I", d.errors['I'])
    answer_explanation = "IndexError: Replacement index 1 out of range for positional args tuple"
    error_hierarchy = d.hierarchy['I']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_one():         
    """ A function with return statements within both try and finally block where output is assumed to be an integer. 

    """

    problem = """{: >4s}


   def fn():
       try:
           return 1
       finally:
           return 1.23

    print("{{:d}}".format(fn()))

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Unknown format code 'd' for object of type 'float'"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_two():         
    """ Call random.sample with a list as the sole argument 

    """

    problem = """{: >4s}

    import random
    random.sample(range(10))

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = """TypeError: Random.sample() missing 1 required positional argument: 'k' 

    {} 
    """.format(d.extra_material["random_sample_choice"]) 
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_ninety_three():         
    """ Call random.sample() with a keyword argument as second argument 

    """

    problem = """{: >4s}

    import random
    random.sample(range(10), k=2)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No error. Sample output is [7,8] 

    {} 
    """.format(d.extra_material["random_sample_choice"]) 
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_four():         
    """ Call random.choices() with a list as the sole arguement 

    """

    problem = """{: >4s}

    import random
    random.choices(range(10))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No error. Sample output is [8] 

    {} 
    """.format(d.extra_material["random_sample_choice"]) 
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_five():         
    """ delete from dictionary with non-existant key 

    """

    problem = """{: >4s}

    myd=dict(a='tom', b='dick')

    del myd['harry']

    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = "KeyError: 'harry'"
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_six():         
    """ Update a dictionary with a dictionary

    """

    problem = """{: >4s}

    myd=dict(a='tom', b='dick')

    myd.update(dict(c='harry'))

    """.format("")

    answer = ("X", d.errors['X'])      
    answer_explanation = "No error. Output is {'a': 'tom', 'b': 'dick', 'c': 'harry'}"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_seven():         
    """ Add a list to an integer with random.choice() and random.choices()

    """

    problem = """{: >4s}

    l = range(10)

    random.choice(l) + random.choices(l)    

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: can only concatenate list (not 'int') to list"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_eight():         
    """Concatenate two lists with random.choices() and random.sample() 

    """

    problem = """{: >4s}

    import random
    l=[1,2,3] 
    random.sample(l,1) + random.choices(l)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Sample output: [9, 0]"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_ninety_nine():         
    """Add a tuple to a tuple  

    """

    problem = """{: >4s}

     (1,) + (2,3)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output: (1, 2, 3)"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_one_hundred():         
    """Add an integer to a tuple 

    """

    problem = """{: >4s}

    (1) + (2,3)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'int' and 'tuple'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_one():         
    """Call the .index() method on a string where the argument is not present 

    """

    problem = """{: >4s}

    "harry".index('h',1)

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = """ValueError: substring not found

    'harry'.rindex('h', 1) also gives ValueError
    """
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_two():         
    """Call the .find() method on a string where the argument is not present 

    """

    problem = """{: >4s}

    "harry".find('h',1)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No Error. Returns -1

    'harry'.rfind('h', 1) also returns -1
    """
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_three():         
    """Call the .find() method on a string where the argument is not present 

    """

    problem = """{: >4s}

    "harry".rindex('y',-1)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No Error. Returns 4 """
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_four():         
    """ Call math.round() on float 

    """

    problem = """{: >4s}

    import math
    math.round(22.2)

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: module 'math' has no attribute 'round'"
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_five():         
    """ Call builtin function 'round() on float 

    """

    problem = """{: >4s}

    round(22.5)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is 22"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_six():         
    """ Unpack a list with a single value and two right-hand-side variables 

    """

    problem = """{: >4s}

    a = 10
    b = 10

    a,b = [10]

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: not enough values to unpack (expected 2, got 1)"
    error_hierarchy = d.hierarchy['V']                                     
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_seven():         
    """ Use safe_substitute with string Template and identifier error

    """

    problem = """{: >4s}

    from string import Template

    template = Template("Hello $name")
    template.safe_substitute(namae="dick")


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 'Hello $name' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_eight():         
    """ Use substitute with string Template and identifier error

    """

    problem = """{: >4s}

    from string import Template

    template = Template("Hello $name")
    template.substitute(namae="dick")


    """.format("")

    answer = ("K", d.errors['K'])
    answer_explanation = "KeyError: 'name' "
    error_hierarchy = d.hierarchy['K']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_nine():         
    """Call 'strip()' string method with more than one argument

    """

    problem = """{: >4s}

    TomDickHarry'.strip(*['T','D'])

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: strip expected at most 1 argument, got 2"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_ten():         
    """Add list to set 
    """

    problem = """{: >4s}

    myset=set()
    myset.add(['tom', 'dick', 'harry'])

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unhashable type: 'list' "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_eleven():         
    """ Add a tuple to a set

    """

    problem = """{: >4s}

    myset = set()
    myset.add(('dick', 'harry'))

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is {('dick', 'harry')}"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twelve():         
    """Call '.pop()' on a list 

    """

    problem = """{: >4s}

   lst=[1,2,3]
   lst.pop()

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """
    No error. Removes '3' and returns it 
    lst.pop(0) removes '1' and returns it
    """
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirteen():         
    """Assign to a list where index is out of range 

    """

    problem = """{: >4s}

    lst=[1,2,3]
    lst[3]=400


    """.format("")

    answer = ("I", d.errors['I'])
    answer_explanation = "IndexError: list assignment index out of range"
    error_hierarchy = d.hierarchy['I']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_fourteen():         
    """Assign an integer to list where slice start index is out of range  

    """

    problem = """{: >4s}

    lst=[1,2,3]
    lst[3:]=400

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: can only assign an iterable "
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifteen():         
    """Assign an iterable to list where slice start index is out of range  

    """

    problem = """{: >4s}

    lst=[1,2,3]
    lst[30:]=[400]

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is [1, 2, 3, 400]"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_sixteen():         
    """ Reassign item in tuple 

    """

    problem = """{: >4s}

    t=([1,2,3],)

    t[0]=[100,200,300]


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'tuple' object does not support item assignment"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_seventeen():         
    """ Reassign an element of a list which is an element of a tuple 

    """

    problem = """{: >4s}

    t=([1,2,3],)

    t[0][0]=[1,2,3]


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is ([[1, 2, 3], 2, 3],) "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_eighteen():         
    """ Pop an item from a set  

    """

    problem = """{: >4s}

    s = set(range(10))
    s.pop()

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """
    No error
    set.pop(): remove and return an arbitrary set element
    """
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_nineteen():         
    """Pop a specific item from a set """

    problem = """{: >4s}

    s = set(range(10))

    s.pop(2)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: set.pop() takes no arguments (1 given)"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty():         
    """ Add two sets 

    """

    problem = """{: >4s}

    {{1,2,3}} + {{4,5,6}}

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unsupported operand type(s) for +: 'set' and 'set'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_one():         
    """ Subtract two sets 

    """

    problem = """{: >4s}

    {{1,2,3}} - {{3,4,5}}

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is {1,2}"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_two():         
    """Make a directory where the directory already exists 

    """

    problem = """{: >4s}

    import os
    os.makedirs('a/b/c/d')
    os.mkdir('a/b/c/d')


    """.format("")

    answer = ("E", d.errors['E'])
    answer_explanation = "FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'a/b/c/d'"
    error_hierarchy = d.hierarchy['E']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_three():         
    """A named variable shadows into a function

    """

    problem = """{: >4s}

    num = 1

    def func():
        num = num + 3
        print(num)

    func()
    print(num)

    """.format("")

    answer = ("U", d.errors['U'])
    answer_explanation = "UnboundLocalError: local variable 'num' referenced before assignment"
    error_hierarchy = d.hierarchy['U']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_four():         
    """Multiply a string by a string using the '*" operator 

    """

    problem = """{: >4s}

    num = '7' * '7'

    print(num)


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: can't multiply sequence by non-int of type 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_twenty_five():         
    """Format a float with builtin 'format' function with invalid format specifier 

    """

    problem = """{: >4s}

    print('1200.2 + 1200.2 equals', format(2400.4, "%.4f"))   

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: Invalid format specifier"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_twenty_six():         
    """Format a float with builtin 'format' function with valid format specifier 

    """

    problem = """{: >4s}

    print('1200.2 + 1200.2 equals', format(2400.4, ".4f"))   

    """.format("")

    answer = ("X", d.errors['V'])
    answer_explanation = "No error.  Output is '1200.2 + 1200.2 equals 2400.4000' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_seven():         
    """The result of modulo() where the second argument is '0' 

    """

    problem = """{: >4s}

    1%0


    """.format("")

    answer = ("Z", d.errors['Z'])
    answer_explanation = "ZeroDivisionError: integer division or modulo by zero"
    error_hierarchy = d.hierarchy['Z']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_eight():         
    """Call 'int()' on '22.2'

    """

    problem = """{: >4s}

    int('22.2')

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: invalid literal for int() with base 10: '22.2'"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_twenty_nine():         
    """Call int() on the output of str(float) 

    """

    problem = """{: >4s}

    int(str(22.))    

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: invalid literal for int() with base 10: '22.0'"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty():         
    """Call int() on the output of float(str) 

    """

    problem = """{: >4s}

    int(float('22.2'))    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_one():         
    """ Decode bytes in the ascii range  (0-127)

    """

    problem = """{: >4s}

    bytes([1,127]).decode()    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is '\\x01\\x7f' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_thirty_two():         
    """ Decode bytes outside the ascii range  (0-127)

    """

    problem = """{: >4s}

    bytes([127,128]).decode()    

    """.format("")

    answer = ("Y", d.errors['Y'])
    answer_explanation = "UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 1: invalid start byte"
    error_hierarchy = d.hierarchy['Y']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_three():         
    """Call bytes on an array with element outside the range  0 <= x < 256 

    """

    problem = """{: >4s}

    bytes([256])

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: bytes must be in range(0, 256)"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_four():         
    """Call bytes on an array with element within the range  0 <= x < 256 

    """

    problem = """{: >4s}

    bytes([255])

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. Output is b'xff'"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_thirty_five():         
    """Call '.pop()' method on bytearray object 

    """

    problem = """{: >4s}

    bytearray([48,65,97]).pop(0)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 48"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_six():         
    """Call '.pop()' method on byte object

    """

    problem = """{: >4s}

    bytes([48,65,97]).pop(0)

    """.format("")

    answer = ("A", d.errors['A'])
    answer_explanation = "AttributeError: 'bytes' object has no attribute 'pop' "
    error_hierarchy = d.hierarchy['A']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_seven():         
    """Call '.replace()' method on bytearray object 

    """

    problem = """{: >4s}

    bytearray([48,65,97]).replace(b'0', b'1')    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is bytearray(b'1Aa')"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_thirty_eight():         
    """Call '.replace()' method on bytes object 

    """

    problem = """{: >4s}

    bytes([48,65,97]).replace(b'0', b'1')

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is b'1Aa' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_thirty_nine():         
    """Starred assignment where target is neither a list or a tuple

    """

    problem = """{: >4s}

    *names = 1,2,3    

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: starred assignment target must be in a list or tuple"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_forty():         
    """Starred assignment where target is explicitly a tuple

    """

    problem = """{: >4s}

    *names, = 1,2,3    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. names identifer is assigned to [1, 2, 3] "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_one():         
    """Call next() on an iterator when there are no further iterator items left 

    """

    problem = """{: >4s}

    name='tom'
    it=iter(name)

    for item in range(len(name)):
        next(it)

    next(it)

    """.format("")

    answer = ("P", d.errors['P'])
    answer_explanation = "StopIteration"
    error_hierarchy = d.hierarchy['P']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_two():         
    """Take part of a set using square-bracket notation  

    """

    problem = """{: >4s}

    {{1,2,3}}[1]

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'set' object is not subscriptable"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_three():         
    """Use the length of a list as an index to abstract an element using square-bracket notation 

    """

    problem = """{: >4s}

    lst=[1,2,3]
    lst[len(lst)]    

    """.format("")

    answer = ("I", d.errors['I'])
    answer_explanation = "IndexError: list index out of range"
    error_hierarchy = d.hierarchy['I']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_forty_four():         
    """ DOCSTRING HERE 

    """

    problem = """{: >4s}

    lst=[1,2,3]

    x=slice(len(lst))

    lst[x]


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is [1,2,3]"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_five():         
    """Call int() on an integer with the base specified 

    """

    problem = """{: >4s}

    int(10, base=2)


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: int() can't convert non-string with explicit base"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_six():         
    """(Call int on a string where the base is specified

    """

    problem = """{: >4s}

    int('10', base=2)    

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No Error. The output is 2"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_seven():         
    """A decimal integer with leading zero

    """

    problem = """{: >4s}

    012

    """.format("")

    answer = ("S", d.errors['S'])     
    answer_explanation = """SyntaxError: leading zeros in decimal integer literals are not permitted;
    use an 0o prefix for octal integers"""
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_forty_eight():         
    """Call int() on a decimal integer with leading zero

    """

    problem = """{: >4s}

    int(012)

    """.format("")

    answer = ("S", d.errors['S'])     
    answer_explanation = """SyntaxError: leading zeros in decimal integer literals are not permitted;
    use an 0o prefix for octal integers"""
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_forty_nine():         
    """Call int() on a string consisting of a leading zero and digits" 

    """

    problem = """{: >4s}

    int('012')

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty():         
    """Call hex() on math.pi

    """

    problem = """{: >4s}

    import math
    hex(math.pi)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: 'float' object cannot be interpreted as an integer"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_one():         
    """ DOCSTRING HERE 

    """

    problem = """{: >4s}

    float.hex(math.pi)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error: output is '0x1.921fb54442d18p+1' "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_two():         
    """Compile a complex expression with 'eval' as third argument

    """

    problem = """{: >4s}
        str="x=\\ny=2\\nprint('x + y =', x+y)"
        x=compile(str, 'test', 'eval')

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = "SyntaxError: invalid syntax"
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_three():         
    """Compile a complex expression with 'exec' as third argument

    """

    problem = """{: >4s}
        str="x=\\ny=2\\nprint('x + y =', x+y)"
        x=compile(str, 'test', 'exec')

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. type(x) gives <class 'code'>"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_four():         
    """Call eval on externally defined global variables 

    """

    problem = """{: >4s}
    x=100
    y=10

    eval('x+y')


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 110"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_five():         
    """Call eval() with one external global variable and one internal global variable

    """

    problem = """{: >4s}

    x=100
    y=10
    eval('x+y', {{'x':'10'}})

    """.format("")

    answer = ("N", d.errors['N'])
    answer_explanation = "NameError: name 'y' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_six():         
    """Call eval with builtin function 'sum()' 

    """

    problem = """{: >4s}

    eval('sum([1,2,3])')

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is 6"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_fifty_seven():         
    """ Call eval with builtin function where '__builtins__' are excluded as global variables

    """

    problem = """{: >4s}

   eval('sum([1,2,3])',{{'__builtins__':{{}}}},{{}})

    """.format("")

    answer = ("N", d.errors['N'])                                                
    answer_explanation = "NameError: name 'sum' is not defined"
    error_hierarchy = d.hierarchy['N']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_eight():         
    """Call a function without specifying required keyword arguments 

    """

    problem = """{: >4s}

    def mixm(*c, a, b):
        return c,a,b

    mixm(1,2,3,4)

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: mixm() missing 2 required keyword-only arguments: 'a' and 'b'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_fifty_nine():         
    """Call a function explicitly specifying required keyword arguments 

    """

    problem = """{: >4s}

    def mixm(*c, a, b):
        return c,a,b

    mixm(1,2,a=10,b=20)

    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is ((1, 2), 10, 20) "
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty():         
    """Open an existing file with mode 'x' 

    """

    problem = """{: >4s}

    f = open('xyz.txt', 'w')
    f.close()
    f = open('xyz.txt', 'x')

    """.format("")

    answer = ("E", d.errors['E'])
    answer_explanation = "FileExistsError: [Errno 17] File exists: 'xyz.txt' "
    error_hierarchy = d.hierarchy['E']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_one():         
    """Add a set to a set 

    """

    problem = """{: >4s}
    s = set((1,2))
    s2 = set((3,4))    

    s.add(s2)


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unhashable type: 'set'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_two():         
    """Update a set with a set 

    """

    problem = """{: >4s}
    s = set((1,2))
    s2 = set((3,4))    

    s.update(s2)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Modifies in place. s becomes {1, 2, 3, 4}"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_three():         
    """Use 'for' loop to iterate over elements of a set

    """

    problem = """{: >4s}
    mys=set('tom', 'dick', 'harry')

    for i in mys:
        print(i) 
    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = """No Error. Output is:
    dick
    tom
    harry"""
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_sixty_four():         
    """ DOCSTRING HERE 

    """

    problem = """{: >4s}
    None
    s1 = 'tom'
    s2 = 'dick'
    print(s1 s2)

    """.format("")

    answer = ("S", d.errors['S'])
    answer_explanation = """SyntaxError: invalid syntax. Perhaps you forgot a comma?
    !! Contrast with string literals """
    error_hierarchy = d.hierarchy['S']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_five():         
    """Call hash on a tuple where the tuple fields are lists 

    """

    problem = """{: >4s}

    tup=([1,2,3],[20,40,50])
    hash(tup)


    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: unhashable type: 'list'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)


def problem_hundred_sixty_six():         
    """Call 'sort' method on a list with both string and integer elements 

    """

    problem = """{: >4s}

    mylist=['0', 'A', 'a', 1]
    mylist.sort()

    """.format("")

    answer = ("T", d.errors['T'])
    answer_explanation = "TypeError: '<' not supported between instances of 'int' and 'str'"
    error_hierarchy = d.hierarchy['T']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_seven():         
    """ DOCSTRING HERE 

    """

    problem = """{: >4s}
    
    mylist =  ['tom', 'dick', 'harry']
    mylist.remove('Tom')

    """.format("")

    answer = ("V", d.errors['V'])
    answer_explanation = "ValueError: list.remove(x): x not in list"
    error_hierarchy = d.hierarchy['V']
    return(problem, answer, answer_explanation,error_hierarchy)

def problem_hundred_sixty_eight():         
    """Call remove on lst from within while loop, where the argument for remove
       it not an element of lst

    """

    problem = """{: >4s}

    while 'Tom' in mylist:
        mylist.remove('Tom')
    else:
        print(mylist)


    """.format("")

    answer = ("X", d.errors['X'])
    answer_explanation = "No error. Output is: ['tom', 'dick', 'harry']"
    error_hierarchy = d.hierarchy['X']
    return(problem, answer, answer_explanation,error_hierarchy)
