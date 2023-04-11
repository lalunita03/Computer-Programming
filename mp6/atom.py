"""
CS 1 22fa
MP6: Crystal Lattices
Student Name: Lea Grohmann

A program defining a simple Atom class representing an element and
an (x, y, z) coordinate position.
"""


class Atom():
    """
    Simple class representation of an atom. Contains information on the
    represented element and (x, y, z) location of the atom in a lattice.

    Attributes:
        - element (str): element name of Atom, e.g. 'Fe'
        - coordinates (float, float, float): (x, y, z) coordinates of Atom
    """

    def __init__(self, element, coordinates):
        """
        Constructs an Atom instance representing the `element` with
        the specified (x, y, z) `coordinates`. While not recommended,
        negative coordinate values are supported, as long as coordinates
        are passed with exactly 3 values.

        Arguments
            - element (str): Name of element (e.g. 'Fe')
            - coordinates (tup): tuple holding (x, y, z) coordinates
              (e.g. (0.0, 0.5, 0.5))

        Raises:
            - ValueError if coordinates is not a 3-element tuple.
        """
        # Technically, we could raise a TypeError for not passing a tuple,
        # but simplifying here keep things concise.
        if type(coordinates) is not tuple or len(coordinates) != 3:
            raise ValueError('coordinates must be a 3-element tuple ' +
                             'representing (x, y, z) Atom coordinates.')

        self.element = element
        self.coordinates = coordinates

    def get_coordinates(self):
        """
        Returns the (x, y, z) coordinates of the this Atom.

        Returns:
            (tuple) - (x, y, z) coordinates of the Atom
        """
        return self.coordinates

    def __str__(self):
        """
        Returns a string representation of this Atom (e.g 'Fe, 0.0 0.0 0.0')

        Returns:
            (str) - representation of this Atom and its coordinates
        """
        (x, y, z) = self.coordinates
        # the standard .xyz file format for an Atom line
        return f'{self.element} {x} {y} {z}'
