"""
Student name: Lea Grohmann

This program contains functions that help generate a program that makes
a file template with function stubs and docstrings.
"""

import os


# Exercise 3.1.
def to_snake_case(s):
    """
    converts a string into snake case seperating words with underscores
    (e.g. "randomString" --> "random_string")

    Arguments:
        `s` (string) - string to be converted to snake case
    
    Return:
        (string) - string in snake case

    """
    new_s_list = []
    i = 0

    for f in range(len(s)):
        if f == 0 or f == len(s) - 1:
            continue
        if s[f].isupper():
            new_s_list.append(s[i:f].lower())
            i = f
    
    new_s_list.append(s[i:].lower())

    return '_'.join(new_s_list)


# Exercise 3.2.
def format_fn_header(name, args):
    """
    Returns a function header based on the function name and arguments of
    the form: "def function_name(arg1, arg2):"

    Arguments:
        `name` (string) - name of function
        `args` (list) - list of strings that represent the arguments of
                        the function
    
    Return:
        (string) - formatted function header
    """
    arguments = ', '.join(args)

    return f'def {to_snake_case(name)}({arguments}):'


# Exercise 3.3.
def generate_args_data():
    """
    Provides functionality to process user input to collect information
    about arguments/parameters in a function template. Repeatedly
    prompts the user to provide argument information until they are done,
    returning a result dict mapping argument name (str) keys to
    a 2-element tuple that stores the type and description of the argument.
    Any variable name that does not adhere to Python snake_case conventions
    is automatically converted to snake_case.

    For example, if a user gives "DNASeq" as an argument name with type of
    "str" and a description of "Sequence of DNA nucleotides." (as the only
    argument), the resulting dictionary would simply be:
    {'dna_seq' : ('str', 'Sequence of DNA nucleotides.')}

    Returns:
            `dict` - mapping of (str) names to (str, str) tuples as described.
    """
    # Initialize an empty dictionary result
    args = {}
    while True:
        arg = input('Add an argument name (<return> for none): ')
        arg = to_snake_case(arg)
        if not arg:
            break
        elif arg in args:
            print(f'There\'s already an argument named {arg}!')
        else:
            arg_type = input(f'What is the expected type of `{arg}`? ')
            if not arg_type:
                arg_type = 'unspecified'

            arg_desc = input(f'Description of `{arg}`: ')
            type_desc = (arg_type, arg_desc)

            args[arg] = type_desc

        # Print a blank line after each argument is specified for formatting
        print()
    return args


# Exercise 3.4.
def generate_return_data():
    """
    Prompts user to input the type and description of the return data. Generates
    and returns return data in a tuple.

    Arguments:
        N/A
    
    Return:
        (tuple) - tuple of strings that contains the return type and the return
        description
    """
    ret_type = ''
    ret_desc = ''
    ret_type = input(f'What is the expected type of the return? ')
    ret_desc = input(f'Description of return: ')
    if not ret_type:
        ret_type = 'unspecified'
    
    return (ret_type, ret_desc)


# Part 3 (Given, requires Exercises 3.1-3.2)
def build_fn_str(fn_name, args, ret, desc):
    """
    Builds a function stub string given arguments.

    Arguments:
        `fn_name` (str) - name of function
        `args` (dict) - mapping of argument name strs to (type, description)
                        str tuples
        `ret` (tuple) - 2-str tuple holding type and description of return
                        (`None` if no return)
        `desc` (str) - description of function for docstring

    Returns:
        (str) - function stub as string with auto-generated docstring
    """
    INDENT = ' ' * 4  # stored as constant in case a user wants to customize it
    # Generate the first line ('def <name>(<args>):' function header)
    first_line = format_fn_header(fn_name, args.keys())
    result = f'{first_line}\n'
    result += f'{INDENT}"""\n'     # Open docstring, start a new line
    result += f'{INDENT}{desc}\n'  # Docstring description

    # Next, add Arguments section if there are any
    if (args):
        result += '\n'
        result += f'{INDENT}Arguments:\n'
        for arg in args:
            (arg_type, arg_desc) = args[arg]
            if arg_desc:
                result += (f'{INDENT * 2}`{arg}` ({arg_type}) - {arg_desc}\n')
            else:
                result += (f'{INDENT * 2}`{arg}` ({arg_type})\n')

    # Next, add Returns section if provided
    if (ret):
        ret_type, ret_desc = ret
        result += '\n'
        result += f'{INDENT}Returns:\n'
        if ret_desc:
            result += (f'{INDENT * 2}({ret_type}) - {ret_desc}\n')
        else:
            result += (f'{INDENT * 2}({ret_type})\n')

    # Finally, close the docstring and add a single pass statement
    # for the function stub string
    result += f'{INDENT}"""\n'
    result += f'{INDENT}pass\n'
    return result


# Part 3 (Given, requires Exercises 3.1-3.4)
def generate_fn(fn_name):
    """
    Generates a function stub string based on user input for
    a function name, any arguments, and any return value.

    Arguments:
        `fn_name` (str) - name of function to generate stub for

    Returns:
        (str) - function stub generated from user input
    """
    # First, prompt user for arguments
    fn_name = to_snake_case(fn_name)
    args = generate_args_data()
    print()
    # Next, prompt for optional return
    has_return = input('Does your function have a return? (y for yes) ')
    has_return = has_return.lower() == 'y'
    ret = ''
    if has_return:
        ret = generate_return_data()

    # Finally, prompt for description to be used function's generated docstring
    desc = input('Finally, provide a description of your function: ')
    fn_stub = build_fn_str(fn_name, args, ret, desc)
    print()

    print(f'Finished generating a function stub for {fn_name}!')
    return fn_stub


# Exercise 3.5.
def save_program(body):
    """
    Creates and saves a file based on the users input for file name and file
    body. Prints a success message once file is created.

    Arguments:
        `body` (string) - body of the file to be created
    
    Returns:
        N/A
    """
    filename = input('What is the name of your file? ')

    while True: 
        if filename == '':
            print('Please provide a non-empty file name, e.g. test.py')

        elif check_rewrite(filename):
            break

        filename = input('What is the name of your file? ')
    
    file = open(filename, 'w')
    file.writelines(body)
    file.close()
    print(f'Successfully wrote to {filename}!')


def check_rewrite(filename):
    """
    Helper function to check if the given `filename` exists, returning
    True if either:
    - The file doesn't exist yet
    - The file does exist, and the user confirms they want to rewrite
    and False otherwise.

    Arguments:
        `filename` (str) - name of file

    Returns:
        (bool)
    """

    if os.path.exists(f'{filename}'):
        
        a = 'Are you sure you want to overwrite? '
        confirm = input('A file is already found with that name. ' + a)
        # True only if they confirm
        return confirm.lower() == 'y'
    return True  # Always return True if the file doesn't exist


# Part 3 (Given, requires Exercises 3.1-3.5)
def generate_program():
    """
    Initializes a program generation feature for users to provide
    information about functions, creating function stubs with docstrings
    and optionally saving the result to a file if the user wants.
    """

    print('First, you\'ll input some function stub data, then have the option')
    print('to save the results to a file!')
    first_line = '"""\nTODO: Author, description\n"""'
    body = first_line
    while True:
        body += '\n\n'  # Two blank lines before each function in Python
        fn_name = input('Please input a new function name (<return> to quit): ')
        if fn_name == '':
            break
        body += generate_fn(fn_name)  # add the next function stub to the body

    print('Finished generating your program template!')
    save_file = input('Do you want to save your program (y for yes)? ')
    if save_file.lower() == 'y':
        save_program(body)
