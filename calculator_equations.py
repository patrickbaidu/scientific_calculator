import math

class InputEquation:
    
    def __init__(self, user_input):
        self.user_input = user_input
        
    def make_into_list(self):
        equation_list = self.user_input.split()
        return equation_list

class Number(InputEquation):
    
    def __init__(self, input_number):
        self.input_number = input_number
    
    def string_to_integer(self):
        number_list = []
        for number in self.input_number:
            if isinstance(number, int): 
                number = int(number)
                number_list.append(number)
            else:
                continue
        return number_list
    
    def append_operands(self):
        operands_list = []
        for character in self.input_number:
            if character.isalnum() and not character.isspace():
                operands_list.append(character)
            else:
                continue
        return operands_list
    
class EquationLine(Number):

    def __init__(self, line_of_equation):
        self.line_of_equation = line_of_equation
    
    def combine_equation(self, number_list, operands_list):
        for number in number_list:
            index_of_number = self.line_of_equation.index(number)
    
    def equation_line(self):
        try:
            pass
        except ValueError as e:
            pass
    
    def 

class SaveResult:
    
    def number_history(self):
        pass
    
    