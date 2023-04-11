"""
CS 1 22fa Final Exam
Part C: OH Queue Manager
Student Name: TODO

Part C.1 Exercises
"""


class Student:
    """
    Represents a simple Student with the following information:

    Attributes:
        - uid (str): Unique student identifier
        - name (str): Full name of the student
        - year (str): Current year status of the student (e.g. 'Freshman')
        - email (str): email of record for the student, ideally ending
                       with '@<school>.edu'
    """
    def __init__(self, uid, name, year, email):
        """
        Constructs a new Student with the following information:

        Arguments:
            - uid (str): Unique student identifier
            - name (str): Full name of student
            - year (str): Year status of student, e.g. 'Freshman'
            - email (str): School email of record for student
        """
        self.uid = uid
        self.name = name
        self.year = year
        self.email = email

    def get_uid(self):
        """
        Returns the uid (unique identifier) of the Student.

        Returns:
            - (str): The Student's uid
        """
        pass  # TODO C.1.1a

    def get_name(self):
        """
        Returns the full name of the student.

        Returns:
            - (str): The Student's full name
        """
        pass  # TODO C.1.1b

    def get_year(self):
        """
        Returns the year status of the Student, such as 'Freshman'.

        Returns:
            - (str): The Student's year status
        """
        pass  # TODO C.1.1c

    def get_email(self):
        """
        Returns the uid (unique identifier) of the Student.

        Returns:
            - (str): The Student's email address (e.g. 'lhovik@caltech.edu')
        """
        pass  # TODO C.1.1d

    def __str__(self):
        """
        Returns the string representation of the student, in the form:
        'Name: <full name>\nUID: <student uid>\nEmail: <email>\nYear: <year>'

        Returns:
            - (str): The specified string representation of the Student
        """
        pass  # TODO C.1.2


class TA(Student):
    """
    A TA is a simple subclass of the Student class, with additional information
    unique to a TA. Any 'HH:MM' time formats are in 24-hour units (e.g. '13:00'
    for 1PM).

    Attributes:
        - (see Student class documentation for inherited attributes)
        - oh_start_time (str): The TA's scheduled OH start time,
          in 'HH:MM' format.
        - oh_end_time (str): The TA's scheduled OH end time,
          in 'HH:MM' format.
    """
    def __init__(self, uid, name, year, email, oh_start_time, oh_end_time):
        """
        Constructs a TA with the given information.

        Arguments:
            - uid (str): Unique student identifier
            - name (str): Full name of the TA
            - year (str): Current year status of the TA (e.g. 'Junior')
            - email (str): email of record for the TA, ideally ending
              with '@<school>.edu', such as 'lhovik@caltech.edu'
            - oh_start_time (str): TA's assigned start time in form 'HH:MM'
            - oh_end_time (str): TA's assigned start time in form 'HH:MM'
        """
        super().__init__(uid, name, year, email)
        self.oh_start_time = oh_start_time
        self.oh_end_time = oh_end_time

    def get_oh_time_frame(self):
        """
        Returns a (str, str) tuple of the TA's scheduled OH, representing
        the start time and end time for their OH, both in 'HH:MM' format
        (24-hour notation).

        Returns:
            - (str, str): This TA's schedule OH start/end times
        """
        pass  # TODO C.1.3
