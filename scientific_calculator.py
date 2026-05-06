from calculator_equations import InputEquation
from calculator_equations import ProperOperands
from calculator_equations import EvaluateEquation

while True:
    
    user_input = input("Enter Equation Here >>> ")
    
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
                print(result, rounded_result)
        else:
            try:
                if result % 1 == 0:
                    print(result)
                else:
                    print(result)
                    print(rounded_result)
            except Exception as e:
                print(f"Invalid Input {e}")