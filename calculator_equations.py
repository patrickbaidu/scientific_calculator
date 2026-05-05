import re

class InputEquation:
    
    def __init__(self, user_input):
        self.equation = user_input
    
    def clean_spaces(self):
        clean_user_input = self.equation.replace(" ", "")
        return clean_user_input
    
    def equation_list(self, user_input):
        equation_list = []
        for equation in user_input:
            equation_list.append(equation)
        equation = "".join(equation_list)
        return equation

class ProperOperands(InputEquation):
    
    def __init__(self, user_input):
        super().__init__(user_input)
    
    def proper_operator(self):
        if "xx" in self.equation:
            return "Invalid"
        elif "XX" in self.equation:
            return "Invalid"
        elif "**" in self.equation:
            return "Invalid"
        else:
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
        
        if "Invalid" in self.equation:
            return "Error:", "Cannot Handle Contiguous Multiplication"
        
        try:
            if re.search(r'[\+\-\/]{2,}', self.equation):
                return "Error: Contiguous Operators", None
            actual_result = eval(self.equation)
            rounded_result = round(actual_result, 3)
            return actual_result, rounded_result
        except ZeroDivisionError:
            return "Error: Divided By Zero.", None
        except Exception:
            return "Error: Invalid Equation", None