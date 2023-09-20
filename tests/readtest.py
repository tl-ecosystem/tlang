from interpreter.interpreter import *
import os

test_files = [
    os.path.join('tests','tests','main.tlang'),
    os.path.join('tests','tests','err_main.tlang'),
    os.path.join('tests','tests','vars.tlang'),
    os.path.join('tests','tests','err_vars.tlang'),
    os.path.join('tests','tests','flags.tlang')
]

class Tester:
    def __init__(self) -> None:
        self.test_files = test_files
        self.dict = {} # {'test.tlang': {expected:'1 2 3', got:'1 2 3'}}
        self.logging = False

    def parser(self, file) -> dict:
        with open(file,'r') as program:
            lines = program.readlines()
        dictt = {'input':[],
                 'flags':[],
                 'expected':[]}
        inputt = False
        flags = False
        expected = False
        for i in lines:
            if i.find('# Input:') != -1:
                flags, expected = False, False
                inputt = True
            elif i.find('# Flags:') != -1:
                inputt, expected = False, False
                flags = True
            elif i.find('# Expected:') != -1:
                flags, inputt = False, False
                expected = True

            elif inputt:
                if i.startswith('# '):
                    dictt.update({'input' : dictt['input'] + [i[2:].replace('\n','')]})
            elif flags:
                if i.startswith('# '):
                    dictt.update({'flags' : dictt['flags'] + [i[2:].replace('\n','').split(' ')]})
                    dictt["flags"] = dictt["flags"][0]
            elif expected:
                if i.startswith('# '):
                    dictt.update({'expected' : dictt['expected'] + [i[2:].replace('\n','')]})

        return dictt
    
    def start(self, logging: bool = False):
        # running the for loop for the test files testing
        self.logging = logging
        for file in self.test_files:
            file_dict = self.parser(file)
            print(f'Testing {file}: ', end='')

            got = self.executing(file_dict['input'], file_dict['flags'], file)

            # saving some debug info
            self.dict.update({file : {'expected' : file_dict['expected'], 'got':got} })

            if self.dict[file]['expected'] == self.dict[file]['got']:
                print(f'\033[32mSuccess\033[30m (debug: {self.dict[file]})\033[0m\n')
            else:
                print(f'\033[31mFailed\033[30m (debug: {self.dict[file]})\033[0m\n')
        

    def executing(self, inputt:list, flags:list, file:str):
        # starting the interpreter to run with the file and the passed arguments
        run = Interpreter()

        argv = ['demo.py'] + [file] + ['-log']
        for i in flags:
            argv += [i]

        try:
            got = run.execute(True, argv, inputt)
        except Exception as error:
            got = [str(error)]
        return got
    
