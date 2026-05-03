import re

class InputEquation:
    
    def __init__(self, user_input):
        self.user_input = user_input
    
    def clean_spaces(self):
        clean_user_input = self.user_input.replace(" ", "")
        return clean_user_input
    
    def equation_list(self, user_input):
        equation_list = []
        for equation in user_input:
            equation_list.append(equation)
        equation = "".join(equation_list)
        return equation

class ProperOperands:
    
    def __init__(self, equation):
        self.equation = equation
    
    def proper_operator(self):
        self.equation = self.equation.replace("x", "*").replace("X", "*")
        self.equation = self.equation.replace(")(", ")*(")
        self.equation = self.equation.replace("^", "**")
        self.equation = re.sub(r'(\d)\(', r'\1*(', self.equation)        
        self.equation = re.sub(r'\)(\d)', r')*\1', self.equation)
        self.equation = re.sub(r'(\d)\(', r'\1*(', self.equation)
        self.equation = re.sub(r'([a-zA-Z])\(', r'\1*(', self.equation)
        
        return self.equation

class EvaluateEquation:
    
    def __init__(self, equation):
        self.equation = equation
    
    def evaluate_equation(self):
        try:
            result = eval(self.equation)
            return result
        except ZeroDivisionError:
            return "Error: Divided By Zero."
        except Exception:
            return "Invalid Equation"
    
    