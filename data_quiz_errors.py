# errors = {"A": 'NameError', "B": 'ValueError', "C": "TypeError", "D": "IndexError",
        # "E": "KeyError", "F":"SyntaxError", "G": "ZeroDivisionError", "H": "AttributeError"}



errors = {"N": 'NameError', "V": 'ValueError', "T": "TypeError", "I": "IndexError",
        "K": "KeyError", "S":"SyntaxError", "Z": "ZeroDivisionError", "A": "AttributeError",
        "F": "FileNotFoundError", "X": "No Error"}

hierarchy = {"N": "BaseException -> Exception -> NameError",
        "V": "BaseException -> Exception -> ValueError",
        "T": "BaseException -> Exception -> TypeError",
        "I": "BaseException -> Exception -> LookupError -> IndexError",
        "K": "BaseException -> Exception -> LookupError -> KeyError", 
        "S": "BaseException -> Exception -> SyntaxError",
        "Z": "BaseException -> Exception -> ArithmeticError -> ZeroDivisionError",
        "A": "BaseException -> Exception -> AttributeError",
        "F": "BaseException -> Exception -> OSError -> FileNotFoundError",
        "X": "No Error"}


