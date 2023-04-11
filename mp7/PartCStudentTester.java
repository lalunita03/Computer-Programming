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
 * javac PartCStudentTester.java (recompile after editing this program)
 * java PartCStudentTester
 * 
 * We strongly recommend you use the Run -> Debug to step through each statement
 * and compare with the expected results! This is similar to setting breakpoints
 * and running in the VSCode Python debugger, and El demo'd this in
 * Lecture 25.
 */
public class PartCStudentTester {

    /**
     * Runs examples of constructing mRNA sequences (C.1.) and using mRNA
     * toString and size() (C.2.). Recommended to start with a breakpoint
     * on the first line and experiment with debugger (remember to use the
     * down arrow to "step into" a constructor/method call).
     */
    public static void c1mRNABasicExamples() {
        // C.1. mRNA constructor
        mRNA mrnaSeq1 = new mRNA("UAGCuagc");
        mRNA mrnaSeq2 = new mRNA("u");           // No error
        mRNA mrnaSeq3 = new mRNA("UuUu");        // No error
        mRNA emptymRNASeq = new mRNA("");        // No error
        mRNA mrnaSeq4 = new mRNA("UGGUCAGAUC");  // No error

        // Neither should be accepted due to invalid 'T' in mRNA
        // These SHOULD throw an IllegalArgumentException (uncomment
        // to continue testing the other examples once you've seen the errors
        // thrown correctly)
        try {
            mRNA invalidmRNA1 = new mRNA("ATCG");
            mRNA invalidmRNA2 = new mRNA("atcg");
        } catch (IllegalArgumentException err) {
            // Correct exception was thrown, now check that the message is correct (unique to mRNA)
            assertEquals(err.getMessage(), "Invalid mRNA sequence. Must only contain AUCG bases.");
        }

        // C.2. mRNA toString and size
        String mseq1Str = mrnaSeq1.toString();
        // "UAGCUAGC"
        assertEquals(mseq1Str, "UAGCUAGC");
        String mseq2Str = mrnaSeq2.toString();
        // "U"
        assertEquals(mseq2Str, "U");
        String mseq3Str = mrnaSeq3.toString();
        // "UUUU"
        assertEquals(mseq3Str, "UUUU");
        String emptyStr = emptymRNASeq.toString();
        // ""
        assertEquals(emptyStr, "");
        String mseq4Str = mrnaSeq4.toString();
        // "UGGUCAGAUC"
        assertEquals(mseq4Str, "UGGUCAGAUC");
    } 

    /**
     * Runs examples of DNA's translate method (C.2.1).
     * Recommended to run through this function with a debugger breakpoint
     * after ensuring Part B and Part C.1. testing code passes.
     */
    public static void c1mRNAPolypeptideExamples() {
        // C.1.3 mRNA toPolypeptide
        // Requires C.1-2 to be correctly implemented
        mRNA mrnaSeq1 = new mRNA("UAGCuagc");
        mRNA mrnaSeq2 = new mRNA("u");           // No error
        mRNA mrnaSeq3 = new mRNA("UuUu");        // No error
        mRNA emptymRNASeq = new mRNA("");        // No error
        mRNA mrnaSeq4 = new mRNA("UGGUCAGAUC");  // No error

        // None of these have an AUG start codon, so polypeptide is ""
        String polypep1 = mrnaSeq1.toPolypeptide();
        String polypep2 = mrnaSeq2.toPolypeptide();
        String polypep3 = mrnaSeq3.toPolypeptide();
        String polypep4 = mrnaSeq4.toPolypeptide();
        String emptyPolypep = emptymRNASeq.toPolypeptide();
        // 5 ""'s
        assertEquals(polypep1, "");
        assertEquals(polypep2, "");
        assertEquals(polypep3, "");
        assertEquals(polypep4, "");
        assertEquals(emptyPolypep, "");

        // In the notation below, we mark [ and ] as the beginning and end of the translation window
        // anything before [ or after ] is ignored, since it's not part of the
        // start/stop window defining translation (we include the bases ignored for review).
        // Translation begins at the first AUG (if found), then translates each subsequent
        // 3-character codon into an amino acid to build to the chain until
        // the last codon added was a STOP codon, or no codons are left to translate
        // DO NOT USE [] ANYWHERE IN YOUR SOLUTION; this is just provided to help
        // read the expected results
        mRNA onlyStartCodon = new mRNA("AUG");
        String met = onlyStartCodon.toPolypeptide();
        // "[AUG]" -> "Met"
        assertEquals(met, "Met");

        mRNA onlyStopCodon1 = new mRNA("UAA");
        String onlyStop1 = onlyStopCodon1.toPolypeptide();
        // ""
        assertEquals(onlyStop1, "");

        mRNA onlyStopCodon2 = new mRNA("UAG");
        String onlyStop2 = onlyStopCodon2.toPolypeptide();
        // ""
        assertEquals(onlyStop2, "");

        mRNA onlyStopCodon3 = new mRNA("UGA");
        String onlyStop3 = onlyStopCodon3.toPolypeptide();
        // ""
        assertEquals(onlyStop3, "");

        // Translation always starts at first start codon, any other starts found
        // are just treated as the AUG Methionine amino acid
        mRNA twoStartsOnly = new mRNA("AUGAUG");
        String twoMets = twoStartsOnly.toPolypeptide();
        // "[AUG-AUG]" -> "Met-Met" (Methionine is still an amino acid)
        assertEquals(twoMets, "Met-Met");

        // 9 bases starting with start codon and ending in stop codon
        // (no extra bases)
        mRNA twoStartsStop = new mRNA("AUGAUGUAA");
        String twoMetsAndStop = twoStartsStop.toPolypeptide();
        // "[AUG-AUG-UAA]" -> "Met-Met-Stp"
        assertEquals(twoMetsAndStop, "Met-Met-Stp");

        // 6 bases starting with start codon and ending in stop codon
        // (no extra bases)
        mRNA startStop = new mRNA("AUGUAG");
        String polypepStartStop = startStop.toPolypeptide();
        // "[AUG-UAG]" -> "Met-Stp"
        assertEquals(polypepStartStop, "Met-Stp");

        // This tests that the translation still works according to the translation
        // rules; translation starts at the first start codon AUG, which happens
        // to be the last codon here.
        mRNA stopStart = new mRNA("UAAAUG");
        String polypepStopStart = stopStart.toPolypeptide();
        // "UAA[AUG]"" -> "Met"
        assertEquals(polypepStopStart, "Met");

        // 12 bases, only 9 are read since stop comes before last three characters
        // The first stop marks the stop of translation, the subsequent stop is ignored
        mRNA twoStartsTwoStops = new mRNA("AUGAUGUAAUGA");
        String polypepTwoStartsTwoStops = twoStartsTwoStops.toPolypeptide();
        // "[AUG-AUG-UAA]UGA" -> "Met-Met-Stp"
        assertEquals(polypepTwoStartsTwoStops, "Met-Met-Stp");

        // Mixing order of start/stop; second stop comes before second start here
        mRNA twoStartsTwoStopsMixed = new mRNA("AUGUAAAUGUGA");
        String polypepTwoStartsTwoStopsMixed = twoStartsTwoStopsMixed.toPolypeptide();
        // "[AUG-UAA]AUGUGA" -> "Met-Stp"
        assertEquals(polypepTwoStartsTwoStopsMixed, "Met-Stp");

        // Another mixed ordering example; second start comes after first stop (so is ignored)
        // and also before the last stop (also ignored)
        mRNA twoStartsTwoStopsMixed2 = new mRNA("AUGUAAUGAAUG");
        String polypepTwoStartsTwoStopsMixed2 = twoStartsTwoStopsMixed2.toPolypeptide();
        // "[AUG-UAA]UGAAUG" -> "Met-Stp"
        assertEquals(polypepTwoStartsTwoStopsMixed2, "Met-Stp");

        // 13 bases; the last codon candidate is a stop, we ignore the extra base character
        // (only read multiples of 3 starting at first start)
        mRNA twoStartsExtraBaseStop = new mRNA("AUGUUAAUGUAAG");
        String polypepTwoStartsExtraBaseStop = twoStartsExtraBaseStop.toPolypeptide();
        // "[AUG-UUA-AUG-UAA]G" -> "Met-Leu-Met-Stp"
        assertEquals(polypepTwoStartsExtraBaseStop, "Met-Leu-Met-Stp");

        // 14 bases; the last codon candidate is a stop, we ignore the extra two bases
        // (only read multiples of 3 starting at first start)
        mRNA twoStartsExtraBaseStop2 = new mRNA("AUGGUUAAUUAAAG");
        String polypepTwoStartsExtraBaseStop2 = twoStartsExtraBaseStop2.toPolypeptide();
        // "[AUG-GUU-AAU-UAA]AG" -> "Met-Val-Asn-Stp"
        assertEquals(polypepTwoStartsExtraBaseStop2, "Met-Val-Asn-Stp");

        // Also 14 bases; tests that codons are correctly parsed in multiples of
        // 3 starting at the first start codon (there is a stop codon in here, but it
        // is ignored since it is offset) 
        mRNA twoStartsExtraBaseNoStop = new mRNA("AUGGUUAAUAAAAG");
        String polypepTwoStartsExtraBaseNoStop = twoStartsExtraBaseNoStop.toPolypeptide();
        // "[AUG-GUU-AAU-AAA]AG" -> "Met-Val-Asn-Lys"
        assertEquals(polypepTwoStartsExtraBaseNoStop, "Met-Val-Asn-Lys");

        // mRNA mrnaSeq1 = new mRNA("UAGCuagc");
        // if we flip AU in the first example, we then have a start codon
        // (two found, only the first is considered)
        mRNA mrnaSeq5 = new mRNA("AUGCaugc");
        String polypep5 = mrnaSeq5.toPolypeptide();
        assertEquals(polypep5, "Met-His");

        // Two codons, but start is last 
        mRNA mrnaSeq6 = new mRNA("AAAAUG");
        String polypep6 = mrnaSeq6.toPolypeptide();
        // "AAA[AUG]" -> "Met"
        assertEquals(polypep6, "Met");

        // Two codons, but start is last and one trailing base
        mRNA mrnaSeq7 = new mRNA("AAAAUGA");
        String polypep7 = mrnaSeq7.toPolypeptide();
        // should be same
        // "AAA[AUG]A" -> "Met"
        assertEquals(polypep7, "Met");
    } 

    /**
     * Runs examples of DNA's translate method (C.2.1).
     * Recommended to run through this function with a debugger breakpoint
     * after ensuring Part B and Part C.1. testing code passes.
     */
    public static void c2DNATranscribeExamples() {
        // C.2.1 DNA transcribe (DNA -> mRNA) 
        // Requires C.1 to be correctly implemented

        // From B.1. Examples
        DNA dnaSeq1 = new DNA("ATCGatcg");  // No error
        DNA dnaSeq2 = new DNA("a");           // No error
        DNA dnaSeq3 = new DNA("AaAa");        // No error
        DNA emptySeq = new DNA("");           // No error
        DNA dnaSeq4 = new DNA("ACCAGTGTAG");  // No error

        String refSeq1 = dnaSeq1.toString();
        String refSeq2 = dnaSeq2.toString();

        // C.2.1. DNA transcribe (DNA -> mRNA)
        mRNA transcribed1 = dnaSeq1.transcribe();
        // original DNA should be unchanged after its transcribe() method ("ATCGATCG")
        assertEquals(refSeq1, dnaSeq1.toString());
        String transcribedmRNAStr1 = transcribed1.toString();
        // "ATCGATCG" -> "UAGCUAGC" (complement DNA, then replace 'T' with 'U')
        assertEquals(transcribedmRNAStr1, "UAGCUAGC");

        mRNA transcribed2 = dnaSeq2.transcribe();
        // original DNA should be unchanged after its transcribe() method ("A")
        assertEquals(refSeq2, dnaSeq2.toString());
        String transcribedmRNAStr2 = transcribed2.toString();
        // "A" -> "U"
        assertEquals(transcribedmRNAStr2, "U");

        mRNA transcribed3 = dnaSeq3.transcribe();
        String transcribedmRNAStr3 = transcribed3.toString();
        assertEquals(transcribedmRNAStr3, "UUUU");

        mRNA transcribed4 = dnaSeq4.transcribe();
        String transcribedmRNAStr4 = transcribed4.toString();
        assertEquals(transcribedmRNAStr4, "UGGUCACAUC");

        mRNA emptyTranscribed = emptySeq.transcribe();
        String transcribedEmptyStr = emptyTranscribed.toString();
        assertEquals(transcribedEmptyStr, "");

        DNA onlyStartCodonDNA = new DNA("TAC");
        mRNA onlyStartCodonTranscribed = onlyStartCodonDNA.transcribe();
        String met2 = onlyStartCodonTranscribed.toString();
        assertEquals(met2, "AUG");

        DNA onlyStopCodon1DNA = new DNA("ATT");
        mRNA onlyStopCodon1Transcribed = onlyStopCodon1DNA.transcribe();
        String stop1Transcribed = onlyStopCodon1Transcribed.toString();
        assertEquals(stop1Transcribed, "UAA");

        DNA onlyStopCodon2DNA = new DNA("ATC");
        mRNA onlyStopCodon2Transcribed = onlyStopCodon2DNA.transcribe();
        String stop2Transcribed = onlyStopCodon2Transcribed.toString();
        assertEquals(stop2Transcribed, "UAG");

        DNA onlyStopCodon3DNA = new DNA("ACT");
        mRNA onlyStopCodon3Transcribed = onlyStopCodon3DNA.transcribe();
        String stop3Transcribed = onlyStopCodon3Transcribed.toString();
        assertEquals(stop3Transcribed, "UGA");

        mRNA twoStartsOnly = new mRNA("AUGAUG");
        DNA twoStartsOnlyDNA = new DNA("TACTAC");
        mRNA twoStartsOnlyTranscribed = twoStartsOnlyDNA.transcribe();
        String twoStartsTranscribedStr = twoStartsOnlyTranscribed.toString();
        // "TACTAC" -> "AUGAUG"
        assertEquals(twoStartsTranscribedStr, twoStartsOnly.toString());

        mRNA twoStartsStop = new mRNA("AUGAUGUAA");
        DNA twoStartsStopDNA = new DNA("TACTACATT");
        mRNA twoStartsStopTranscribed = twoStartsStopDNA.transcribe();
        String twoStartsStopTranscribedStr = twoStartsStopTranscribed.toString();
        // "TACTACATT" -> "AUGAUGUAA"
        assertEquals(twoStartsStopTranscribedStr, twoStartsStop.toString());

        mRNA twoStartsTwoStops = new mRNA("AUGAUGUAAUGA");
        DNA twoStartsTwoStopsDNA = new DNA("TACTACATTACT");
        mRNA twoStartsTwoStopsTranscribed = twoStartsTwoStopsDNA.transcribe();
        String twoStartsTwoStopsTranscribedStr = twoStartsTwoStopsTranscribed.toString();
        assertEquals(twoStartsTwoStopsTranscribedStr, twoStartsTwoStops.toString());

        mRNA startStop = new mRNA("AUGUAG");
        DNA startStopDNA = new DNA("TACATC");
        mRNA startStopTranscribed = startStopDNA.transcribe();
        String startStopTranscribedStr = startStopTranscribed.toString();
        assertEquals(startStopTranscribedStr, startStop.toString());

        mRNA stopStart = new mRNA("UAAAUG");
        DNA stopStartDNA = new DNA("ATTTAC");
        mRNA stopStartTranscribed = stopStartDNA.transcribe();
        String stopStartTranscribedStr = stopStartTranscribed.toString();
        assertEquals(stopStartTranscribedStr, stopStart.toString());
    } 

    /**
     * Runs examples of DNA's translate method (C.2.1).
     * Recommended to run through this function with a debugger breakpoint
     * after ensuring Part B and Part C.1-2.1. testing code passes.
     * 
     * Note: Your DNA translate method should be fairly short. This testing
     * code seems long, but if your mRNA's toPolypeptide() and
     * DNA's transcribe() methods work, this one should too (assuming you're not
     * overcomplicating translate).
     */
    public static void c2DNATranslateExamples() {
        // C.2.2. DNA translate (DNA -> mRNA -> codon -> polypeptide)
        // Requires C.1-2.1 to be correctly implemented
        // Unliked transcribe, translate only considers a valid translation window
        // starting at the first START codon and ending until we reach one of the
        // STOP codons or the end of the string (ignoring extra bases)

        // From B.1. Examples
        DNA dnaSeq1 = new DNA("ATCGatcg");    // No error
        DNA dnaSeq2 = new DNA("a");           // No error
        DNA dnaSeq3 = new DNA("AaAa");        // No error
        DNA emptySeq = new DNA("");           // No error
        DNA dnaSeq4 = new DNA("ACCAGTGTAG");  // No error

        String translated1 = dnaSeq1.translate();
        String translated2 = dnaSeq2.translate();
        String translated3 = dnaSeq3.translate();
        String translated4 = dnaSeq4.translate();
        String translatedEmptyStr = emptySeq.translate();

        // Again, all 5 should be "", since no START_CODON ("AUG") was found
        assertEquals(translated1, "");
        assertEquals(translated2, "");
        assertEquals(translated3, "");
        assertEquals(translated4, "");
        assertEquals(translatedEmptyStr, "");

        DNA onlyStartCodonDNA = new DNA("TAC");
        String onlyStartTranslated = onlyStartCodonDNA.translate();
        // DNA -> complement -> mRNA -> codon -> amino acid chain
        // "TAC" -> "ATG" -> "AUG" -> "Str"
        assertEquals(onlyStartTranslated, "Met");

        DNA onlyStopCodon1DNA = new DNA("ATT");
        String onlyStop1Translated = onlyStopCodon1DNA.translate();
        // DNA -> mRNA -> codon -> amino acid chain
        // "TAA" -> "UAA" -> "" (no start codon)
        assertEquals(onlyStop1Translated, "");

        DNA onlyStopCodon2DNA = new DNA("ATC");
        String onlyStop2Translated = onlyStopCodon2DNA.translate();
        // "" (no start codon)
        assertEquals(onlyStop2Translated, "");

        DNA onlyStopCodon3DNA = new DNA("ACT");
        String onlyStop3Translated = onlyStopCodon3DNA.translate();
        // "" (no start codon)
        assertEquals(onlyStop3Translated, "");

        DNA twoStartsOnlyDNA = new DNA("TACTAC");
        mRNA twoStartsOnly = new mRNA("AUGAUG");
        String twoStartsOnlyTranslated = twoStartsOnlyDNA.translate();
        // "TACTAC" -> "AUGAUG" -> "[AUG-AUG]" -> "Met-Met"
        assertEquals(twoStartsOnlyTranslated, twoStartsOnly.toPolypeptide());

        DNA twoStartsStopDNA = new DNA("TACTACATT");
        mRNA twoStartsStop = new mRNA("AUGAUGUAA");
        String twoStartsStopTranslated = twoStartsStopDNA.translate();
        // "TACTACATT" -> "AUGAUGUAA" -> "[AUG-AUG-UAA]" -> "Met-Met-Stp"
        assertEquals(twoStartsStopTranslated, twoStartsStop.toPolypeptide());

        DNA twoStartsTwoStopsDNA = new DNA("TACTACATTACT");
        // The rest of the examples hard-code the chains, but still
        // refer to the mRNA examples in the transcription test function
        String twoStartsTwoStopsTranslated = twoStartsTwoStopsDNA.translate();
        assertEquals(twoStartsTwoStopsTranslated, "Met-Met-Stp");

        DNA startStopDNA = new DNA("TACATC");
        String startStopTranslated = startStopDNA.translate();
        assertEquals(startStopTranslated, "Met-Stp");

        DNA stopStartDNA = new DNA("ATTTAC");
        String stopStartTranslated= stopStartDNA.translate();
        assertEquals(stopStartTranslated, "Met");

        DNA twoStartsTwoStopsMixedDNA = new DNA("TACATTTACTCT");
        String twoStartsTwoStopsMixedTranslated = twoStartsTwoStopsMixedDNA.translate();
        assertEquals(twoStartsTwoStopsMixedTranslated, "Met-Stp");

        DNA twoStartsTwoStopsMixed2DNA = new DNA("TACATTACTTAC");
        String twoStartsTwoStopsMixed2Translated = twoStartsTwoStopsMixed2DNA.translate();
        assertEquals(twoStartsTwoStopsMixed2Translated, "Met-Stp");

        DNA twoStartsExtraBaseStopDNA = new DNA("TACAATTACATTC");
        String twoStartsExtraBaseStopTranslated = twoStartsExtraBaseStopDNA.translate();
        assertEquals(twoStartsExtraBaseStopTranslated, "Met-Leu-Met-Stp");

        DNA twoStartsExtraBaseStop2DNA = new DNA("TACCAATTAATTTC");
        String twoStartsExtraBaseStop2Translated = twoStartsExtraBaseStop2DNA.translate();
        assertEquals(twoStartsExtraBaseStop2Translated, "Met-Val-Asn-Stp");

        DNA twoStartsExtraBaseNoStopDNA = new DNA("TACCAATTATTTTC");
        String twoStartsExtraBaseNoStopTranslated = twoStartsExtraBaseNoStopDNA.translate();
        assertEquals(twoStartsExtraBaseNoStopTranslated, "Met-Val-Asn-Lys");
    }

    public static void main(String[] args) {
        // C.1.1. mRNA(String seq) constructor, toString(), size()
        c1mRNABasicExamples();
        // C.1.2. mRNA's toPolypeptide() (requires above to work)
        c1mRNAPolypeptideExamples();
        // C.2.1. DNA's transcribe()  (requires above to work)
        c2DNATranscribeExamples();
        // C.2.2. DNA's translate() (requires above to work)
        c2DNATranslateExamples();

        // Some extra examples to test translation/transcription exercises
        // copied from DNAStudentTester.java, but provided so you can
        // add more tests if you'd like
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