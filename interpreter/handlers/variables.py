from interpreter.handlers.tools import *


class Variables():

    def __init__(self):
        self.variables = {'0':None}
    

    def variable_asssignment(self, line:str, LOGGING:bool=False): 
        append_to_file('Process: Variable assignement\n', LOGGING)
        var_value = None
        if line.find('=') == -1:
            append_to_file(f'Caught Syntax Error in line: {line}', LOGGING, True)
        
        temp = line[line.find('=')+1: len(line)]

        var_value = reco_type(temp,LOGGING=LOGGING)
     
        try:
            self.variables.update({line[1:line.find('=')].replace(' ',''): var_value})
            append_to_file(f'{self.variables}\nProccess Variable assignement completed\n\n', LOGGING)

        except Exception as error:
            append_to_file(f'Problem with the naming of the variable: {type(error).__name__} \n{error}', LOGGING, True)


    def return_variable_value(self, name:str):
        try:
            return self.variables[name]
        except:
            append_to_file(f"The variable {name} hasn't been assigned.", exception=True)