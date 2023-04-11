"""
CS 1 22fa

Final Exam Part C.1: Entry and QueueManager classes

Tests for Part C.1 Grading.
- Test coverage for exercises C.1.1-C.1.10 (oh_manager.py only)

Students can ask on Discord if they have questions about test
results, but also double-check against spec examples and refer
to comments in respective test functions.
"""

from student_classes import Student, TA
from oh_manager import Entry, QueueManager
import oh_manager


# C.1.1. Basic getters for Entry class
def test_c11_entry_getters():
    """
    Entry constructor is given, and should be unchanged

    Tests the following getters for basic functionality as specified in spec:
    - get_question
    - get_student
    - get_response_ta
    - get_assignment
    - get_response_time
    """
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman', 'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')
    # C.1.1 get_question
    assert q1.get_question() == 'What is a list?'
    assert q2.get_question() == 'What is a tuple?'
    assert q3.get_question() == 'Is the Final take-home? Can we celebrate?'

    # C.1.2 get_student
    s1 = q1.get_student()
    s2 = q2.get_student()
    s3 = q3.get_student()
    assert isinstance(s1, Student)
    assert isinstance(s2, Student)
    assert isinstance(s3, Student)

    # These are already provided, so should all work unless the student did
    # something unspecified (incorrect)
    assert s1.get_email() == 'lhovik@caltech.edu'
    assert s1.get_name() == 'Lorem Hovik'
    assert s1.get_uid() == '2187112'
    assert s1.get_year() == 'Freshman'
    assert str(s1) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman'

    assert s2.get_email() == 'oppa@caltech.edu'
    assert s2.get_name() == 'Oppa'
    assert s2.get_uid() == '012345'
    assert s2.get_year() == 'Sophomore'

    # C.1.3 get_response_TA
    # Should be left as None while Unresolved
    assert q1.get_response_ta() is None
    assert q2.get_response_ta() is None
    assert q3.get_response_ta() is None

    # C.1.4 get_assignment
    assert q1.get_assignment() == 'MP1'
    assert q2.get_assignment() == 'General'
    assert q3.get_assignment() == 'Final'

    # C.1.5 get_response_time
    # Should be left as -1 when unresolved
    assert q1.get_response_time() == -1
    assert q2.get_response_time() == -1
    assert q3.get_response_time() == -1
    # For testing only; don’t access attributes directly
    q1.response_time = 30
    assert q1.get_response_time() == 30


# C.1.2 Entry's __str__ method
def test_c12_entry_str():
    """
    An Entry __str__ representation should simply be its associated Student's
    str followed by '\n' and the question information as specified in the spec.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1, 'Final',
               '20:30')

    s1 = q1.get_student()
    s2 = q2.get_student()
    s3 = q3.get_student()
    # First, check that Student's __str__ is unchanged from given
    assert str(s1) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman'
    # Next, check the Entry's __str__, which simply adds one line to the
    # associated student's str
    q1_str = str(q1)
    assert q1_str == f'{s1}\nQuestion for MP1: What is a list?'

    q2_str = str(q2)
    assert q2_str == f'{s2}\nQuestion for General: What is a tuple?'

    q3_str = str(q3)
    assert q3_str == f'{s3}\nQuestion for Final: Is the Final take-home? Can we celebrate?'

    # There should not have been any output in this method
    assert output == []


# C.1.3 QueueManager's __init__ constructor
def test_c13_qm_init():
    """
    The QueueManager constructor should simply initialize 3 attributes
    as described.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)
    manager = QueueManager()
    assert isinstance(manager.unresolved_entries, list)  # default (empty list)
    assert manager.unresolved_entries == []
    assert isinstance(manager.resolved_entries, list)  # default (empty list)
    assert manager.resolved_entries == []
    assert isinstance(manager.tas, dict)  # default (empty list)
    assert manager.tas == {}

    # There should not have been any output in this method
    assert output == []


# C.1.4 QueueManager's __len__ -> int method
def test_c14_qm_len():
    """
    Tests the QueueManager's __len__ method, which is simply the length
    of its unresolved_entires list.
    """
    # There should not have been any output in this method
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    assert len(manager) == 0
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')
    manager.unresolved_entries.extend([q1, q2])  # only for testing
    manager.unresolved_entries.extend([q3])  # only for testing
    assert len(manager) == 3
    # There should not have been any output in this method
    assert output == []


# C.1.5 QueueManager's enter_ta(TA) -> None method
def test_c15_qm_enter_ta():
    """
    Tests the QueueManager's enter_ta(TA) method, which adds a TA
    to the tas dictionary attribute.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    # The tas dictionary should be initialized as empty
    assert manager.tas == {}
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    manager.unresolved_entries.extend([q1, q2])  # only for testing
    ta1 = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu',
             '18:00', '22:00')  # oh_time_frame() -> ('18:00', '22:00')
    test_ret = manager.enter_ta(ta1)
    # This method shouldn't return anything
    assert test_ret is None

    assert isinstance(manager.tas, dict)  # new TA added
    # Check that the TA's UID is a str mapping to a TA
    assert '2177843' in manager.tas
    added_ta1 = manager.tas['2177843']
    assert isinstance(added_ta1, TA)
    assert str(added_ta1) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'

    # Test adding two more TAs
    ta2 = TA('1234567', 'Maddie Ramos', 'Sophomore', 'maddie@caltech.edu',
             '11:00', '13:00')
    ta3 = TA('0101', 'Claude Shannon', 'Senior', 'cs@caltech.edu',
             '01:01', '10:10')
    manager.enter_ta(ta2)
    manager.enter_ta(ta3)
    assert len(manager.tas) == 3
    assert '1234567' in manager.tas
    assert '0101' in manager.tas

    added_ta2 = manager.tas['1234567']
    added_ta3 = manager.tas['0101']
    assert isinstance(added_ta2, TA)
    assert isinstance(added_ta3, TA)

    # These should both pass assuming they were added correctly and unchanged
    assert str(ta1) != str(ta2) and str(ta1) != str(ta3)
    assert ta1.get_oh_time_frame() == ('18:00', '22:00')

    # There should still be no return if the TA is already in the manager
    test_ret = manager.enter_ta(ta1)
    assert test_ret is None

    # There should be exactly one print statement
    assert len(output) == 1
    assert output[0] == 'This TA is already in the QueueManager.'


# C.1.6 QueueManager's get_ta(str) -> TA/None method
def test_c16_get_ta():
    """
    Tests the QueueManager's get_ta(ta_uid) method, which returns a
    TA object corresponding to a given ta_uid string, returning None
    (without any print output or error) if the uid is not a key in the current
    tas dictionary.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    assert len(manager) == 0
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    manager.unresolved_entries.extend([q1, q2])  # only for testing
    ta1 = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu',
             '18:00', '22:00')
    test_ret = manager.enter_ta(ta1)
    # This method shouldn't return anything
    assert test_ret is None

    assert isinstance(manager.tas, dict)  # new TA added
    # Check that the TA's UID is a str mapping to a TA
    assert '2177843' in manager.tas
    added_ta1 = manager.tas['2177843']
    assert isinstance(added_ta1, TA)
    assert str(added_ta1) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'

    ta2 = TA('1234567', 'Maddie Ramos', 'Sophomore', 'maddie@caltech.edu',
             '11:00', '13:00')
    ta3 = TA('0101', 'Claude Shannon', 'Senior', 'cs@caltech.edu',
             '01:01', '10:10')
    manager.enter_ta(ta2)
    manager.enter_ta(ta3)
    assert len(manager.tas) == 3
    assert '1234567' in manager.tas
    assert '0101' in manager.tas

    added_ta2 = manager.tas['1234567']
    added_ta3 = manager.tas['0101']
    assert isinstance(added_ta2, TA)
    assert isinstance(added_ta3, TA)

    # These should both pass assuming they were added correctly and unchanged
    assert str(ta1) != str(ta2) and str(ta1) != str(ta3)
    assert ta1.get_oh_time_frame() == ('18:00', '22:00')

    assert isinstance(manager.tas, dict)
    assert len(manager.tas) == 3

    ta1_info = manager.get_ta('2177843')  # get existing TA
    ta2_info = manager.get_ta('1234567')
    ta3_info = manager.get_ta('0101')
    assert isinstance(ta1_info, TA)
    assert isinstance(ta2_info, TA)
    assert isinstance(ta3_info, TA)
    assert str(ta1_info) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'
    assert str(ta2_info) == 'Name: Maddie Ramos\nUID: 1234567\nEmail: maddie@caltech.edu\nYear: Sophomore'
    assert str(ta3_info) == 'Name: Claude Shannon\nUID: 0101\nEmail: cs@caltech.edu\nYear: Senior'
    assert manager.get_ta('123') is None  # UID not in dictionary
    assert manager.get_ta('21778430') is None  # UID not in dictionary

    # There should be no output in this method
    assert len(output) == 0


# C.1.7 QueueManager's add_entry(Entry) -> None method
def test_c17_add_entry():
    """
    Tests the QueueManager's add_entry(Entry) method, which adds the given
    Entry object to the manager's list of unresolved_entries (which
    should have been initialized to an empty list when the QueueManager
    was constructed)
    """
    # There shouldn't be any output after this test function
    output = []

    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')

    assert len(manager) == 0
    manager.add_entry(q1)
    assert q1.get_question() == 'What is a list?'
    assert len(manager.unresolved_entries) == 1

    assert q2.get_question() == 'What is a tuple?'
    manager.add_entry(q2)
    assert len(manager.unresolved_entries) == 2

    manager.add_entry(q3)
    assert q3.get_question() == 'Is the Final take-home? Can we celebrate?'
    assert len(manager.unresolved_entries) == 3
    assert isinstance(manager.unresolved_entries, list)
    assert isinstance(manager.unresolved_entries[0], Entry)
    assert isinstance(manager.unresolved_entries[1], Entry)
    assert isinstance(manager.unresolved_entries[2], Entry)

    # There should be no output in this method
    assert len(output) == 0


# C.1.8 QueueManager's get_next_entry() -> Entry/None method
def test_c18_get_next_entry():
    """
    Tests the QueueManager's get_next_entry() method, which should return
    the next Entry in the queue, in a first-in-first-out order.
    If the list of unresolved_entries is empty, this method should
    return None (no errors should be raised, and nothing should be printed)
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')
    # len(manager) returns the length of the unresolved_entries
    assert len(manager) == 0
    manager.add_entry(q1)
    assert len(manager) == 1
    manager.add_entry(q2)
    assert len(manager) == 2  # there are 2 entries in the queue
    manager.add_entry(q3)
    assert len(manager) == 3  # there are 3 entries in the queue

    # We have 3 Entries in the QueueManager's list of unresolved_entries
    # now. Next, start processing the queue manager, with each call to
    # get_next_entry returning the earliest Entry added to the queue
    # that is still in the unresolved_list.

    next = manager.get_next_entry()  # get 'dequeue' first entry
    assert isinstance(next, Entry)
    assert str(next) == 'Name: Lorem Hovik\nUID: 2187112\nEmail: lhovik@caltech.edu\nYear: Freshman\nQuestion for MP1: What is a list?'
    assert len(manager) == 2  # there are 2 entries left

    next2 = manager.get_next_entry()  # get second entry
    assert isinstance(next2, Entry)
    assert str(next2) == 'Name: Oppa\nUID: 012345\nEmail: oppa@caltech.edu\nYear: Sophomore\nQuestion for General: What is a tuple?'
    assert len(manager) == 1  # there is 1 entry left

    next3 = manager.get_next_entry()  # get last entry
    assert str(next3) == f'{student1}\nQuestion for Final: Is the Final take-home? Can we celebrate?'
    assert len(manager) == 0  # there are 0 entries left

    next4 = manager.get_next_entry()
    # there were no entries left, and no error should be raised
    assert next4 is None

    # Nothing should have been printed in this method
    assert output == []


# C.1.9 QueueManager's add_resolved_entry(Entry, TA) -> None method
def test_c19_add_resolved_entry(mocker):
    """
    Tests the QueueManager's add_resolved_entry(Entry, TA) method, which should
    add the given Entry to the manager's resolved_entries list. This method
    shouldn't change the unresolved_list; the spec examples show this
    usage with get_next_entry() -> Entry followed by
    add_resolved_entry(Entry, TA).
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')
    q4 = Entry('Is it true there are peacocks on campus?', student2,
               'General', '20:59')
    q5 = Entry('I just need to tell you all that Pikachu is always the very best.', student2, 'General', '21:00')

    ta1 = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu',
             '18:00', '22:00')
    ta2 = TA('1234567', 'Maddie Ramos', 'Sophomore', 'maddie@caltech.edu',
             '11:00', '13:00')
    assert isinstance(manager.unresolved_entries, list)
    assert len(manager.unresolved_entries) == 0
    assert isinstance(manager.resolved_entries, list)
    assert len(manager.resolved_entries) == 0

    # The Entry's resolve_entry method should be called here
    # as required in the spec
    spy1 = mocker.spy(Entry, 'resolve_entry')

    manager.add_entry(q1)
    # currently no response TA
    assert q1.response_ta is None
    # unresolved_entries should still be a list, now with 1 Entry
    assert isinstance(manager.unresolved_entries, list)
    assert len(manager.unresolved_entries) == 1
    assert isinstance(manager.unresolved_entries[0], Entry)
    assert str(manager.unresolved_entries[0]) == str(q1)

    # resolved should still be a list, still empty
    assert isinstance(manager.resolved_entries, list)
    assert len(manager.resolved_entries) == 0

    next = manager.get_next_entry()  # get entry
    # unresolved entries should now be empty
    assert manager.unresolved_entries == []

    manager.add_resolved_entry(next, ta1)
    assert spy1.call_count == 1
    # unresolved entries should still be empty
    assert manager.unresolved_entries == []
    assert str(next) == str(q1)

    # resolved_entries should still be a list, now with 1 entry
    assert isinstance(manager.resolved_entries, list)
    # entry moved to resolved_entries with the assigned TA (ta1)
    assert len(manager.resolved_entries) == 1
    assert str(manager.resolved_entries[0]) == str(next)
    assert isinstance(q1.response_ta, TA)  # response TA added
    assert str(q1.response_ta) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'

    # 1 new entry added to unresolved, different student (s2)
    manager.add_entry(q2)
    assert len(manager.unresolved_entries) == 1
    # resolved should still have the single resolved entry from above
    assert len(manager.resolved_entries) == 1

    # add another entry, same student (s1) as q1
    manager.add_entry(q3)
    assert len(manager.unresolved_entries) == 2

    # add another entry, same student (s2) as q2
    manager.add_entry(q4)
    assert len(manager.unresolved_entries) == 3

    # add another entry, same student (s1) as q1 and q5
    manager.add_entry(q5)
    assert len(manager.unresolved_entries) == 4
    # resolved should still have the single resolved entry
    assert len(manager.resolved_entries) == 1

    # Next, process the 4 entries we just added
    next2 = manager.get_next_entry()
    assert len(manager.unresolved_entries) == 3
    # The same TA can be assigned to multiple entries
    # ta1 has now resolved two entries, q1 and q2
    manager.add_resolved_entry(next2, ta1)
    # As shown in the spec examples, add_resolved_entry
    # does not handle the moving of Entrys; get_next_entry
    # is the method which removes and returns the next entry
    # to pass to this method
    assert len(manager.unresolved_entries) == 3

    # q2 and next2 should have the same information
    assert str(q2.response_ta) == str(ta1)
    assert str(next.response_ta) == str(ta1)

    # q2 moved to resolved
    assert len(manager.unresolved_entries) == 3
    assert len(manager.resolved_entries) == 2

    next3 = manager.get_next_entry()
    # A second TA is used to correct specific TA-assignment
    manager.add_resolved_entry(next3, ta2)
    # q3 moved to resolved
    assert len(manager.unresolved_entries) == 2
    assert len(manager.resolved_entries) == 3

    assert str(q3.response_ta) == str(ta2)
    assert str(next3.response_ta) == str(ta2)

    # q4 moved to resolve; this is the 3rd Entry ta1 has resolved
    next4 = manager.get_next_entry()
    manager.add_resolved_entry(next4, ta1)
    assert str(q4.response_ta) == str(ta1)
    assert str(next4.response_ta) == str(ta1)
    # 4 calls to Entry's resolve_entry expected so far
    assert spy1.call_count == 4

    assert len(manager.unresolved_entries) == 1
    assert len(manager.resolved_entries) == 4
    # sanity check that these are both still lists of TAs
    assert isinstance(manager.unresolved_entries, list)
    assert isinstance(manager.resolved_entries, list)
    assert isinstance(manager.unresolved_entries[0], Entry)
    assert isinstance(manager.unresolved_entries[0].student, Student)
    assert manager.unresolved_entries[0].response_ta is None
    assert isinstance(manager.resolved_entries[0], Entry)
    assert isinstance(manager.resolved_entries[-1], Entry)
    assert isinstance(manager.resolved_entries[0].response_ta, TA)
    assert isinstance(manager.resolved_entries[0].student, Student)
    assert str(manager.resolved_entries[0].response_ta) == str(ta1)


# C.1.10 and C.1.11 basic getters (1-liners each)
def test_c1_10_and_11():
    """
    Tests the QueueManager's two getters for resolved_entries and
    unresolved_entries, both which should return a list of Entrys as
    described in the spec.

    Requires everything else to work so far.
    """
    # There shouldn't be any output after this test function
    output = []
    # Override output for testing print statements
    oh_manager.print = lambda s='': output.append(s)

    manager = QueueManager()
    student1 = Student('2187112', 'Lorem Hovik', 'Freshman',
                       'lhovik@caltech.edu')
    student2 = Student('012345', 'Oppa', 'Sophomore', 'oppa@caltech.edu')
    q1 = Entry('What is a list?', student1, 'MP1', '18:20')
    q2 = Entry('What is a tuple?', student2, 'General', '18:26')
    q3 = Entry('Is the Final take-home? Can we celebrate?', student1,
               'Final', '20:30')
    q4 = Entry('Is it true there are peacocks on campus?', student2,
               'General', '20:59')
    q5 = Entry('I just need to tell you all that Pikachu is always the very best.', student2, 'General', '21:00')

    ta1 = TA('2177843', 'Foo Bar', 'Sophomore', 'foobar@caltech.edu',
             '18:00', '22:00')
    ta2 = TA('1234567', 'Maddie Ramos', 'Sophomore', 'maddie@caltech.edu',
             '11:00', '13:00')
    assert isinstance(manager.unresolved_entries, list)
    assert len(manager.unresolved_entries) == 0
    assert isinstance(manager.resolved_entries, list)
    assert len(manager.resolved_entries) == 0

    # C.1.10 Empty list case
    assert manager.get_resolved_entries() == []
    # C.1.11 Empty list case
    assert manager.get_unresolved_entries() == []

    empty_unresolved = manager.get_unresolved_entries()
    assert empty_unresolved == []

    empty_resolved = manager.get_resolved_entries()
    assert empty_resolved == []

    manager.add_entry(q1)
    next = manager.get_next_entry()  # get entry
    # entry moved to resolved_entries with the assigned TA (ta1)
    manager.add_resolved_entry(next, ta1)

    # Both the resolved_entries attribute and the list returned
    # should match
    one_resolved = manager.get_resolved_entries()
    assert isinstance(manager.resolved_entries, list)
    # resolved_entries should still be a list, now with 1 entry
    assert len(manager.resolved_entries) == 1
    assert isinstance(manager.resolved_entries[0], Entry)
    assert isinstance(one_resolved, list)
    assert len(one_resolved) == 1
    assert isinstance(one_resolved[0], Entry)
    assert one_resolved[0].response_ta.get_uid() == ta1.get_uid()
    assert str(manager.resolved_entries[0]) == str(next)
    # Ok if they make a copy of the Entry, as long as it is compatible
    assert str(one_resolved[0]) == str(manager.resolved_entries[0])
    assert isinstance(q1.response_ta, TA)  # response TA added
    assert str(q1.response_ta) == 'Name: Foo Bar\nUID: 2177843\nEmail: foobar@caltech.edu\nYear: Sophomore'

    # unresolved should now be empty
    empty_unresolved = manager.get_unresolved_entries()
    assert empty_unresolved == []
    assert empty_unresolved == manager.unresolved_entries

    # 1 new entry added to unresolved, different student (s2)
    manager.add_entry(q2)
    one_unresolved = manager.get_unresolved_entries()
    assert str(one_unresolved[0]) == str(q2)
    assert str(one_unresolved[0].student) == str(student2)
    # resolved should still have the single resolved entry from above
    assert len(manager.get_resolved_entries()) == 1

    # add another entry, same student (s1) as q1
    manager.add_entry(q3)
    q2_q3_unresolved = manager.get_unresolved_entries()
    assert len(q2_q3_unresolved) == 2
    assert isinstance(q2_q3_unresolved[0], Entry)
    assert isinstance(q2_q3_unresolved[1], Entry)
    assert q2_q3_unresolved[0].response_ta is None
    assert q2_q3_unresolved[1].response_ta is None

    # add another entry, same student (s2) as q2
    manager.add_entry(q4)
    assert len(manager.get_unresolved_entries()) == 3

    # add another entry, same student (s1) as q1 and q5
    manager.add_entry(q5)
    assert len(manager.get_unresolved_entries()) == 4
    # resolved should still have the single resolved entry
    assert len(manager.get_resolved_entries()) == 1

    # Next, process the 4 entries we just added
    next2 = manager.get_next_entry()
    # The same TA can be assigned to multiple entries
    # ta1 has now resolved two entries, q1 and q2
    manager.add_resolved_entry(next2, ta1)

    # q2 and next2 should have the same information
    assert str(q2.response_ta) == str(ta1)
    assert str(next.response_ta) == str(ta1)

    # q2 moved to resolved
    assert len(manager.get_unresolved_entries()) == 3
    # len(manager) should be equivalent
    assert len(manager) == 3
    assert len(manager.get_resolved_entries()) == 2

    next3 = manager.get_next_entry()
    # A second TA is used to correct specific TA-assignment
    manager.add_resolved_entry(next3, ta2)
    # q3 moved to resolved
    assert len(manager.get_unresolved_entries()) == 2
    assert len(manager.get_resolved_entries()) == 3

    assert str(q3.response_ta) == str(ta2)
    assert str(next3.response_ta) == str(ta2)

    # q4 moved to resolve; this is the 3rd Entry ta1 has resolved
    next4 = manager.get_next_entry()
    manager.add_resolved_entry(next4, ta1)
    assert str(q4.response_ta) == str(ta1)
    assert str(next4.response_ta) == str(ta1)

    # Final state
    assert len(manager.get_unresolved_entries()) == 1
    assert len(manager.get_resolved_entries()) == 4

    # No output should have been printed in this method
    assert output == []


def test_additional_requirements(mocker):
    """
    Function to help students catch some additional requirements
    that are easy to check for. Students are required to follow the
    spec requirements for full credit. If there is a question about
    this test failing for some reason, the student can ask on Discord.
    If it's an import assertion error, double-check that VSCode hasn't
    added any unspecified imports.
    """
    # There should not be any explicit calls to dunder methods
    # like __str__, __len__, __init__.
    # The only occurrences should come from the method definitions.
    counts = {'TODO': 0, ' pass': 0, 'import ': 0,
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
