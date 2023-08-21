import sys

math_chars = ['+', '-', '/', '*', '**',['(',')']]
logical_operations = ['>', '<', '!=', '==']
escape_chars = [' '] + math_chars[:len(math_chars)-1] + logical_operations + [')']
variable_declaration_chars = ['$', '=']

special_caracters = ('p(','n(','w(','i(','$', '@s', 'r()')

def formating_line( line: str) -> str:
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