"""
CS 1 Fall 2022
Final Exam Part B
Provided DNA.py for reference in the Final Exam Part B. A simplified
version of the DNA.py from MP7.

Defines a function compute_dna_errors to compute error scores for two
sequence strings representing DNA sequences.

Also defines a DNA class representing a single strand of DNA comprised
of the 4 base nucleotides, 'A', 'T', 'C', 'G', as well a possible
'?' characters for an unknown base. Other characters are not allowed
in the DNA sequence.

------------------------------------------------------------
B.4: Written Responses
Note: You should answer B.4 _after_ completing B.2 and B.3.
------------------------------------------------------------
B.4.1: Written Response (2 points)
2-3 sentences after implementing B.2 and B.3 discussing:
a. 1 advantage of the function-based approach of B.2 over B.3's OOP
- you don't need to create a whole DNA object to use check if two
sequences are matching
b. 1 advantage of the OOP-based approach of B.3 over over B.2's function
- the error handeling is already taken care of in the constructor of the
DNA class which makes it shorter and
------------------------------------------------------------
B.4.2: Written Responses
The following statements include various bugs and style issues students have
run into when working with functions and OOP. These are important to understand
at the end of CS1. Unlike Part A, you are welcome to write these in the
Python interpreter to check your answers as follows:

python3
>>> from partb import *  # loads your B.2 function and DNA class
>>> seq1_str = 'ACCtCGAGaTCCGTTTGA'
>>> ...

See spec for instructions of what is required for a. and b. answers.

seq3_str = 'AC?TCGAGAT?CGT?TA'
seq4_str = 'TTGTG?TCAG?G'
seq3_dna = DNA(seq3_str)
seq4_dna = DNA(seq4_str)

------------------------------------------------------------
B.4.2 Answers (6 points possible)
1. error_count = compute_dna_errors(seq3_dna, seq4_dna)
a. error
b. this function expects two strings as arguments but two DNA's are
being passed in which won't work. In this case the person should
review the how methods inside of classes work. Because the method
compute_dna_errors that is inside of the DNA class takes a DNA as
an argument. The person could just call the method on one of the
DNA's and then pass in the other one as an argument.
2. error_count = compute_dna_errors(seq3_dna.seq, seq4_dna.seq)
a. no error
b. no error
3. error_count = compute_dna_errors(seq3_dna.__str__(), seq4_dna.__str__())
a. error
b. the __str__() is not a method that should be called like that it works in
the background a better way of doing this would be str(seq3_dna).
4. error_count = compute_dna_errors(str(seq3_str), str(seq4_str))
a. error
b. both sequences are already strings so theres no point in converting them
to strings again
5. error_count = DNA.compute_dna_errors(DNA.self, seq4_dna)
a. error
b. you have to call the method on a DNA that is defined not on the name of the
class. DNA should be replaced by seq4_dna or seq3_dna because they are defined
and have a sequence stored in them. also DNA.self is not a thing and the method
should only have one argument
6. error_count = seq3_dna.compute_dna_errors(self, seq4_dna)
a. error
b. the method only takes one argument. self is not an argument that you have
to manually pass in it is passed in automatically. So the self should be
delted
7. error_count = seq3_dna.compute_dna_errors(seq4_dna)
a. no error
b. no error
8.
original_seq3_dna = seq3_dna
seq3_dna.seq = seq3_dna.complement()
error_count = compute_dna_errors(original_seq3_dna, seq3_dna)
# expected to be 0 when comparing a DNA with its exact complement counterpart

a. error
b. theres no complement method in DNA but if there was it would still be error.
it would be the same error that I described in 1.b
9.
try:
    seq1 = input('Provide a seq1: ')
    seq2 = input('Provide a seq2: ')
    error_count = compute_dna_errors(seq1, seq2)
    print(f'{error_count} errors found.')
except ValueError as err:
    raise ValueError(str(err))
a. no error
b. no error
------------------------------------------------------------
"""

# A program constant that students can use for error-handling
INVALID_DNA_ERR = 'Invalid DNA sequence. Must only contain ATCG? characters.'

# Use this dictionary to get the complement base in B.2 only (you should
# not be using it in B.3, think about why).
BASES = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}


def compute_dna_errors(dna_str1, dna_str2):
    """
    Computes the number of errors found between two DNA sequences. The DNA
    sequences must only contain ATCG? characters. There are two types of
    errors, base mutations and unmatched nucleotides. The base mutation is
    an error where the nucleotide from one strand are paired with the wrong
    base in the other strand. This error counts as 2 errors. The unmatched
    nnucleotide error is when there is an unknown base ('?'). This error
    counts as 1 error. This method is case insensitive.

    Arguments:
        `dna_seq1` (str) - first DNA sequence string
        `dna_seq2` (str) - second DNA sequence string

    Returns:
        (int) - number of errors
    """
    errors = abs(len(dna_str1) - len(dna_str2))
    length = min(len(dna_str1), len(dna_str2))
    dna_str1 = dna_str1.upper()
    dna_str2 = dna_str2.upper()

    for i in range(length):

        if (dna_str1[i] != '?' and dna_str1[i] not in BASES) or \
           (dna_str2[i] != '?' and dna_str2[i] not in BASES):
            raise ValueError(INVALID_DNA_ERR)

        if dna_str1[i] == '?' or dna_str2[i] == '?':
            errors += 1
        elif BASES[dna_str1[i]] != dna_str2[i]:
            errors += 2

    return errors


class DNA:
    """
    Represents a DNA strand comprised of 4 base nucleotides. Each nucleotide
    is one of 'A', 'T', 'C', 'G' (standardized to uppercase), or '?' if
    unknown.

    Attributes:
        - seq (str): Sequence string of DNA nucleotide bases.
    """

    def __init__(self, seq):
        """
        Initializes a new DNA sequence using the provided seq str.
        Case insensitivity is supported for the given seq, but a DNA sequence
        is standardized in upper-case.

        Arguments:
            - seq (str): sequence of 'A', 'T', 'C', 'G' bases or '?' for an
              unknown base.

        Raises:
            - ValueError if provided seq is not comprised of ATCG
              nucleotide bases or the ? character for an unknown base.
        """
        seq = seq.upper()
        for base in seq:
            if base != 'A' and base != 'T' and \
               base != 'C' and base != 'G' and base != '?':
                raise ValueError(INVALID_DNA_ERR)
        self.seq = seq

    def __str__(self):
        """
        Returns the string representation of this DNA strand, which is simply
        the sequence of nucleotides.

        Returns:
            - (str): String representation of this DNA strand, e.g. 'ATACG?C'
        """
        return self.seq

    def __len__(self):
        """
        Returns the length of the DNA, defined as the number of bases in
        its sequence (including unknown bases).

        Returns:
            - (int): length of this DNA strand
        """
        return len(self.seq)

    def base_complement(self, base):
        """
        Returns the complement of the provided base character,
        ignoring letter-case (the complement is returned in upper-case).
        If base is given as the ? unknown character, returns ? (the complement
        is also unknown).

        Arguments:
            - base (str): nucleotide base character

        Returns:
            - (str): complement of `base`, in upper-case

        Raises:
            - ValueError if the passed base is neither a valid DNA
              nucleotide base nor ? to represent an unknown base.
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
        elif base == '?':
            return base  # Keep ? as its complement
        else:
            raise ValueError('Invalid base.')

    def compute_dna_errors(self, dna2):
        """
        Computes the number of errors found between two DNA sequences. There
        are two types of errors, base mutations and unmatched nucleotides.
        The base mutation is an error where the nucleotide from one strand are
        paired with the wrong base in the other strand. This error counts as 2
        errors. The unmatched nnucleotide error is when there is an unknown
        base ('?'). This error counts as 1 error.

        Arguments:
            `dna2` (DNA) - second DNA to be compared to this DNA

        Returns:
            (int) - number of errors
        """
        errors = abs(len(self.seq) - len(dna2.seq))
        length = min(len(self.seq), len(dna2.seq))

        for i in range(length):

            if self.seq[i] == '?' or dna2.seq[i] == '?':
                errors += 1
            elif self.base_complement(self.seq[i]) != dna2.seq[i]:
                errors += 2

        return errors

    def print_helix1(self):
        pass  # Optional B.5

    def print_helix2(self, n):
        pass  # Optional B.5


if __name__ == '__main__':
    # You may add more code here to test your answers, but must keep any
    # testing code in this main block so that nothing is printed when importing
    # partb from a test program. These examples are not exhaustive, but you
    # should refer to the spec examples for more test cases.
    seq1_str = 'ACCtCGAGaTCCGTTTGA'
    seq2_str = 'TGGAgCTCtAGGCAAACT'  # an exact complement

    error_count = compute_dna_errors(seq1_str, seq2_str)
    assert 0 == error_count
    error_count = compute_dna_errors(seq2_str, seq1_str)
    assert 0 == error_count

    seq3_str = 'AC?TCGAGAT?CGT?TA'
    seq4_str = 'TTGTG?TCAG?G'
    error_count = compute_dna_errors(seq3_str, seq4_str)

    error_count = compute_dna_errors('????', '')
    error_count = compute_dna_errors('??Aa', 'aA')
    # should raise a ValueError with specified message
    # error_count = compute_dna_errors('TATA', 'DOG')

    seq1_dna = DNA(seq1_str)
    seq2_dna = DNA(seq2_str)
    error_count = seq1_dna.compute_dna_errors(seq2_dna)
    assert 0 == error_count
    seq5_dna = DNA('AC?A')
    empty_dna = DNA('')
    # will raise a ValueError with specified message
    # dog_dna = DNA('DOG')
