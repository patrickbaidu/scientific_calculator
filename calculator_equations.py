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
    
    