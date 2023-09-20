import sys

math_chars = ['+', '-', '/', '*', '**', '%',['(',')']]
logical_operations = ['>', '<', '!=', '==']
escape_chars = [' '] + math_chars[:len(math_chars)-1] + logical_operations + [')']


def formating_line( line: str) -> str: # easily can be simpler
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
    return n_line[:len(n_line)-1] if n_line.endswith('\n') else n_line # just in case it's the last line or not


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


def find_loop(object:str, find, isolation:tuple=(0,0,None)) -> int:
    '''
    how many times it has found a char in a string
    :isolation: it will count only if the exact position + [0] or + [1] and what to be isolated from.
    '''
    num_of_finds = 0
    start = 0
    while object.find(find,start) != -1: 
        temp_pos = object.find(find,start)
        if isolation == temp_pos:
            num_of_finds += 1
        elif object[temp_pos+isolation[0]] != isolation[2]:
            num_of_finds += 1
        elif object[temp_pos+isolation[1]] != isolation[2]:
            num_of_finds += 1
        
        start = object.find(find,start+1)
        
    return num_of_finds


def replace_only_to():
    '''
    optimising line 202 interpreter.py
    '''
    pass


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
    

def logical_statement(): # probably not neede
    pass


def bool_init(object: str) -> bool:
    '''
    Check if it a bool.
    '''
    object = object.replace(' ','')
    if object == 'True':
        return True
    elif object == 'False':
        return False
    else:
        raise Exception(f"{object} is not a bool")
    

def spacial_split(line: str) -> list[str]: # Probably not needed
    '''
    Splits spaces from line into a list.  
    '''
    return line.split()


def append_to_file(line:str|list[str,],except_line:str='', logging: bool = True, exception : bool = False, file_name:str='') -> None: # For one line visibility in code.
    '''
    Append text to a file.
    Also can handle exceptions by raising the text that was used to the file.
    Suitable for logging into a file. 
    :what: line to append to text
    :logging: bool, handles the if it will log or not
    :exception: if set to True it will also output an exception with the same line that was appended to text
    '''
    log_name = 'script_runtime.log'
    if file_name != '':
        log_name = file_name

    if logging:
        with open(log_name, 'a') as logger:
            if type(line) == list:
                for i in line:
                    logger.write(i)
                logger.write(except_line)
            else:
                logger.write(line)

    if exception:
        if except_line != '':
            raise Exception(except_line)
        else:
            raise Exception(line)


def reco_type(line:str, onlytype:bool = False, LOGGING:bool = False):
    '''
    Required that the line that is going to be imported to be only the recognising of the character.
    Onlytype: will give only the type of the said variable
    '''

    append_to_file(f'Recognision Proccess started\n\n', LOGGING)
    var_value = None
    temp = line
    temp_pos = line.find('"')
    append_to_file(f'Trying string on {temp}\n', LOGGING)
    if temp_pos != -1:
        if line.find('"', temp_pos+1) != -1:
            var_value = line[temp_pos+1: line.find('"', temp_pos+1)]
    else:
        try:
            append_to_file(f'Trying integer on {temp}\n', LOGGING)
            var_value = int(temp)
        except:
            try:
                append_to_file(f'Trying float on {temp}\n', LOGGING)
                var_value = float(temp)
            except:
                try:
                    append_to_file(f'Trying bool on {temp}\n', LOGGING)
                    var_value = bool_init(temp)
                except:
                    append_to_file(f"The variable could not be identified.", LOGGING, True)
            
    append_to_file(f'The type of {var_value} is {type(var_value)}\nRecognision Proccess completed\n\n', LOGGING)
    return var_value