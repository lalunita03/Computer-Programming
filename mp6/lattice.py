"""
CS 1 22fa
MP6: Crystal Lattices
Student Name: Lea Grohmann

This program defines a CubicLattice class which represents the 3D crystal
arrangement of Atom's.

"""
import math
from atom import Atom


class CubicLattice():
    """
    Simple class representation of the crystal structure of a collection of
    atoms. Contains information about the location and element of each atom,
    the name of the crystal lattice, and the number of atoms in the crystal
    lattice. Contains functions to analyze properties of the crystal.

    Attributes:
        `lparam` (int/float) - the side length of the CubicLattice
        `atoms` (list) - list of Atom's that make up the CubicLattice
    """

    def __init__(self, lparam, atoms=[], in_filename=None):
        """
        Constructs a CubicLattice instance that represents the 3D lattice
        formed the `atoms`.

        Arguments:
            `lparam` (int/float) - lattice parameter of the cubic structure
                                    (must be positive) in Angstrom
            `atoms` (list) - list of Atom's (optional)
            `in_filename` (str) - filepath to an .xyz file with the relavant
                                  information about the atoms (optional)

        Raises:
            FileNotFound error if an invalid (non empty) filename is passed
            for `in_filename`
        """
        if lparam <= 0:
            raise ValueError('lparam must be positive.')
        self.lparam = lparam

        if in_filename is None:
            self.atoms = atoms
        else:
            self.atoms = self.get_atoms_from_xyz(in_filename)

    def get_lattice_parameter(self):
        """
        Returns the lattice parameter representing the length of each face of
        this CubicLattice. Assumes that the lattice is a cube so all face
        lengths are equal.

        Returns:
            (int/float) - lattice parameter in Angstroms
        """
        return self.lparam

    def get_cell_volume(self):
        """
        Returns the volume of this CubicLattice assuming that the structure
        is a cube.

        Returns:
            (int/float) - volume in Angstrom^3
        """
        return self.lparam**3

    def get_unique_elements(self):
        """
        Returns a list of the unique elements in this CubeLattice.

        Returns:
            (list) - list of string representing the unique elements
        """
        elements = []
        for atom in self.atoms:
            if not (atom.element in elements):
                elements.append(atom.element)
        return elements

    def get_number_atoms(self):
        """
        Calculates the relative number of atoms of the lattice based on the
        positions of the atoms

        Returns:
            (float) - relative number of atoms
        """
        number = 0.0
        for atom in self.atoms:
            coords = atom.get_coordinates()
            if is_corner(coords, self.lparam):
                number += 1 / 8
            elif is_cell_center(coords, self.lparam):
                number += 1
            elif is_face_center(coords, self.lparam):
                number += 1 / 2

        return number

    def get_inverted_cell(self):
        """
        Returns an inverted version of this lattice. Does not modify the
        orginal lattice

        Returns:
            (CubicLattice) - inverted lattice
        """
        inverted_atoms = []
        a = self.lparam
        for atom in self.atoms:
            (x, y, z) = atom.get_coordinates()
            inverted_coords = (abs(x - a), abs(y - a), abs(z - a))
            inverted_atom = Atom(atom.element, inverted_coords)
            inverted_atoms.append(inverted_atom)

        return CubicLattice(a, atoms=inverted_atoms)

    def as_xyz(self, crystal_name):
        """
        Returns a string representation of the crystal given
        a specified `crystal_name` that is in standard .xyz file format.

        An XYZ file format is strictly as follows (guaranteeing each
        Atom_I_Element line to be comprised of 4 components):

        # of atoms N
        Name of the crystal (basically a comment)
        Atom_1_Element Atom_1_X Atom_1_Y Atom_1_Z
        Atom_2_Element Atom_2_X Atom_2_X Atom_2_Z
        ...
        Atom_N_Element Atom_N_X Atom_N_Y Atom_N_Z

        For example (16 lines total):
        14
        Aluminum FCC
        Al 0 0 0
        ...
        Al 2.0 2.0 4

        Arguments:
            - crystal_name (str): Name of crystal to specify (the second
              line in .xyz format)

        Returns:
            - (str) .xyz data format of crystal, with each line ending with
              '\n' (including the last)
        """
        num_atoms = len(self.atoms)
        body = f'{num_atoms}\n{crystal_name}\n'

        for atom in self.atoms:
            (x, y, z) = atom.get_coordinates()
            body += f'{atom.element} {x} {y} {z}\n'

        return body

    def write_to_xyz(self, crystal_name, out_filename):
        """
        Writes the current crystal to an XYZ file, which is a standard
        file format compatible with 3D crystal-viewing software.
        See `CubicLattice.as_xyz` for more information on the XYZ
        representation.

        Note: Overwrites file if one already exists.

        Arguments:
            - crystal_name (str): Crystal name; the second line in .xyz file.
            - out_filename (str): Filename to write to (should end in .xyz)

        Returns:
            - None (crystal data is written to `out_filename`)
        """
        body = self.as_xyz(crystal_name)
        with open(out_filename, 'w') as xyz_file:
            xyz_file.writelines(body)

    def get_atoms_from_xyz(self, in_filename):
        """
        Given an in_filename, returns a list of Atoms created from the file
        specifications, which should be in valid .xyz format.
        See `CubicLattice.as_xyz` for a summary of a valid XYZ format.

        Note that the (x, y, z) coordinates specified by each XYZ Atom line
        are converted to floats for the list of constructed Atoms.

        Arguments:
            - in_filename (str): Name of .xyz file to import (e.g. 'ex1.xyz')

        Returns:
            - (list[Atom]): list of Atoms constructed from imported file data

        Raises:
            - FileNotFoundError if `in_filename` doesn't exist
        """
        atoms = []
        with open(in_filename) as xyz_file:
            num_atoms = int(xyz_file.readline())
            _ = xyz_file.readline()

            for i in range(num_atoms):
                atom_str = xyz_file.readline().strip()
                atom_list = atom_str.split(' ')
                coords = (float(atom_list[1]), float(atom_list[2]),
                          float(atom_list[3]))
                atoms.append(Atom(atom_list[0], coords))

        return atoms


# ----------------------------------------
# END CubicLattice class definition
# ----------------------------------------
# 3 helper _functions_ for lattice coordinates; note that these
# generalize for any 3D cube representation, not just 3D crystal lattices.
# DO NOT CHANGE these three functions.
def is_corner(coordinates, length):
    """
    Returns whether the given coordinates are on a corner of a cube with
    side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff passed coordinates match corners of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be 0 or
        # the length of the cube
        if coord != 0 and coord != length:
            return False
    return True


def is_cell_center(coordinates, length):
    """
    Returns whether the given coordinates are at the center of a
    cube with side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are the center of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be length/2
        # if it is the cube's center
        if coord != length / 2:
            return False
    return True


def is_face_center(coordinates, length):
    """
    Returns whether the given coordinates are on the center of a cube's _face_
    with side length `length`. In other words, they are not at one of the 8
    corners or the center of the cube.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are at the center of any of the 6
                  faces of a `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    # By definition, coordinates must not be a corner or the center of the cube
    return not (is_corner(coordinates, length) or
                is_cell_center(coordinates, length))
