"""
CS 1 22fa Final Exam
Part C: OH Queue Manager
Student Name: Lea Grohmann

This program has functions that help a user make make on QueueManager
and modify it based on the users input
"""

from oh_manager import QueueManager, Entry
from student_classes import Student, TA
# Use the time module for real-time timestamps when processing OH question
# entries
from time import localtime, time, sleep
import csv

# Program constants that should be used for CSV file columns related to
# resolved and unresolved question logs, respectively.
RESOLVED_QUESTION_LOG_COLUMNS = ['assignment',
                                 'question',
                                 'response_time',
                                 'response_ta',
                                 'ta_timeframe']
UNRESOLVED_QUESTION_LOG_COLUMNS = ['student_uid',
                                   'student_name',
                                   'student_email',
                                   'assignment',
                                   'question']


# Given, do not change
def prompt_add_ta(oh_manager):
    """
    Prompts the user for TA information, adding a new TA to the
    given `oh_manager` if the TA isn't already in the manager.

    Arguments:
        - oh_manager (OHManager)
    """
    ta_name = input('Enter the TA\'s name: ')
    ta_uid = input('Enter the TA\'s UID: ')
    ta_year = input('Enter the TA\'s Grade/Year: ')
    ta_email = input('Enter the TA\'s email: ')
    oh_start_time = input('Enter start time for your OH in HH:MM (hrs 0-23): ')
    oh_end_time = input('Enter end time for your OH in HH:MM (hrs 0-23): ')
    add_ta(oh_manager, ta_uid, ta_name, ta_year, ta_email,
           oh_start_time, oh_end_time)


def add_ta(oh_manager, uid, name, year, email, start_time, end_time):
    """
    Creates a new TA and adds to the `oh_manager`. Times should be consistent
    with 'HH:MM' 24-hour time format (e.g. '13:00' for 1PM).

    There is no validation on valid start/end times following 'HH:MM' 24-hour
    format, but that is optional room for improvement that could be implemented
    with a validate_oh_times(start, end) helper function.

    Arguments:
        - uid (str): TA's student identifier (e.g. '1234567')
        - name (str): Name of TA to add (e.g. 'Maddie Ramos')
        - year (str): Year/status of the TA (e.g. 'Sophomore')
        - email (str): TA's email on record (e.g. 'maddie@caltech.edu')
        - start_time (str): Start time for TA's scheduled OH (e.g. '11:00')
        - end_time (str): End time for TA's scheduled OH (e.g. '13:00')
    """
    ta = TA(uid, name, year, email, start_time, end_time)
    oh_manager.enter_ta(ta)


def answer_next_question(oh_manager):
    """
    Prompts the user for a TA UID to assign the next Entry of the given
    `oh_manager`. If the UID does not correspond to a TA in the manager,
    or there are no unresolved entries in the manager, prints an appropriate
    error message.

    Arguments:
        - oh_manager (OHManager)
    """
    ta_uid = input('Enter the answering TA\'s UID: ')
    ta = oh_manager.get_ta(ta_uid)
    if not ta:
        print('TA not found.')
    else:
        if len(oh_manager) == 0:
            print('No currently unresolved questions found.')
            return
        entry = oh_manager.get_next_entry()
        print(entry)
        resolution_status = input('Enter "y" if the question is resolved. ')
        if resolution_status == "y":
            oh_manager.add_resolved_entry(entry, ta)
        else:
            oh_manager.add_entry(entry)


def log_resolved_questions(oh_manager, resolved_filename):
    """
    Given an `oh_manager` and filename to write to, logs all of the manager's
    resolved questions to the given filename, in order. Note that the
    file will be overwritten if it already exists. The given filename will
    be written to as a CSV file using RESOLVED_QUESTION_LOG_COLUMNs as
    the column names.

    Arguments:
        - oh_manager (OHManager)
        - resolved_filename (str): New filename to write to
    """
    with open(resolved_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=RESOLVED_QUESTION_LOG_COLUMNS)
        writer.writeheader()

        entries = []
        for entry in oh_manager.get_resolved_entries():
            e = {}
            e['assignment'] = entry.get_assignment()
            e['question'] = entry.get_question()
            e['response_time'] = entry.get_response_time()
            e['response_ta'] = entry.get_response_ta().name
            e['ta_timeframe'] = entry.get_response_ta().get_oh_time_frame()

            entries.append(e)

        writer.writerows(entries)


def log_unresolved_questions(oh_manager, unresolved_filename):
    """
    Given an `oh_manager` and filename to write to, logs all of the manager's
    unresolved questions to the given filename. Note that the file will be
    overwritten if it already exists. The given filename will be written to
    as a CSV file using UNRESOLVED_QUESTION_LOG_COLUMNs as
    the column names.


    Arguments:
        - oh_manager (OHManager)
        - unresolved_filename (str): New filename to write to
    """
    with open(unresolved_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=UNRESOLVED_QUESTION_LOG_COLUMNS)
        writer.writeheader()

        entries = []
        for entry in oh_manager.get_resolved_entries():
            e = {}
            student = entry.get_student()
            e['student_uid'] = student.get_uid()
            e['student_name'] = student.get_name()
            e['student_email'] = student.get_email()
            e['assignment'] = entry.get_assignment()
            e['question'] = entry.get_question()
            entries.append(e)

        writer.writerows(entries)


# Given, do not change
def display_oh_header():
    """
    Prints a header for the interactive OH queue interface.

    Returns:
        - None
    """
    print('-' * 30)
    print('Office Hours')
    print('-' * 30)


# Given, do not change
def display_options():
    """
    Prints an option menu for the interactive OH queue.

    Returns:
        - None
    """
    print('OPTIONS:')
    print('A. Enter TA')
    print('B. Create Question Entry (For Students)')
    print('C. Answer Next Question Entry (For TAs)')
    print('D. End Office Hours and Log Information')
    print()


# Given, do not change
def oh_main():
    """
    The main UI for the interactive OH queue, providing features for queue
    management, such as adding TAs, creating question entries, answering
    active (unresolved) questions, and information-logging. Supports the
    following options:
    - A: Add a TA to the manager through user input prompts
    - B: Add an Entry with student information to the manager through user
         input prompts; the entry is marked with the current timestamp.
    - C: Answer the next question at the front of OH queue manager, marking
         it resolved with provided TA information
    - D: Exports the queue manager's resolved and unresolved question logs
         to respective CSV files.

    Return:
        - None
    """
    oh_manager = QueueManager()

    while True:
        display_oh_header()
        display_options()
        selection = input('Select a letter option from above: ')
        if selection.upper() == 'A':
            add_ta(oh_manager)
            print('Successfully added TA to session.')
            sleep(2)
        elif selection.upper() == 'B':
            time_of_day = localtime(time())
            entry_hour = time_of_day.tm_hour
            entry_min = time_of_day.tm_min
            entry_time = f'{entry_hour:02d}:{entry_min:02d}'

            student_name = input('Enter the student\'s name: ')
            student_uid = input('Enter the student\'s UID: ')
            student_year = input('Enter the student\'s Grade/Year: ')
            student_email = input('Enter the student\'s email: ')
            student = Student(student_uid, student_name, student_year,
                              student_email)

            entry_question = input('Enter your question: ')
            assignment = input('Enter the corresponding assignment ' +
                               'for your question: ')

            entry = Entry(entry_question, student, assignment, entry_time)
            oh_manager.add_entry(entry)
            print('Successfully submitted question entry.')
            sleep(2)
        elif selection.upper() == 'C':
            answer_next_question(oh_manager)
            sleep(2)
        elif selection.upper() == 'D':
            print('Creating resolved question file: ')
            resolved_filename = input('Enter filename: ')
            log_resolved_questions(oh_manager, resolved_filename)
            print('Creating unresolved question file:')
            unresolved_filename = input('Enter filename: ')
            log_unresolved_questions(oh_manager, unresolved_filename)
            quit()


if __name__ == '__main__':
    oh_main()
