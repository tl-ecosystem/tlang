from interpreter.handlers.tools import *


class Variables():

    def __init__(self):
        self.variables = {'0':None} # {"main" : {'0':None}} 
    

    def variable_asssignment(self, line:str, LOGGING:bool=False): 
        append_to_file('Process: Variable assignement\n', LOGGING)
        var_value = None
        annotation = False

        temp_line_find = line.find('=')

        if temp_line_find == -1:
            append_to_file(f'Caught Syntax Error in line: {line}', LOGGING, True)
        
        temp = line[line.find('=')+1: len(line)]

        temp_annotation_pos = line[:temp_line_find-1].find('<-')
        if temp_annotation_pos != -1:
            annotation = True
            append_to_file(f'Found Annotation of variable\n', LOGGING)
            temp_type = line[temp_annotation_pos+2:temp_line_find]

            append_to_file(f'type -> {temp_type}\n', LOGGING)
            try:
                if temp_type == 'int' or temp_type == 'integer':
                    var_value = int(temp)
                elif temp_type == 'float':
                    var_value = float(temp)
                elif temp_type == 'bool' or temp_type == 'boolean':
                    var_value = bool(temp)
                elif temp_type == 'str' or temp_type == 'string':
                    var_value = temp
                else:
                    append_to_file(f"There is no annotation {temp_type}, for {temp}",LOGGING, True)
            except:
                append_to_file(f"The annotation was wrong, check log, {temp_type} for {temp}",LOGGING, True)
        else:
            append_to_file(f'No Annotation Found\n', LOGGING)
            var_value = reco_type(temp,LOGGING=LOGGING)

        # var_value = reco_type(temp,LOGGING=LOGGING)
     
        try:
            if annotation:
                self.variables.update({line[1:line.find('<-')].replace(' ',''): var_value})
            else:
                self.variables.update({line[1:line.find('=')].replace(' ',''): var_value})
            
            append_to_file(f'{self.variables}\nProccess Variable assignement completed\n', LOGGING)

        except Exception as error:
            append_to_file(f'Problem with the naming of the variable: {type(error).__name__} \n{error}', LOGGING, True)


    def return_variable_value(self, name:str):
        try:
            return self.variables[name]
        except:
            append_to_file(f"The variable {name} hasn't been assigned.", exception=True)