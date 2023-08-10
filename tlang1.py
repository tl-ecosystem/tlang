import sys

VER = 'v0.1'

math_chars = ['+', '-', '/']
logical_operations = ['>', '<', '!=', '==']
escape_chars = [' ', ')'] + math_chars # TODO maybe delete later
printing_chars = ['(', ')']
input_chars = ['(', ')']
return_chars = ['(', ')']
if_chars = ['(', ')']
while_chars = ['(', ')']
variable_declaration_chars = ['$', '=']

special_caracters = ('p','n','w','i','$')




def find_multiple(line, charset:list|str) -> dict: #TODO make this and then update the printing
    pos_dict = {}
    pos = [] 
    for char in charset:
        for i in range(len(line)): #searching in the line for the char
            if line(i) == char:
                pos += [i]#storing position of char
        pos_dict += {char : pos}
        pos = [] #reseting pos of chars
    return(pos_dict)

def print_method(line, char, vars):
    temp_var_list = []
    temp_line = list(line)

    if line[line.find(char)+1] == '(' and line[len(line)-2] == ')':
        for i in range(len(line[line.find(char)+2:len(line)-2])):
            if line[i] == '$': #for variable handling
                # temp_line.
                # temp_var_list += vars[line.find('$')+1: ]
                pass
        print(line[line.find(char)+2:len(line)-2])

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

    def variable_handler(self, line, char): #TODO
        # if variable is to  
        self.variables.update() #TODO FINISH THE variable handler
                                #e.x. 'name' of variable

class Interpreter(Variables, Functions):
    def __init__(self):
        Variables.__init__(self)
        Functions.__init__(self)
        self.argv = sys.argv
        self.ran = False # used if the interpreter completed what it was told to do

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

        elif self.argv[1] == '--docs': #TODO add the documentation here
            print("\nDocumentation with --docs\n"+
                  "There is no documentation at the momment\n\n"+
                  "Type --help to learn more\n")
            self.ran = True # used if the interpreter completed what it was told to do
    
    def script_execution_handler(self):
        if self.ran != True:
            try:
                with open(self.argv[1], 'r') as f:
                    self.tscript = f.readlines()
                self.script_execution()
            except:
                print(f'Exception Raised, type --help to learn more')

    def execute(self): #TODO change the execute function handles the argv, and make it more safe
        if len(self.argv) > 1:
            self.argv_handler()
            self.script_execution_handler()
        else:
            print('\033[31mFatal error\033[0m, there was no input')


    def script_execution(self):
        for line in self.tscript: # line
            for char in line: # char
                if char == 'p': # print
                    print_method(line, char, self.variables)
                    break
                if char == '$': # variable declaration
                    self.variable_handler(line, char)
                    break


if __name__ == '__main__':
    run = Interpreter()
    run.execute()


# run files from the terminal, e.x. tleng_inter.py hellow.tleng
#   add a --help, --version, --docs and a -log in the end of 'tleng_inter.py hellow.tleng -log'
#   tleng_inter.py --help [D]
#   tleng_inter.py --version [D]
#   tleng_inter.py --docs [/]
# varibles
# comments *
# functions (Local variables, return)
# if statement
# while/for loop

# built in function length, random, type

# live interpreter []
