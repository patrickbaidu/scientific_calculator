from calculator_equations import InputEquation
from calculator_equations import ProperOperands
from calculator_equations import EvaluateEquation
from calculator_equations import Color

while True:
    
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