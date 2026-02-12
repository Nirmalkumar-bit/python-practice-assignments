# Task: Implement dispatch(command, *args).
# Supported commands and rules:
# - "add": requires exactly 2 numeric args -> return sum
# - "pow": requires exactly 2 numeric args, exponent must be int >= 0 -> return base ** exp
# - "echo": requires exactly 1 str arg -> return it
# Invalid handling:
# - If command not a str: TypeError("command must be a str")
# - If command unknown: ValueError("unknown command")
# - If wrong number of args: TypeError("wrong number of arguments")
# - If argument types invalid for a command: TypeError("invalid argument type")
# - If pow exponent invalid: ValueError("exponent must be a non-negative int")
# Expected outcome:
# - dispatch("add", 2, 3) returns 5
# - dispatch("pow", 2, -1) raises ValueError("exponent must be a non-negative int")
# - dispatch("echo", 1) raises TypeError("invalid argument type")


def dispatch(command, *args):
    if not isinstance(command, str):
        raise TypeError("command must be a str")
    
    # ADD
    if command == "add":
        if len(args) != 2:
            raise TypeError("wrong number of arguments")
        
        a, b = args
        if type(a) not in (int, float) or type(b) not in (int, float):
            raise TypeError("invalid argument type")
        
        return a + b
    
    # POW
    elif command == "pow":
        if len(args) != 2:
            raise TypeError("wrong number of arguments")
        
        base, exp = args
        
        if type(base) not in (int, float) or type(exp) is not int:
            raise TypeError("invalid argument type")
        
        if exp < 0:
            raise ValueError("exponent must be a non-negative int")
        
        return base ** exp
    
    # ECHO
    elif command == "echo":
        if len(args) != 1:
            raise TypeError("wrong number of arguments")
        
        value = args[0]
        if not isinstance(value, str):
            raise TypeError("invalid argument type")
        
        return value
    
    # UNKNOWN COMMAND
    else:
        raise ValueError("unknown command")
    # TODO
    pass


if __name__ == "__main__":
    print(dispatch("add", 2, 3))