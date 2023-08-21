from interpreter.interpreter import *

if __name__ == '__main__':
    run = Interpreter()
    try:
        run.execute()
    except SyntaxError as error:
        append_to_file(f"{error}")
        print(f"check log file for more info for error {error}")
        print("Exiting...")

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