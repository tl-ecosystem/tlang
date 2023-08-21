from interpreter.handlers.variables import *
from interpreter.handlers.functions import *

VER = 'v0.2dev.03'

class Interpreter(Variables, Functions):
    def __init__(self):
        Variables.__init__(self)
        Functions.__init__(self)
        self.flag = sys.argv
        self.app_flags = self.flag[2:]
        self.ran = False # used if the interpreter completed what it was told to do
        self.LOGGING = False # not as supposed to work, but near enough for now, also not exactly a constant

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
                  "There should always be one line free in the end of the progam\n"+
                  "Type --help to learn more\n")
            self.ran = True # used if the interpreter completed what it was told to do
    

    def script_execution_handler(self):
        if self.ran != True:
            with open(self.flag[1], 'r') as f:
                self.tscript = f.readlines()
            if len(self.flag) > 2:
                if self.flag[2] == '-log':
                    self.LOGGING = True
            self.function_logging(self.tscript)
            self.main_execution()


    def execute(self):
        if len(self.flag) > 1:
            self.argv_handler()
            self.script_execution_handler()
        else:
            print('\033[31mFatal error\033[0m, there was no input')


    def main_execution(self):
        for line in self.tscript: # TODO as a while acting as a for loop

            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function declaration
                pass
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.LOGGING)
            elif line.startswith('w('): #TODO
                pass
            # Comments are lines that the interpreter doesn't find any key words

    def function_execution(self):
        for line in self.tscript: # TODO as a while acting as a for loop

            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function declaration
                pass
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.LOGGING)
            elif line.startswith('w('): #TODO
                pass
    
    
    def math_operations(self, operat) -> str:
        return str(eval(operat))

    def formater(self, line) -> str:
        '''
        Check the strings for any use of a variable and replace it 
            (it is not allowed to make any mathematical operation inside a string) 

        Check if (with the math chars list) there is a mathematical operation and return the str(integer-float)
        Check if (with the logical operations list) there is a logical operation Return the value of str(True or False)
            Also if one of the sides in a logical operation need math, use the top checks
        '''

        new_line = ''

        return new_line
    #built in functions of tlang pseudo-programming language

    def print_func(self, line:str, vars): #TODO check if it easier to just search for every declared variable in the line 
        temp_dct = {}
        temp_str = '' 
        temp_var_list = []

        separated_line = []

        # if line.startswith('p(') and line.endswith(')\n'):
        # print(line[:len(line)-2])
        # for i in range(2, len(line[2: len(line) - 2])):
            # if line[i] == '$': 
            #     temp_var_name = find_startwith_multiple(line[i+1:],self.variables)
            #     temp_var_list += [temp_var_name]
            #     temp_dct.update({temp_var_name:self.return_variable_value(temp_var_name)}) 

        start = 0
        last_start = len(line)-1
        while line.find(',',start) != -1: # formatting for the line
            last_start = start
            start = line.find(',',start) if line.find(',',start) != -1 else find_once_multiple(line, escape_chars, start)
            if line.find('"') != -1:
                temp = line.find('"')
                separated_line += [line[last_start+1:temp-1].replace(' ','') + line[temp+1:line.find('"', temp+1)] + line[line.find('"', temp+1):start-1].replace(' ','')]
                                # First part of the sepration line ,___" then the inside of the string "_______" and then the outside of the string again "___, until the next ","
            else: 
                separated_line += [line[last_start+1:start-1].replace(' ','')]


        for sep in separated_line:
        #     for i in range(len(sep)):
        #         if sep[i] == '$': 
        #             temp_var_name = find_startwith_multiple(line[i+1:],self.variables)
        #             temp_var_list += [temp_var_name]
        #             temp_dct.update({temp_var_name:self.return_variable_value(temp_var_name)}) 
            
            
        # print(temp_var_list, temp_dct)
            temp_str = sep
            temp_var_list = list(self.variables.keys())
            temp_dct = self.variables
            for i in temp_var_list:
                temp_str = temp_str.replace('$'+i,str(temp_dct[i]))

        print(temp_str)
        # print(line[2:len(line)-2])
