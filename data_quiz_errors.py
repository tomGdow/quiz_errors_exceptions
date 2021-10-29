import problems_quiz_errors as p

errors = {"N": 'NameError', "V": 'ValueError', "T": "TypeError", "I": "IndexError",
        "K": "KeyError", "S":"SyntaxError", "Z": "ZeroDivisionError", "A": "AttributeError",
        "F": "FileNotFoundError", "X": "No Error", "D": "IndentationError", "R": "AssertionError",
        "U": "UnboundLocalError", "E": "FileExistsError"}

hierarchy = {
        "N": "BaseException -> Exception -> NameError",
        "V": "BaseException -> Exception -> ValueError",
        "T": "BaseException -> Exception -> TypeError",
        "I": "BaseException -> Exception -> LookupError -> IndexError",
        "K": "BaseException -> Exception -> LookupError -> KeyError", 
        "S": "BaseException -> Exception -> SyntaxError",
        "Z": "BaseException -> Exception -> ArithmeticError -> ZeroDivisionError",
        "A": "BaseException -> Exception -> AttributeError",
        "F": "BaseException -> Exception -> OSError -> FileNotFoundError",
        "E": "BaseException -> Exception -> OSError -> FileExistsError",
        "D": "BaseException -> Exception -> SyntaxError -> IndentationError",
        "R": "BaseException -> Exception -> AssertionError",             
        "U": "BaseException -> Exception -> NameError -> UnboundLocalError",
        "X": "No Error"}

extra_material = {

        "random_sample_choice" : """NOTE

        random.sample(range(10))       //    TypeError
        random.choice(range(10))       //    2    (an integer)
        random.choices(range(10)       //    [2]  (a list)

        random.sample(range(10), 1)    //    [2]  (a list)
        random.choice(range(10), 1)    //    TypeError
        random.choices(range(10), 1)   //    TypeError

        random.sample(range(10), k=1)  //    [4]
        random.choices(range(10, k=1)  //    [1]  (a list)
        """

        }
