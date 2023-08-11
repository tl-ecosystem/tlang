import sys

VER = 'v0.2dev'

math_chars = ['+', '-', '/', '*']
logical_operations = ['>', '<', '!=', '==']
escape_chars = [' '] + math_chars + logical_operations + [')']
variable_declaration_chars = ['$', '=']

special_caracters = ('p','n','w','i','$')


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

def find_once_multiple(line: str, charset: list | str) -> tuple:
    """
    find once from a charset and return the position of the char that was found as a tuple
    """
    for char in charset:
        if line.find(char) != -1:
            return (line.find(char), char)

    return (-1,'') #if there is no finding then return 


def find_loop(object:str, find) -> int:
    '''
    how many times it has found a char in a string
    '''
    num_of_finds = 0
    start = 0
    while object.find(find,start) != -1: 
        num_of_finds += 1
        start = object.find(find,start)
        
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


def bool_init(object):
    object = object.replace(' ','')
    if object == 'True':
        return True
    elif object == 'False':
        return False
    else:
        raise Exception(f"{object} is not a bool")


class InstructionSet():
    def __init__(self):
        pass

    def instruction_set_handler(self):
        pass


class Functions():
    def __init__(self):
        self.functions = {}
        pass

    def function_handler(self):
        pass

class While_Loop():
    def __init__(self):
        self.instructions = []
        pass

    def while_loop_handler(self):
        pass

class Variables():
    def __init__(self):
        self.variables = {}

    def variable_asssignment(self, line:str, LOGGING:bool=False): #TODO
        var_value = None
        try:
            temp = line[line.find('=')+1: len(line)-1]
        except:
            print(f'Caught Syntax Error in line: {line}')

        try:
            var_value = int(temp)
        except:
            try:
                var_value = float(temp)
            except:
                try:
                    var_value = bool_init(temp)
                except:
                    var_value = str(temp)
                

        try:
            self.variables.update({line[1:line.find('=')].replace(' ',''): var_value})
            if LOGGING:
                print(self.variables)
        except Exception as error:
            print(f'Problem with the naming of the variable: {type(error).__name__} \n{error}, \nReport to developer.') #TODO add color
            sys.exit()

    def variable_handler(self): 
        pass


    def return_variable_value(self, name:str):
        try:
            return self.variables[name]
        except:
            raise Exception(f"The variable {name} hasn't been assigned.")


class Interpreter(Variables, Functions):
    def __init__(self):
        Variables.__init__(self)
        Functions.__init__(self)
        self.argv = sys.argv
        self.ran = False # used if the interpreter completed what it was told to do
        self.LOGGING = False #not as supposed to work, but near enough for now, also not exactly a constant

    def argv_handler(self):
        if self.argv[1] == '--help':
            print("\nHELP with --help\n" +
                  "    To run a script written in tleng you need to type in the terminal\n"+
                  "        --> python tleng_inter.py name_of_file.tleng\n\n"+
                  "    You can also put -log in the end to get a full traceback \n" +
                  "        --> python tleng_inter.py name_of_file.tleng -log\n\n"+
                  "    --version : to get the version of the interpreter\n"+
                  "    --docs : to get the full documentation of the pseudo-programming language\n"+
                  "    --help : to get the this page\n")
            self.ran = True # used if the interpreter completed what it was told to do

        elif self.argv[1] == '--version':
            print("\nVERSION with --version\n"+
                  f"Current version is: {VER}\n\n"+
                  "Type --help to learn more\n")
            self.ran = True # used if the interpreter completed what it was told to do

        elif self.argv[1] == '--docs': #TODO add the documentation here (p done)
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
            with open(self.argv[1], 'r') as f:
                self.tscript = f.readlines()
            if len(self.argv) > 2:
                if self.argv[2] == '-log':
                    self.LOGGING = True
            self.script_execution()


    def execute(self):
        if len(self.argv) > 1:
            self.argv_handler()
            self.script_execution_handler()
        else:
            print('\033[31mFatal error\033[0m, there was no input')


    def script_execution(self):
        for line in self.tscript: # line
            if line.startswith('p(') != True and line.startswith('$') != True: # check if it is printing stuff
                line = line.replace(' ','') #remove spaces

            if line.startswith('p('): # print
                self.print_method(line, self.variables)
                continue
            if line.startswith('$'): # variable declaration
                self.variable_asssignment(line, self.LOGGING)
                continue
    
    #built in functions of tlang pseudo-programming language

    def print_method(self, line:str, vars): #rewrite this function to get the string after p(
        if line.startswith('p(') and line.endswith(')\n'):
            for i in range(len(line[2: len(line) - 2])):
                if line[i] == '$': 
                    temp_var_name = find_startwith_multiple(line[i+1:],self.variables)
                    print(self.return_variable_value(temp_var_name), end='') 
                else:
                    print(line[i+2], end='')
            print('')
            # print(line[2:len(line)-2])


if __name__ == '__main__':
    run = Interpreter()
    run.execute()


# run files from the terminal, e.x. tleng_inter.py hellow.tleng
#   add a --help, --version, --docs and a -log in the end of 'tleng_inter.py hellow.tleng -log'
#   tleng_inter.py --help [D]
#   tleng_inter.py --version [D]
#   tleng_inter.py --docs [/]
# printing TODO change and add support to math, and separationg using , 
# varibles TODO change string to be only gathered in "", fix bug with just writing $var == {'var' : '$var'}
# comments *
# functions (Local variables, return) later add support for kargs for functions
# if statement
# while/for loop
# built in function length, random, type
# add logging

# live interpreter []