from calculator_equations import InputEquation
from calculator_equations import ProperOperands
from calculator_equations import EvaluateEquation
from calculator_equations import Color

print(f"\n{Color.cyan + Color.bold + Color.underline}{"-"*20}A SCIENTIFIC CALCULATOR{"-"*20}{Color.end}")
print(f"{Color.bold}OPERATIONS AVAILABLE: [+, -, x, /, ^, sqrt, ln, log, e, pi, sin, cos, tan, arcsin, arccos, arctan]{Color.end}")
print(f"""
    {Color.green}Please Use These Symbols Equivalent to the Operations Above: {Color.end}
    1. {Color.bold}+{Color.end}             : Addition              9. {Color.bold}pi{Color.end}        : Pi Constant
    2. {Color.bold}-{Color.end}             : Subtraction           10. {Color.bold}sin(x){Color.end}   : Sine Function
    3. {Color.bold}x or X or *{Color.end}   : Multiplication        11. {Color.bold}cos(x){Color.end}   : Cosine Function
    4. {Color.bold}/{Color.end}             : Division              12. {Color.bold}tan(x){Color.end}   : Tangent Function
    5. {Color.bold}^{Color.end}             : Exponent              13. {Color.bold}asin(x){Color.end}  : Inverse Sin Function
    6. {Color.bold}sqrt(x){Color.end}       : Square Root           14. {Color.bold}acos(x){Color.end}  : Inverse Cosine Function
    7. {Color.bold}log(x, base){Color.end}  : Logarithm with Base   15. {Color.bold}atan(x){Color.end}  : Inverse Tangent Function
    8. {Color.bold}e{Color.end}             : Euler's Constant
    
    
    Note: (x) is the number you want to input.
    """)

while True:
    
    print(f"Enter {Color.red + Color.bold}Quit{Color.end} or {Color.red + Color.bold}Exit{Color.end} to Halt the Program.")
    user_input = input(f"{Color.yellow + Color.bold}Enter Equation Here >>> {Color.end}")
    
    if user_input.strip().title() == "Quit" or user_input.strip().title() == "Exit":
        print(f"{Color.green + Color.bold}Thank You For Using the Program!{Color.end}")
        break
    else:
        user_input = InputEquation(user_input)
        clean_spaces = user_input.clean_spaces()
        equation = user_input.equation_list(clean_spaces)
        proper_equation = ProperOperands(equation)
        proper_equation = proper_equation.proper_operator()
        equation = EvaluateEquation(proper_equation)
        result, rounded_result = equation.evaluate_equation()

        if isinstance(result, str):
                print("\n", result, "\n")
        else:
            try:
                if result % 1 == 0:
                    result = str(result)
                    print(f"{Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}\n")
                else:
                    result = str(result)
                    rounded_result = str(rounded_result)
                    print(f"{Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}")
                    print(f"{Color.blue + Color.bold}ROUNDED RESULT: {Color.end}", f"{Color.purple + Color.bold}{rounded_result}{Color.end}\n")
            except Exception as e:
                print(f"\n{Color.red + Color.bold}Invalid Input {e}{Color.end}\n")