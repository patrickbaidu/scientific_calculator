from calculator_equations import InputEquation
from calculator_equations import ProperOperands
from calculator_equations import EvaluateEquation
from calculator_equations import Color

while True:
    print(f"{Color.cyan + Color.bold + Color.underline}{"-"*12}A SCIENTIFIC CALCULATOR{"-"*12}{Color.end}")
    print(f"{Color.bold}OPERATIONS AVAILABLE: [+, -, x, /, ^, sqrt, ln, log, e, pi, sin, cos, tan, arcsin, arccos, arctan]{Color.end}")
    print(f"""
        {Color.green}Please Use These Symbols Equivalent to the Operation Above: {Color.end}
        1. + : Addition                     10. pi : Pi Constant
        2. - : Subtraction                  11. sin : Sine Function
        3. x or X or * : Multiplication     12. cos : Cosine Function
        4. / : Division                     13. tan : Tangent Function
        5. ^ : Exponent                     14. asin : Inverse Sin Function
        6. sqrt : Square Root               15. acos : Inverse Cosine Function
        7. ln : Natural Logarithm           16. atan : Inverse Tangent Function
        8. log : Logarithm with Base
        9. e : Euler's Constant
        Note: (x) is the number you want to input.
        """)
    user_input = input(f"{Color.yellow + Color.bold}Enter Equation Here >>> {Color.end}")
    
    if user_input == "Break":
        print("Thank You For Using the Program!")
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
                print(result)
        else:
            try:
                if result % 1 == 0:
                    result = str(result)
                    print(f"{Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}")
                else:
                    result = str(result)
                    rounded_result = str(rounded_result)
                    print(f"{Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}")
                    print(f"{Color.blue + Color.bold}ROUNDED RESULT: {Color.end}", f"{Color.purple + Color.bold}{rounded_result}{Color.end}")
            except Exception as e:
                print(f"{Color.red + Color.bold}Invalid Input {e}{Color.end}")