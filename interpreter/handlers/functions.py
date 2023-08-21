from interpreter.handlers.tools import *

class Functions(): # using the number of the line as the indicator to where to go
    def __init__(self):
        '''
        A table that contains any function that was declared.
        '''
        # Save the line of the function into a dictionary
        self.functions = {}
        pass

    def function_handler(self, name: str, pos: tuple):
        self.functions.update({name : pos})
        pass

    def function_lookup(self, name, logging) -> tuple:
        if name in self.functions:
            return self.functions[name]
        else:
            if logging:
                append_to_file(f"The function with the name: {name}, doesn't exist.")
            raise Exception(f"The function with the name: {name}, doesn't exist.\nCheck log file")
    
    def function_logging(self, script, logging: bool = False):
        line = ''
        index = 0
        temp_name = '' # not used
        temp_start = 0
        temp_end = 0 # not used

        if logging: # for debugging
            append_to_file("Proccess: Finding functions\n")

        while index != len(script):
            line: str = formating_line(script[index])
            if line.startswith('@s'):
                temp_start = index
                self.function_handler(line[2:], (temp_start,0)) #(start,end)
            elif line.startswith('@e'):
                if line[2:] in self.functions:
                    self.function_handler(line[2:], (self.functions[line[2:]][0],index))
            
            if logging: # for debugging
                append_to_file(f'self.functions = {self.functions}\n')
                
            index += 1