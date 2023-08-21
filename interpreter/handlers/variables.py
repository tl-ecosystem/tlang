from interpreter.handlers.tools import *

class Variables():
    def __init__(self):
        self.variables = {}

    def variable_asssignment(self, line:str, LOGGING:bool=False): 
        var_value = None
        if line.find('=') == -1:
            raise Exception(f'Caught Syntax Error in line: {line}')
        
        temp = line[line.find('=')+1: len(line)-1]
        
        temp_pos = line.find('"')
        if temp_pos != -1:
            if line.find('"', temp_pos+1) != -1:
                var_value = line[temp_pos+1: line.find('"', temp_pos+1)]
        else:
            try:
                var_value = int(temp)
            except:
                try:
                    var_value = float(temp)
                except:
                    try:
                        var_value = bool_init(temp)
                    except:
                        raise Exception(f"The variable: '{line[1:line.find('=')].replace(' ','')}' could not be assigned")
                

        try:
            self.variables.update({line[1:line.find('=')].replace(' ',''): var_value})
            if LOGGING:
                print(self.variables)
        except Exception as error:
            print(f'Problem with the naming of the variable: {type(error).__name__} \n{error}, \nReport to developer.') #TODO add color
            sys.exit()


    def return_variable_value(self, name:str):
        try:
            return self.variables[name]
        except:
            raise Exception(f"The variable {name} hasn't been assigned.")