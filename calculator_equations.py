import re
import math
from math import * 

_sin, _cos, _tan = sin, cos, tan
_asin, _acos, _atan = asin, acos, atan

sin = lambda x: _sin(radians(x))
cos = lambda x: _cos(radians(x))
tan = lambda x: _tan(radians(x))
asin = lambda x: degrees(_asin(x))
acos = lambda x: degrees(_acos(x))
atan = lambda x: degrees(_atan(x))

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
            return f"⚠️ {Color.red + Color.bold}Error: Cannot Handle Contiguous Multiplication{Color.end}", None
        else:
            try:
                if re.search(r'[\+\-\/]{2,}', self.equation):
                    return f"⚠️ {Color.red + Color.bold}Error: Contiguous Operators{Color.end}", None
                actual_result = eval(self.equation)
                rounded_result = round(actual_result, 3)
                return actual_result, rounded_result
            except ZeroDivisionError:
                return f"⚠️ {Color.red + Color.bold}Error: Divided By Zero.{Color.end}", None
            except Exception:
                return f"⚠️ {Color.red + Color.bold}Error: Invalid Equation{Color.end}", None

class MenuOption:
    
    def show_options():
        menu_option = print(f"""
{Color.green}Please Use These Symbols Equivalent to the Operations Above: {Color.end}
1. {Color.bold}+{Color.end}             : Addition              9.  {Color.bold}pi{Color.end}       : Pi Constant
2. {Color.bold}-{Color.end}             : Subtraction           10. {Color.bold}sin(x){Color.end}   : Sine Function
3. {Color.bold}x or X or *{Color.end}   : Multiplication        11. {Color.bold}cos(x){Color.end}   : Cosine Function
4. {Color.bold}/{Color.end}             : Division              12. {Color.bold}tan(x){Color.end}   : Tangent Function
5. {Color.bold}^{Color.end}             : Exponent              13. {Color.bold}asin(x){Color.end}  : Inverse Sin Function
6. {Color.bold}sqrt(x){Color.end}       : Square Root           14. {Color.bold}acos(x){Color.end}  : Inverse Cosine Function
7. {Color.bold}log(x, base){Color.end}  : Logarithm with Base   15. {Color.bold}atan(x){Color.end}  : Inverse Tangent Function
8. {Color.bold}e{Color.end}             : Euler's Constant


Note: (x) is the number you want to input.
""")
        return menu_option

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