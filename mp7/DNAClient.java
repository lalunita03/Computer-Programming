/**
 * CS 1 22fa MP 7 Part C.3
 * Porting Classes in Python and Java
 * Student name: Lea Grohmann
 * @author (original): El Hovik and Adam Abbas
 * 
 * This program provides functionality to get a DNA given a filename encoding
 * a DNA sequence, as well as print the corresponding polypeptide chain
 * resulting from translation and transcription from 
 * DNA -> mRNA -> polypeptide (amino acid chain).
 */
// Imports required for file-processing in Java
import java.io.*;
import java.util.Scanner;

public class DNAClient {

    /**
     * (Provided main method)
     * Runs the client program with a sample dna sequence file.
     */
    public static void main(String[] args){
        // Unknown file example
        // String exampleDNAFile = "unknown.txt";

        // Invalid file contents example (does not contain nucleotide bases)
        // String exampleDNAFile = "pikachurin_house_mouse_polypeptide.txt";

        // This file has 4134 bases
        String exampleDNAFile = "pikachurin_house_mouse_seq.txt";
        DNA pikachurinDNA = getDNA(exampleDNAFile);
        if (pikachurinDNA != null) {
            System.out.println("Translated protein sequence for " + 
                               exampleDNAFile + ":");
            // Test DNA -> mRNA transcription
            printTranscription(pikachurinDNA);
            // Test DNA -> mRNA -> codon -> polypeptide translation 
            printTranslation(pikachurinDNA);
        }
    }

    /**
     * Given a filename, returns a new DNA object that contains
     * the sequence built from the file's contents.
     * 
     * If no file exists matching the given filename, prints
     * an error message.
     * 
     * @param filename - filename to load a new DNA object from, which should
     * be a valid sequence of DNA base nucleotide characters 
     * (case in-sensitive).
     * @return - DNA object constructed from filename's contents
     */
    public static DNA getDNA(String filename) {
        // Note: Java is stricter when requiring try/catch
        // for file-processing, and we've given you the try/catch
        // code, which should not modified (nor do you need to use
        // try/catch anywhere in MP7).

        // Initial result to null; null is returned if an error occurred,
        // after printing out the error message to the client.
        DNA result = null;
        try {
            File proteinFile = new File(filename);
            String seq = "";
            // Begin student TODOs: Finish C.3.1., removing any TODOs in your 
            // final submission

            Scanner reader = new Scanner(proteinFile);

            while (reader.hasNextLine()) {
                seq += reader.nextLine();
            }

            reader.close();

            result = new DNA(seq);
        } catch (FileNotFoundException err) {
            System.out.println("No sequence file found.");
        } catch (IllegalArgumentException err) {
            // Print out error message if this exception is raised from
            // DNA constructor due to an invalid sequence.
            // We can use err.getMessage() to print the string that was
            // passed to IllegalArgumentException in the class used
            System.out.println(err.getMessage());
        }
        return result;
    }

    /**
     * (Provided printTranslation method)
     * Given a DNA object, prints the result polypeptide chain of 
     * amino acids through DNA -> mRNA -> codon -> polypeptide translation.
     * Note that translation only considers a "read window"
     * starting from an mRNA start codon and ending with either the first
     * stop codon, or the end of the string (ignoring extra bases after the
     * last 3-character codon) if no stop codon is found in the window.
     * Both the start and stop codons are used in the translated
     * polypeptide.
     * 
     * @param dna - DNA object to translate
     */
    public static void printTranslation(DNA dna) {
        System.out.println("DNA -> mRNA -> protein translation results: ");
        String polypeptideChain = dna.translate();
        System.out.println(polypeptideChain);
    }

    /**
     * (Provided printTranscription method)
     * Given a DNA object, prints the result mRNA sequence through 
     * DNA -> mRNA transcription.
     * 
     * @param dna - DNA object to transcribe
     */
    public static void printTranscription(DNA dna) {
        System.out.println("DNA -> mRNA transcription results: ");
        mRNA transcribed = dna.transcribe();
        System.out.println(transcribed);
    }
}