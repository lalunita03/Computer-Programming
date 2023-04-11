"""
CS 1 22fa
MP6: Crystal Lattices
Student Name: Lea Grohmann

Provides functionality for creating "Simple" CubicLattices, "Body-Centered"
CubicLattices, and "Face-Centered" Cubic Lattices.
"""
from atom import Atom
from lattice import CubicLattice


# Provided Function for Part D
def get_corner_atoms(element, lparam):
    """
    Returns a list of corner Atoms, all having the specified `element` name
    and with each having an (x, y, z) position at one of the corners for a
    cube of `lparam` length.

    The origin corner is set to (0, 0, 0) and the diagonally-opposite corner at
    (length, length, length). For example, if length is 2, the Atom positioned
    at the origin corner would still have coordinates (0, 0, 0), but the
    diagonally-opposite Atom would have coordinates (2, 2, 2).

    Arguments:
        - element (str): name to give to each corner Atom
        - lparam (int): length of cube to scale corners by

    Returns:
        - (list[Atom]): list of 8 corner Atoms having positions distributed in
          a cube of length `lparam`.
    """
    atoms = []
    # Corner positions for a unit cube (1 corresponds to length of cube)
    CORNERS = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
               (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    for (x, y, z) in CORNERS:  # 8 corners
        # Scale the corners by lparam
        scaled_corner = (float(x * lparam), float(y * lparam),
                         float(z * lparam))
        atoms.append(Atom(element, scaled_corner))
    return atoms


def create_SC(element, lparam):
    """
    Returns a SC (Simple) CubicLattice comprised of atoms of the passed
    element and having the specified lattice parameter.
    The lattice will have a collection of Atoms positioned to represent a
    simple CubicLattice, defined as having exactly 8 corner atoms.

    Arguments:
        - element (str): element name of all Atoms in the returned lattice
        - lparam (int/float): lattice parameter (length) of returned lattice

    Returns:
        - (CubicLattice) - CubicLattice in a SC form comprised of `element`
          Atoms and having the passed lattice parameter.
    """
    atoms = get_corner_atoms(element, lparam)
    return CubicLattice(lparam, atoms=atoms)


def create_BCC(element, lparam):
    """
    Returns a BCC (Body-Centered) CubicLattice comprised of atoms
    (of the passed element) and having the specified lattice parameter.
    The lattice will have a collection of Atoms positioned to represent a
    body-centered lattice, defined as having 8 corner atoms and 1 center atom.

    Arguments:
        - element (str): element name of all Atoms in the returned lattice
        - lparam (int/float): lattice parameter (length) of returned lattice

    Returns:
        - (CubicLattice) - CubicLattice in a BCC form comprised of `element`
          Atoms and having the passed lattice parameter.
    """
    atoms = get_corner_atoms(element, lparam)
    center_coords = (lparam / 2, lparam / 2, lparam / 2)
    atoms.append(Atom(element, center_coords))
    return CubicLattice(lparam, atoms=atoms)


def create_FCC(element, lparam):
    """
    Returns a FCC (Face-Centered Cubic) CrystalLattice comprised of atoms
    (of the passed element) and having the specified lattice parameter.
    The lattice will have a collection of Atoms positioned to represent a
    face-centered lattice, defined as having 8 corner atoms and 6 face atoms.

    Arguments:
        - element (str): element name of all Atoms in the returned lattice
        - lparam (int): lattice parameter (length) of returned lattice

    Returns:
        - (CubicLattice) - CubicLattice in a FCC form comprised of `element`
          Atoms and having the passed lattice parameter.
    """
    atoms = get_corner_atoms(element, lparam)
    FACES = [(0.5, 0.5, 0.0), (0.5, 0.0, 0.5), (0.0, 0.5, 0.5),
             (1.0, 0.5, 0.5), (0.5, 1.0, 0.5), (0.5, 0.5, 1.0)]

    for (x, y, z) in FACES:
        face_coords = (x * lparam, y * lparam, z * lparam)
        atoms.append(Atom(element, face_coords))

    return CubicLattice(lparam, atoms=atoms)
