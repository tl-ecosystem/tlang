# from interpreter.handlers.config import *

class Logger():
    '''
    Should only be called when we need to add something to the list of logging. 
    When the program is finished there should be a signal that will indicate to write the logged list into a file ending in {file name}.log
    '''
    def __init__(self) -> None:
        self.log_list = [] # add lines of what the code does here
        self.trace_list = [] # add program line codes when logging is false.
    
    def log_to_file(self, logging, file_name) -> None: # When done, instruct to log the lines here.
        '''
        Append text to a file.
        '''
        if logging:
            with open(file_name + '.log', 'a') as logger:
                for i in self.log_list:
                    logger.write(i)

    def update_log_list(self, line, logging, exception:bool=False) -> None:
        if logging:
            self.log_list += [line]

            if exception:
                raise Exception(line)
        else:
            logging

