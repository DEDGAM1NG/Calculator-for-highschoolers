from pyparsing import Word, alphas, Literal, nums, Or

# Define grammar for parsing the equation
identifier = Word(alphas)
variable = Word(alphas, max=1)
integer = Word(nums).setParseAction(lambda t: int(t[0]))
multiple = Word(nums).setParseAction(lambda t2: int(t2[0]))

# Define operators and expressions
plus = Literal("+")
minus = Literal("-")
times = Literal("*")
divide = Literal("/")
terms = Or([plus, minus, times, divide])
equals = Literal("=")

# Define the grammar for the whole expression
expression = (multiple + variable + terms + integer) | (variable + terms + integer)

# Parse the equation
equation_str = input("Enter an equation: ")

try:
    result = expression.searchString(equation_str)
    
    if len(result) == 1:
        result = result[0]
    else:
        raise Exception("Invalid equation format")

    # Example input string
    char_to_find = 'x'  # You can change this to 'y' if needed

    # Split the equation into left and right parts
    parts = equation_str.split('=')

    # Initialize variables to store the values
    multiple_of_variable = 1  # Default value if no multiple is specified
    lhs = 0
    operator = None
    rhs = 0
    result_value = None

    if (result[0] == char_to_find) or (result[2] == char_to_find):
        result_value = char_to_find
        
    multiple_of_variable = 1 if result[0] == char_to_find else int(result[0])
    if (result[0] == char_to_find):
        lhs = int(result[2])
        operator = result[1]
    else:
        lhs = int(result[3])
        operator = result[2]
    rhs = int(parts[1])
    # Perform the calculation based on the operator
    if operator == "+":
        x_value = (rhs - lhs) / multiple_of_variable
    elif operator == "-":
        x_value = (lhs - rhs) / multiple_of_variable
    elif operator == "*":
        x_value = rhs / (lhs * multiple_of_variable)
    elif operator == "/":
        x_value = lhs / (rhs * multiple_of_variable)

    print("What x is being operated with:", multiple_of_variable)
    print(f"x = {x_value}")
    print("Left-hand side:", lhs)
    print("Operator:", operator)
    print("Right-hand side:", rhs)
    print("Result:", result_value)

except Exception as e:
    print("Error:", e)
