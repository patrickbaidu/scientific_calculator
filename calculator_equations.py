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
            return
        elif "XX" in self.equation:
            return
        elif "**" in self.equation:
            return
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
        try:
            if re.search(r'[\+\-\/]{2,}', self.equation):
                return "Error: Multiple Operators"
            result = eval(self.equation)
            result = round(result, 2)
            return result
        except ZeroDivisionError:
            return "Error: Divided By Zero."
        except Exception:
            return "Invalid Equation"
    
    