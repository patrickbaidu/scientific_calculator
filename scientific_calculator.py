#Pseudocoding My Flow for My Code

#from the calculator functions I wanna get my methods.
# I should have an equation for addition, subtraction, multiplication, and division.
# I will need a user input function to get the number inputs (E.g. 1+2-3+4) where the characters for equations are acceptable.
# I will have a saved result for my variable whenever an equation is done.
# I will have a second user input to know if the user still wants to continue the program or not.
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