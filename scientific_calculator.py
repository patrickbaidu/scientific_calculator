from calculator_equations import InputEquation
from calculator_equations import ProperOperands
from calculator_equations import EvaluateEquation
from calculator_equations import Color
from calculator_equations import MenuOption

print(f"\n{Color.cyan + Color.bold + Color.underline}{"-"*20}A SCIENTIFIC CALCULATOR{"-"*20}{Color.end}")
print(f"{Color.bold}OPERATIONS AVAILABLE: [+, -, x, /, ^, sqrt, ln, log, e, pi, sin, cos, tan, arcsin, arccos, arctan]{Color.end}")
MenuOption.show_options()

while True:
    
    print(f"{Color.cyan}━{Color.end}"*60)
    print(f"Enter {Color.red + Color.bold}Quit{Color.end} or {Color.red + Color.bold}Exit{Color.end} to Halt the Program.")
    print(f"Enter {Color.green + Color.bold}Menu{Color.end} to Show Options for Operations.")
    user_input = input(f"{Color.yellow + Color.bold}Enter Equation Here >>> {Color.end}")
    print(f"{Color.cyan}━{Color.end}"*60)
    
    if user_input.strip().title() == "Quit" or user_input.strip().title() == "Exit":
        print(f"\n{Color.green + Color.bold}THANK YOU FOR USING THIS PROGRAM ^__^!{Color.end}\n")
        break
    elif user_input.strip().title() == "Menu":
        MenuOption.show_options()
    else:
        user_input = InputEquation(user_input)
        clean_spaces = user_input.clean_spaces()
        equation = user_input.equation_list(clean_spaces)
        proper_equation = ProperOperands(equation)
        proper_equation = proper_equation.proper_operator()
        equation = EvaluateEquation(proper_equation)
        result, rounded_result = equation.evaluate_equation()

        if isinstance(result, str):
                print(f"\n{result}", "\n")
        else:
            try:
                if result % 1 == 0:
                    result = str(result)
                    print(f"\n😎 {Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}\n")
                else:
                    result = str(result)
                    rounded_result = str(rounded_result)
                    print(f"\n😎 {Color.green + Color.bold}RESULT: {Color.end}", f"{Color.purple + Color.bold}{result}{Color.end}")
                    print(f"👍 {Color.blue + Color.bold}ROUNDED RESULT: {Color.end}", f"{Color.purple + Color.bold}{rounded_result}{Color.end}\n")
            except Exception as e:
                print(f"\n⚠️ {Color.red + Color.bold}Invalid Input {e}{Color.end}\n")