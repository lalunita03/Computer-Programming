"""
Author: El Hovik
CS 1 22fa
Version: 11/01/22

Tests for MP4 Grading.

Students can ask on Discord if they have questions about test
results, but also double-check against spec examples and refer
to comments in respective test functions.

For any tests that require earlier functions to work, the requirements
are noted above the test function in an # comment.
"""

# Needed to import all functions from student solutions
# without qualifying for pytest purposes; refer to lecture
# on why import * is ok in this case (but usually not otherwise)
from mp4_pokemon import *
# This added import is a requirement for overriding print/input
# to test output/input on io functions
import mp4_pokemon
# Needed for mock
import builtins


# It's generally poor practice to use global variables like this,
# but this is ok for testing to avoid re-implementing a local
# mock_input function. Some test functions will reset this
# global to test different input value cases shown in the spec/
# edge cases.
input_values = []


# Helper functions for tests
def mock_input(s):
    """
    Overrides the built-in input function to keep track of
    input values for functions that take user input.
    """
    print(s, end='')
    next_input = input_values[0]
    del input_values[0]
    return next_input


# mock the input
mp4_pokemon.input = mock_input


def copy_file(infile, outfile):
    """
    Helper function to copy test files in order to retain
    contents of compare files. `infile` must be a valid filename.
    `outfile` is overwritten if it already exists.

    Arguments:
        - `infile` (str): name of input file to copy from
        - `outfile` (str): name of output file to copy to

    Returns:
        - None
    """
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            for line in fin:
                fout.write(line)


def distance(s1, s2):
    """
    Returns 0 if s1 and s2 match without leading/trailing spaces,
    otherwise 3 (> 1). Used to add leniency for minor typos in output.
    """
    if s1.strip() == s2.strip():
        return 0
    else:
        return 2  # hack for quick fix without levenshtein


# An additional test to help catch spec requirements for students
# It is not extensive, but students should fix anything they see if it
# violates a requirement in the spec.
def test_additional_requirements():
    with open('mp4_pokemon.py') as f:
        imports = 0
        line_num = 1
        for line in f:
            # Should not have any collected_example.csv remaining in
            # final submission (all should be changed to collected.csv)
            assert 'collected_example' not in line
            if '151' in line:
                # 151 should not be hard-coded anywhere, unless it is from
                # the docstring in display_pokedex
                assert '#151: Mew (Psychic)' in line

            # debugging print statements should not be left in
            assert not line.startswith('print(')
            if line.lstrip().startswith('#'):
                assert 'print(' not in line

            # should not use read() or readlines()
            assert 'read()' not in line
            assert 'readlines()' not in line
            if 'import ' in line:
                imports += 1
            line_num += 1
        # should not change imports provided
        assert imports == 3


# Exercise 1.a.
def test_load_data(capsys):
    # Tests load_data using examples from spec
    # copy in case function incorrectly changes the contents
    copy_file('pts_mini.csv', 'pts_mini_copy.csv')
    rows = load_data('pts_mini_copy.csv')
    assert rows == [{'x': '0', 'y': '1'}, {'x': '2', 'y': '-1'}]

    # copy in case function incorrectly changes the contents
    copy_file('moves.csv', 'moves_copy.csv')
    rows = load_data('moves_copy.csv')
    assert rows[0] == {'name': 'Energy Ball', 'type': 'Grass',
                       'accuracy': '1', 'dp': '90', 'buff': '', 'buff_amt': ''}
    assert len(rows) == 156
    assert rows[155] == {'name': 'Poison Fang', 'type': 'Poison',
                         'accuracy': '1', 'dp': '50', 'buff': '', 'buff_amt': ''}

    rows = load_data('missing_file.csv')
    out, err = capsys.readouterr()
    # Expects error message in output.
    assert out.strip() == 'missing_file.csv not found. Aborting.'
    assert err == ''
    # Either None or [] will be accepted in error case.
    assert rows is None or rows == []


# Exercise 1.b.
def test_clear_data(capsys):
    # Tests clear_data examples from spec
    copy_file('pts_mini.csv', 'pts_mini_copy.csv')
    ret = clear_data('pts_mini_copy.csv')
    # clear_data should not return anything
    assert ret is None
    out, err = capsys.readouterr()
    # Test success case
    assert out.strip() == 'pts_mini_copy.csv data successfully cleared!'

    clear_data('missing_file.csv')
    out, err = capsys.readouterr()
    # Test error case
    assert out.strip() == 'missing_file.csv not found. Aborting.'


# Exercise 2.a.
# Requires 1.a. load_data to be correct
def test_load_pokedex(mocker):
    # Make a copy of pokedex.csv just in case the original changes
    # (it shouldn't)
    copy_file('pokedex.csv', 'pokedex_copy.csv')
    pokedex = load_data('pokedex.csv')

    # spy on load_data; this should be called once in load_pokedex!
    spy1 = mocker.spy(mp4_pokemon, 'load_data')
    test_pokedex = load_pokedex()
    # load_data should be called exactly once
    assert spy1.call_count == 1
    # load_pokedex and load_data('pokedex') both do the same thing (hint!)
    assert pokedex == test_pokedex

    # Confirm that they didn't change contents of pokedex.csv
    assert pokedex == load_data('pokedex.csv')

    # Test cases from spec
    # load_pokedex should be a list of dictionaries
    assert isinstance(pokedex, list)
    # Normally, we don't hard-code numbers. But for testing with an expected
    # value, it's ok and this helps catch off-by-one bugs in load_pokedex
    assert len(pokedex) == 151

    first_pokemon = pokedex[0]
    # first Pokemon in result list should be a dict
    assert isinstance(first_pokemon, dict)
    assert first_pokemon['name'] == 'Bulbasaur'
    # 11 columns in pokedex.csv, so 11 keys in each row dict
    assert len(first_pokemon.keys()) == 11

    # Last case
    assert pokedex[150]['name'] == 'Mew'
    assert int(pokedex[150]['pid']) == 151

    # Revert in case they changed pokedex.csv so other tests don't fail
    copy_file('pokedex_copy.csv', 'pokedex.csv')


# Exercise 2.b.
# Requires 1.a. load_data to be correct
def test_load_collected(mocker):
    # Make a copy of collected_example.csv just in case the original changes
    # (it shouldn't) and reset collected.csv for testing purposes
    copy_file('collected_example.csv', 'collected.csv')
    copy_file('collected_example.csv', 'collected_example_copy.csv')
    collected = load_data('collected_example.csv')
    # spy on load_data; this should be called once in load_collected!
    spy1 = mocker.spy(mp4_pokemon, 'load_data')
    test_collected = load_collected()
    assert spy1.call_count == 1

    assert collected == test_collected
    # Confirm that they didn't change collected.csv
    assert collected == load_data('collected.csv')
    # Confirm that they didn't change collected_example.csv
    assert collected == load_data('collected_example.csv')

    # Test cases from spec
    # load_collected should return a list of dictionaries
    assert isinstance(collected, list)
    # 4 rows in the example collected dataset that was copied
    # from collected_example.csv
    assert len(collected) == 4

    # First Pokemon case (remember that a cid of 1 represents the first
    # row in the collected.csv dataset, not the pid)
    first_cid = 1
    first_collected = collected[first_cid - 1]

    assert first_collected['name'] == 'Pikachu'
    assert int(first_collected['pid']) == 25

    # 7 columns in COLLECTED_COLUMNS/collected.csv
    assert len(first_collected.keys()) == 7
    # Revert in case they changed collected.csv
    copy_file('collected_example_copy.csv', 'collected_example.csv')
    copy_file('collected_example_copy.csv', 'collected.csv')


# Exercise 3.a.
# Requires load_data() to work.
def test_display_pokedex(mocker):
    output = []
    # Override output for testing print statements
    mp4_pokemon.print = lambda s='': output.append(s)
    pokedex = load_data('pokedex.csv')

    # A few quick assertions to catch a broken load_data dependency
    assert isinstance(pokedex, list)
    assert isinstance(pokedex[0], dict)
    assert len(pokedex) == 151

    # The student should not be using load_data or load_pokedex in
    # display_pokedex
    spy1 = mocker.spy(mp4_pokemon, 'load_data')
    spy2 = mocker.spy(mp4_pokemon, 'load_pokedex')

    ret = display_pokedex(pokedex)
    # Should _not_ call load_data
    assert spy1.call_count == 0
    # Should _not_ call load_pokedex
    assert spy2.call_count == 0
    # display_pokedex shouldn't have any return
    assert ret is None

    assert len(output) == 154  # 3 for header + 151 pokemon
    assert 'Bulbasaur' in output[3]  # Test that pokemon name is in output
    assert 'Grass' in output[3]  # Test that type is in output
    assert '1' in output[3]  # test that cid is correct
    # The rest test for exact expected outputs indicated in spec
    assert output[3] == '#1: Bulbasaur (Grass)'
    assert output[4] == '#2: Ivysaur (Grass)'
    # Last line case
    assert output[153] == '#151: Mew (Psychic)'


# Exercise 3.b.
# Requires load_data() to work.
def test_display_collected(mocker):
    # Make a copy of collected_example.csv just in case the original changes
    # (it shouldn't) and reset collected.csv for testing purposes
    copy_file('collected_example.csv', 'collected.csv')
    copy_file('collected.csv', 'collected_copy.csv')
    # Override output for testing print statements
    output = []
    mp4_pokemon.print = lambda s='': output.append(s)
    collected = load_data('collected.csv')

    # The student should not be using load_data or load_collected in
    # display_collected
    spy1 = mocker.spy(mp4_pokemon, 'load_data')
    spy2 = mocker.spy(mp4_pokemon, 'load_collected')

    # A few quick assertions to catch a broken load_collected dependency
    assert isinstance(collected, list)
    assert len(collected) > 0
    assert isinstance(collected[0], dict)

    ret_test = display_collected(collected)

    # Should _not_ call load_data
    assert spy1.call_count == 0
    # Should _not_ call load_collected
    assert spy2.call_count == 0

    # Should not have any return
    assert ret_test is None

    assert len(output) == 7 # 3 for header + 4 pokemon in example dataset
    for i, s in enumerate(output):  # leniency here in first few lines
        if 'Pikachu' in s:
            output = output[i:]

    assert 'Pikachu' in output[0]  # Test that pokemon name is in output
    assert 'Sparky' in output[0]  # Test nickname is in output
    assert '"Sparky"' in output[0]  # Test nickname is in quotes
    assert '1' in output[0]  # test that cid is correct
    # The rest test for exact expected outputs
    assert output[0] == '1: Pikachu "Sparky" (Electric)'
    assert output[1] == '2: Magikarp "Finny" (Water)'
    assert output[2] == '3: Mew "Mu" (Psychic)'
    assert output[3] == '4: Paras "PARAS" (Bug)'
    # restore just in case student  modifies (they shouldn't)
    copy_file('collected_example.csv', 'collected.csv')


# Exercise 4.
# Requires load_data correct
def test_add_pokemon(capsys, mocker):
    # Reset contents of collected.csv using 4-Pokemon test collection
    copy_file('collected_example.csv', 'collected.csv')

    # Test example from demo
    pokedex = load_data('pokedex.csv')
    collected = load_data('collected.csv')
    global input_values

    # First case: Use inputs 'y' to nickname prompt,
    # then gives 'Bulby' as nickname
    input_values = ['y', 'Bulby']

    # spy on open; should be called exactly once with 'a'
    spy1 = mocker.spy(builtins, 'open')

    # Get Bulbasaur's pokedex.csv data
    new_pokemon = pokedex[0]  # Bulbasaur row dict

    # Add a Bulbasaur to the collection using student's add_pokemon
    # add_pokemon should take a dict as the argument
    test_ret = add_pokemon(new_pokemon)

    # either are fine, both are equivalent
    assert spy1.called_once_with('collected.csv', 'a') or \
           spy1.called_once_with('collected.csv', mode='a')

    # add_pokemon should not return anything
    assert test_ret is None

    # Let's see if Bulby was successfully added
    bulby_added = load_data('collected.csv')

    # Updated collection should have one more row compared to original
    assert len(collected) == len(bulby_added) - 1
    # The row dicts preceding the added bulbasaur should match that of
    # the original 4-Pokemon collected dataset
    assert collected == bulby_added[:-1]
    assert bulby_added[-1] == {'hp': '200', 'pid': '1',
                               'level': '5', 'name': 'Bulbasaur', 'nickname': 'Bulby',
                               'type': 'Grass', 'weakness': 'Fire'}
    # Two new pokemon, both with same pokedex id (pid) (for test case, pid of 1
    # for Bulbasaur)
    prompts = ['Do you want to give a name to your new Bulbasaur (y for yes)? ',
               'What nickname do you want to give? ']
    out, err = capsys.readouterr()
    if '\n' in out:
        out = out.split('\n')
        prompt_lines = ''.join(out)
    else:
        prompt_lines = out

    # First, check correctness of prompt_lines; these compare the input prompts
    # with the expected ones
    expected_prompts = ''.join(prompts)

    # Small leniency
    assert distance(prompt_lines, expected_prompts) <= 2

    # Case 2: user chooses 'n' for rename; sometimes the decision paralysis is
    # too real.
    input_values = ['n']
    new_pokemon = pokedex[0]  # Another Bulbasaur! Will we get an egg...?
    add_pokemon(new_pokemon)

    bulbasaur_added = load_data('collected.csv')
    # nickname should default to name (Bulbasaur) upper-cased (BULBASAUR)
    assert bulbasaur_added[-1] == {'hp': '200', 'pid': '1',
                                   'level': '5', 'name': 'Bulbasaur',
                                   'nickname': 'BULBASAUR',
                                   'type': 'Grass', 'weakness': 'Fire'}

    # Two bulbasaur rows should have been added so far
    assert len(collected) == len(bulbasaur_added) - 2

    out, err = capsys.readouterr()
    assert out == prompts[0]

    # reset collected.csv
    copy_file('collected_copy.csv', 'collected.csv')

    # More examples from spec
    pikachu_pid = 25
    pikachu = pokedex[pikachu_pid - 1]
    input_values = ['y', 'Sparkster']
    add_pokemon(pikachu)

    # Replace 'Bulbasaur' from test prompt above to Pikachu now
    prompts[0] = prompts[0].replace('Bulbasaur', 'Pikachu')
    out, err = capsys.readouterr()
    assert out == ''.join(prompts)

    # Reload the collected dataset (it was reset for this test case)
    collected = load_data('collected.csv')

    # Pikachu should be added to collected
    assert len(collected) == 5

    # The user's inputted nickname should be saved when added to
    # collected
    assert collected[4]['nickname'] == 'Sparkster'

    # Bulbasaur added after Pikachu in add_pokemon spec example
    bulbasaur_pid = 1
    bulbasaur = pokedex[bulbasaur_pid - 1]

    # anything that's not 'y' or 'Y' is considered 'n'
    input_values = ['no']

    # Nickname should now be referring to Bulbasaur
    prompts[0] = prompts[0].replace('Pikachu', 'Bulbasaur')

    # Add the BULBASAUR!
    add_pokemon(bulbasaur)
    out, err = capsys.readouterr()

    assert out == prompts[0]
    collected = load_data('collected.csv')

    # BULBASAUR should be added to collected after Sparkster
    assert len(collected) == 6

    # The user's inputted nickname should be saved when added to
    # collected
    assert collected[5]['nickname'] == 'BULBASAUR'


# Exercise 5.
def test_abandon_pokemon():
    # Reset collected files just in case, save reference
    copy_file('collected_example.csv', 'collected.csv')
    copy_file('collected.csv', 'collected_copy.csv')

    # abandon_pokemon prompts a user for cid values referring to which
    # collected Pokemon they want to abandon
    # The first three cids are invalid
    # The rest will delete first cid, then new first, then second, last left
    global input_values
    input_values = ['-1', '5', '0']

    # Save built-in print to reset after tests
    old_print = print
    mp4_pokemon.print = lambda s='': output.append(s)

    output = []
    # Test the first three invalid values
    for _ in range(3):
        test_ret = abandon_pokemon()  # all should be be errors
        assert test_ret is None
        # Strip off the display lines (3 header + 4 Pokemon)
        output = output[7:]

        # Make sure they have printed something in error-case
        assert len(output) > 0
        assert output.pop(0).startswith('Invalid ')

    # Next, we test for valid cids
    input_values = ['1', '1', '2', '1']

    test_ret = abandon_pokemon()  # Remove first pokemon (cid 1)
    # abandon_pokemon should not return anything
    assert test_ret is None
    output = output[7:]

    # Check that they have printed something in success-case
    # (leniency since only shown in output, but no more than 1 line)
    assert len(output) == 0 or len(output) == 1
    # This hurt.
    if len(output) == 1:
        # 2 character leniency with success message
        assert distance(output.pop(
            0), 'Successfully said goodbye to Pikachu!') <= 2

    abandon_pokemon()
    output = output[6:]
    # optional success message, but no more than 1 line
    assert len(output) == 0 or len(output) == 1

    # Tests that the first removal updated contents correctly
    if len(output) == 1:
        assert distance(output.pop(
            0), 'Successfully said goodbye to Magikarp!') <= 2

    # Test 2nd-to-last case
    abandon_pokemon()
    output = output[5:]
    assert len(output) == 0 or len(output) == 1
    if len(output) == 1:
        assert distance(output.pop(
            0), 'Successfully said goodbye to Paras!') <= 2

    # Test last-Pokemon case; should lead to empty collection and no
    # error
    abandon_pokemon()
    output = output[4:]
    # Make sure they have printed something in only-Pokemon case.
    assert len(output) == 0 or len(output) == 1
    if len(output) == 1:
        assert distance(output.pop(
            0), 'Successfully said goodbye to Mew!') <= 2

    # # reset print and collected.csv
    mp4_pokemon.print = old_print
    # Reset collection
    copy_file('collected_copy.csv', 'collected.csv')


# Exercise 6.
# Requires load_data correct
def test_rename_pokemon(capsys):
    # Reset collected files just in case, save reference
    copy_file('collected_example.csv', 'collected.csv')
    copy_file('collected.csv', 'collected_copy.csv')
    ref_collected = load_data('collected.csv')

    # erroneous cids
    # first pokemon has cid of 1, not 0 and only 4 pokemon in collected.csv
    # so 5 is invalid
    # for i in [-1, 0, 5]:
    #     collected = load_data('collected.csv')
    #     rename_pokemon(i, 'foo', collected)
    #     out = capsys.readouterr().out
    #     out = out.replace('.', '').strip()
    #     # leniency in error message
    #     assert out.startswith('Invalid ')

    # New nicknames to test with
    new_names = ['Sparkster', 'Splash', 'Mu', 'PARAS']
    success_msg = 'Successfully renamed {} to {}!'
    for i, nickname in enumerate(new_names):
        cid = i + 1
        collected = load_data('collected.csv')
        ref_collected = load_data('collected.csv')
        pokemon = ref_collected[i]
        rename_pokemon(cid, nickname, collected)
        out = capsys.readouterr().out.strip()
        # leniency whether old name is interpreted as nickname or name
        assert distance(out, success_msg.format(pokemon['nickname'], nickname)) <= 2 or \
               distance(out, success_msg.format(pokemon['name'], nickname)) <= 2

    # reset collected.csv
    copy_file('collected_copy.csv', 'collected.csv')


# Exercise 7
def test_load_moves(capsys):
    # Make a copy of moves.csv in case their function changes the
    # contents (it shouldn't)
    copy_file('moves.csv', 'moves_copy.csv')
    moves = load_moves()

    # Testing spec examples
    assert len(moves) == 156
    # moves should be a dictionary with str keys and Move values
    assert isinstance(moves, dict)
    # { 'Energy Ball' : Move('Energy Ball', ...), ... }
    ergy_ball = moves['Energy Ball']
    assert isinstance(ergy_ball, Move)

    assert ergy_ball.name == 'Energy Ball'
    # Uses the string representation of Move objects (students should not
    # hard-code this)
    assert str(ergy_ball) == 'Energy Ball: (Type: Grass, DP: 90)'

    # should not have any output
    captured = capsys.readouterr()
    assert not captured.out

    # Testing error case
    test_err_unknown_move = False
    try:
        moves['Flee']
    except KeyError:
        test_err_unknown_move = True
    assert test_err_unknown_move
    # Restore moves.csv in case
    copy_file('moves_copy.csv', 'moves.csv')


# Exercise 8
# Requires 1.a. load_data correct
def test_generate_move_list():
    pokedex = load_data('pokedex.csv')
    bulbasaur = pokedex[0]
    # generate_move_list takes a dict argument (a row
    # from pokedex.csv)
    bulbasaur_moves = generate_move_list(bulbasaur)
    assert isinstance(bulbasaur_moves, list)
    # List should have 4 strings for Bulbasaur (example in spec)
    assert len(bulbasaur_moves) == 4
    assert bulbasaur_moves == ['Vine Whip', 'Growl', 'Amnesia', 'Magical Leaf']

    # Caterpie has 2 moves
    caterpie = pokedex[9]
    # only move1 and move2 are non-empty
    caterpie_moves = generate_move_list(caterpie)
    # List should have 2 strings, since caterpie's move3 and move4 keys
    # map to '' values
    assert len(caterpie_moves) == 2
    assert caterpie_moves == ['Tackle', 'Bug Bite']

    # "A pathetic excuse for a Pokemon"
    magikarp = pokedex[128]
    magikarp_moves = generate_move_list(magikarp)
    # Magikarp simply knows splash. One day it will grow up to be a strong
    # Gyrados...
    assert magikarp_moves == ['Splash']
