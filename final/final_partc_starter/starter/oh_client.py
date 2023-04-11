"""
CS 1 22fa Final Exam
Part C: OH Queue Manager
Student Name: TODO

Part C.3 Exercises
"""

from oh_manager import QueueManager, Entry
from student import Student, TA
from time import localtime, time, sleep
import csv


RESOLVED_QUESTION_LOG_COLUMNS = ['assignment_name',
                                 'question',
                                 'response_time',
                                 'response_ta',
                                 'ta_timeframe']
UNRESOLVED_QUESTION_LOG_COLUMNS = ['student_uid',
                                   'student_name',
                                   'student_email',
                                   'assignment_name',
                                   'question']


def add_ta(oh_manager: QueueManager):
    ta_name = input("Enter the TA's name: ")
    ta_uid = input("Enter the TA's UID: ")
    ta_year = input("Enter the TA's Grade/Year: ")
    ta_email = input("Enter the TA's email: ")
    oh_start_time = input("Enter start time for your OH in HH:MM (hrs 0-23): ")
    oh_end_time = input("Enter end time for your OH in HH:MM (hrs 0-23): ")

    # TODO: C.3.1a Create a TA object with the information collected above
    # TODO: C.3.1b Add the created TA instance to oh_manager


def answer_next_question(oh_manager: QueueManager):
    ta_uid = input("Enter the answering TA's UID: ")
    ta = oh_manager.get_ta(ta_uid)
    if not ta:
        print("TA not found.")
    else:
        if len(oh_manager) <= 0:
            print("No currently unresolved questions found.")
            return
        entry = oh_manager.get_next_entry()
        print(entry)
        resolution_status = input('Enter "y" if the question is resolved. ')
        # TODO: C.3.2 Handle entry based on the resolution_status


def log_resolved_questions(oh_manager: QueueManager, resolved_filename: str):
    pass  # TODO: C.3.3


def log_unresolved_questions(oh_manager: QueueManager,
                             unresolved_filename: str):
    pass  # TODO: C.3.4


def display_oh_header():
    """
    Prints a header for the interactive OH queue interface.

    Returns:
        - None
    """
    print('-' * 30)
    print(f" Office Hours")
    print('-' * 30)


def display_options():
    """
    Prints a option menu for the interactive OH queue.

    Returns:
        - None
    """
    print('OPTIONS:')
    print('A. Enter TA')
    print('B. Create Question Entry (For Students)')
    print('C. Answer Next Question Entry (For TAs)')
    print('D. End Office Hours and Log Information')
    print()


def oh_main():
    """
    The main interactive OH queue, providing features for queue management,
    such as adding TAs, creating question entries, answering questions, and
    information logging.

    Return:
        - None
    """
    oh_manager = QueueManager()

    while True:
        display_oh_header()
        display_options()
        selection = input("Select a letter option from above: ")
        if selection.upper() == 'A':
            add_ta(oh_manager)
            print("Successfully added TA to session.")
            sleep(2)
        elif selection.upper() == 'B':
            time_of_day = localtime(time())
            entry_hour = time_of_day.tm_hour
            entry_min = time_of_day.tm_min
            entry_time = f'{entry_hour:02d}:{entry_min:02d}'

            student_name = input("Enter the student's name: ")
            student_uid = input("Enter the student's UID: ")
            student_year = input("Enter the student's Grade/Year: ")
            student_email = input("Enter the student's email: ")
            student: Student = Student(student_uid, student_name, student_year,
                                       student_email)

            entry_question = input("Enter your question: ")
            assignment_name = input("Enter the corresponding" +
                                    "assignment name for your question: ")

            entry: Entry = Entry(entry_question, student,
                                 assignment_name, entry_time)
            oh_manager.add_entry(entry)
            print("Successfuly submitted question entry.")
            sleep(2)
        elif selection.upper() == 'C':
            answer_next_question(oh_manager)
            sleep(2)
        elif selection.upper() == 'D':
            print("Creating resolved question file: ")
            resolved_filename = input("Enter filename: ")
            log_resolved_questions(oh_manager, resolved_filename)
            print("Creating unresolved question file:")
            unresolved_filename = input("Enter filename: ")
            log_unresolved_questions(oh_manager, unresolved_filename)
            quit()


if __name__ == '__main__':
    oh_main()
