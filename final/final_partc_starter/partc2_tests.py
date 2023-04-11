"""
CS 1 22fa

Final Exam Part C.2: OH Client Program (oh_client.py)

Tests for Part C.2 Grading.
- Test coverage for exercises C.2.1-C.2.4

NOTE: this client program relies on the oh_manager.py classes
working.

Students can ask on Discord if they have questions about test
results, but also double-check against spec examples and refer
to comments in respective test functions.
"""

from student_classes import Student, TA
from oh_manager import Entry, QueueManager
from oh_client import *
import oh_client


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
oh_client.input = mock_input


def test_c21_add_ta():
    """
    C.2.1. add_ta function in oh_client.py, which is used in prompt_add_ta,
    factoring out the add_ta functionality from user input for testing
    """   
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_client.print = lambda s='': output.append(s)

    manager = QueueManager()
    # From spec examples
    unknown_ta = manager.get_ta('2177843')
    assert unknown_ta is None
    # >>> prompt_add_ta(manager) # examples
    # Enter the TA's name: Foo Bar
    ta_name = 'Foo Bar'
    # Enter the TA's UID: 2177843
    ta_uid = '2177843'
    # Enter the TA's Grade/Year: Sophomore
    ta_year = 'Sophomore'
    # Enter the TA's email: foobar@caltech.edu
    ta_email = 'foobar@caltech.edu'
    # Enter the start time for your OH in HH:MM format (hours 0-23): 18:00
    ta_oh_start = '18:00'
    # Enter the end time for your OH in HH:MM format (hours 0-23): 22:00
    ta_oh_end = '22:00'
    add_ta(manager, ta_uid, ta_name, ta_year, ta_email, ta_oh_start, ta_oh_end)
    assert len(manager.tas) == 1
    ta1 = manager.get_ta('2177843')
    assert isinstance(ta1, TA)
    # same examples as C.1 tests
    assert str(ta1) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'
    add_ta(manager, '1234567', 'Maddie Ramos', 'Sophomore', 'maddie@caltech.edu', '11:00', '13:00')
    assert len(manager.tas) == 2
    ta2 = manager.get_ta('1234567')
    assert str(ta2) == 'Name: Maddie Ramos\nUID: 1234567\nEmail: maddie@caltech.edu\nYear: Sophomore'

    add_ta(manager, '0101', 'Claude Shannon', 'Senior', 'cs@caltech.edu', '01:01', '10:10')
    assert len(manager.tas) == 3
    ta3 = manager.get_ta('0101')
    assert str(ta3) == 'Name: Claude Shannon\nUID: 0101\nEmail: cs@caltech.edu\nYear: Senior'
    assert output == []


def test_c2_answer_next_question():
    """
    An Entry __str__ representation should simply be its associated Student's
    str followed by '\n' and the question information as specified in the spec.
    """
    output = []
    # Override output for testing print statements
    oh_client.print = lambda s='': output.append(str(s))
    global input_values

    manager = QueueManager()
    ta = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu', '18:00', '22:00')
    student = Student('2187112', 'Lorem Hovik', 'Freshman', 'lhovik@caltech.edu')
    q1 = Entry('What is a list?', student, 'MP1', '18:20')
    q2 = Entry('Is it true there are peacocks on campus?', student, 'General', '18:25')
    manager.enter_ta(ta)
    manager.add_entry(q1)
    manager.add_entry(q2)
    unknown_uid = '2345328'
    input_values = [unknown_uid]
    answer_next_question(manager)  # Ex. Giving UID for TA not in QueueManager
    # From spec examples:
    # Enter the answering TA's UID: 2345328  
    # There should be exactly one print statement
    assert len(output) == 1
    assert output[0] == 'TA not found.'
    output = []
    
    # Foo Bar TA's uid
    ta_uid = '2177843'
    # Reset input values for next example
    input_values = [ta_uid, 'n']
    answer_next_question(manager)  # Ex. Question not resolved (re-enters queue)
    # From spec examples:
    # Enter the answering TA's UID: 2177843
    # Entry's string representation is output after giving known uid
    # assert ''.join(output) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman\n' + \
    #                           'Question for MP1: What is a list?'
    assert ''.join(output) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman\n' + \
                              'Question for MP1: What is a list?'
    # Enter "y" if the question has been resolved. n
    # In this example, the TA uid was known, but they did not resolve the question,
    # so the manager is unchanged (still 2 entries in the unresolved queue)
    # Remember to put the question _back_ at the end of the queue!
    assert len(manager.unresolved_entries) == 2
    assert len(manager.resolved_entries) == 0

    output = []
    # Reset input values for next example
    input_values = [ta_uid, 'y']
    answer_next_question(manager)  # Ex. Question resolved (removed from queue)
    assert ''.join(output) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman\n' + \
                              'Question for General: Is it true there are peacocks on campus?' 
    # Enter "y" if the question has been resolved. y
    # Double-check state of unresolved entries vs. resolved entries
    # In this example, the TA uid was known, and they confirmed to resolve the next entry
    # Moved q1 from unresolved to resolved
    assert len(manager.unresolved_entries) == 1
    assert len(manager.resolved_entries) == 1

    output = []
    # Reset input values for next example
    input_values = [ta_uid, 'y']
    answer_next_question(manager)  # Ex. Question resolved (removed from queue)
    assert ''.join(output).rstrip() == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman\n' + \
                              'Question for MP1: What is a list?'
    # Enter "y" if the question has been resolved. y
    # Double-check state of unresolved entries vs. resolved entries
    # Both questions were resolved at this point
    assert len(manager.unresolved_entries) == 0
    assert len(manager.resolved_entries) == 2

    output = []
    # Reset input values for empty-queue example
    input_values = [ta_uid]
    answer_next_question(manager)  # Ex. Queue is now empty
    # Enter the answering TA's UID: 2177843
    # No currently unresolved questions found.
    assert ''.join(output) == 'No currently unresolved questions found.'
    # Double-check that unresolved_entries is actually empty
    assert len(manager.unresolved_entries) == 0
    assert len(manager.resolved_entries) == 2

def test_c23_log_resolved_entries():
    """
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_client.print = lambda s='': output.append(str(s))
    manager = QueueManager()

    student1 = Student('2187112', 'Lorem Hovik', 'Freshman', 'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    ta1 = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu', '18:00', '22:00')
    ta3 = TA('0101', 'Claude Shannon', 'Senior', 'cs@caltech.edu', '01:01', '10:10')
    # Add resolved entries
    # (from spec examples)
    q1 = Entry('What is a list?', student1, 'MP1', '01:20')
    q2 = Entry('Is it true there are peacocks on campus?', student2, 'General', '18:25')
    q3 = Entry('How do I write a good docstring?', student1, 'Final', '18:26')
    manager.add_resolved_entry(q1, ta3) # Timestamp: 01:20
    manager.add_resolved_entry(q2, ta1) # Timestamp: 18:25
    manager.add_resolved_entry(q3, ta3) # Timestamp: 18:26
    # Log resolved (i.e., q1, q2, and q3)
    # They should be logging to the given filename, not hard-coding resolved.csv
    log_resolved_questions(manager, 'resolved_test.csv')

    row1 = ['MP1', 'What is a list?', '6', 'Claude Shannon', '(01:01-10:10)']
    row2 = ['General', 'Is it true there are peacocks on campus?', '12', 'Foo Bar', '(18:00-22:00)']
    row3 = ['Final', 'How do I write a good docstring?', '13', 'Claude Shannon', '(01:01-10:10)']
    expected_rows = [row1, row2, row3]
    with open('resolved_test.csv', 'r') as f:
        # Leniency if there's an extra \n at the end
        reader = csv.reader(f)
        # just check that response_time is an int, since its computed based on real-time
        # Column fieldnames should be first row in CSV reader
        fieldnames = next(reader)
        # From oh_client.py RESOLVED_QUESTION_LOG_COLUMNS
        assert fieldnames == ['assignment', 'question', 'response_time', 'response_ta', 'ta_timeframe']
        for i in range(len(expected_rows)):  # 3 rows expected after column header
            expected_row = expected_rows[i]
            actual_row = next(reader)
            for col_index in range(len(expected_row)):
                # Leniency check on col 2 (resolved_time, which depends on local time)
                if col_index == 2:
                    try:
                        response_time = int(actual_row[col_index])
                    except ValueError as err:
                        assert False == f'Expected integer value for response_time, but found: {actual_row[col_index]}'
                else:
                    # Otherwise, check for equality
                    assert expected_row[col_index] == actual_row[col_index]
        try:
            # Leniency if there's an extra \n at the end
            line = next(reader)
            assert not line or False == 'Extra rows found in CSV file'
        except StopIteration as err:
            assert True # No more rows found


#        assert f.read().rstrip() == '''assignment,question,response_time,response_ta,ta_timeframe
#MP1,What is a list?,6,Claude Shannon,(18:00-22:00)
#MP1,What is a dictionary?,2,Foo Bar,(18:00-22:00)
#MP1,How do I write a good docstring?,4,Claude Shannon,(18:00-22:00)'''

    # There shouldn't be any other output printed from C.2.3
    assert output == []


def test_c24_log_unresolved_questions():
    """
    Tests the QueueManager's __len__ method, which is simply the length
    of its unresolved_entires list.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_client.print = lambda s='': output.append(str(s))
    manager = QueueManager()

    student1 = Student('2187112', 'Lorem Hovik', 'Freshman', 'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    # Add resolved entries
    # (from spec examples)
    q1 = Entry('What is a list?', student1, 'MP1', '01:20')
    q2 = Entry('Is it true there are peacocks on campus?', student2, 'General', '18:25')
    q3 = Entry('How do I write a good docstring?', student1, 'Final', '18:26')
    manager.add_entry(q1) 
    manager.add_entry(q2) 
    manager.add_entry(q3)
    # Log unresolved (i.e., q1, q2, and q3)
    # They should be logging to the given filename, not hard-coding unresolved.csv
    log_unresolved_questions(manager, 'unresolved_test.csv')

    row1 = ['2187112', 'Lorem Hovik', 'lhovik@caltech.edu', 'MP1', 'What is a list?']
    row2 = ['012345', 'Oppa', 'oppa@caltech.edu', 'General', 'Is it true there are peacocks on campus?']
    row3 = ['2187112', 'Lorem Hovik', 'lhovik@caltech.edu', 'Final', 'How do I write a good docstring?']
    expected_rows = [row1, row2, row3]
    with open('unresolved_test.csv', 'r') as f:
        # Leniency if there's an extra \n at the end
        reader = csv.reader(f)
        # just check that response_time is an int, since its computed based on real-time
        # Column fieldnames should be first row in CSV reader
        fieldnames = next(reader)
        # From oh_client.py UNRESOLVED_QUESTION_LOG_COLUMNS
        assert fieldnames == ['student_uid', 'student_name', 'student_email', 
                              'assignment', 'question']
        for i in range(len(expected_rows)):  # 3 rows expected after column header
            expected_row = expected_rows[i]
            actual_row = next(reader)
            for col_index in range(len(expected_row)):
                # check for equality
                assert expected_row[col_index] == actual_row[col_index]
        # Finally, double-check that there weren't any unspecified rows added
        try:
            line = next(reader)
            # Leniency if there's an extra \n at the end
            assert not line or False == 'Extra rows found in CSV file'
        except StopIteration as err:
            assert True # No more rows found

    # There shouldn't be any other output printed from C.2.4
    assert output == []


def test_c23_c24_log_empty_cases():
    """
    Tests for edge-cases overlooked by students (e.g. loop bound errors)
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_client.print = lambda s='': output.append(str(s))
    manager = QueueManager()
    ta = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu', '18:00', '22:00')
    manager.enter_ta(ta)
    try:
        log_resolved_questions(manager, 'resolved_empty.csv')
        # It doesn't matter how students handle this case, as long as an error isn't thrown
        # (they can ignore the file-writing, write an empty file, or write just the single
        # column header)
    except Exception as err:
        assert False == 'Empty resolved_entries.csv should not throw an error'
    try:
        log_unresolved_questions(manager, 'unresolved_empty.csv')
    except Exception as err:
        assert False == 'Empty unresolved_entries.csv should not throw an error'


def test_additional_requirements(mocker):
    # There should not be any explicit calls to dunder 
    # methods like __str__, __len__, __init__
    # the only occurrences should come from the method definitions.
    counts = {'TODO' : 0, ' pass': 0, 'import ': 0,
              '__str__': 0, '__init__': 0, '__len__': 0}
    with open('oh_manager.py') as f:
        for line in f:
            for key in counts:
                if key == ' pass':
                    if ' pass ' in line or line.rstrip()[-4:] == 'pass':
                        counts[' pass'] += 1
                elif key in line:
                    counts[key] += 1
    assert counts['TODO'] == 0
    assert counts[' pass'] == 0
    assert counts['import '] == 2
    # Both classes have __init__
    assert counts['__init__'] == 2
    # Only Entry has __str__
    assert counts['__str__'] == 1
    # Only QueueManager has __len__
    assert counts['__len__'] == 1
