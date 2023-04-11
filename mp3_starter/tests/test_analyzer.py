"""
Author: El Hovik
Version: 10/19/2022

Helper tests for students on the 22fa MP3 (analyzer.py).
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
        test_analyzer.py
        ... other tests

In your terminal make sure you are in cs1/assignments/mp3/
and then run (in the terminal, not in the >>> interpreter):
pytest tests/test_analyzer.py

If you run into an error for a file-not-found, make sure to
double check the instructions above! We are also happy to help
resolve testing questions in OH/Discord.
"""

# Needed to import all functions from student solutions
# without qualifying for pytest purposes; refer to lecture
# on why import * is ok in this case (but usually not otherwise)
from analyzer import print_fns, file_info
# This added import is a requirement for overriding print/input
# to test output/input on io functions


# Exercise 1.1
def test_print_fns(capsys):
    output_template = 'Functions in {}:'

    print_fns('tests/sample_files/math_fns.py')
    captured = capsys.readouterr().out
    captured = captured.rstrip()
    lines = captured.split('\n')
    # Leniency in whether a student has an extra space after :
    header = lines[0].rstrip()
    # Functions in math_fns.py:
    #     average(x, y)
    #     print_intro()
    #     start()
    assert header == output_template.format('tests/sample_files/math_fns.py')
    # Each function should be listed in order they are declared
    # in the program, indented by 4 spaces and without the trailing :
    assert lines[1] == '    average(x, y)'
    assert lines[2] == '    print_intro()'
    assert lines[3] == '    start()'

    # Ensure only header and three functions printed
    assert len(lines) == 4

    # Testing against spec's dice_example.py
    print_fns('tests/sample_files/dice_example.py')
    captured = capsys.readouterr().out
    captured = captured.rstrip()

    lines = captured.split('\n')
    # Leniency in whether a student has an extra space after :
    header = lines[0].rstrip()
    # Functions in dice_example.py: 
    #     dice(n, m)
    assert header == output_template.format('tests/sample_files/dice_example.py')
    # Ensure only header and one function printed
    assert len(lines) == 2  
    assert lines[1] == '    dice(n, m)'


# Exercise 1.1 Extra test cases
def test_print_fns_extra_cases(capsys):
    """
    Additional test suite to test against some lecture code,
    1 of which has no functions (lec02_code.py), and two of
    which have functions mixed with non-function code. 
    """
    output_template = 'Functions in {}:'
    # Example of .py program with 0 functions
    print_fns('tests/sample_files/lec02_code.py')
    captured = capsys.readouterr().out
    captured = captured.rstrip()
    lines = captured.split('\n')

    # Leniency in whether a student has an extra space after :
    header = lines[0].rstrip()
    # Functions in lec02_code.py:
    assert header == output_template.format('tests/sample_files/lec02_code.py')
    # No other print statements expected
    assert len(lines) == 1  

    # Example of .py program with 2 functions
    print_fns('tests/sample_files/lec03_fns.py')
    captured = capsys.readouterr().out
    captured = captured.rstrip()
    lines = captured.split('\n')

    # Leniency in whether a student has an extra space after :
    header = lines[0].rstrip()

    # Functions in lec03_fns.py:
    assert header == output_template.format('tests/sample_files/lec03_fns.py')

    # Leniency in whether a student has an extra space after :
    # Each function should be listed in order they are declared
    # in the program, indented by 4 spaces and without the trailing :
    assert lines[1] == '    say_hello(name)'
    assert lines[2] == '    f(x, y)'
    # Ensure only header and 2 functions printed
    assert len(lines) == 3

    # Example of .py program with 4 functions, one of which is 0-arguments
    print_fns('tests/sample_files/lec05_practice.py')
    captured = capsys.readouterr().out
    captured = captured.rstrip()
    lines = captured.split('\n')

    header = lines[0].rstrip()
    # Functions in lec05_practice.py:
    #     get_median(lst)
    #     get_range(lst)
    #     vowel_count(s)
    #     generate_lst()
    assert header == output_template.format('tests/sample_files/lec05_practice.py')
    assert lines[1] == '    get_median(lst)'
    assert lines[2] == '    get_range(lst)'
    assert lines[3] == '    vowel_count(s)'
    assert lines[4] == '    generate_list()'
    # Ensure only header and 4 functions printed
    assert len(lines) == 5


# Exercise 1.2
def test_file_info():
    assert file_info('tests/sample_files/rooter.txt') == \
        {'lines': 238, 'words': 2371, 'characters': 15381}
    assert file_info('tests/sample_files/hamlet.txt') == \
        {'lines': 7996, 'words': 32006, 'characters': 197341}
    assert file_info('tests/sample_files/babbage_tabbed.txt') == \
        {'lines': 154, 'words': 1159, 'characters': 7435}
    # note that this provided program has \t characters
    assert file_info('tests/sample_files/math_fns.py') == \
        {'lines': 48, 'words': 173, 'characters': 1090}
    # 2 \t characters on one line + 1 ending \n == \
    assert file_info('tests/sample_files/two_tab_test.txt') == \
        {'lines': 1, 'words': 0, 'characters': 3}
    assert file_info('tests/sample_files/four_tab_test.txt') == \
        {'lines': 2, 'words': 7, 'characters': 45}
    # Empty file case
    assert file_info('tests/sample_files/empty_file.txt') == \
        {'lines': 0, 'words': 0, 'characters': 0}


