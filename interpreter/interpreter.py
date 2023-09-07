from interpreter.handlers.variables import *
from interpreter.handlers.functions import *
from interpreter.handlers.tools import *

# ngl i am tired of this project, gotta finish it though

__ver__ = 'v0.4dev.03'

class Interpreter(Variables, Functions):
    def __init__(self):
        Variables.__init__(self)
        Functions.__init__(self)
        self.flag = sys.argv
        self.script_flags = self.flag[2:]
        self.ran = False # used if the interpreter completed what it was told to do
        self.logging = False # not as supposed to work, but near enough for now, also not exactly a constant
        self.curr_line = 0 # current line


    def argv_handler(self): # for color in text: \033[30m .test. \033[0m ([0m normal, [30m gray, [31m red, [32m green, [33m yellow, [34m blue)
        if self.flag[1] == '--help':
            print("\nHELP with \033[34m--help\033[0m" + "\n" +
                  "    To run a script written in tlang you need to type in the terminal\n"+
                  "        --> \033[32mpython tlang1.py name_of_file.tlang\033[0m" + "\n\n"+ # python tleng_inter.py name_of_file.tleng
                  "    You can also put \033[34m-log\033[0m in the end to get a full traceback" + "\n" +
                  "        --> \033[32mpython tlang1.py name_of_file.tlang -log\033[0m" + "\n\n"+ # python tleng_inter.py name_of_file.tleng -log
                  "    \033[34m--version\033[0m : to get the version of the interpreter" + "\n"+
                  "    \033[34m--docs\033[0m : to get the full documentation of the pseudo-programming language\n"+
                  "    \033[34m--help\033[0m : to get this page\n")
            self.ran = True # used if the interpreter completed what it was told to do

        elif self.flag[1] == '--version':
            print("VERSION with \033[34m--version\033[0m\n\n"+
                  f"Current version is: \033[32m{__ver__}\033[0m\n\n"+
                  "Type \033[34m--help\033[0m to learn more\n")
            self.ran = True # used if the interpreter completed what it was told to do

        elif self.flag[1] == '--docs': #TODO add the documentation here (p done)
            print("\nDocumentation with --docs\n"+
                  "Comments are anything that the interpreter doens't recognise as a special keyword/keychar\n\n"+
                  "p() : can print stuff to the terminal\n"+
                  "    e.x. p(hello world)\n\n"+
                  "$name_var : you can create a variable with $ and then following it with the name \n"+
                  "          For declaration you need to have it like so.\n"+
                  "          e.x.    $var = hello world\n"+
                  "          It will automatically assign the variable to it's type\n"+
                  "          The types that the language supports are:\n"+
                  "             1. Integer\n"+
                  "             2. Float\n"+
                  "             3. String\n"+
                  "             4. Bool\n"+
                  "Type \033[34m--help\033[0m to learn more\n")
            self.ran = True # used if the interpreter completed what it was told to do
    

    def script_execution_handler(self):
        if self.ran != True:
            with open(self.flag[1], 'r') as f:
                self.tscript = f.readlines()
            if len(self.flag) > 2:
                if self.flag[2] == '-log':
                    self.script_flags = self.flag[3:]
                    self.logging = True
                    with open('script_runtime.log', 'w') as logger:
                        logger.write(f"File {self.flag[1]} Executed currently running:\n")
            self.variables.update({'0':self.script_flags}) 
            temp_int = 1
            for i in self.script_flags:
                self.variables.update({f'{temp_int}': i})
                temp_int += 1
            del temp_int

            self.function_logging(self.tscript, self.logging)
            self.main_execution()


    def execute(self):
        if len(self.flag) > 1:
            self.argv_handler()
            self.script_execution_handler()
        else:
            print('\033[31mFatal error\033[0m, there was no input')
            print('Type \033[34m--help\033[0m, to get some help.')


    def main_execution(self):
        # get the pos of the main function and then run
        # if there is no pos of the main function then raise an exception
        try:
            pos = self.function_lookup('main', self.logging)
        except:
            append_to_file(f'Function main was not found.', self.logging, True)    
        append_to_file(f'Proccess: Main Execution\n', self.logging)

        for line in self.tscript[pos[0]:pos[1]]: # TODO as a while acting as a for loop
            self.curr_line += 1
            append_to_file(f'Line: {pos[0]+self.curr_line} is being interpreted\n', self.logging)
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
            # Comments are lines that the interpreter doesn't find any key words
            #
            append_to_file(f'Line: {pos[0]+self.curr_line} succesfully interpreted\n\n', self.logging)


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
        append_to_file('SubProcess: formater\n', self.logging) 
        new_line = []
        temp_str: str = ''
        if split_commas:
            new_line = self.comma_splitter(line)
        else:
            new_line += [line]
        temp_line = []
        metadata_line = [] # to dynamically find if something is eval ready or not

        append_to_file(f'{new_line}\n', self.logging)

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

                append_to_file(f'{temp_str} with var ${var}\n', self.logging) 

            temp_line += [temp_str]
            append_to_file(f'{temp_line}\n\n', self.logging) 

            del temp_find

        new_line = temp_line
        temp_line = []
        for sep in new_line:
            try:
                temp_line += str(sep)
            except:
                pass
        append_to_file('Check for printing\n', self.logging)
        temp_line = []
        if for_printing:
            append_to_file('Printing is True\n', self.logging)
            for sep in new_line:
                append_to_file(f'replacing on {sep}\n', self.logging)
                temp_line += [sep.replace('"','')]
            new_line = temp_line
            append_to_file(f'Replaced " for printing: {temp_line}\n', self.logging)
        else:
            append_to_file('Printing is False\n', self.logging)
        
        append_to_file('SubProcess: Formater Completed\n', self.logging) 
        
        return new_line
    

    # --------------------------------built in functions of tlang pseudo-programming language ---------------------------


    def print_func(self, line:str, vars): #TODO check if it easier to just search for every declared variable in the line 
        append_to_file('Process: Printing\n', self.logging) 
        
        temp_line = self.formater(line, for_printing=True)

        for seps in temp_line:
            append_to_file(f'Printing: {seps}\n', self.logging) 
            print(seps + ' ', end='')
        print('')

        append_to_file('Process Print Completed\n', self.logging)
        # print(line[2:len(line)-2])
