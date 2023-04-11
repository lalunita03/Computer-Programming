"""
Student name: Lea Grohmann

This module analyzes the content and statistics of files.
"""


import os


# Exercise 1.1.
def print_fns(filename):
    """""
    Given a filename, outputs a report of any defined functions in the
    corresponding file, where a function must be defined as a valid Python
    function statement line starting with "def ".

    For example, a program containing a single function "def foo(x, y):"
    would correspond to

    foo(x, y)

    in one line of the output. Prints an error if the filename isn't found.

    Arguments:
        - `filename` (str) - name of file to analyze.

    Returns:
        - `None`
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    else:
        print(f'Functions in {filename}: ')
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            if line.startswith('def '):
                line = line.replace('def ', '    ')
                line = line.replace(':', '')
                print(line)
        file.close()


# Exercise 1.2.
def file_info(filename):
    """
    Given a filename, analyzes the contents of the file, returning a
    dictionary with the following keys:
    - 'words' (word count of file)
    - 'lines' (line count of file)
    - 'characters' (character count of file, including '\n' characters)

    Supports any file extension, and prints an error message if the file
    isn't found.

    Arguments:
        - `filename` (str) - Name of file to analyze

    Returns:
        - (dict) - dictionary of three str keys having int count values
                   (or `None` if filename is invalid)

    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')

    else:
        file = open(filename, 'r')
        dictionary = {'lines': 0, 'words': 0, 'characters': 0}

        for line in file:
            words = line.split()
            dictionary['lines'] += 1
            dictionary['words'] += len(words)
            dictionary['characters'] += len(line)
        
        file.close()
        return dictionary
