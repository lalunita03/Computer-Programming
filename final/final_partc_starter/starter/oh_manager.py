"""
CS 1 22fa Final Exam
Part C: OH Queue Manager
Student Name: TODO

Part C.2 Exercises
"""

from student import Student, TA
from time import localtime, time


class Entry:
    """
    Represents an OH Queue Entry, managing information for a single OH
    Queue entry with the following:

    Attributes:
        - student (Student): Student instance corresponding to the student
        - question (str): The student's submitted question
        - assignment_name (str): the name of the assignment, such as 'MP8'
        - entry_time (str): Time of entry in "HH:MM" format (24-hour notation)
        - response_ta (TA): TA assigned to the queue Entry, or None if none
                            yet assigned
        - response_time (int): # of minutes it took to respond
        - resolved_time (str): Time of resolution in "HH:MM" format (24-hour)

    Note that our Entry is a simplification, and does not account for
    different dates, only times. As such, we choose to represent response_time
    as # of minutes elapsed as opposed to a string timestamp, since some
    ambitious staff members may help students past 00:00 midnight. Room
    for improvement!
    """
    def __init__(self, question, student, assignment_name, entry_time):
        """
        Constructs a new Entry with provided arguments, initializing
        a response_TA to None and response_time to -1 (representing an
        active/unresolved entry).

        Arguments:
            - question (str)
            - student (Student)
            - assignment_name (str)
            - entry_time (str): time of creation in form HH:MM
        """
        self.question = question
        self.student = student
        self.assignment_name = assignment_name
        self.entry_time = entry_time
        self.response_ta = None
        self.response_time = -1
        self.resolved_time = ""

    def get_question(self):
        """
        Returns the question asked by the student.

        Returns:
            - (str): the student's question
        """
        pass  # TODO: C.2.1a

    def get_student(self):
        """
        Returns the Student instance corresponding to the student who
        created the entry.

        Returns:
            - (Student): the Student instance
        """
        pass  # TODO: C.2.1b

    def get_response_ta(self):
        """
        Returns the TA that responded to the entry. If the entry is
        unresolved, returns None.

        Returns:
            - (TA): the TA instance (or None)
        """
        pass  # TODO: C.2.1c

    def get_assignment_name(self):
        """
        Returns the name of the assignment,

        Returns:
            - (str): the assignment name
        """
        pass  # TODO: C.2.1d

    def get_response_time(self):
        """
        Returns the time taken for the TA to respond to the entry.

        Returns:
            - (int): the response time, in minutes
        """
        pass  # TODO: C.2.1e

    def __str__(self):
        """
        Returns the string representation of the entry, in the form:
        'Name: <full name>\nUID: <student uid>\nEmail: <student email>\n' +
        'Year: <student year>\nQuestion for <assignment_name>: <question>'

        Returns:
            - (str): string representation of the Entry
        """
        pass  # TODO: C.2.2

    def resolve_entry(self, ta):
        """
        Resolves an Entry given a TA, setting the response TA and the
        response and resolution times based on the current time.

        Arguments:
            - ta (TA): the TA resolving the entry

        Returns:
            - None
        """
        completion_time = localtime(time())
        completion_hour = completion_time.tm_hour
        completion_min = completion_time.tm_min
        (entry_hour, entry_min) = tuple(self.entry_time.split(':'))
        (total_hours, total_min) = (completion_hour - int(entry_hour),
                                    completion_min - int(entry_min))
        self.resolved_time = f'{completion_hour:02d}:{completion_min:02d}'
        self.response_time = total_min + (total_hours * 60)
        self.response_ta = ta


# TODO: Write a module docstring and method docstrings for this class.
class QueueManager:
    """
    TODO docstring
    """
    def __init__(self):
        pass  # TODO: C.2.3

    def __len__(self):
        pass  # TODO: C.2.4

    def enter_ta(self, ta: TA):
        pass  # TODO: C.2.5

    def get_ta(self, uid):
        pass  # TODO: C.2.6

    def add_entry(self, entry: Entry):
        pass  # TODO: C.2.7

    def get_next_entry(self):
        pass  # TODO: C.2.8

    def add_resolved_entry(self, entry: Entry, ta: TA):
        pass  # TODO: C.2.9

    def get_resolved_entries(self):
        pass  # TODO: C.2.10

    def get_unresolved_entries(self):
        pass  # TODO: C.2.11
