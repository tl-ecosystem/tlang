# PyTLang - Expiremental Branch, WIP

TODO:

1. Documentation: ~
2. Variables: 
3. Variables - Int: Yes
4. Variables - Float: Yes
5. Variables - String: Yes
6. Variables - Boolean: Yes
7. Variables - Lists: No
8. Variables - Assignment: ~
9. Variables - Reassignment: ~
10. Variables - String access list: No
11. Variables - Annotation (i,f,b,s): Yes
12. Variables - Imuttable: No
13. Printing:
14. Printing - Formater: ~
15. Printing - printer: Yes
16. Printing - evaluator: No
17. Functions:
18. Functions - Recognising: Yes
19. Functions - Call: No
20. Functions - Arguments: No
21. Functions - Arguments Vars: No
22. Functions - Arguments Vars Name: No
23. Functions - Arguments Annotation: No



An interpreted programming language created using Python. A fun little project (do not copy, I made this project without reading how an actual Interpreter works, so everything is created from scratch).

To run a script written in tleng you need to type in the terminal

    --> python pytlang.py name_of_file.tlang
    
You can also put `-log` in the end to get a full traceback:

    --> python pytlang.py name_of_file.tlang -log
    
`--version` : to get the version of the interpreter

`--docs` : to get the full documentation of the pseudo-programming language

`--help` : to get this page

## Requirements

1. Python 3.11.4 and later

## DOCUMENTATION


- ### Comments
Anything that isn't a scpecial keychar/keyword is considered a comment

- ### Explicitness in syntax

This language requires you to follow some strict rules, even though the interpreter might not tell you anything, for the smoothest experience always follow the syntax to not get some weird behaviour.

In terms of the spaces, and the indents, this language is whitespace free for most of the time, if not then this documentation will mention it.

Due to not using a semicolon, every single line is supposed to hold one or a part of a function.

For the Code to run there must be always a main function where the code runs from.

Flags are counted what is typed after the input of the file, if typed -log, then it will take only what is typed after it as flags. Check Variables Docs. 

- ### Printing to the terminal

`p()` (p = print) is for printing anything put inside will be printed

    p("Hello World")

- ### Variables 

You can create variables using the `$` and name them whatever you want, the type of the variable will be assigned automativally

    $var_name = Hello World
    
There are four types of variables that the Language supports.

1. Integer

2. Float

3. String

4. Bool

To access the flags written for the `.tlang` file type `$` and follow it by the position you wrote it. You can also type `$0` to see every flag (BEST FOR DEBUGGING).

    -> python3 new_tlang.py demo.tlang -log Hello World    
    
    p($1, $2)
    -> Hello World

    p($0)
    -> ['Hello', 'World']


- ### Creating Functions

You can create a function by typing `@s` (s = start), to finish the function you need to type `@e` (e = end) and then the name of the function:
    
    @s Function_name
        p("This is a function in PyTlang")
    @e Function_name

To pass arguments in the function you need to type `$1`, according to how many arguments you have passed that much the number goes up, for control though you can also adjust how many arguments can go through in the square brackets (see example). If you want to see every flag then you can type `$0` (for debug porpuses only):

#### Reminder : if in main the only thing that gets passed is the flags when the program runs.
#### Exception : if you want to access the flags that you passed to the program then you need to explicitely pass them in the function as arguments.

    @s add [2]
        p("the sum of $1 + $2 is", $1 + $2)
    @e add

    @s main
        @add[ 5, 5 ]
    @e main

If you want to return something from the function then you can type it in `r()` (r = return):

    @s add [2]
        r($1 + $2)
    @e add

    @s main
        $var_1 = 5
        $var_2 = 6
        p("The sum of $var_1 + $var2 =", @add[ $var_1, $var_2 ])
    @e main

- ### If statements

`i(state)s` -> starting if
`ie` -> ending if or elif
`ie(state)s` -> continuing if to elif
`es` -> end if or (and) start else clause ONLY if the previous if ended

Syntax:

    @s square_root [1]
        i($1 > 0)s
            r($1**0.5)
        ie($1 == 0)s
            r(0)
        es
            r("Number smaller than one is not permitted")
        ee
    @e square_root

- ### While/For statement

#### While loop use:

`wf(state)s` -> will loop only if the state is true <br>
`wf()e` -> end of while loop

#### For loop use:

Syntax:

    @s factorial  [1]
        $temp = 1
        wf($var = 1, $var < $1)s
            $temp = $temp * $var
        wf($var++)e
        r($temp)
    @e factorial

- ### Math operations

TLang supports

1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Power
6. Remainder
7. Follows Padmas rule if basic equation

- ### Built-in functions
1. length -> len("Demo") used for strings returns a 
2. random -> rand(start, finish) None will be auto to 0 - 100
3. type -> type($var) return the type of the variable

- ### Debugging TLang Code

After you type the file you can also type -log, when you run the program a new file will be created in the working directory with every step that the language takes to run.

    -> python pytlang.py demo.tlang -log

## Contribution

#### WARNING: Code poorly optimized, and written like spaghetti. The reason is because this project was supposed to be small, but accidently made it bigger than envisioned, which led to me writing poor base code in short time. Leading to a mess in the long time. Please understand if I fix any issues considering optimazation or readability is going to happen ONLY because I need the language for a particular use for another project.

You can fork the code and then add your changes, I will later review and merge if deemed necessary.

## Expiremental Features


You might be able to create names for the variables you pass in a function. These new created variables are constants. (Not implemented)

    @s add {$num_1, $num_2}
        p("the sum of $1 + $2 is", $1 + $2)
    @e add -> null

Switch Case: (Not implemented)

    int -> $var = 5
    &switch($var)s
        case(6)s
            p("Saturday")
        case(6)e
        
        case(7)s
            p("Sunday")
        case(7)e

        default|s
            p("Looking forward for the weeknd)
        default|e

    &switch()s

Basic Algebraic equations (Not implemented)

    algebra(5+x=10)
    -> x = 5

    algebra(10-y+5=5, show)
    -> 10-y+5=5 => y = 10

    algebra(5+7*x-2=20, step)
    -> 5+7*x-2=20
    -> Simplify:
    -> 5-2 + 7x = 20
    -> 3 + 7x = 20
    -> Make into teams (found best -> x = nums):
    -> 3 - 3 + 7x = 20 -3
    -> 7x = 17
    -> Remove fraction:
    -> 7x/7 = 17/7
    -> x = 17 / 7 