# not_permitted_chars 

variables = {'var' : [5,True,int], 'bruh': 'World'} # list implemantation for mut and imut variables [value, mutable] type is already on the number. 
                                                    # No need to complicate things
Imutable_variables = {'var' : int, 'bruh': str} # weird implementation

temp = '"$var hello $bruh \$hello, $var",$bruh '

temppos = 0

temp.isalnum()
#not needed, but useful
#every character that a string doesn't need
not_var_chars = ['"',"'", '!','@', '#', '$','%','^','&','*','(',')',',','.',';',':','{','}','[',']','-', '`','~','/','?']

# updated version of var
all_chars_vars = ['_']

# algorithm
temp_str = temp
in_quotes = False
in_var_name = False
whitespace = False
var_name = ''
for i in temp:
    if i == '"' and in_quotes:
        in_quotes = False
    elif i == '"' and in_quotes == False:
        in_quotes = True
    # if in_quotes:

    if i == " \ ".replace(' ','') and in_quotes:
        whitespace = True

    if i == '$' and whitespace != True:
        in_var_name = True

    #to avoid confusion and ending the var name recognition immedietly.
    elif in_var_name:
        if i.isalnum() or i == '_':
            var_name += i
        else:
            temp_str = temp_str.replace(f'${var_name}',f'{variables[var_name]}',1)
            var_name = ''
            in_var_name = False
    
    if i != " \ ".replace(' ',''):
        whitespace = False
if var_name != '':
    temp_str = temp_str.replace(f'${var_name}',f'{variables[var_name]}',1)
    del var_name
    in_var_name = False


print(temp, temp_str)

dictt = {'input':[]}
dictt.update({'input':[1]})
dictt.update({'input':dictt['input']+[2]})
print(dictt, '1 2 3 4 5 6'.split(' '))
    





