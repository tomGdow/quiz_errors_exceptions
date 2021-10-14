import problems_quiz_errors as p

errors = {"N": 'NameError', "V": 'ValueError', "T": "TypeError", "I": "IndexError",
        "K": "KeyError", "S":"SyntaxError", "Z": "ZeroDivisionError", "A": "AttributeError",
        "F": "FileNotFoundError", "X": "No Error", "D": "IndentationError", "R": "AssertionError",
        "U": "UnboundLocalError"}

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
        "D": "BaseException -> Exception -> SyntaxError -> IndentationError",
        "R": "BaseException -> Exception -> AssertionError",             
        "U": "BaseException -> Exception -> NameError -> UnboundLocalError",
        "X": "No Error"}


