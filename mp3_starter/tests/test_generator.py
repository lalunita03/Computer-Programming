"""
Author: El Hovik
Version: 10/19/2022

Helper tests for students on the 22fa MP3 (generator.py).
These should be used to catch subtle bugs/edge cases; you
_may_ ask how to interpret a test error on Discord/OH; anything
we haven't learned that you see here you don't need to worry about,
but we have provided a few comments to help understand what
each test case is checking.

Note: One of the tests will create temporary files for
edge cases.

To run:

Your directory should look like (after renaming
your unzipped mp3_starter folder to mp3 if you haven't):
mp3/
    analyzer.py
    fixer.py
    generator.py
    tests/
        test_generator.py
        ... other tests

In your terminal make sure you are in cs1/assignments/mp3/
and then run (in the terminal, not in the >>> interpreter):
pytest tests/test_generator.py

If you run into an error for a file-not-found, make sure to
double check the instructions above! We are also happy to help
resolve testing questions in OH/Discord.
"""

# Needed to import all functions from student solutions
# without qualifying for pytest purposes; refer to lecture
# on why import * is ok in this case (but usually not otherwise)
from generator import *
# This added import is a requirement for overriding print/input
# to test output/input on io functions
import generator
import os


# Testing helper functions for file cleanup and input/print overriding.
def delete_test_files():
    """
    Deletes 2 test files when testing Exercise 5: save_program to reset
    directory contents when testing different cases (students don't need
    to handle file-not-found cases, but can if they want).
    """
    test_files = ['foo_test.py', 'foo_test2.py']
    for filename in test_files:
        if os.path.exists(filename):
            os.remove(filename)


def check_file_contents(filename, body):
    """
    Checks the contents of the given file, asserting that the file
    exists and that its contents match the given body string.

    Arguments:
        - filename (str) - name of file to check
        - body (str) - contents of file to compare against

    Output:
        - AssertionError if conditions are not met
    """
    # Assert that the file exists
    assert os.path.exists(filename)
    with open(filename, 'r') as f:
        assert f.read() == body


# ------------------------------------------------------------
# generator.py Tests
# ------------------------------------------------------------
# Exercise 3.1
def test_to_snake_case():
    # snek_case unchanged
    assert to_snake_case('snek_case') == 'snek_case'
    # Java... Classic.
    assert to_snake_case('camelCase') == 'camel_case'
    # starting uppercase ch P should be lowercase, middle uppercase ch C should be _c
    assert to_snake_case('PascalCase') == 'pascal_case'
    # ignore nums
    assert to_snake_case('removeAll3') == 'remove_all3'
    assert to_snake_case('123') == '123'
    # Caterpillar beats leaf. Python beats caterpillar.
    assert to_snake_case('cAtTeRpIlLaRcAsE') == 'c_at_te_rp_il_la_rc_ase'
    # empty case
    assert to_snake_case('') == ''
    # example from spec
    assert to_snake_case('FooBAR') == 'foo_b_ar'


# Exercise 3.2 Tests: format_fn_header()
def test_format_fn_header():
    # example from spec, 2-fully specified int args
    fn_name = 'dice'
    args = {'n': ('int', 'Number of dice to roll (>= 1)'),
            'm': ('int', 'Number of sides per dice (>= 1)')}
    fn_header = format_fn_header(fn_name, args.keys())
    assert fn_header == 'def dice(n, m):'

    # example from spec, 1 int arg specified, no description
    fn_name = 'factorial'
    args = {'n': ('int', '')}
    fn_header = format_fn_header(fn_name, args.keys())
    assert fn_header == 'def factorial(n):'

    # example from spec, 0 args specified
    # requires to_snake_case to be correct
    fn_name = 'sayHello'
    args = {}
    fn_header = format_fn_header(fn_name, args.keys())
    assert fn_header == 'def say_hello():'


# Exercise 3.3 Tests: gen_args_data()
def gen_args_io_helper(capsys, input_values, prompts, exp_args):
    """
    Helper function for testing gen_args_data() to:
    - override input function with list of tested input_values
    - compare student's input prompts with the list of prompts (in order)
    - check that the returned arguments match that of the `exp_args` dictionary
    """
    # test program assertion, not affected by student code
    assert len(input_values) % 3 == 1
    arg_count = len(input_values) // 3
    # Essentially, this multiplies the 3-line prompts
    # depending on number of expected processed argument
    # in user prompting, then adds the first prompt as the final
    # prompt (when the user quits by giving '')
    prompts = (prompts[:3] * arg_count) + [prompts[0]]
    for i in range(len(input_values)):
        if i % 3 == 0:
            # each time we get a new argument from user, change
            # the expected argument name in subsequent two prompts
            # this argument name should be in snake_case in student
            # code and surrounded by `` as shown in examples
            snake_cased_arg_name = to_snake_case(input_values[i])
        if '{}' in prompts[i]:
            # replace `{}` with snake_cased name when referring
            # to arg in prompt
            prompts[i] = prompts[i].format(snake_cased_arg_name)

    # override user input, capture values
    def mock_input(s):
        print(s, end='')
        next_input = input_values[0]
        del input_values[0]
        return next_input

    # override input function to catch it
    generator.input = mock_input
    args = generate_args_data()
    # Check that the student's function returns the expected dictionary
    # of arguments.
    assert args == exp_args

    out, err = capsys.readouterr()
    # fix new line differences in capsys call
    assert out.replace('\n', '') == ''.join(prompts).replace('\n', '')
    assert err == ''  # no error expected


# Exercise 3.3 testing function
def test_generate_args_data(capsys):
    # Example from spec; 1 round of arg prompts with camelCased fn name
    input_values = ['dnaString', 'str', 'DNA sequence', '']
    prompts = ['Add an argument name (<return> for none): ',
               'What is the expected type of `{}`? ',
               'Description of `{}`: ',
               'Add an argument name (<return> for none): ']
    # generate_args_data should use to_snake_case
    expected_args = {'dna_string': ('str', 'DNA sequence')}
    gen_args_io_helper(capsys, input_values, prompts, expected_args)

    # Testing empty input cases
    input_values = ['']
    expected_args = {}
    gen_args_io_helper(capsys, input_values, prompts, expected_args)

    # Testing 2 rounds of fully-specified inputs
    input_values = ['dnaString', 'str', 'DNA sequence', 'base', 'str',
                    'Single-character nucleotide base', '']
    expected_args = {'dna_string': ('str', 'DNA sequence'),
                     'base': ('str', 'Single-character nucleotide base')}
    gen_args_io_helper(capsys, input_values, prompts, expected_args)

    # Testing 1 round of provided arg name with no type/desc
    input_values = ['n', '', '', '']
    # Empty type -> 'unspecified', empty description -> ''
    expected_args = {'n': ('unspecified', '')}
    gen_args_io_helper(capsys, input_values, prompts, expected_args)


# Exercise 3.4 Tests: gen_ret_io_helper()
# This could be refactored bit, but WIP duties call...
def gen_ret_io_helper(capsys, input_values, prompts, expected_ret):
    """
      Helper function for testing gen_args_data() to:
    - override input function with list of tested input_values
    - compare student's input prompts with the list of prompts (in order)
    - check that the returned arguments match that of the `expected_ret` tuple
    """
    assert len(input_values) % 2 == 0

    # override user input, capture values
    def mock_input(s):
        print(s, end='')
        next_input = input_values[0]
        del input_values[0]
        return next_input

    # override input function to catch it
    generator.input = mock_input
    ret_data = generate_return_data()
    # Check that the student returns the expected (type, desc) tuple
    assert ret_data == expected_ret

    out, err = capsys.readouterr()
    # fix new line differences in capsys call
    assert out.replace('\n', '') == ''.join(prompts).replace('\n', '')
    assert err == ''  # no error expected


# Exercise 3.4 testing function
def test_generate_return_data(capsys):
    # These prompts don't use any previous input (different than B.5.)
    prompts = ['What is the expected type of the return? ',
               'Description of return: ']

    # Testing fully-specified return
    # inputs = [<type>, <desc>]
    inputs = ['float', 'Percentage of `base` in `dna_string` (0.0 to 100.0).']
    gen_ret_io_helper(capsys, inputs, prompts, tuple(inputs))
    # Testing return with only type specified (empty desc -> '')
    inputs = ['float', '']
    gen_ret_io_helper(capsys, inputs, prompts, ('float', ''))
    # Testing return with unspecified type and desc
    # (empty type -> 'unspecified')
    inputs = ['', '']
    gen_ret_io_helper(capsys, inputs, prompts, ('unspecified', ''))
    # Testing with unspecified type, specified description
    inputs = ['', 'Who knows...']
    gen_ret_io_helper(capsys, inputs, prompts, ('unspecified', 'Who knows...'))


# Exercise 3.G: Given (should be unchanged)
def test_build_fn_str():
    # Testing dice example from spec
    fn_name = 'dice'
    args = {'n': ('int', 'Number of dice to roll (>= 1)'),
            'm': ('int', 'Number of sides per dice (>= 1)')}
    ret_data = ('int', 'Sum of `n` randomly-rolled `m`-sided dice.')
    fn_desc = 'Simulates `n` randomly-rolled `m`-sided dice, returning the sum of all rolls.'
    output = []
    # Override output for testing print statements
    generator.print = lambda s='': output.append(s + '\n')
    student_result = build_fn_str(fn_name, args, ret_data, fn_desc)
    expected_fn_stub = '' + \
"""def dice(n, m):
    \"\"\"
    Simulates `n` randomly-rolled `m`-sided dice, returning the sum of all rolls.

    Arguments:
        `n` (int) - Number of dice to roll (>= 1)
        `m` (int) - Number of sides per dice (>= 1)

    Returns:
        (int) - Sum of `n` randomly-rolled `m`-sided dice.
    \"\"\"
    pass
"""
    assert expected_fn_stub == student_result

    # Testing foobar example from spec; -1 for sad docstring :(
    fn_name = 'FooBAR'
    args = {'c_at_er_pi_ll_ar': ('unspecified', '')}
    ret_data = ('dict', '')
    fn_desc = 'Who knows...'

    expected_fn_stub = '' + \
    """def foo_b_ar(c_at_er_pi_ll_ar):
    \"\"\"
    Who knows...

    Arguments:
        `c_at_er_pi_ll_ar` (unspecified)

    Returns:
        (dict)
    \"\"\"
    pass
"""
    output = []
    student_result = build_fn_str(fn_name, args, ret_data, fn_desc)
    assert expected_fn_stub == student_result


# Exercise 3.5 Tests: save_program()
def save_program_io_helper(capsys, test_body, input_values, prompts):
    num_inputs = len(input_values)
    output = []
    generator.print = lambda s='': output.append(s + '\n')
    assert num_inputs >= 1 and num_inputs <= 3
    file_name = input_values[0]

    # override user input, capture values
    def mock_input(s):
        print(s, end='')
        next_input = input_values[0]
        del input_values[0]
        return next_input

    # override input function to catch it
    generator.input = mock_input
    test_ret = save_program(test_body)
    assert test_ret is None

    out, err = capsys.readouterr()
    # fix new line differences in capsys call
    out = out.split('\n')
    assert out[0].startswith(prompts[0].format(file_name))
    expected_output = "Successfully wrote to {}!\n"
    if num_inputs == 1:
        assert output[0] == expected_output.format(file_name)
    elif num_inputs == 2:
        assert out[0] == ''.join(prompts)
        assert output[0] == expected_output.format(file_name)

    assert err == ''  # no error expected


# Test function for save_program() (ignoring optional confirmation feature)
def test_save_program(capsys):
    # Test 1: Testing the example from the spec when saving a program body
    # to a a new file called foo_test.py
    delete_test_files()
    body = '"""TODO: File header"""\n\ndef foo():\n    pass\n\n'
    prompts = ['What is the name of your file? ']
    save_program_io_helper(capsys, body, ['foo_test.py'], prompts)
    check_file_contents('foo_test.py', body)


# Additional tests provided if student wants to check their optional
# confirmation feature
def test_save_program_confirmation_optional(capsys):
    # Test 2 (Optional): Testing the example from the spec for a confirmation
    # when a user overwrites a file.
    delete_test_files()
    with open('foo_test.py', 'w') as f:
        f.write('Some contents\n')

    body = '"""TODO: File header"""\n\ndef foo():\n    pass\n\n'
    prompts = ['What is the name of your file? ',
               'A file is already found with that name. Are you sure you want to overwrite? ']
    save_program_io_helper(capsys, body, ['foo_test.py', 'y'], prompts)
    check_file_contents('foo_test.py', body)

    delete_test_files()
    with open('foo_test.py', 'w') as f:
        f.write('Some contents\n')

    body = '"""TODO: File header"""\n\ndef foo():\n    pass\n\n'
    prompts = ['What is the name of your file? ',
               'A file is already found with that name. Are you sure you want to overwrite? ',
               'What is the name of your file? ']
    save_program_io_helper(capsys, body, ['foo_test.py', 'n', 'foo_test2.py'], prompts)
    check_file_contents('foo_test.py', 'Some contents\n')
    check_file_contents('foo_test2.py', body)
