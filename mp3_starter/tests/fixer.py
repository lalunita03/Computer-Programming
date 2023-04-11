"""
Student name: Lea Grohmann

This program provides a functions that fix files by replacing
all tabs in a file with spaces.
"""


import os


def tabs_to_spaces(filename, tab_length):
    """
    replaces all tabs in a file with spaces and creates a new file.
    Prints how many tabs were replaced and how many lines had tabs.

    Arguments:
        `filename` (string) - name of file to be used
        `tab_length` (int) - number of spaces that replace one tab
    
    Returns:
        N/A

    """
    if not os.path.exists(filename):
        print(f'{filename} not found. Aborting.')
    
    else:
        file = open(filename, 'r')
        spaced_file = open('spaced_' + filename, 'w')
        lines_with_tabs = 0
        tabs_replaced = 0

        for line in file:
            # adds 1 when statement is True, 0 when statement is False
            lines_with_tabs += '\t' in line
            tabs_replaced += line.count('\t')
            line = line.replace('\t', ' ' * tab_length)
            spaced_file.write(line)
        
        file.close()
        spaced_file.close()

        print(f'Lines with tabs: {lines_with_tabs}')
        print(f'Tabs replaced: {tabs_replaced}')
