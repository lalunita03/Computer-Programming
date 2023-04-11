"""
CS1 22fa MP5 Part B
Starter Code

Student Name: Lea Grohmann
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Separating this to keep things clean; this function
# returns a dictionary of { col -> [row values]}
# to make it easier to work with for plotting.
from mp5_utils import collect_column_data

# Constants for plotting the single trajectory
# We use offset factors here to generalize the label positioning
# for large vs. small distances
X_LABEL_OFFSET = 700
Y_LABEL_OFFSET = 50

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


# Exercise B.1.
def calculate_velocity(vi, launch_angle):
    """
    Calculates the x and y components of the initial velocity, returns
    the velocities as a tuple.

    Arguments:
        `vi` (int/float) - initial velocity of the object, in m/s
        `launch_angle` (int/float) - launch angle, in degrees from horizon

    Returns:
        (tuple) - represents the (initial x velocity, initial y velocity)
    """
    rad_angle = math.radians(launch_angle)
    vxi = vi * math.cos(rad_angle)
    vyi = vi * math.sin(rad_angle)
    return (vxi, vyi)


# Exercise B.2.
def calculate_position(dt, vi, launch_angle, gravity):
    """
    Calculates and returns the (x, y) position after a given period of time.
    (assumes that the initial position is (0, 0), and that there is no air
    resistance)

    Arguments:
        `dt` (int/float) - period of time in seconds
        `vi` (int/float) - initial velocity of the object, in m/s
        `launch_angle` (int/float) - launch angle, in degrees from horizon
        `gravity` (int/float) - gravity in m/s^2

    Returns:
        (tuple) - (x, y) position of the object
    """
    (X0, Y0) = (0, 0)
    (vxi, vyi) = calculate_velocity(vi, launch_angle)
    x = X0 + vxi * dt
    y = Y0 + vyi * dt - gravity * dt**2 / 2
    return (x, y)


# Exercise B.3.
def flight_time(vi, launch_angle, gravity):
    """
    Calculates the total flight time (abbreviated as tof) (assumes that
    the initial position is (0, 0) and that there is no air resistance)

    Arguments:
        `vi` (int/float) - initial velocity of the object, in m/s
        `launch_angle` (int/float) - launch angle, in degrees from horizon
        `gravity` (int/float) - gravity in m/s^2

    Returns:
        (float) - total fight time, in s
    """
    (_, vyi) = calculate_velocity(vi, launch_angle)
    tof = 2 * vyi / gravity
    return tof


# Exercise B.4.
def generate_rocket_positions(vi, launch_angle, gravity, tof):
    """
    Takes a total time of flight and generates a tuple that contains two
    lists (one for x and one for y), represeting the x and y coordinates
    during the objects flight time. (assumes that the initial position
    is (0, 0) and that there is no air resistance)

    Arguments:
        `vi` (int/float) - initial velocity of the object, in m/s
        `launch_angle` (int/float) - launch angle, in degrees from horizon
        `gravity` (int/float) - gravity in m/s^2
        `tof` (float) - time of flight

    Return:
        (tuple) - tuple of lists, of the form (x positions, y positions)
    """
    xs = []
    ys = []

    for i in np.arange(0, tof, 0.1):
        px, py = calculate_position(i, vi, launch_angle, gravity)
        xs.append(px)
        ys.append(py)

    # Handle the last coordinate case when y == 0.0 (rocket hits ground)
    if ys[-1] != 0.0:
        px, py = calculate_position(tof, vi, launch_angle, gravity)
        xs.append(px)
        ys.append(py)

    return (xs, ys)


# Exercise B.5.
def plot_trial_data(ax):
    """
    Processes trial data from trial_data.csv to compare launches
    on a single Axes `ax`.

    Plots points of interest on the `ax` for each trial with annotated
    labels for each point, sharing the corresponding line color.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    column_data = collect_column_data('trial_data.csv')
    trials = column_data['Trial']
    vis = column_data['Initial Velocity']
    launch_angles = column_data['Launch Angle (degrees)']
    gravities = column_data['Gravity']
    # Asserting an invariant pre-condition (should always be true,
    # independent of any user input). Don't use assert for error-handling.
    assert len(trials) == len(vis) == len(launch_angles) == len(gravities)

    trial_count = len(trials)

    for i in range(trial_count):
        launch_angle = int(launch_angles[i])
        gravity = int(gravities[i])
        vi = int(vis[i])
        trial_no = trials[i]
        tof = flight_time(vi, launch_angle, gravity)

        (xs, ys) = generate_rocket_positions(vi, launch_angle, gravity, tof)

        # The highest point is exactly mid-launch
        highest_pt = calculate_position(tof / 2, vi, launch_angle, gravity)

        # The rocket lands at the last (x, y) position
        landing_pt = (xs[-1], ys[-1])

        legend_label = f'Trial #{trial_no} ({tof:.1f}s)'
        lines = ax.plot(xs, ys, label=legend_label, linewidth=LINE_WIDTH,
                        markersize=MARKER_SIZE)

        # Gets the line color of the plotted line (since only one line
        # was plotted above, lines should be a list of 1 Line2D object).
        # This makes it easier to color plot labels with the same color as
        # the corresponding trajectory line.
        line_color = lines[0].get_color()

        # Pass the two points of interest to plot the labelled
        # points sharing the same line color as the line,
        # and passing the required Axes which contains state
        # and methods for the plot we've been modifying
        plot_labels(highest_pt, landing_pt, line_color, ax)


# Provided
def plot_labels(highest_pt, landing_pt, line_color, ax):
    """
    Plots the points of interest on the `ax` with annotated labels
    for each point, sharing the passed `line_color`.

    Arguments:
        - highest_point (int/float, int/float): (x, y) of launch peak
        - landing_pt (int/float, int/float): (x, y) of landing point
        - line_color (str): line color for labels to share with a plotted line
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # Plot total distance marker/label
    (half_dist, max_y) = highest_pt
    (total_dist, last_y) = landing_pt

    # Plot max height marker/label
    max_height_label = f'{max_y:.0f}m'
    max_label_coords = (half_dist + X_LABEL_OFFSET,
                        max_y + Y_LABEL_OFFSET)

    # Make sure you can reason about what these next statements do
    ax.annotate(max_height_label, xy=highest_pt,
                xytext=max_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(half_dist, max_y, marker='D',
            color=line_color, markersize=MARKER_SIZE)

    # Plot the label marking the total distance traveled
    dist_label = f'{total_dist:.0f}m'
    dist_label_coords = (total_dist - X_LABEL_OFFSET,
                         Y_LABEL_OFFSET)

    ax.annotate(dist_label, xy=landing_pt,
                xytext=dist_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(total_dist, last_y, marker='*',
            color=line_color, markersize=MARKER_SIZE)


# Provided
def configure_plot(ax):
    """
    Configures the settings of the `ax` plot, including
    setting up the legend for the markers, defining the x and y
    axis bounds and labels, and the title of the plot.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # A bit of a hack, but add the marker symbols to the legend
    # without adding a legend item for each plotted marker
    # Note: 'k' is the shorthand for black ('b' is blue)
    ax.plot([], [], 'k*', label='Max Distance', markersize=MARKER_SIZE)
    ax.plot([], [], 'kD', label='Max Height', markersize=MARKER_SIZE)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.legend(loc='upper left')
    X_BOUND_OFFSET = 100
    Y_BOUND_OFFSET = 100
    xbounds = ax.get_xbound()
    ybounds = ax.get_ybound()
    ax.set_xlim(xbounds[0] - X_BOUND_OFFSET, xbounds[-1] + X_BOUND_OFFSET)
    ax.set_ylim(ybounds[0], ybounds[-1] + (Y_BOUND_OFFSET))

    ax.set_title('Bottle Rocket Launch Experiments')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of launches based on trial_data.csv.
    """
    fig, ax = plt.subplots()
    plot_trial_data(ax)
    configure_plot(ax)
    fig.set_size_inches(12, 8)
    plt.show()


if __name__ == '__main__':
    start()
