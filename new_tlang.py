#!/etc/bin/python3
#I don't know how to make it work

from interpreter.interpreter import *
from tests.readtest import *
import sys

if __name__ == '__main__':
    flags = sys.argv
    if flags[1] == 'testing':
        print('Testing Interpreter:')
        print('Running Tester: \n')
        tester = Tester()
        if flags[2] == '-log':
            tester.start(True)
        else:
            tester.start()

    else:
        run = Interpreter()
        try:
            run.execute()
        except Exception as error:
            append_to_file(f"{error}")
            print(f"check log file for more info for error: \n-> {error}")
            print("Exiting...")

# run files from the terminal, e.x. tleng_inter.py hellow.tleng
#   tleng_inter.py --docs [/]
# tester TODO
# printing TODO change and add support to math, and separationg using , 
# varibles TODO change string to be only gathered in "", fix bug with just writing $var == {'var' : '$var'}
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