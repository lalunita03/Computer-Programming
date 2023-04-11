"""
CS1 22fa MP5 Provided Utils

Factors out a utility CSV processing function to generate a dictionary
mapping column names to an ordered list of values in that column.

Generalized to work with any CSV file. Students do not need to modify this
at all, and it is imported for them in mp5_partb.py (they are welcome to use it
in mp5_partc.py as well).

Note: In practice, there are other libraries we can use to quickly work with
CSV/tabular data in Python and Matplotlib, including pandas. Using such
libraries is preferred in general, but we intentionally do not teach pandas
in CS 1 in order to keep the material in scope (pandas is very useful, but
introduces a lot of new terminology/paradigms that is more useful to learn
after a foundation in CS1).
"""
import csv
import os


# Given
def collect_column_data(filename):
    """
    Given a filename string corresponding to a CSV file,
    returns a dictionary of column-based data, where each
    key corresponds to a column name and maps to a list of values
    (in order) for that column in the CSV file.

    So if the CSV file has 4 columns and 10 rows of data (ignoring column
    headers), the result would be a dictionary of 4 keys each mapping
    to a 10-element list.

    Each list holds data as strings to generalize for different datasets.
    Anyone using this function should convert the types as needed for their
    application.

    Arguments:
        - filename (str): Filename of CSV file to process
    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
        return {}
    else:
        with open(filename, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            result = {}
            # Initialize the keys for the result dictionary with empty
            # lists we'll populate with row data
            for column_name in csvreader.fieldnames:
                result[column_name] = []

            for row in csvreader:
                # We have to do a nested loop since we're processing row-by-row
                # but need to collect each key=value pair for the result dict
                for column_name, value in row.items():
                    result[column_name].append(value)
            return result
