"""
CS1 22fa MP5 Part A
Starter Code

Student Name: Lea Grohmann
"""
import numpy as np
import matplotlib.pyplot as plt
import math

GRAVITY = 9.81          # m/s^2
ANGLE_OF_LAUNCH = 45    # in degrees from horizon
INITIAL_VELOCITY = 150  # m/s

# Constants for plotting the single trajectory
# Note: We could use offset factors (e.g. 5%) here to generalize the
# label positioning large vs. small distances, but to make it easier
# to test without floating point subtleties, we will use constants
X_LABEL_OFFSET = 150
Y_LABEL_OFFSET = 10

# Default marker size for plotted points
MARKER_SIZE = 8
# Default line width for plotted trajectories
LINE_WIDTH = 2


# Exercise A.1.
def calculate_velocity():
    """
    Calculates the x and y components of the initial velocity, returns
    the velocities as a tuple

    Arguments:
        none

    Returns:
        (tuple) - represents the (initial x velocity, initial y velocity)
    """
    rad_angle = math.radians(ANGLE_OF_LAUNCH)
    vxi = INITIAL_VELOCITY * math.cos(rad_angle)
    vyi = INITIAL_VELOCITY * math.sin(rad_angle)
    return (vxi, vyi)


# Exercise A.2.
def calculate_position(dt):
    """
    Calculates and returns the (x, y) position after a given period of time
    (assumes the initial position is (0, 0) and there is no air resistance)

    Arguments:
        `dt` (int/float) - period of time in seconds

    Returns:
        (tuple) - (x, y) position of the object
    """
    (X0, Y0) = (0, 0)
    (vxi, vyi) = calculate_velocity()
    x = X0 + vxi * dt
    y = Y0 + vyi * dt - GRAVITY * dt**2 / 2
    return (x, y)


# Exercise A.3.
def flight_time():
    """
    Calculates the total flight time (abbreviated as tof) (assumes that
    the initial position is (0, 0) and there is no air resistance)

    Arguments:
        none

    Returns:
        (float) - total fight time, in s
    """
    (_, vyi) = calculate_velocity()
    tof = 2 * vyi / GRAVITY
    return tof


# Exercise A.4.
def generate_rocket_positions(tof):
    """
    Takes a total time of flight and generates a tuple that contains two
    lists (one for x and one for y), represeting the x and y coordinates
    during the objects flight time. (assumes that the initial position
    is (0, 0) and that there is no air resistance)

    Arguments:
        `tof` (float) - time of flight

    Return:
        (tuple) - tuple of lists, of the form (x positions, y positions)
    """
    xs = []
    ys = []
    for i in np.arange(0, tof, 0.1):
        px, py = calculate_position(i)
        xs.append(px)
        ys.append(py)
    # Handle the last coordinate case when y == 0.0 (rocket hits ground)
    if ys[-1] != 0.0:
        px, py = calculate_position(tof)
        xs.append(px)
        ys.append(py)
    return (xs, ys)


# Exercise: A.5.
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
    # (1146.788990825688, 573.3944954128439)
    (half_dist, max_y) = highest_pt
    # (2293.577981651376, 0.0)
    (total_dist, last_y) = landing_pt

    # Plot max height marker/label
    # '573m'
    maxh_label = f'{max_y:.0f}m'
    # (1296.788990825688, 583.3944954128439)
    maxh_label_coords = (half_dist + X_LABEL_OFFSET,
                         max_y + Y_LABEL_OFFSET)

    # Make sure you can reason about what these next statements do
    ax.annotate(maxh_label, xy=highest_pt, xytext=maxh_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(half_dist, max_y, marker='D', color=line_color,
            markersize=MARKER_SIZE)

    # Next, we plot the label marking the total distance traveled
    # (when the rocket lands)

    # '2294m'
    dist_label = f'{total_dist:.0f}m'
    # (996.788990825688, 10)
    dist_label_coords = (total_dist - X_LABEL_OFFSET,
                         Y_LABEL_OFFSET)

    ax.annotate(dist_label, xy=landing_pt, xytext=dist_label_coords,
                color=line_color, horizontalalignment='center')
    ax.plot(total_dist, last_y, marker='*', color=line_color,
            markersize=MARKER_SIZE)


# Exercise A.6.
def plot_launch(ax):
    """
    Plots the launch data on the provided `ax`, creating a trajectory
    line graph with two plotted points of interest (max height and total
    distance traveled). Also sets up the legend for the plot, including
    the trajectory line and markers for the max height and landing points.

    Arguments:
        - ax (Axes): Axes object to plot on

    Returns:
        - None
    """
    # Generate the x/y values for the line
    tof = flight_time()
    (xs, ys) = generate_rocket_positions(tof)

    # The highest point is exactly mid-launch
    highest_pt = calculate_position(tof / 2)

    # The rocket lands at the last (x, y) position
    landing_pt = (xs[-1], ys[-1])

    legend_label = f'Launch Trajectory ({tof:.1f}s)'

    lines = ax.plot(xs, ys, 'b--', label=legend_label, linewidth=LINE_WIDTH,
                    markersize=MARKER_SIZE)
    # The rest of the code below should be unmodified

    # Get the line color of the plotted line (lines is a list
    # of all lines plotted above, but we only have one)
    line_color = lines[0].get_color()

    # Pass the two points of interest to plot the labelled
    # points sharing the same line color as the line,
    # and passing the required Axes which contains state
    # and methods for the plot we've been modifying
    plot_labels(highest_pt, landing_pt, line_color, ax)


# Provided
def configure_plot(ax):
    """
    Configures the settings of the `ax` plot, including
    setting up the legend for the markers, defining the x and y
    axis bounds and labels, and the title of the plot.
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

    ax.set_title('Bottle Rocket Launch: Trajectory on Earth')


# Provided
def start():
    """
    "Launching point" of the program! Sets up the plotting configuration
    and initializes the plotting of the test launch data using this
    program's constants for an example initial velocity, angle, and gravity
    rate.
    """
    fig, ax = plt.subplots()
    plot_launch(ax)
    configure_plot(ax)
    fig.set_size_inches(8, 8)
    plt.show()


if __name__ == '__main__':
    start()
