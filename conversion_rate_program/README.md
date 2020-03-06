# Conversion Rate Program

## Project Scope
This program was written to fulfill Lab 2, 3, 4, and 5 assignments for the course *COSC 1336: Fundamentals of Programming*. Lab 2 corresponds to [Learning Module 2](https://github.com/emnharris/COSC-1336/wiki/2.-Input,-Processing,-and-Output), which introduces variables, math operations, data output, and formatting. Lab 3 corresponds to [Learning Module 3](https://github.com/emnharris/COSC-1336/wiki/3.-Decision-Structures-and-Boolean-Logic), which builds on Module 2 by introducing `if-elif-else` statements and logical operators. Lab 4 corresponds to [Learning Module 4](https://github.com/emnharris/COSC-1336/wiki/4.-Repetition-Structures), which introduces repetitive structures, `while` and `for` loops. Lab 5 (parts 1 and 2) corresponds to [Learning Module 5](https://github.com/emnharris/COSC-1336/wiki/5.-Functions), which introduces functions and modules.

### Limitations
Because Learning Modules 2, 3, and 4 introduce the most basic Python skills, intial versions of this program were intentionally designed to use very simple statements and have limited functionality. For example, in Lab 3 students were instructed to force the program to fail rather than prompt a user for new data should the input data not be validated. This instruction was modified in Lab 4 to allow the user up to three attempts using invalid data before termination. Part 1 of Lab 5 introduced functions, which allowed for a cleaner program, but students were still limited to very basic applications (e.g., value-returning functions were not allowed). Part 2 of Lab 5 finally allowed for value-returning functions.

The conversions were also limited to five different calculations, and the user was to have no choice but to run all 5 calculations every time, rather than selecting the desired conversion. The program could not be rerun even if the user had more data they wanted to convert. Additionally, the program had to use imprecise conversion rates and specific thresholds for data validation as provided by the instructor. No data validation was to be put in place should the user input a string rather than a number, causing the program to fail in this circumstance.

### Branches
The branch **felipe_torture** was added to differentiate programs that were adjusted after taking into account critiques from software engineer [@felipe-lee](https://github.com/felipe-lee). These programs are branched rather than merged (for the time being), because they change the program in ways that tighten the logic/syntax of the program, implement standards that students were not instructed to use, and/or complexify the program past the level required of the lab assignments.

### Future Plans
As my Python skills progress, I may revisit this program and continue to expand its functionality past the requirements of the lab assignments. Higher-level goals for this program include implementing a method for choosing which calculation to perform and allowing the user to continue to run the program, building some kind of GUI, and adding the option to convert USD ($) to GBP (£) using the latest conversion rates scraped from the internet or fetched via API.

## Set Up
Because *COSC 1336: Fundamentals of Programming* is an introductory course to programming, the program was written purely with Python  and is meant to be run from the terminal without any further set up required.

If you are unfamiliar with running programs from the terminal, read [these directions](https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs) for Windows, Mac, and Linux. If you have Python IDLE installed, you can open the program file and run from there. If you have an enhanced text editor such as Visual Studio Code, you can run from a terminal within such editors.

Please note that if you run versions of this program committed after 20 October 2019, you will need to make sure you have downloaded the `convert` module (see [Repo Descriptions](https://github.com/emnharris/COSC-1336/tree/master/conversion_rate_program#repo-file-descriptions)). Save this module in the same place as the program file, and the Python interpreter should be able to read and import the module automatically.

## Repo File Descriptions
- Lab 2 entailed creating a simple conversion rate program ([Lab_2_instructions.pdf](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/Lab_2_instructions.pdf)). 
- Lab 3 built upon the same program by adding simple data validation ([Lab_3_instructions.pdf](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/Lab_3_instructions.pdf)).
- Lab 4 built further on the same program by adjusting the data validation to loop 3 attempts before terminating the program ([Lab_4_instructions.pdf](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/Lab_4_instructions.pdf)).
- Lab 5 (part 1) restructured the program by splitting many of its subtasks into functions. ([Lab_5_instructions.pdf](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/Lab_5_instructions.pdf)).
- Lab 5 (part 2) exported the functions into a `convert` module ([convert.py](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/convert.py)).
- The conversion program itself has been committed as one file ([conversion_rate_program.py](https://github.com/emnharris/COSC-1336/blob/master/conversion_rate_program/conversion_rate_program.py)).
