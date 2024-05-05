# PyTlang

WIP : [TODO](docs/todo.md)

A programming interpreted language created using Python. A fun little project.

To run a script written in tlang you need to type in the terminal:


An interpreted programming language created using Python. A fun little project (do not copy, I made this project without reading how an actual Interpreter works, so everything is created from scratch).

Create a file ending in .tlang

Write the following:

    @s main
        p("Hello world!")
    @e main

To run a script written in PyTlang you need to type in the terminal:

    --> python pytlang.py name_of_file.tlang
    
You can also put `-log` in the end to get a full traceback:

    --> python pytlang.py name_of_file.tlang -log
    
### Other flags include: 

`--version` : to get the version of the interpreter

`--docs` : to get the full documentation of the pseudo-programming language

`--help` : to get help on the flags of the interpreter

`--testing` : unit tests to ensure it interprets correctly


## Documentation:

See the documentation of PyTLang [here](docs/main.md).

## Requirements
1. Python 3.11.4 and later

## Contribution

> ### ⚠️ WARNING: Code poorly optimized, and written like spaghetti. The reason is because this project was supposed to be small, but accidently made it bigger than envisioned, which led to me writing poor base code in short time. Leading to a mess in the long time. Please understand if I fix any issues considering optimazation or readability is going to happen ONLY because I need the language for a particular use for another project.

You can fork the code and then add your changes, I will later review and merge if deemed necessary.

Ideas for contribution:
- Optimization of code.
- Adding more features.
- Make the documentation more readable.
- Fixing spelling issues.