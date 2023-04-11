"""
CS 1 22fa
MP6 Testing Program to test methods/functions in isolation;
use test_lattice.py for testing import/export functionality.
"""
from atom import Atom
from lattice import *  # import the CubicLattice and 3 helper functions
# Convenience function for sorting objects
from operator import attrgetter

# A.1.
def test_atom_unchanged():
    """
    Some tests to ensure Atom.py is unchanged outside of docstrings
    students are required to add.
    """
    fe0 = Atom('Fe', (0, 0, 0))
    assert fe0.element == 'Fe'
    assert fe0.coordinates == (0, 0, 0) or fe0.coordinates == (0., 0., 0.)
    k0 = Atom('K', (0, 0, 0))
    assert k0.element == 'K'
    k1 = Atom('K', (1.0, 1.0, 1.0))
    assert k1.element == 'K'
    assert k1.coordinates == (1.0, 1.0, 1.0)
    assert k1.coordinates == k1.get_coordinates()
    assert str(k1) == 'K 1.0 1.0 1.0'
    expected_value_error = False
    try:
        Atom('K', (1.0, 1.0, 1.0, 1.0))
    except ValueError:
        expected_value_error = True
    assert expected_value_error

    expected_value_error = False
    try:
        Atom('K', (1.0, 1.0))
    except ValueError:
        expected_value_error = True
    assert expected_value_error

    expected_value_error = False
    try:
        # They should not change the conditional
        Atom('K', [1.0, 1.0, 1.0])
    except ValueError:
        # Should still raise ValueError on 3-element list 
        expected_value_error = True
    assert expected_value_error


# B.1.
def test_lattice_constructor():
    """
    Tests CubicLattice constructor with atoms passed
    as an argument.
    """
    fe0 = Atom('Fe', (0.0, 0.0, 0.0))
    fe1 = Atom('Fe', (1.0, 1.0, 1.0))
    k0 = Atom('K', (1.0, 0.5, 0.5))
    # Single-atom 1x1x1 lattice test
    ex0 = CubicLattice(1.0, [fe0])
    assert ex0.lparam == 1.0
    assert ex0.atoms
    assert len(ex0.atoms) == 1
    assert ex0.atoms[0].element == 'Fe'

    # 2 corner fe atoms, 1x1x1 lattice test, testing atoms default
    # param syntax
    # Optional arguments can either be omitted or specified
    ex1 = CubicLattice(1.0, atoms=[fe0, fe1])
    assert ex1.lparam == 1.0
    assert ex1.atoms
    assert len(ex1.atoms) == 2
    assert ex1.atoms[0].element == 'Fe'
    assert ex1.atoms[1].element == 'Fe'
    assert ex1.atoms[0].get_coordinates() != \
           ex1.atoms[1].get_coordinates()

    # 2 corner fe atoms, 1 k atom in middle, 1x1x1 lattice test
    ex2 = CubicLattice(1.0, [fe0, k0, fe1])
    assert ex2.lparam == 1.0
    assert len(ex2.atoms) == 3
    assert ex2.atoms[0].element == 'Fe'
    assert ex2.atoms[1].element == 'K'
    assert ex2.atoms[2].element == 'Fe'
    assert ex2.atoms[0].get_coordinates() != \
           ex2.atoms[1].get_coordinates() 
    assert ex2.atoms[0].get_coordinates() != \
           ex2.atoms[2].get_coordinates() 
    assert ex2.atoms[1].get_coordinates() != \
           ex2.atoms[2].get_coordinates() 

    # Changing lparam
    # a center atom for lparam == 3
    na0 = Atom('Na', (1.5, 1.5, 1.5))
    ex3 = CubicLattice(3.0, [fe0, na0])
    assert ex3.lparam == 3.0
    assert ex3.atoms
    assert len(ex3.atoms) == 2
    assert ex3.atoms[1].get_coordinates() == (1.5, 1.5, 1.5)

    # Testing float vs. int lparam (1.5 should not be converted to int)
    ex4 = CubicLattice(1.5, [fe0, na0])
    assert ex4.lparam == 1.5

# B.1.
def test_lattice_constructor_default_atoms():
    """
    Tests to ensure atoms is supported as an optional 
    parameter, defaulting to [] if not specified.
    """
    # atoms should default to []
    # Optional arguments can either be omitted or specified
    ex1 = CubicLattice(1.0)
    ex2 = CubicLattice(1.5, atoms=[])
    assert ex1.atoms == []
    assert ex1.lparam == 1.0
    assert ex2.atoms == []
    assert ex2.lparam == 1.5


# B.2.
def test_lattice_get_lparam():
    fe0 = Atom('Fe', (0.0, 0.0, 0.0))
    ex0 = CubicLattice(1.0, [fe0])
    assert ex0.get_lattice_parameter() == 1.0
    assert ex0.get_lattice_parameter() == ex0.lparam

    ex1 = CubicLattice(2.0, [fe0])
    assert ex1.get_lattice_parameter() == 2.0
    assert ex1.get_lattice_parameter() == ex1.lparam

    fe2 = Atom('Fe', (0.75, 0.75, 1.5))
    ex2 = CubicLattice(1.5, [fe0, fe2])
    assert ex2.get_lattice_parameter() == 1.5
    assert ex2.get_lattice_parameter() == ex2.lparam

# B.4.
def test_get_unique_elements():
    """
    Tests B.4. using spec examples and additional edge cases. 
    """
    fe0 = Atom('Fe', (0.0, 0.0, 0.0))
    # Single fe atom case
    ex0 = CubicLattice(1.0, [fe0])
    ex0_elements = ex0.get_unique_elements()
    # Should return a list 
    assert isinstance(ex0_elements, list)
    # Should return a list of strings
    assert ex0_elements == ['Fe']

    # 3 different atom case
    fe1 = Atom('Fe', (0.5, 0.5, 0.5))
    na0 = Atom('Na', (0.0, 0.0, 0.0))
    k0 = Atom('K', (1.0, 1.0, 0.0))
    ex1 = CubicLattice(1.0, [fe0, na0, k0])
    ex1_elements = ex1.get_unique_elements()
    # sort to support different ordered results that
    # are still correct
    ex1_elements.sort()
    assert ex1_elements == ['Fe', 'K', 'Na']

    # 2 same elements, 2 other element case
    ex2 = CubicLattice(1.0, [fe0, na0, fe1, k0])
    ex2_elements = ex2.get_unique_elements()
    ex2_elements.sort()
    assert ex2_elements == ['Fe', 'K', 'Na']

    # Empty lattice case, unique elements should be []
    empty_crystal = CubicLattice(1.0)
    empty_elements = empty_crystal.get_unique_elements()
    assert empty_elements == [] # atoms defaults to []


# B.5.
def test_get_number_atoms_unit_one_atom():
    """
    Tests B.4. for 1x1x1 lattice with 1 atom (each type tested)
    """
    # Example 0: A simple 1x1x1 lattice with a corner atom
    assert is_corner((0., 0., 0.), 1) 
    fe0 = Atom('Fe', (0., 0., 0.))
    ex0 = CubicLattice(1, [fe0])  # (0., 0., 0.) is a corner 
    test0 = ex0.get_number_atoms()
    assert test0 == 0.125  # 1/8

    # Example 1: A simple 1x1x1 lattice with a single cell-centered atom
    assert not is_corner((.5, .5, .5), 1)   # not a corner
    assert is_cell_center((.5, .5, .5), 1)  # a center atom
    fe1 = Atom('Fe', (.5, .5, .5))
    ex1 = CubicLattice(1, [fe1])  # (.5, .5, .5) with a lattice parameter of 1 is the center 
    test1 = ex1.get_number_atoms()
    # get_number_atoms should always return a float
    assert test1 == 1.0  # 1/1

    # Example 2: A simple 1x1x1 cubic lattice with a single face-centered atom
    assert is_face_center((.5, .5, 0.), 1)
    fe2 = Atom('Fe', (.5, .5, 0.))
    ex2 = CubicLattice(1, [fe2]) # (.5, .5, 0.) with a lattice parameter of 1 is on a face
    test2 = ex2.get_number_atoms()
    assert test2 == 0.5  # 1/2


# B.5.
def test_get_number_atoms_unit_multiple_atoms():
    """
    Tests B.4. for 1x1x1 lattice with multiple atoms.
    """

    # Example 3: A 1x1x1 lattice with 1 center + 1 corner
    fe1 = Atom('Fe', (.5, .5, .5)) 
    na0 = Atom('Na', (0., 0., 0.))
    ex3 = CubicLattice(1, [fe1, na0]) # 1 center atom + 1 corner atom
    test3 = ex3.get_number_atoms()
    assert test3 == 1.125  # 1 + 1/8

    # Example 4: A 1x1x1 lattice with 3 corner atoms
    fe0 = Atom('Fe', (0.0, 0.0, 0.0))
    fe3 = Atom('Fe', (1.0, 1.0, 1.0))
    na1 = Atom('Na', (1.0, 0.0, 0.0))
    ex4 = CubicLattice(1, [fe0, fe3, na1])  # 3 corners 
    test4 = ex4.get_number_atoms()
    assert test4 == 0.375  # 1/8 + 1/8 + 1/8


# B.5.
def test_get_number_atoms_change_lparam():
    """
    Tests B.5. for different lparam values.
    """

    # Example 5: A 3x3x3 lattice with a single corner atom
    assert is_corner((0., 0., 0.), 1) 
    assert is_corner((0., 0., 0.), 3) 
    fe0 = Atom('Fe', (0.0, 0.0, 0.0))  # still a corner atom
    ex5 = CubicLattice(3, [fe0]) 
    test5 = ex5.get_number_atoms()
    assert test5 == 0.125  # 1/8, same as test0

    # Example 6: A 3x3x3 lattice with corner and face(s)
    al0 = Atom('Al', (3.0, 3.0, 3.0))
    # Not a corner when lparam is 1.0
    assert not is_corner((3.0, 3.0, 3.0), 1.0)
    assert is_corner((3.0, 3.0, 3.0), 3.0)

    # both face atoms for 3.0 lparam
    al1 = Atom('Al', (3.0, 1.5, 3.0))
    assert not is_corner((3.0, 1.5, 3.0), 3)
    assert is_face_center((3.0, 1.5, 3.0), 3)

    al2 = Atom('Al', (3.0, 3.0, 1.5))
    assert is_face_center((3.0, 3.0, 1.5), 3)

    # 1 corner + 1 face
    ex6 = CubicLattice(3.0, [al0, al1])
    test6 = ex6.get_number_atoms()
    assert test6 == 0.625  # 1/8 + 1/2

    # 1 corner + 2 faces
    ex7 = CubicLattice(3.0, [al0, al1, al2]) 
    test7 = ex7.get_number_atoms()
    assert test7 == 1.125  # 1/8 + 1/2 + 1/2

    # 1 corner + 2 faces + 1 center
    al3 = Atom('Al', (1.5, 1.5, 1.5))
    ex8 = CubicLattice(3.0, [al0, al1, al2, al3])
    test8 = ex8.get_number_atoms()
    assert test8 == 2.125  # 1/8 + 1/2 + 1/2 + 1

def compare_atom_lists(atoms1, atoms2):
    """
    Returns whether two lists of Atoms contain
    the same Atom information, ignoring order.
    """
    # First, check lengths
    assert len(atoms1) == len(atoms2)
    # Next, sort before checking values
    atoms1_sorted = sorted(atoms1, key=attrgetter('element', 'coordinates')) 
    atoms2_sorted = sorted(atoms2, key=attrgetter('element', 'coordinates')) 
    # Now that they are sorted, we check each atom's element and coordinates
    for i, atom1 in enumerate(atoms1_sorted):
        atom2 = atoms2_sorted[i]
        assert atom1.element == atom2.element
        assert atom1.coordinates == atom2.coordinates

# B.6.
def test_get_inverted_cell():
    # variables are suffixed with coordinates to make it easier
    # to reason about. Requires __init__ constructor
    # to work correctly.
    fe000 = Atom('Fe', (0.0, 0.0, 0.0))
    fe111 = Atom('Fe', (1.0, 1.0, 1.0))
    na100 = Atom('Na', (1.0, 0.0, 0.0))
    ex4_orig_atoms = [fe000, fe111, na100]
    ex4 = CubicLattice(1.0, [fe000, fe111, na100])# 3 corners 
    ex4_atoms = ex4.atoms
    assert len(ex4.atoms) == 3

    for i, atom in enumerate(ex4_orig_atoms):
        # Should have the same str representation
        # we aren't using == in case students make copies of atoms
        # in constructor to implement immutability, which is
        # great, but not required.
        assert str(atom) == str(ex4_atoms[i])
    
    ex4_inverted = ex4.get_inverted_cell()
    expected_ex4_inverted_atoms = [Atom('Fe', (1.0, 1.0, 1.0)),
                                   Atom('Fe', (0.0, 0.0, 0.0)),
                                   Atom('Na', (0.0, 1.0, 1.0))]
    compare_atom_lists(ex4_inverted.atoms, expected_ex4_inverted_atoms)
    # The original ex4 CubicLattice should not be changed when
    # get_inverted_cell is called.
    # for i, atom in enumerate(ex4_orig_atoms):
    #     # Should have the same str representation
    #     # we aren't using == in case students make copies of atoms
    #     # in constructor to implement immutability, which is
    #     # great, but not required.
    #     assert str(atom) == str(ex4_atoms[i])

    # Testing case when lparam is > 1.0
    fe222 = Atom('Fe', (2.0, 2.0, 2.0))
    na200 = Atom('Na', (2.0, 0.0, 0.0))
    ex5_orig_atoms = [fe000, fe222, na200]
    ex5 = CubicLattice(2.0, ex5_orig_atoms) # changing lattice parameter

    expected_ex5_inverted_atoms = [Atom('Fe', (2.0, 2.0, 2.0)),
                                   Atom('Fe', (0.0, 0.0, 0.0)),
                                   Atom('Na', (0.0, 2.0, 2.0))]
    ex5_inverted = ex5.get_inverted_cell()
    compare_atom_lists(expected_ex5_inverted_atoms, ex5_inverted.atoms)

    # Testing inverting different corner positions 
    ex6_orig_atoms = [Atom('Fe', (1.0, 1.0, 1.0)),
                      Atom('Fe', (0.0, 0.0, 0.0)),
                      Atom('Fe', (1.0, 0.0, 0.0)),
                      Atom('Na', (0.0, 1.0, 0.0)),
                      Atom('Na', (0.0, 0.0, 1.0)),
                      Atom('Na', (1.0, 0.0, 1.0)),
                      Atom('Na', (0.0, 1.0, 1.0)),
                      Atom('Na', (1.0, 0.0, 1.0))]

    ex6 = CubicLattice(1.0, atoms=ex6_orig_atoms)
    expected_e6_inverted_atoms = [Atom('Fe', (0.0, 0.0, 0.0)),
                                  Atom('Fe', (1.0, 1.0, 1.0)),
                                  Atom('Fe', (0.0, 1.0, 1.0)),
                                  Atom('Na', (1.0, 0.0, 1.0)),
                                  Atom('Na', (1.0, 1.0, 0.0)),
                                  Atom('Na', (0.0, 1.0, 0.0)),
                                  Atom('Na', (1.0, 0.0, 0.0)),
                                  Atom('Na', (0.0, 1.0, 0.0))]
    ex6_inverted = ex6.get_inverted_cell()
    compare_atom_lists(expected_e6_inverted_atoms, ex6_inverted.atoms)

    # Testing inverting different positions with 1.5 lparam
    ex7_orig_atoms = [Atom('Fe', (1.5, 1.5, 1.5)),
                      Atom('Fe', (0.0, 0.0, 0.0)),
                      Atom('Na', (0.75, 0.75, 0.75)),
                      Atom('Fe', (0.75, 0.0, 0.75)),
                      Atom('Na', (0.0, 1.0, 0.0)),
                      Atom('Na', (0.0, 0.0, 1.5)),
                      Atom('Na', (1.5, 0.75, 0.75)),
                      Atom('Na', (1.5, 0.75, 0.0))]

    ex7 = CubicLattice(1.5, atoms=ex7_orig_atoms)
    expected_e7_inverted_atoms = [Atom('Fe', (0.0, 0.0, 0.0)),
                                  Atom('Fe', (1.5, 1.5, 1.5)),
                                  Atom('Na', (0.75, 0.75, 0.75)),
                                  Atom('Fe', (0.75, 1.5, 0.75)),
                                  Atom('Na', (1.5, 0.5, 1.5)),
                                  Atom('Na', (1.5, 1.5, 0.0)),
                                  Atom('Na', (0.0, 0.75, 0.75)),
                                  Atom('Na', (0.0, 0.75, 1.5))]
    ex7_inverted = ex7.get_inverted_cell()
    compare_atom_lists(expected_e7_inverted_atoms, ex7_inverted.atoms)

    # Testing empty lattice case
    ex8 = CubicLattice(1.5)
    ex8_inverted = ex8.get_inverted_cell()
    assert ex8_inverted.lparam == 1.5
    assert ex8_inverted.atoms == []
