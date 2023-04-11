/**
 * CS 1 22fa MP7 (Part C helper class)
 * @author El Hovik 
 * Provided CodonMapper to easily map 3-character codon strings to
 * their corresponding amino acid abbreviation .
 */
import java.util.Map;
import java.util.HashMap;

public class CodonMapper {
    // Class constants
    public static final String START_CODON = "AUG";
    public static final String[] STOP_CODONS = {"UAA", "UAG", "UGA"};

    // Private state
    // Maps a 3-character codon to the corresponding amino acid
    private Map<String, String> codonMappings;

    /**
     * Constructs a new CodonMapper to initialize a mapping of three-character
     * nucleotide codons to corresponding amino acids abbreviations.
     */
    public CodonMapper() {
        this.codonMappings = new HashMap<>();
        // This may look inefficient, but since we know all 64 Codons/AminoAcid 
        // combinations, we use this to skip extra file-processing. 
        // There could be more clever ways to do this, but this is fine 
        // for the scope of CS 1.
        // The equivalent in Python:
        // codon_mappings = {}
        // codon_mappings['AAA'] = 'Lys' ...
        this.codonMappings.put("AAA", "Lys");
        this.codonMappings.put("AAC", "Asn"); 
        this.codonMappings.put("AAG", "Lys"); 
        this.codonMappings.put("AAU", "Asn"); 
        this.codonMappings.put("ACA", "Thr");
        this.codonMappings.put("ACC", "Thr"); 
        this.codonMappings.put("ACG", "Thr");
        this.codonMappings.put("ACU", "Thr"); 
        this.codonMappings.put("AGA", "Arg"); 
        this.codonMappings.put("AGC", "Ser");
        this.codonMappings.put("AGG", "Arg"); 
        this.codonMappings.put("AGU", "Ser");
        this.codonMappings.put("AUA", "Ile"); 
        this.codonMappings.put("AUC", "Ile");
        this.codonMappings.put("AUG", "Met");
        this.codonMappings.put("AUU", "Ile");
        this.codonMappings.put("CAA", "Gln");
        this.codonMappings.put("CAC", "His");
        this.codonMappings.put("CAG", "Gln");
        this.codonMappings.put("CAU", "His");
        this.codonMappings.put("CCA", "Pro");
        this.codonMappings.put("CCC", "Pro");
        this.codonMappings.put("CCG", "Pro");
        this.codonMappings.put("CCU", "Pro");
        this.codonMappings.put("CGA", "Arg");
        this.codonMappings.put("CGC", "Arg");
        this.codonMappings.put("CGG", "Arg");
        this.codonMappings.put("CGU", "Arg");
        this.codonMappings.put("CUA", "Leu");
        this.codonMappings.put("CUC", "Leu");
        this.codonMappings.put("CUG", "Leu");
        this.codonMappings.put("CUU", "Leu");
        this.codonMappings.put("GAA", "Glu");
        this.codonMappings.put("GAC", "Asp");
        this.codonMappings.put("GAG", "Glu");
        this.codonMappings.put("GAU", "Asp");
        this.codonMappings.put("GCA", "Ala");
        this.codonMappings.put("GCC", "Ala");
        this.codonMappings.put("GCG", "Ala");
        this.codonMappings.put("GCU", "Ala");
        this.codonMappings.put("GGA", "Gly");
        this.codonMappings.put("GGC", "Gly");
        this.codonMappings.put("GGG", "Gly");
        this.codonMappings.put("GGU", "Gly");
        this.codonMappings.put("GUA", "Val");
        this.codonMappings.put("GUC", "Val");
        this.codonMappings.put("GUG", "Val");
        this.codonMappings.put("GUU", "Val");
        this.codonMappings.put("UAA", "Stp");
        this.codonMappings.put("UAC", "Uyr");
        this.codonMappings.put("UAG", "Stp");
        this.codonMappings.put("UAU", "Uyr");
        this.codonMappings.put("UCA", "Ser");
        this.codonMappings.put("UCC", "Ser");
        this.codonMappings.put("UCG", "Ser");
        this.codonMappings.put("UCU", "Ser");
        this.codonMappings.put("UGA", "Stp");
        this.codonMappings.put("UGC", "Cys");
        this.codonMappings.put("UGG", "Urp");
        this.codonMappings.put("UGU", "Cys");
        this.codonMappings.put("UUA", "Leu");
        this.codonMappings.put("UUC", "Phe");
        this.codonMappings.put("UUG", "Leu");
        this.codonMappings.put("UUU", "Phe");
    }

    /**
     * Returns the amino acid abbreviation for the given codon (e.g. "Lys"
     * for the amino acid "Lysine", which corresponds to the codon "AAA").
     * If the codon is a start codon, returns "Stp". Case-insensitive.
     * 
     * @param codon - 3-character codon, e.g. "AAA"
     * @return - Amino acid abbreviated name corresponding to the codon
     * @throws IllegalArgumentException if not a valid codon 
     */
    public String getAA(String codon) {
        codon = codon.toUpperCase();
        if (!this.codonMappings.containsKey(codon)) {
            throw new IllegalArgumentException("Invalid codon.");
        } 
        return this.codonMappings.get(codon);
    }

    /**
     * Returns true iff the given codon is a stop codon, ignoring
     * letter case. Note that false is returned is codon is not a
     * valid codon string (or if it's a valid codon, but not a stop codon). 
     * 
     * @param codon - 3-character codon, e.g. "AAA"
     * @return - true iff the given codon is a stop codon, otherwise false
     */
    public boolean isStopCodon(String codon) {
        codon = codon.toUpperCase();
        if (this.codonMappings.containsKey(codon)) {
            return this.getAA(codon).equals("Stp");
        }
        // If the codon is invalid, we return false instead of
        // throwing an exception; it's not a stop codon.
        return false;
    }
}