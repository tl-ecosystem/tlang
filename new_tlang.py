#!/etc/bin/python3
#I don't know how to make it work

from interpreter.interpreter import *
from tests.readtest import *
import sys

def flag_response(flag): # for color in text: \033[30m .test. \033[0m ( [0m normal, [30m gray, [31m red, [32m green, [33m yellow, [34m blue )
    if flag[1] == '--help':
        print("\nHELP with \033[34m--help\033[0m" + "\n" +
              "    To run a script written in tlang you need to type in the terminal\n"+
              "        --> \033[32mpython tlang1.py name_of_file.tlang\033[0m" + "\n\n"+ # python tlang_inter.py name_of_file.tleng
              "    You can also put \033[34m-log\033[0m in the end to get a full traceback" + "\n" +
              "        --> \033[32mpython tlang1.py name_of_file.tlang -log\033[0m" + "\n\n"+ # python tlang_inter.py name_of_file.tleng -log
              "    \033[34m--version\033[0m : to get the version of the interpreter" + "\n"+
              "    \033[34m--docs\033[0m : to get the full documentation of the pseudo-programming language\n"+
              "    \033[34m--help\033[0m : to get this page\n")

    elif flag[1] == '--version':
        print("VERSION with \033[34m--version\033[0m\n\n"+
              f"Current version is: \033[32m{Config.__ver__}\033[0m\n\n"+
              "Type \033[34m--help\033[0m to learn more\n")

    elif flag[1] == '--docs': #TODO add the documentation here (p done)
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
        
    elif flag[1] == '--tester':
        print('Testing Interpreter:')
        print('Running Tester: \n')
        tester = Tester()
        try:
            if flags[2] == '-log':
                tester.start(True)
        except:
            tester.start()


if __name__ == '__main__':
    flags = sys.argv
    flags_list = ['--help','--docs','--version','--tester']

    temp_bool = False
    for i in flags_list:
        if flags[1].find(i) > -1:
            temp_bool = True
    
    if len(flags) < 1:
        print('\033[31mFatal error\033[0m, there was no input')
        print('Type \033[34m--help\033[0m, to get some help.')

    elif temp_bool:
        flag_response(flag=flags)

    elif flags[1].endswith('.tlang'):
        logging = False
        try: 
            if flags[2] == "-log":
                logging = True
                program = Interpreter(logging=logging, flags=flags[3:],file_name=flags[1])
        except:
            program = Interpreter(logging=logging, flags=flags[2:], file_name=flags[1])

        try:
            program.execute()
            if logging:
                program.log_to_file(logging=logging, file_name=flags[1])

        except Exception as error:
            program.log_list += [error]
            if logging:
                program.log_to_file(logging=logging, file_name=flags[1])
            else:
                pass
                # traceback smh

            print(f"check log file for more info for error: \n-> {error}")
            print("Exiting...")
    else:
        print('\033[31mFatal error\033[0m, wrong input')
        print('Neither File or Flag was detected please')
        print('Type \033[34m--help\033[0m, to get some help.')




# run files from the terminal, e.x. tleng_inter.py hellow.tleng
#   tleng_inter.py --docs [/]
# tester TODO
# printing TODO change and add support to math, and separationg using , 
# variables TODO change string to be only gathered in "", fix bug with just writing $var == {'var' : '$var'}
# comments with #
# functions (Local variables, return) later add support for kargs for functions
# if statement
# while/for loop
# built in function length, random, type
# caching

"""
PUSH COMMITS WHEN:
    A SOLVE TO A PROBLEM HAS BEEN MADE OR 
    WHEN A GOAL HAS BEEN ACHIEVED
MERGE TO MAIN WHEN:
    A WHOLE GOAL HAS BEEN ACHIEVED
"""

# ---------------------------------------------------------------------

"""
- new_tlang.py
- demo.tlang

/interpreter/ (folder)
|- interpreter.py
|
|- /handlers/ (folder)
|  |- functions.py
|  |- if.py
|  |- tools.py
|  |- variables.py
|  |- while.py

"""