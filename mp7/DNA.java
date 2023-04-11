/**
 * CS 1 22fa MP 7 Parts B/C
 * Porting Classes in Python and Java
 * Student name: Lea Grohmann
 * Starter code for DNA.java
 * @author (original): El Hovik and Adam Abbas
 * 
 * This class represents a DNA sequence comprised of A', 'C', 'G', 'T' 
 * nucleotides. The class supports simple methods to represent the sequence 
 * as a String, get a complement sequence, compute information about
 * nucleotide counts and percentages, and transcription and translation to
 * mRNA and polypeptide Strings (chains of amino acids).
 */
import java.util.Random;

public class DNA {
    // String of DNA base characters in upper-case
    private String seq;
    // For the optional B.6. exercise
    private static Random mutator = new Random();
    private static final double MUTATION_RATE = 0.1;

    /**
     * Initializes a new (single-strand) DNA sequence using the provided 
     * seq String. A DNA sequence contains a sequence of the 4 DNA base 
     * nucleotides, 'A', 'T', 'C', 'G' (standardized to uppercase).
     * 
     * @param seq - sequence of 'A', 'T', 'C', 'G' bases.
     * @throws IllegalArgumentException if the sequence
     * is not comprised of ATCG nucleotide bases.
     */
    public DNA(String seq) {
        seq = seq.toUpperCase();
        for (int i = 0; i < seq.length(); i++) {
            if (seq.charAt(i) != 'A' && seq.charAt(i) != 'T' && seq.charAt(i) != 'C' && seq.charAt(i) != 'G') {

                String message = "Invalid DNA sequence. Must only contain ATCG bases.";
                throw new IllegalArgumentException(message);
            }
        }
        this.seq = seq;
    }

    /**
     * Returns the string representation of the DNA sequence,
     * defined as the sequence of nucleotide bases.
     * 
     * @return string sequence of nucleotide bases
     */
    public String toString() {
        return this.seq;
    }

    /**
     * Returns the size of the DNA sequence, defined as the number of 
     * nucleotide bases it contains.
     * 
     * @return - number of bases in the sequence
     */
    public int size() { 
        return this.seq.length();
    }

    /**
     * (Provided private helper method, do not change)
     * Returns the complement of the provided base character,
     * ignoring letter-case (the complement is returned in upper-case).
     * 
     * @param base - nucleotide base
     * 
     * @return - complement of `base`, in upper-case.
     * 
     * @throws IllegalArgumentException if the passed base
     * is not a valid DNA nucleotide base character.
     */
    private static char baseComplement(char base) {
        // to upper-case a char in Java, we need to use
        // the Character class.
        base = Character.toUpperCase(base);
        if (base == 'A') {
            return 'T';
        } else if (base == 'T') {
            return 'A';
        } else if (base == 'C') {
            return 'G';
        } else if (base == 'G') {
            return 'C';
        } else {
            String errMsg = "Invalid base.";
            throw new IllegalArgumentException(errMsg);
        }
    }

    /**
     * Returns the complement sequence of the DNA sequence
     * 
     * @return - complement DNA sequence
     */
    public String complement() {
        String result = "";

        for (int i = 0; i < seq.length(); i++) {
            result += baseComplement(seq.charAt(i));
        }
        return result;
    }

    /**
     * Returns the number of occurences of a base in the DNA sequence
     * 
     * @param base - nucleotide base
     * 
     * @return - number of occurances of base
     * 
     * @throws IllegalArgumentException if passed a base is not
     * a valid DNA nucleotide base character.
     */
    public int countOccurrences(char base) {
        int result = 0;
        base = Character.toUpperCase(base);

        if (base != 'A' && base != 'T' && base != 'C' && base != 'G') {
            throw new IllegalArgumentException("Invalid base.");
        }
        for (int i = 0; i < seq.length(); i++) {
            if (base == seq.charAt(i)) {
                result++;
            }
        }
        return result;
    }

    /**
     * Returns the percentage of a base present in the DNA sequence
     * 
     * @param base - nucleutide base
     * 
     * @return - percentage of base in DNA
     * 
     * @throws IllegalArgumentException if the base passed is not a
     * valid DNA nucleotide base character.
     */
    public double percentageOf(char base) {
        int occurances = countOccurrences(base);

        if (occurances == 0) {
            return 0.0;
        }

        return (double) occurances / size();
    }

    /**
     * Transcribes the current DNA sequence to mRNA, by 
     * taking the complement of all of the bases and 
     * switching the "T" nucleotide to "U".
     * 
     * @return the transcribed mRNA
     */
    public mRNA transcribe() { 
        String compDNA = complement();
        String seqRNA = compDNA.replace('T', 'U');
        return new mRNA(seqRNA);
    }

    /**
     * Translates the current DNA to an Amino Acid chain by 
     * transcribing to an RNA chain, finding the start codon 
     * ("AUG") and then parsing 3-letter codons and looking
     * up their respective amino acids in the "codon.txt" files.
     * 
     * @return full string of translated Amino Acids
     */
    public String translate() {
        String polypeptide = transcribe().toPolypeptide();
        return polypeptide;
    }

    /**
     * Optional B.6.
     */
    public DNA mutate(int mutationTime) {
        String mutatedSeq = this.seq;
        // Provided pseudocode:
        // For mutationTime times:
        // if mutator.nextDouble() < MUTATION_RATE
        // randomly select an index of the mutatedSeq, and
        // replace mutatedSeq with the prefix (unchanged), the complement
        // of the randomly-selected character, and the suffix (unchanged)
        // Note that the result String should have the same length as this.seq
        // and this.seq should not be changed as a result of this method.
        // TODO (Optional): B.6.

        return new DNA(mutatedSeq);
    }
}
