from interpreter.handlers.tools import *

class Variables():
    def __init__(self):
        self.variables = {}

    def variable_asssignment(self, line:str, LOGGING:bool=False): 
        if LOGGING:
            append_to_file('Process: Variable assignement\n')
        var_value = None
        if line.find('=') == -1:
            if LOGGING:
                append_to_file(f'Caught Syntax Error in line: {line}')
            raise Exception(f'Caught Syntax Error in line: {line}')
        
        temp = line[line.find('=')+1: len(line)]
        
        temp_pos = line.find('"')
        if LOGGING:
            append_to_file(f'Trying string on {temp}\n')
        if temp_pos != -1:
            if line.find('"', temp_pos+1) != -1:
                var_value = line[temp_pos+1: line.find('"', temp_pos+1)]
        else:
            try:
                if LOGGING:
                    append_to_file(f'Trying integer on {temp}\n')
                var_value = int(temp)
            except:
                try:
                    if LOGGING:
                        append_to_file(f'Trying float on {temp}\n')
                    var_value = float(temp)
                except:
                    try:
                        if LOGGING:
                            append_to_file(f'Trying bool on {temp}\n')
                        var_value = bool_init(temp)
                    except:
                        raise Exception(f"The variable: '{line[1:line.find('=')].replace(' ','')}' could not be assigned")
                

        try:
            self.variables.update({line[1:line.find('=')].replace(' ',''): var_value})
            if LOGGING:
                append_to_file(f'{self.variables}\nProccess Completed succesfully\n\n')

        except Exception as error:
            print(f'Problem with the naming of the variable: {type(error).__name__} \n{error}, \nReport to developer.') #TODO add color
            sys.exit()


    def return_variable_value(self, name:str):
        try:
            return self.variables[name]
        except:
            raise Exception(f"The variable {name} hasn't been assigned.")