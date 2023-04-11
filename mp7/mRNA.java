/**
 * CS 1 22fa MP 7 Part B/C
 * Porting Classes in Python and Java
 * Student name: Lea Grohmann
 * @author (original): El Hovik and Adam Abbas
 * 
 * This class represents an mRNA sequence comprised of 'A', 'C', 'G', 'U' 
 * nucleotides. The class supports simple methods to represent the sequence as 
 * a String and return a polypeptide chain of amino acids through translation.
 * 
 * TODO: Finish this class, removing any TODOs in your final submission. 
 */
public class mRNA { 
    private String seq;
    /**
     * Initializes a new (single-strand) mRNA sequence using the provided 
     * seq String. A mRNA sequence contains a sequence of the 4 mRNA base 
     * nucleotides, 'A', 'U', 'C', 'G' (standardized to uppercase).
     * 
     * @param seq - sequence of 'A', 'U', 'C', 'G' bases.
     * @throws IllegalArgumentException if the sequence
     * is not comprised of AUCG nucleotide bases.
     */
    public mRNA(String seq) {
        seq = seq.toUpperCase();
        for (int i = 0; i < seq.length(); i++) {
            if (seq.charAt(i) != 'A' && seq.charAt(i) != 'U' && seq.charAt(i) != 'C' && seq.charAt(i) != 'G') {

                String message = "Invalid mRNA sequence. Must only contain AUCG bases.";
                throw new IllegalArgumentException(message);
            }
        }
        this.seq = seq;
    }

    /**
     * Returns the string representation of the mRNA sequence,
     * defined as the sequence of nucleotide bases.
     * 
     * @return string sequence of nucleotide bases
     */
    public String toString() { 
        return this.seq;
    }

    /**
     * Returns the size of the mRNA sequence, defined as the number of 
     * nucleotide bases it contains.
     * 
     * @return - number of bases in the sequence
     */
    public int size() { 
        return this.seq.length();
    }

    /**
     * Translation. Returns a polypeptide chain represented as a series of 
     * amino acids, starting with the start codon 'AUG'. Returns "" if
     * translation is not possible due to no start codon in the mRNA sequence.
     * Translation reads from left to right in the sequence, starting with
     * the first 'AUG' sequence. Processes a polypeptide chain
     * from that open read window the either the first stop codon, or
     * the end of the sequence if none found (if the sequence read
     * is not a multiple of 3, any remaining bases will be omitted from the end of
     * the chain.)
     * 
     * @return - polypeptide chain in form of acd-acd-acd-...acd
     * where each acd is an amino acid abbreviation.
     */
    public String toPolypeptide() {
        CodonMapper mappings = new CodonMapper();
        String START_CODON = "AUG";
        String chain = "";


        int start = this.seq.indexOf(START_CODON);

        if (start == -1) {
            return chain;
        }
        
        String subseq = this.seq.substring(start);
        chain = mappings.getAA(START_CODON);

        int remainder = subseq.length() % 3;
        int stop = subseq.length() - remainder - 2;
        for (int i = 3; i < stop; i += 3) {
            String codon = subseq.substring(i, i + 3);
            chain += "-" + mappings.getAA(codon);

            if (mappings.isStopCodon(codon)) {
                break;
            }
        }
        return chain;
    }
}
