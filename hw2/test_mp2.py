# Version: 22fa
from mp2_mastermind import *


def test_make_random_code():
    """
    Tests the random_code() function for MP2.
    """
    colors = 'RGBYOW'
    used = list(colors)
    for i in range(200):
        code = make_random_code()
        assert len(code) == 4
        for char in code:
            assert char in colors
            if char in used:
                # remove the character from used; we expect this to be empty
                # after 200 runs
                used.remove(char)

    assert len(used) == 0 # all characters should have been used at some point


def make_random_codes(n):
    codes = []
    for _ in range(n):
        # We assume that make_random_code() works.
        codes.append(make_random_code())
    return codes


def test_count_exact_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        # count_exact_matches should always be a value between 0 (the '----' case)
        # and 4 (the 'bbbb' case)
        assert 0 <= count_exact_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_exact_matches('RRRR', 'RRRR') == 4
    assert count_exact_matches('RRRR', 'OOOO') == 0
    assert count_exact_matches('RROO', 'OORR') == 0
    assert count_exact_matches('RORR', 'RROR') == 2
    assert count_exact_matches('RORY', 'RYOR') == 1
    assert count_exact_matches('RGRY', 'RGRR') == 3
    assert count_exact_matches('RGBY', 'GBYR') == 0
    assert count_exact_matches('RGBY', 'RGOO') == 2
    assert count_exact_matches('RGBY', 'RWBW') == 2
    assert count_exact_matches('RGBY', 'WOWO') == 0


def test_count_letter_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        assert 0 <= count_letter_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'GBYR') == 4
    assert count_letter_matches('ROGO', 'RRGG') == 2
    assert count_letter_matches('RGBY', 'OROG') == 2
    assert count_letter_matches('RGBY', 'BWBR') == 2
    assert count_letter_matches('RBBY', 'GRBO') == 2
    assert count_letter_matches('RGBY', 'WOWO') == 0


def test_compare_codes():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        comp = compare_codes(c1, c2)
        assert len(comp) == 4
        for char in comp:
            assert char in 'bw-'

    # Check specific answers.
    assert compare_codes('RGBY', 'RGBY') == 'bbbb'
    assert compare_codes('RGBY', 'GBYR') == 'wwww'
    assert compare_codes('RGBY', 'OROG') == 'ww--'
    assert compare_codes('RGBY', 'BWBR') == 'bw--'
    assert compare_codes('RGBY', 'WOWO') == '----'

