/**
 * A starter client for students to test examples from the spec as they
 * work through Parts B/C.
 * 
 * To run: 
 * Add any test code in the main function; we recommend using the examples
 * from the spec to iteratively check each exercise.
 * 
 * javac DNA.java
 * javac mRNA.java (if you're working on mRNA.java)
 * javac DNAStudentTester.java (recompile after editing this program)
 * java DNAStudentTester
 * 
 * We strongly recommend you use the Run -> Debug to step through each statement
 * and compare with the expected results! This is similar to setting breakpoints
 * and running in the VSCode Python debugger, and El will demo this in
 * Lecture 25.
 */
public class DNAStudentTester {
    public static void main(String[] args){
        // From B.1. Examples
        DNA dnaSeq1 = new DNA("ATCGatcg");  // No error
        // The following should give a _compiler_ error if you uncomment
        // and try to compile, due to illegal reference of private field
        // System.out.println(dnaSeq1.seq);   // Compiler error in Java
        DNA dnaSeq2 = new DNA("a");           // No error
        DNA dnaSeq3 = new DNA("AaAa");        // No error
        DNA emptySeq = new DNA("");           // No error
        DNA dnaSeq4 = new DNA("ACCAGTGTAG");  // No error
        // Should give a runtime error (your IllegalArgumentException should be raised)
        // DNA invalidSeq = new DNA("catdog");   

        // Examples from B.2.
        String seq1 = dnaSeq1.toString();
        // "ATCGATCG"
        String emptySeqStr = emptySeq.toString();
        // ""
        System.out.println(dnaSeq1);
        // ATCGATCG
        System.out.println(emptySeq);
        // 
        int seq1Len = dnaSeq1.size(); 
        System.out.println(seq1Len);
        // 8
        int seq2Len = dnaSeq2.size(); 
        System.out.println(seq2Len);
        // 1
        int seq3Len = dnaSeq3.size();
        System.out.println(seq3Len);
        // 4
        int seq4Len = emptySeq.size();
        System.out.println(seq4Len);
        // 0

        // DNA sequence variables defined above
        // Examples from B.3
        String comp1 = dnaSeq1.complement();
        // "TAGCTAGC"
        String comp2 = dnaSeq2.complement();
        // "T"
        String comp4 = dnaSeq3.complement();
        // "TTTT"
        String emptyComp = emptySeq.complement();
        // ""
        dnaSeq4 = new DNA("ACCAGTGTAG");
        comp4 = dnaSeq4.complement();
        // "TGGTCACATC"
        DNA doubleCompSeq = new DNA(comp4);
        System.out.println(doubleCompSeq); // uses toString()
        // TGGTCACATC
        String doubleComp = doubleCompSeq.complement();
        // "ACCAGTGTAG", back to dnaSeq4

        // Examples from B.4
        // DNA sequence variables defined above
        int a1Count = dnaSeq1.countOccurrences('a');
        // 2
        int t1Count = dnaSeq1.countOccurrences('T');
        // 2
        a1Count = dnaSeq2.countOccurrences('A');
        // 1
        int a3Count = dnaSeq3.countOccurrences('A');
        // 4
        int a4Count = emptySeq.countOccurrences('A');
        // 0

        // This one SHOULD throw an IllegalArgumentException (uncomment
        // to continue testing the other examples once you've seen the error
        // thrown correctly)
        // int d1Count = dnaSeq1.countOccurrences('d');
        // Exception java.lang.IllegalArgumentException: Invalid base.
        // Traceback omitted
        int c4Count = dnaSeq4.countOccurrences('C');
        // 2
        int g4Count = dnaSeq4.countOccurrences('G');
        // 3
        int gc4Count = c4Count + g4Count;
        // 5 
        double gcContent = gc4Count * 1.0 / dnaSeq4.size();
        // 5 / 10 -> 0.5 (HW1!)

        // Examples from B.5
        t1Count = dnaSeq1.countOccurrences('T');
        // 2
        double t1Percent = dnaSeq1.percentageOf('T');
        // can't reassign types for an already-defined variable
        t1Percent = dnaSeq1.percentageOf('t');
        // 0.25
        int a2Count = dnaSeq2.countOccurrences('A');
        // 1
        double a2Percent = dnaSeq2.percentageOf('A');
        // 1.0
        a3Count = dnaSeq3.countOccurrences('A');
        // 4
        double a3Percent = dnaSeq3.percentageOf('A');
        // 1.0
        int emptyACount = emptySeq.countOccurrences('A');
        // 0
        double emptyAPercent = emptySeq.percentageOf('A');
        // 0.0
        // This one SHOULD throw an IllegalArgumentException (uncomment
        // to continue testing the other examples once you've seen the error
        // thrown correctly)
        // double d1Percent = dnaSeq1.percentageOf('d');
        // Exception java.lang.IllegalArgumentException: Invalid base.
        // Traceback omitted
        // Same here
        // double d2Percent = emptySeq.percentageOf('d');
        // Exception java.lang.IllegalArgumentException: Invalid base.
        // Traceback omitted

        // Some extra examples to test translation/transcription exercises
        String exampleSeq = "ACGTGACATA"; 
        String expectedComp = "TGCACTGTAT";
        String expectedmRNASeq = "UGCACUGUAU";
        // Example constructor
        DNA emptyDNA = new DNA("");
        DNA exampleDNA = new DNA(exampleSeq);

        // You can use the provided assert functions to test equality
        // Here are some examples.
        assertEquals(exampleDNA.size(), 10);
        System.out.println(exampleDNA.size());
        // We only use try/catch here for testing purposes, because
        // we _expect_ an IllegalArgumentException to be thrown, and we
        // want to report if it isn't.
        try{
            exampleDNA = new DNA("F"); 
            // DNA should throw an error!
            System.out.println("DNA(\"F\") does not throw an (expected) IllegalArgumentException");
            assert false; 
        } catch (IllegalArgumentException e) {
            System.out.println("DNA(\"F\") throws an (expected) IllegalArgumentException");
        }
        // for (int i = 0; i < seq.length(); i++){
        //     assert DNA.baseComplement(seq.charAt(i)) == comp.charAt(i);
        // } 
        assertEquals(exampleDNA.complement(), expectedComp);
        
        assertEquals(exampleDNA.countOccurrences('A'), 4);
        assertEquals(exampleDNA.countOccurrences('T'), 2);
        assertEquals(emptyDNA.countOccurrences('A'), 0);
        
        double cPercent = exampleDNA.percentageOf('C');
        assertEquals(cPercent, 2.0 / 10); // 2 of 10 chars are c/C
        mRNA transcribedmRNA = exampleDNA.transcribe();
        // One example for mRNA.toString()
        assertEquals(transcribedmRNA.toString(), expectedmRNASeq);
        DNA exampleDNAtoCodon = new DNA("TACTTTCTCATT");
        String translated = exampleDNAtoCodon.translate();
        // transaltion must include "Met" for start and "Stp" for (stop if found)
        assertEquals(translated, "Met-Lys-Glu-Stp");

        // Feel free to add more calls here!
    }

    /**
     * Some helper assertion functions for different types.
     */

    public static void assertEquals(int val1, int val2) {
        if (val1 != val2) {
            throw new AssertionError("\nExpected: " + val1 + "\nActual: " + val2);
        }
    }

    // Remember that getPercentage should return a double
    public static void assertEquals(double val1, double val2) {
        if (val1 != val2) {
            throw new AssertionError("\nExpected: " + val1 + "\nActual: " + val2);
        }
    }

    public static void assertEquals(String s1, String s2) {
        if (!s1.equals(s2)){ 
            throw new AssertionError("Expected: " + s1 + "\nActual: " + s2);
        }
    }

}