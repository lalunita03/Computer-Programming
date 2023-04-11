"""
CS 1 Fall 2022 MP7
MP7 Provided DNA.py for reference in Porting Python to Java (students
do not need to modify this program in MP7).
Original Author: El Hovik

Defines a DNA class representing a single strand of DNA comprised
of the 4 base nucleotides, 'A', 'T', 'C', 'G'.
"""


class DNA:
    """
    Represents a DNA strand comprised of 4 base nucleotides. Each nucleotide
    is one of 'A', 'T', 'C', 'G' (standardized to uppercase).

    Attributes:
        - seq (str): Sequence string of DNA nucleotide bases.
    """
    # not required but a useful class constant
    BASES = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    def __init__(self, seq):
        """
        Initializes a new DNA sequence using the provided seq str.
        Case insensitivity is supported for the given seq, but a DNA sequence is
        standardized in upper-case.

        Arguments:
            - seq (str): sequence of 'A', 'T', 'C', 'G' bases.

        Raises:
            - ValueError if provided seq is not comprised of ATCG
              nucleotide bases.
        """
        seq = seq.upper()
        for base in seq:
            if base != 'A' and base != 'T' and base != 'C' and base != 'G':
                err_msg = 'Invalid DNA sequence. Must only contain ' + \
                          'ATCG bases.'
                raise ValueError(err_msg)
        self.seq = seq

    def __str__(self):
        """
        Returns the string representation of this DNA strand, which is simply
        the sequence of nucleotides.

        Returns:
            - (str): String representation of this DNA strand, e.g. 'ATACGC'
        """
        return self.seq

    def __len__(self):
        """
        Returns the length of the DNA, defined as the number of bases in
        its sequence.

        Returns:
            - (int): length of this DNA strand
        """
        return len(self.seq)

    def base_complement(self, base):
        """
        Returns the complement of the provided base character,
        ignoring letter-case (the complement is returned in upper-case).

        Arguments:
            - base (str): nucleotide base character

        Returns:
            - (str): complement of `base`, in upper-case

        Raises:
            - ValueError if the passed base is not a valid DNA nucleotide base.
        """
        base = base.upper()
        if base == 'A':
            return 'T'
        elif base == 'T':
            return 'A'
        elif base == 'C':
            return 'G'
        elif base == 'G':
            return 'C'
        else:
            raise ValueError('Invalid base.')

    def complement(self):
        """
        Returns the complement DNA sequence. For example, if this DNA
        is comprised of the bases 'ATACGC', its complement is returned as
        'TATGCG'.

        Returns:
            - (str): the complement DNA sequence.
        """
        result = ''
        for ch in self.seq:
            result += self.base_complement(ch)
        return result

    def count_occurrences(self, base):
        """
        Returns the number of occurrences of the given nucleotide base,
        ignoring letter-casing.

        Arguments:
            - base (str): nucleotide base char (one of ATCG)

        Returns:
            - (int): count of given base in this sequence

        Raises:
            - ValueError if given an invalid base
        """
        base = base.upper()
        if base != 'A' and base != 'T' and base != 'C' and base != 'G':
            raise ValueError('Invalid base.')
        return self.seq.count(base)

    def percentage_of(self, base):
        """
        Returns the percentage of the given base (ignoring
        letter-casing) in this DNA sequence as a float value
        between 0.0 and 1.0. (100%). Note that the percentage of any
        valid base in an empty DNA will be considered 0.0 (but the base
        validation will take precedence).

        Arguments:
            - base (str) nucleotide base char (one of ATCG)

        Returns:
            - (float): Percentage of base between 0.0 and 1.0

        Raises:
            - ValueError if given an invalid base
        """
        # self.count_occurrences does the error-handling for use, so don't
        # duplicate it here
        occurrences = self.count_occurrences(base)
        if occurrences == 0:
            return 0.0  # handles '' case too
        return occurrences / len(self.seq)
