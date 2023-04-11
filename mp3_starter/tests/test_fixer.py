"""
Author: El Hovik
Version: 10/19/2022

Helper tests for students on the 22fa MP3 (fixer.py).
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
        test_fixer.py
        ... other tests

In your terminal make sure you are in cs1/assignments/mp3/
and then run (in the terminal, not in the >>> interpreter):
pytest tests/test_fixer.py

If you run into an error for a file-not-found, make sure to
double check the instructions above! We are also happy to help
resolve testing questions in OH/Discord.
"""

# Imports the student's tabs_to_spaces function from
# their fixer.py. 
from fixer import tabs_to_spaces


# Helper function for tests
def mock_file_info(filename):
    """
    Mocks a version of the file_info function in an inefficient, but correct
    way for isolating tests in fixer.py without dependence on
    a student's working analyzer.file_info solution. As mentioned
    in class, you shouldn't use f.read(), so you should really just ignore
    this solution (any solution that looks like this will receive 0)... 
    It also returns a tuple, while your file_info should
    return a dictionary.
    """
    with open(filename, 'r') as f:
        text = f.read()
        # (lines, words, chs)
        return (text.count('\n'), len(text.split()), len(text))


def test_tabs_to_spaces_spec_examples(capsys):
    """
    Tests the four examples in the spec:
    - tabs_to_spaces('math_fns.py', 4)
    - tabs_to_spaces('math_fns.py', 2)
        - Adjusting the tab-space amount
    - tabs_to_spaces('two_tab_test.txt', 4)
        - file containing only 2 tab characters ('\t\t\n')
    - tabs_to_spaces('four_tab_test.txt', 4)
        - file containing 4 tab characters across two lines,
          separated by words
    """
    output_template = 'Lines with tabs: {}\nTabs replaced: {}\n'

    # Test 1: Replace math_fns.py '\t' with 4 ' '
    tabs_to_spaces('math_fns.py', 4)
    captured = capsys.readouterr()
    # Expected output values
    lines_changed = 29
    tab_count = 34
    # Compare the print output of the function with the expected
    # If this fails, double-check your print statements in tabs_to_spaces
    assert captured.out == output_template.format(lines_changed, tab_count)

    # Now, use our (inefficient but correct) function to test the contents
    # Each tuple contains (# lines, # words, # characters) in a given file,
    # similar to wc shown in the spec (these would also match the expected
    # _values_ of the _dictionary keys_ returned in your analyzer.file_info
    # function)
    (old_linec, old_wordc, old_chc) = mock_file_info('math_fns.py')
    (new_linec, new_wordc, new_chc) = mock_file_info('spaced_math_fns.py')

    # Line count should be unchanged
    assert old_linec == new_linec
    # Word count should be unchanged
    assert old_wordc == new_wordc
    # Spaced file should have 4 * tab_count (orig count + orig tabs * 3)
    assert old_chc + tab_count * 3 == new_chc

    # Test 2: Replace math_fns.py '\t' with 2 ' '
    tabs_to_spaces('math_fns.py', 2)
    captured = capsys.readouterr()
    assert captured.out == output_template.format(lines_changed, tab_count)

    # values for 2-space tab replacement
    (new_linec, new_wordc, new_chc) = mock_file_info('spaced_math_fns.py')
    # Line count should be unchanged
    assert old_linec == new_linec
    # Word count should be unchanged 
    assert old_wordc == new_wordc
    # Spaced file should have 2 * tab_count (orig count + orig tabs)
    assert old_chc + tab_count == new_chc

    # file containing only 2 tab characters ('\t\t\n')
    tabs_to_spaces('two_tab_test.txt', 4)
    captured = capsys.readouterr()
    # Expected output values
    lines_changed = 1
    tab_count = 2
    assert captured.out == output_template.format(lines_changed, tab_count)
    # Note: '\t\t\n' is treated as three characters
    (old_linec, old_wordc, old_chc) = (1, 0, 3)
    # values for 2-space tab replacement
    (new_linec, new_wordc, new_chc) = mock_file_info('spaced_two_tab_test.txt')

    # Line count should be unchanged
    assert old_linec == new_linec
    # Word count should be unchanged 
    assert old_wordc == new_wordc
    # Spaced file should have 4 * tab_count (orig count + orig tabs)
    # '\t\t\n' -> '        \n'
    assert old_linec + (4 * tab_count) == new_chc

    # file containing 4 tab characters across two lines,
    # separated by words
    tabs_to_spaces('four_tab_test.txt', 4)
    # Expected output values
    lines_changed = 2
    tab_count = 4
    # Values from $ wc four_tab_test.txt
    (old_linec, old_wordc, old_chc) = (2, 7, 45)

    (new_linec, new_wordc, new_chc) = mock_file_info('spaced_four_tab_test.txt')
    # Line count should be unchanged
    assert old_linec == new_linec
    # Word count should be unchanged
    assert old_wordc == new_wordc
    # Spaced file should have 4 * tab_count (orig count + orig tabs)
    assert old_chc + (3 * tab_count) == new_chc


def test_tabs_to_spaces_edge_cases(capsys):
    """
    Note: This test function will create temporary files to test against some
    edge cases.
    """
    output_template = 'Lines with tabs: {}\nTabs replaced: {}\n'
    tabs_to_spaces('math_fns.py', 2)
    captured = capsys.readouterr()
    with open('one_tab_test.txt', 'w') as f:
        f.write('\t\n')
    f.close()
    tabs_to_spaces('one_tab_test.txt', 20)
    captured = capsys.readouterr()
    lines_changed = 1
    tab_count = 1
    assert captured.out == output_template.format(1, 1)
    spaced20_wc = mock_file_info('spaced_one_tab_test.txt')
    assert spaced20_wc[0] == 1
    assert spaced20_wc[1] == 0
    # 21 = 20 \t + 1 \n
    assert spaced20_wc[2] == 21
    # Removes all tabs (0 spaces), has some inner and trailing \t
    with open('tab0_test.txt', 'w') as f:
        f.write('\tLorem ipsum:\tA good boi...\nLanguage:\tWoof.\t\n')
    f.close()
    tabs_to_spaces('tab0_test.txt', 0)
    captured = capsys.readouterr()
    lines_changed = 2
    tab_count = 4
    assert captured.out == output_template.format(lines_changed, tab_count)
    test_wc = mock_file_info('spaced_tab0_test.txt')
    assert test_wc[0] == 2
    assert test_wc[1] == 5 
    assert test_wc[2] == 41
