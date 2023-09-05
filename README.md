# TLangPy
#### WARNING: Code poorly optimized, and written like spaghetti. The reason is because this project was supposed to be small, but accidently made it bigger than envisioned, which led to me writing poor code due to the short time. Please understand if I fix any issues considering optimazation or readability is going to happen ONLY because I need the language for a particular use for another project.

A pseudo-programming interpreted language created using Python. A fun little project.

To run a script written in tleng you need to type in the terminal

    --> python tlang1.py name_of_file.tlang
    
You can also put -log in the end to get a full traceback: WARNING -log is currently printing OLNY every assigned variable when it's assigned

    --> python tlang1.py name_of_file.tlang -log
    
--version : to get the version of the interpreter

--docs : to get the full documentation of the pseudo-programming language

--help : to get this page


## DOCUMENTATION

Anything that isn't a scpecial keychar/keyword is considered a comment

### Explicitness in syntax

This language requires you to follow some strict rules, even though the interpreter might not tell you anything, for the smoothest experience always follow the syntax to not get some weird behaviour.

In terms of the spaces, and the indents, this language is whitespace free for most of the time, if not then this documentation will mention it.

Due to not using a semicolon every single line is supposed to hold one or a part of a function.

### Printing to the terminal

`p()` (p = print) is for printing anything put inside will be printed

    p(Hello World)

### Creating Variables 

You can create variables using the `$` and name them whatever you want, the type of the variable will be assigned automativally

    $var_name = Hello World
    
There are four types of variables that the Language supports.

- Integer
- Float
- String
- Bool

### Creating Functions

You can create a function by typing `@s` (s = start), an then to finish the function you need to type `@e` (e = end) and then the name of the function:
    
    @s Function_name
        p("This is inside a function in PyTlang")
    @e Function_name

To pass arguments in the function you need to type `$1`, according to how many arguments you have passed that much the number goes up, if you want to see every flag then you can type $0 (for debug porpuses only):
#### Reminder : if in main the only thing that gets passed is the flags when the program runs
#### Exception : if you want to access the flags that you passed to the program then you need to explicitely pass them in the function as arguments 

    @s add
        p("the sum of $1 + $2 is", $1 + $2)
    @e add

    @s main
        @add[ 5, 5 ]
    @e main

If you want to return something from the function then you can type it in `r()` (r = return):

    @s add
        r($1 + $2)
    @e add

    @s main
        $var_1 = 5
        $var_2 = 6
        p("The sum of $var_1 + $var2 =", @add[ $var_1, $var_2 ])
    @e main
