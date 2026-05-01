import math

class InputEquation:
    
    def __init__(self, user_input):
        self.user_input = user_input
        
    def make_into_list(self):
        equation_list = self.user_input.split()
        return equation_list

class Number:
    
    def __init__(self, input_number):
        self.input_number = input_number
    
    def string_to_integer(self, list_of_equation):
        number_list = []
        for number in list_of_equation:
            if isinstance(number, int): 
                number = int(number)
                number_list.append(number)
            else:
                continue
        return number_list
    
    def append_operands(self, list_of_equation):
    
class SimpleEquation(Number):

    def __init__(self):
        pass
    
    def addition(self, number_input):
        pass
    
    def subtraction(self, number_input):
        pass
    
    def multiplication(self, number_input):
        pass
    
    def division(self, number_input):
        pass
    
class Parentheses(SimpleEquation):
    
    def prioritize(self):
        pass

class SaveResult:
    
    def number_history(self):
        pass
    
    