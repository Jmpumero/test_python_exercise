# Exercise:

    The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

    The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

## Example :

    INPUT
    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

    OUTPUT:
    ASTRID-RENE: 2
    ASTRID-ANDRES: 3
    RENE-ANDRES: 2

# Environment:

    python 3.9.5

    to run the program you must install python version 3.9 or higher, open a terminal in the directory where you find the files: main.py,lib.py and example.txt. in the terminal run the command  ```python main.py```

# Solution:

    For this exercise in very general terms consists of comparing the time range of each employee (by traversing the employee list) and accounting for each occurrence.

# Architecture:

Based on a modular design it is divided in 3 main files: main.py, lib.py and example.txt.

### main.py:

    It is the main file or input file of the program, in it is the call to the main function that later will call the functions defined in the lib.py file for the solution of the problem.

### lib.py:

    this file contains the definitions of the functions necessary for the solution of the exercise such as: processing the data coming from the file, creating the data structures, time conversion, etc. The functions defined in this file will be imported and later used in the main.py file.

### example.txt:

    this file contains the program input data in the format established in the exercise example; this file will be processed by the main program.

# Approach:

    for this exercise I focus on two key points;

### first:

    The reading and processing of data: This point start with the reading of the file and make the corresponding character manipulations to build a data structure (in this case an object containing lists of objects) based on each line (string) of the file in order to make a conversion of the times, define and give structure to the information obtained.

### second:

        Data traversal and comparison: Once the entire file was read and the data was stored in a well-defined structure, we proceeded to run through this structure to make the corresponding comparisons between each employee. Using two for cycles, the external one which goes through the employees and the internal one which goes through the schedule of each employee, for the comparison of the schedule ranges I approached it in the following way supported by this drawing:

A1=.....|**\_**|................|******\_\_******|
A2=.|\_|......|\_**\_|.....|\_\_\_**|.........|**_|............|_**|

min1<=max2 and max1>=min2 then is a valid range

and add some validation
