from interpreter.handlers.variables import *
from interpreter.handlers.functions import *
from interpreter.handlers.tools import *
from interpreter.handlers.config import *
from interpreter.handlers.logger import *
import os
# ngl i am tired of this project, gotta finish it though

class Interpreter(Variables, Functions):
    '''
    Wrapper class of every other class.
    '''
    def __init__(self, logging=False, testing = False, flags:None|list = None, inputt:None|list = None, file_name: None|str = None):
        # Initialize the config class with the class variables
        Config.FILE_NAME = file_name
        Config.LOG_FILE = file_name
        Config.LOGGING = logging
        Config.FLAGS = flags
        Config.TESTING = testing
        if testing:
            Config.LOG_FILE.replace(os.path.join('tests','tests'), os.path.join('tests','logs'))
        Config.INPUT = inputt

        Variables.__init__(self)
        Functions.__init__(self)
        Logger.__init__(self)

        self.test_list = [] # always save here
        self.testing= False
        self.curr_line = 0 # current line
    

    def execute(self):
        if self.ran != True: # if any previous function didn't ran the run this
            with open(Config.FILE_NAME, 'r') as f:
                self.tscript = f.readlines()

            self.log_list += [f"Currently executing script: {Config.FILE_NAME}"]
            self.variables.update({'0':self.script_flags}) 
            temp_int = 1
            for i in self.script_flags:
                self.variables.update({f'{temp_int}': i})
                temp_int += 1
            del temp_int

            self.function_logging(self.tscript, self.logging)
            self.main_execution()


    def main_execution(self):
        # get the pos of the main function and then run
        # if there is no pos of the main function then raise an exception
        try:
            pos = self.function_lookup('main', logging=self.logging)
        except:
            append_to_file(self.log_list, f'Function main was not found.', self.logging, True, file_name=self.log_file)    
        append_to_file(f'Proccess: Main Execution\n', logging=self.logging, file_name=self.log_file)

        for line in self.tscript[pos[0]:pos[1]]: # TODO as a while acting as a for loop
            self.curr_line += 1
            append_to_file(f'Line: {pos[0]+self.curr_line} is being interpreted\n',logging= self.logging, file_name=self.log_file)
            line : str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function call
                pass
                # self.function_execution(self.function_lookup())
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.logging)
            elif line.startswith('w('): # TODO while statement
                pass
            elif line.startswith('i('): # TODO if statement
                pass
            elif line.startswith('#') or line == '':
                continue
            else:
                append_to_file(f"Syntax error, could not interpret line {pos[0]+self.curr_line} -> \"{line}\"", self.logging, True, file_name=self.log_file)
            # Comments are lines that the interpreter doesn't find any key words
            #
            append_to_file(f'Line: {pos[0]+self.curr_line} succesfully interpreted\n\n', self.logging, file_name=self.log_file)


    def function_execution(self, pos: tuple):
        for line in self.tscript[pos[0]:pos[1]]: # TODO as a while acting as a for loop

            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function call
                pass
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.logging)
            elif line.startswith('w('): #TODO
                pass
            elif line.startswith('r('): #TODO
                pass    
            elif line.startswith('#'):
                continue
            else:
                append_to_file("Syntax error, could not interpret this line", self.logging, True, file_name=self.log_file)
    
    def math_operations(self, operat) -> str:
        return str(eval(operat))
    

    def comma_splitter(self, line: str) -> list: # I HONESTLY DON'T KNOW HOW THIS WORKS RELIABLY
        '''
        Formats the line for the easier readibility of other built-in functions (it basically clears any whitespace)
        '''
        n_line = []
        index = 0
        temp_str = ''
        in_comma = False
        quote_num = 0
        while index != len(line): # a controlable for loop as a while loop 
            if line[index] == '"': # char = line[index]
                quote_num += 1
            if quote_num % 2 == 0:
                in_comma = False
            else:
                in_comma = True
            if line[index] == ',' and in_comma == False:
                n_line += [temp_str]
                temp_str = ''
                index += 1
            elif index + 1 == len(line) and in_comma == False:
                if line[index] == ')':
                    n_line += [temp_str]    
                else:
                    temp_str += line[index] 
                    n_line += [temp_str]
                index += 1              
            else:
                temp_str += line[index]
                index += 1
        return n_line


    def formater(self, line, split_commas:bool = True, for_printing:bool=False) -> list: #add splitting commas to make the implementation of If and while easier
        '''
        Check the strings for any use of a variable and replace it 
            (it is not allowed to make any mathematical operation inside a string) 

        Check if (with the math chars list) there is a mathematical operation and return the str(integer-float)
        Check if (with the logical operations list) there is a logical operation Return the value of str(True or False)
            Also if one of the sides in a logical operation need math, use the top checks
        '''
        append_to_file('SubProcess: formater\n', self.logging, file_name=self.log_file) 
        new_line = []
        temp_str: str = ''
        if split_commas:
            new_line = self.comma_splitter(line)
        else:
            new_line += [line]
        temp_line = []
        metadata_line = [] # to dynamically find if something is eval ready or not

        append_to_file(f'{new_line}\n', self.logging, file_name=self.log_file)

        for sep in new_line:
            temp_var_list = list(self.variables.keys())
            temp_dct = self.variables

            temp_str = sep
            temp_find = sep.find('$')
            many_vars = find_loop(sep, '$') - find_loop(sep, '\$') # simplicity over optimization
            # if temp_find > -1:
            #     if sep[temp_find+1] 

            

            for var in temp_var_list: # TODO dynamically check every variable in sep and strings and numerals, and add in metadata 
                                      # we can use the reco_type function from tools.py
                                      # TODO room for optimization, newer algorithm for finding stuff
                temp_str: str = temp_str.replace('$'+var,str(temp_dct[var]))
                many_vars -= find_loop(temp_str, '$'+var) - find_loop(temp_str, '\$'+var)

                append_to_file(f'{temp_str} with var ${var}\n', self.logging, file_name=self.log_file) 

            temp_line += [temp_str]
            append_to_file(f'{temp_line}\n\n', self.logging, file_name=self.log_file) 

            del temp_find

        new_line = temp_line
        temp_line = []
        for sep in new_line:
            try:
                temp_line += str(sep)
            except:
                pass
        append_to_file('Check for printing\n', self.logging, file_name=self.log_file)
        temp_line = []
        if for_printing:
            append_to_file('Printing is True\n', self.logging, file_name=self.log_file)
            for sep in new_line:
                append_to_file(f'replacing on {sep}\n', self.logging, file_name=self.log_file)
                temp_line += [sep.replace('"','')]
            new_line = temp_line
            append_to_file(f'Replaced " for printing: {temp_line}\n', self.logging, file_name=self.log_file)
        else:
            append_to_file('Printing is False\n', self.logging, file_name=self.log_file)
        
        append_to_file('SubProcess: Formater Completed\n', self.logging, file_name=self.log_file) 
        
        return new_line
    

    # --------------------------------built in functions of tlang pseudo-programming language ---------------------------


    def print_func(self, line:str, vars): #TODO check if it easier to just search for every declared variable in the line 
        append_to_file('Process: Printing\n', self.logging, file_name=self.log_file) 
        
        temp_line = self.formater(line, for_printing=True)
        temp_test_line: str = ''

        for seps in temp_line:
            append_to_file(f'Printing: {seps}\n', self.logging, file_name=self.log_file) 
            temp_test_line += seps.replace('\n', '\n') + ' '
            
            if self.testing: # TODO
                continue
            else:
                print(seps.replace('\n', '\n') + ' ', end='')
        
        self.test_list += [temp_test_line]

        append_to_file('Proccess Print Completed\n', self.logging, file_name=self.log_file)
        # print(line[2:len(line)-2])


