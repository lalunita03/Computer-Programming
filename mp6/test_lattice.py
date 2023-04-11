from lattice import *
from lattice_client import *
from atom import Atom
import os
import random
import pytest

TEST_COORDS_1 = [(0, 0, 0), (1, 1, 1), (.5, .5, .5)]

ATOM_ORIGIN = [Atom('Ir', (0, 0, 0))]
ATOM_CORNER = [Atom('Au', (1, 1, 1))]
ATOM_TWO_AXES = [Atom('Pt', (0, 1, 1))]
ATOM_ONE_AXIS = [Atom('Y', (1, 0, 0))]
ATOM_CENTER = [Atom('Fe', (.5, .5, .5))]
ATOM_CORNER_DOUBLE_ATOM_FACE = [
    Atom('H', (1, 1, 1)),
    Atom('O', (1, 1, 0)),
    Atom('O', (1, 0, 1))
]

ATOM_INPUTS = [
    ATOM_ORIGIN, ATOM_CORNER, ATOM_TWO_AXES, 
    ATOM_CORNER_DOUBLE_ATOM_FACE,
    ATOM_CENTER
]


def _gen_lattice_param_test_inp(a_list):
    """
    Generates a random test lattice for an atom list. 
    """
    return (a_list, random.randint(1, 50))


@pytest.mark.parametrize('atom_list, lp', [_gen_lattice_param_test_inp(inp)
                                           for inp in ATOM_INPUTS])
def test_get_lattice_parameter(atom_list, lp):
    assert CubicLattice(lp, atom_list).get_lattice_parameter() == lp


@pytest.mark.parametrize('atom_list, expected_elements', [(ATOM_ORIGIN, ['Ir']), (ATOM_CORNER_DOUBLE_ATOM_FACE, ['H', 'O']), ([*ATOM_ORIGIN, *ATOM_CORNER, *ATOM_ORIGIN, *ATOM_CORNER], ['Ir', 'Au'])])
def test_get_unique_elements(atom_list, expected_elements): 
    assert CubicLattice(1, atom_list).get_unique_elements() == expected_elements

@pytest.mark.parametrize('atom_list,lp', [_gen_lattice_param_test_inp(inp)
                                           for inp in ATOM_INPUTS])
def test_cell_volume(atom_list, lp):
    assert CubicLattice(lp, atom_list).get_cell_volume() == lp * lp * lp

@pytest.mark.parametrize('atom_list,expected_coord', [(ATOM_CORNER, ATOM_ORIGIN), (ATOM_TWO_AXES, ATOM_ONE_AXIS)])
def test_inverted_cell(atom_list, expected_coord):
    og_crystal = CubicLattice(1, atom_list)
    original_atoms = og_crystal.atoms
    # print(f'{original_atoms=}')
    inverted_crystal = og_crystal.get_inverted_cell()
    assert inverted_crystal.atoms[0].coordinates == expected_coord[0].coordinates
    assert og_crystal.atoms == original_atoms # Assure no overwrite


@pytest.mark.parametrize('atom_list,lp,expected',
                         [(ATOM_CORNER, 2, 1), (ATOM_TWO_AXES, 2, .5),
                          (ATOM_CORNER_DOUBLE_ATOM_FACE, 2, 2)])
def test_number_atoms(atom_list, lp, expected):
    assert CubicLattice(lp, atom_list).get_number_atoms() == expected 



IRON_BCC_FNAME = 'iron_bcc_out.xyz'
IRON_BCC = create_BCC('Fe', 3.5) 

ALUMINUM_FCC_FNAME = 'aluminum_fcc_out.xyz'
ALUMINUM_FCC = create_FCC('Al', 4) 

POLONIUM_SC_FNAME = 'polonium_sc_out.xyz'
POLONIUM_SC = create_SC('Po', 3.34)

@pytest.mark.parametrize('crystal,crystal_name,act_filename', [(IRON_BCC, 'Iron BCC', IRON_BCC_FNAME), (ALUMINUM_FCC, 'Aluminum FCC', ALUMINUM_FCC_FNAME), (POLONIUM_SC, 'Polonium SC', POLONIUM_SC_FNAME)])
def test_create_and_write(crystal, crystal_name, act_filename):
    crystal.write_to_xyz(crystal_name, os.path.join('student_files/', act_filename))
    
    with open(os.path.join('test_files/', f'{act_filename}')) as test_dat: 
        test_out = test_dat.readlines() 

    standardized_stud_out = ''
    with open(os.path.join('student_files', f'{act_filename}')) as stud_dat: 
        stud_out = stud_dat.readlines()
        # First, check that the number of lines is equal
        assert len(stud_out) == len(test_out)

        # Check that # of atoms is the same
        assert test_out[0] == stud_out[0]
        # Check that crystal name is the same
        assert test_out[1] == stud_out[1]

        # standardize both outs to floats (accepts 0 vs. 0.0, but 
        # requires 2.5 not 2)
        # Remove first two lines already tested
        test_out = test_out[2:]
        stud_out = stud_out[2:]
        standardized_stud_out = []
        standardized_test_out = []

        # First, standardize lines to use floats for all coordinate values
        for i, line in enumerate(stud_out):
            expected_line = test_out[i] 
            # Each atom line should have 4 components 'el x y z'
            assert line.count(' ') == 3
            # Standardize student output comparison to floats
            # Get actual values for each atom line
            (element_act, x_act, y_act, z_act) = line.split()
            # Get expected values for each atom line
            (element_exp, x_exp, y_exp, z_exp) = expected_line.split()
            standardized_stud_out.append(f'{element_act} {float(x_act)} {float(y_act)} {float(z_act)}\n')
            standardized_test_out.append(f'{element_exp} {float(x_exp)} {float(y_exp)} {float(z_exp)}\n')

        # Now that everything's standardized, sorting can be used to
        # assert expected xyz representation
        standardized_stud_out.sort()
        standardized_test_out.sort()
        assert standardized_stud_out == standardized_test_out


@pytest.mark.parametrize('in_filename, reference', [(IRON_BCC_FNAME, IRON_BCC), (ALUMINUM_FCC_FNAME, ALUMINUM_FCC), (POLONIUM_SC_FNAME, POLONIUM_SC)])
def test_read_xyz(in_filename, reference):
    created_crystal = CubicLattice(1.0, in_filename=f'test_files/{in_filename}')
    actual_coords = [atom.coordinates for atom in created_crystal.atoms] 
    actual_coords = [(float(x), float(y), float(z)) for (x, y, z) in actual_coords] 
    exp_coords = [atom.coordinates for atom in reference.atoms]
    exp_coords = [(float(x), float(y), float(z)) for (x, y, z) in exp_coords] 
    # Sort to ignore ordering differences, as long as the contents are correct  
    actual_coords.sort()
    exp_coords.sort()
    assert actual_coords == exp_coords

