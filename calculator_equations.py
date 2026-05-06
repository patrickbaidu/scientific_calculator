import re
import math
from math import * 

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
            self.equation = self.equation.replace("e", str(math.e))
            self.equation = self.equation.replace("pi", str(math.pi))
            self.equation = re.sub(r'(\d)\(', r'\1*(', self.equation)        
            self.equation = re.sub(r'\)(\d)', r')*\1', self.equation)
            self.equation = re.sub(r'(\d)\(', r'\1*(', self.equation)
            self.equation = re.sub(r'(<![ngs])([a-zA-Z])\(', r'\1*(', self.equation)
            return self.equation

class EvaluateEquation:
    
    def __init__(self, equation):
        self.equation = equation
    
    def evaluate_equation(self):
        
        if "Invalid" in self.equation:
            return f"{Color.red + Color.bold}Error: Cannot Handle Contiguous Multiplication{Color.end}", None
        else:
            try:
                if re.search(r'[\+\-\/]{2,}', self.equation):
                    return f"{Color.red + Color.bold}Error: Contiguous Operators{Color.end}", None
                actual_result = eval(self.equation)
                rounded_result = round(actual_result, 3)
                return actual_result, rounded_result
            except ZeroDivisionError:
                return f"{Color.red + Color.bold}Error: Divided By Zero.{Color.end}", None
            except Exception:
                return f"{Color.red + Color.bold}Error: Invalid Equation{Color.end}", None

class Color:
    
    purple = '\033[95m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    green = '\033[92m'