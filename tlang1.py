import sys

VER = 'v0.2dev.03'

math_chars = ['+', '-', '/', '*', '**',['(',')']]
logical_operations = ['>', '<', '!=', '==']
escape_chars = [' '] + math_chars[:len(math_chars)-1] + logical_operations + [')']
variable_declaration_chars = ['$', '=']

special_caracters = ('p(','n(','w(','i(','$', '@s', 'r()')

def formating_line(self, line: str) -> str:
    '''
    Formats the line for the easier readibility of other built-in functions (it basically clears any whitespace)
    '''
    # Will take a line and, 
    #   clear every space it has, if there is a string it will ignore the spaces inside of it
    #   return the line as a whole 
    #   use cases: easier to detect the logical operations in the brackets and fixes white space at the start of the line 
    n_line = ''
    index = 0
    while index != len(line): # a controlable for loop as a while loop 
        if line[index] == '"': # char = line[index]
            if line.find('"',index+1) != -1:
                detected_str = line[index: line.find('"',index+1)]
                n_line += detected_str
                index += len(detected_str)
            else:
                n_line += line[index]
                index += 1
        elif line[index] != ' ':
            n_line += line[index]
            index += 1
        else:
            index += 1
    return n_line[:len(n_line-1)] if n_line.endswith('\n') else n_line # just in case it's the last line or not

def find_multiple(line: str, charset: list | str) -> dict: #TODO make this and then update the printing
    """
    Find multiple positions of chars from a charset in a string and return a dictionary that contains it
    """
    pos_dict = {}
    pos = [] 
    for char in charset:
        for i in range(len(line)): #searching in the line for the char
            if line[i] == char:
                pos += [i]#storing position of char
        pos_dict.update({char : pos}) 
        pos = [] #reseting pos of chars
    return(pos_dict)

def find_once_multiple(line: str, charset: list | str, start) -> tuple:
    """
    find once from a charset and return the position of the char that was found as a tuple
    """
    for char in charset:
        if line.find(char) != -1:
            return (line.find(char, start), char)

    return (-1,'') #if there is no finding then return 


def find_loop(object:str, find) -> int:
    '''
    how many times it has found a char in a string
    '''
    num_of_finds = 0
    start = 0
    while object.find(find,start) != -1: 
        num_of_finds += 1
        start = object.find(find,start+1)
        
    return num_of_finds

def find_startwith_multiple(line: str, words: dict | list | str) -> str:
    '''
    checks from a wordset if the start of the string matches with the word from the wordset
    '''
    temp_words = words

    if type(words) is dict: # making words into a list for the for loop
        temp_words = list(words.keys())
    
    for word in temp_words:
        if line.startswith(word):
            return word
    return line[0:find_once_multiple(line,escape_chars)[0]].replace(' ','')
    
def logical_statement():
    pass


def bool_init(object: str):
    object = object.replace(' ','')
    if object == 'True':
        return True
    elif object == 'False':
        return False
    else:
        raise Exception(f"{object} is not a bool")


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

    def function_lookup(self) -> tuple:
        pass
    
    def function_logging(self, script):
        line = ''
        index = 0
        temp_name = '' # not used
        temp_start = 0
        temp_end = 0 # not used
        while index != len(script):
            line: str  = formating_line(script[index])
            if line.startswith('@s'):
                temp_start = index
                self.function_handler(line[2:], (temp_start,0)) #(start,end)
            elif line.startswith('@e'):
                if line[2:] in self.functions:
                    self.function_handler(line[2:], (self.functions[line[2:]][0],index))
                    
                
            index += 1
        
class While_Loop(): # using the starter number of the loop to continiusly go back to and do the loop again
    def __init__(self):
        '''
        A loop that lasts as long as the logical operation stays True!
        '''
        # Saves the line number from the starting poin of the loop into a variable
        self.instructions = []
        pass

    def while_loop_handler(self):
        pass

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
        for line in self.tscript[]: # TODO as a while acting as a for loop

            line: str = formating_line(line) # str added for better pylint highlighting 
            if line.startswith('@'): #Function declaration
                pass
            elif line.startswith('p('): # print, also handles variable detection
                self.print_func(line.replace('p(',''), self.variables) #line.replace('p(','') then also change the print_func
            elif line.startswith('$'): # variable declaration or re-declaration
                self.variable_asssignment(line, self.LOGGING)
            elif line.startswith('w('): #TODO
                pass
            elif line.startswith('#'):
                continue
            else:
                lo
    
    
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


if __name__ == '__main__':
    run = Interpreter()
    run.execute()


# run files from the terminal, e.x. tleng_inter.py hellow.tleng
#   tleng_inter.py --docs [/]
# printing TODO change and add support to math, and separationg using , 
# varibles TODO change string to be only gathered in "", fix bug with just writing $var == {'var' : '$var'}
# comments *
# functions (Local variables, return) later add support for kargs for functions
# if statement
# while/for loop
# built in function length, random, type
# add logging
# dynamic comments with {} (removed when formating line)

"""
PUSH COMMITS WHEN:
    A SOLVE TO A PROBLEM HAS BEEN MADE OR 
    WHEN A GOAL HAS BEEN ACHIEVED
MERGE TO MAIN WHEN:
    A WHOLE GOAL HAS BEEN ACHIEVED
"""
