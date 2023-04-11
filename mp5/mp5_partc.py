"""
CS1 22fa MP5 Part C

Student Name: Lea Grohmann

Brief Overview: This porogram analyzes the relationship between certain
                properties of planets and vizualizes them by plotting a graph
                (approved by Professor Hovik because of the conversion of mass
                to ln(mass))

Data Source(s): planets.csv
Data Science Question: What's the relationship between the mass of a
                    planet and the number of satilites of the planet?

Room for Improvement: There is no visable relationship between the mass of a
                    planet and the number of its satellites, it would be good
                    to look at different properties to see if there is a more
                    clear relationship
"""

import matplotlib.pyplot as plt
import csv
import math

X_LABEL_OFFSET = 1
Y_LABEL_OFFSET = -1

X_BOUND_OFFSET = 2
Y_BOUND_OFFSET = 5

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


def collect_column_data(col_name, filename):
    """
    Collects the data of one column in a csv file and returns data as a list

    Arguments:
        `col_name` (str) - name of the column
        `filename` (str) - name of the csv file

    Returns:
        (list) - list that stores the values of the entries in that column
    """
    col_data = []

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            col_data.append(row[col_name])

    return col_data


def scientific_to_float(number):
    """
    Converts a number in scientific notation to a float, for example
    '3.302×10^23' --> 3.302e+23

    Arguments:
        `number` (str) - number of form 'a×10^b'

    Returns:
        (float) - number in float notation
    """
    x_pos = number.find('×')
    hat_pos = number.find('^')

    base = float(number[:x_pos])
    exponent = float(number[hat_pos + 1:])

    return base * (10**exponent)


def plot_labels(name, mass, satellite, ax):
    """
    Plots the labels and points corresponding to a planet in the data set

    Arguments:
        `name` (str) - name of the planet
        `mass` (float/int) - mass of the planet (kg)
        `satellite` (int) - number of satellites of the planet
        `ax` (Axes) - Axes object to plot on

    Returns:
        none
    """
    ax.plot(mass, satellite, marker='*', color='#FFD700',
            markersize=MARKER_SIZE)

    planet_label_coords = (mass + X_LABEL_OFFSET, satellite + Y_LABEL_OFFSET)
    ax.annotate(name, xy=(mass, satellite), xytext=planet_label_coords,
                color='#FFD700', horizontalalignment='center')


def plot_planet_data(ax, filename):
    """
    Plots the natural log of a planet's mass (kg) vs its number of satellites.

    Arguments:
        `ax` (Axes) - Axes object to plot on
        `filename` (str) - name of the csv file containing the planet data
                        (must have the following columns: 'Name', 'Mass',
                        'Satellites', where 'Mass' must be written in
                        scientific notation)

    Returns:
        none
    """
    names = collect_column_data('Name', filename)
    masses = collect_column_data('Mass', filename)
    satellites = collect_column_data('Satellites', filename)

    assert len(names) == len(masses) == len(satellites)

    for i in range(len(masses)):
        masses[i] = math.log(scientific_to_float(masses[i]))
        satellites[i] = int(satellites[i])
        plot_labels(names[i], masses[i], satellites[i], ax)

    ax.set_facecolor('#000080')


def configure_plot(ax):
    """
    Configures the general settings of the plot such as, axis labels, chart
    title, and axis bounds

    Arguments:
        `ax` (Axes) - Axes object to plot on

    Returns:
        none
    """
    ax.set_xlabel('ln(Mass) in ln(kg)')
    ax.set_ylabel('# of Satellites')
    ax.set_title("Relationship between planets' masses and #'s of satellites")

    xbounds = ax.get_xbound()
    ybounds = ax.get_ybound()
    ax.set_xlim(xbounds[0] - X_BOUND_OFFSET, xbounds[-1] + X_BOUND_OFFSET)
    ax.set_ylim(ybounds[0], ybounds[-1] + Y_BOUND_OFFSET)


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of the planets' properties (mass and
    number of satellites) in planets.csv.

    """
    fig, ax = plt.subplots()

    plot_planet_data(ax, 'planets.csv')
    configure_plot(ax)

    fig.set_size_inches(8, 8)
    plt.show()


if __name__ == '__main__':
    start()
