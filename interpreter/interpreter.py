from interpreter.handlers.variables import *
from interpreter.handlers.functions import *

VER = 'v0.4dev.01'

class Interpreter(Variables, Functions):
    def __init__(self):
        Variables.__init__(self)
        Functions.__init__(self)
        self.flag = sys.argv
        self.script_flags = self.flag[2:]
        self.ran = False # used if the interpreter completed what it was told to do
        self.LOGGING = False # not as supposed to work, but near enough for now, also not exactly a constant
        self.line = 0

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
                  f"Current version is: \033[32m{VER}\033[0m\n\n"+
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
                    self.LOGGING = True
                    with open('script_runtime.log', 'w') as logger:
                        logger.write(f"File {self.flag[1]} Executed currently running:\n")
            self.function_logging(self.tscript, self.LOGGING)
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
        pos = self.function_lookup('main', self.LOGGING)
        append_to_file(f'Proccess: Main Execution\n', self.LOGGING)

        for line in self.tscript[pos[0]:pos[1]]: # TODO as a while acting as a for loop
            self.line += 1
            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function call
                pass
                # self.function_execution(self.function_lookup())
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.LOGGING)
            elif line.startswith('w('): #TODO
                pass
            # Comments are lines that the interpreter doesn't find any key words
            append_to_file(f'Line: {pos[0]+self.line} succesfully interpreted\n', self.LOGGING)


    def function_execution(self, pos: tuple):
        for line in self.tscript[pos[0]:pos[1]]: # TODO as a while acting as a for loop

            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function call
                pass
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.LOGGING)
            elif line.startswith('w('): #TODO
                pass
            elif line.startswith('r('): #TODO
                return 'smt?'     
    
    def math_operations(self, operat) -> str:
        return str(eval(operat))
    
    def comma_splitter(self, line: str) -> list: # I HONESTLY DON'T KNOW HOW THIS WORKS RELIABLY
        '''
        Formats the line for the easier readibility of other built-in functions (it basically clears any whitespace)
        '''
        n_line = []
        index = 0
        temp_str = ''
        in_quote = False
        quote_num = 0
        while index != len(line): # a controlable for loop as a while loop 
            if line[index] == '"': # char = line[index]
                quote_num += 1
            if quote_num % 2 == 0:
                in_quote = False
            else:
                in_quote = True
            if line[index] == ',' and in_quote == False:
                n_line += [temp_str]
                temp_str = ''
                index += 1
            elif index + 1 == len(line) and in_quote == False:
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

    def formater(self, line) -> list:
        '''
        Check the strings for any use of a variable and replace it 
            (it is not allowed to make any mathematical operation inside a string) 

        Check if (with the math chars list) there is a mathematical operation and return the str(integer-float)
        Check if (with the logical operations list) there is a logical operation Return the value of str(True or False)
            Also if one of the sides in a logical operation need math, use the top checks
        '''
        append_to_file('SubProcess: formater\n', self.LOGGING) 
        new_line = []
        temp_str: str = ''
        new_line = self.comma_splitter(line)
        temp_line = []
        metadata_line = []

        append_to_file(f'{new_line}\n', self.LOGGING)

        for sep in new_line:
            temp_var_list = list(self.variables.keys())
            temp_dct = self.variables

            temp_str = sep
            for var in temp_var_list: #TODO add the find_multiple to add if it is mostly numerals then add to metadata that it is eval ready, pos2: True
                                      #TODO also add string recognition, to just add a string and not the "" 
                temp_str: str = temp_str.replace('$'+var,str(temp_dct[var]))
                append_to_file(f'{temp_str}\n', self.LOGGING) 
            temp_line += [temp_str]
            append_to_file(f'{temp_line}\n\n', self.LOGGING) 

        new_line = temp_line
        temp_line = []
        for sep in new_line:
            try:
                temp_line += str(sep)
            except:
                pass
        append_to_file('SubProcess: Formater Completed\n', self.LOGGING) 
        return new_line
    #built in functions of tlang pseudo-programming language

    def print_func(self, line:str, vars): #TODO check if it easier to just search for every declared variable in the line 
        append_to_file('Process: Printing\n', self.LOGGING) 
        
        temp_line = self.formater(line)

        for seps in temp_line:
            append_to_file(f'Printing: {seps}\n', self.LOGGING) 
            print(seps + ' ', end='')
        print('')

        append_to_file('Process Print Completed\n', self.LOGGING)
        # print(line[2:len(line)-2])
