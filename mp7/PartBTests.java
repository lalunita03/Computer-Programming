/**
 * CS 1 22fa
 * Tests for MP7 Part B (DNA Porting, B.1 - B.5)
 * 
 * @author El Hovik
 * 
 * Instructions:
 * - To run these tests, simply compile and run as you would another
 * Java program,
 * making sure you've already compiled DNA.java:
 * $ javac DNA.java
 * $ javac PartBTests.java
 * $ java PartBTests
 * 
 * Any errors printed should be descriptive enough to catch a case you
 * don't  handle, and most tests include examples from the spec, as well as
 * some additional test cases. If you're unsure about why a test fails,
 * double-check the comments for the corresponding test function here.
 */
public class PartBTests {
    public static final String EXPECTED_CONSTRUCTOR_ERR = "Invalid DNA sequence. Must only contain ATCG bases.";
    public static final String EXPECTED_INVALID_BASE_ERR = "Invalid base.";
    // This is one of the few cases where a global field is ok, since we're
    // keeping track of passed tests (almost always only makes sense for testing)
    public static int passed = 0;

    public static void main(String[] args) {
        int i = 1;
        int testCount = 6;
        try {
            // B.1 Tests
            String testConstructorLogs = testB1ConstructorValidation();
            printResults(testConstructorLogs, "B.1 DNA(String seq) Validation");
            i++;
            // B.1 (this.seq) and B.2a Tests
            String testSeqFieldtoStringLogs = testseqFieldAndB2toString();
            printResults(testSeqFieldtoStringLogs, "B.1/2a DNA this.seq and toString()");
            i++;
            // B.2b Tests
            String testSizeLogs = testB2size();
            printResults(testSizeLogs, "B.2b DNA size()");
            i++;
            // B.3 Tests
            String testComplementLogs = testB3complement();
            printResults(testComplementLogs, "B.3 DNA complement()");
            i++;
            // B.4 Tests
            String testCountOccurrencesLogs = testB4countOccurrences();
            printResults(testCountOccurrencesLogs, "B.4 DNA countOccurrences(char base)");
            i++;

            // B.5 Tests
            String testPercentageOfLogs = testB5percentageOf();
            printResults(testPercentageOfLogs, "B.5 DNA percentageOf(char base)");
            i++;

            System.out.println();
            System.out.println("Total tests passed: " + passed + "/" + testCount);
        } catch (Exception e) {
            String row = generateErrorRow();
            String logs = "\n**TESTS ABORTING**: Unexpected exception thrown\n";
            logs += row + "\n";
            logs += "  - " + e.toString() + "\n";
            logs += "  - Please check your code for this test before testing the other cases).\n";
            logs += "  - Total tests ran before unexpected exception: " + (i - 1) + "/" + testCount + "\n";
            logs += row + "\n";
            System.out.println(logs);
        }
    }

    /**
     * Helper function to print test results out
     * 
     * @param logs     - logs collected during a test function
     * @param testName - name of test to print results out
     */
    public static void printResults(String logs, String testName) {
        String result = logs.isEmpty() ? "PASSED" : "FAILED";
        if (!logs.isEmpty()) {
            String row = generateErrorRow();
            testName = row + "\n" + testName;
            result += "\nResults:\n" + logs;
            result += row;
        } else {
            passed++;
        }
        System.out.println(testName + " Test Results: " + result);
    }

    /**
     * Tests DNA constructor
     * - letter casing should be ignored (sequences are saved in uppercase)
     * - an IllegalArgument should be thrown if given an invalid base
     * - Empty strings are allowed (an empty DNA sequence)
     * 
     * @return true iff all constructor validation tests pass
     */
    public static String testB1ConstructorValidation() {
        String logs = "";
        try {
            DNA dnaSeq1 = new DNA("ATCGatcg"); // No error
            DNA dnaSeq2 = new DNA("a"); // No error
            DNA dnaSeq3 = new DNA("AaAa"); // No error
            DNA dnaSeq4 = new DNA("ACCAGTGTAG"); // No error
            DNA dnaSeq5 = new DNA("GCGGCCATGCATGGGG"); // No error
            DNA dnaSeq6 = new DNA("ATATATATA"); // No error
            // No error
            DNA dnaSeq7 = new DNA("ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG");
            DNA emptySeq = new DNA(""); // No error
        } catch (Exception e) {
            logs += "  - Unexpected exception thrown for _valid_ DNA sequence\n" +
                    "    (double-check that letter-casing is handled correctly):\n";
            logs += "  - " + e.toString();
        }
        try {
            DNA invalidSeq = new DNA("catdog");
            logs += "  - Expected IllegalArgumentException for _invalid_ DNA sequence but none was thrown.\n";
        } catch (IllegalArgumentException e) {
            // logs += "Correctly throws IllegalArgumentException for invalid DNA
            // sequence.\n";
            if (!e.getMessage().equals(EXPECTED_CONSTRUCTOR_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
            return logs;
        } catch (Exception e) {
            logs += "  - Unexpected exception thrown for _invalid_ DNA sequence.\n";
            logs += "  - " + e.toString();
        }
        return logs;
    }

    /**
     * Tests this.seq (Constructor) and DNA toString
     * - Should simply return the sequence, which should be saved in uppercase
     * at the constructor; these tests also test for the constructing
     * saving the sequence correctly in upper-case.
     * - An empty DNA sequence has the string representation ""
     * 
     * @return true iff all B.1/2a toString tests pass
     */
    public static String testseqFieldAndB2toString() {
        // All toString should return seq that was upper-cased in constructor
        String logs = "";
        DNA dnaSeq1 = new DNA("ATCGatcg");
        DNA dnaSeq2 = new DNA("a");
        // dnaSeq1.toString() should give "ATCGATCG"
        DNA dnaSeq3 = new DNA("AaAa");
        DNA dnaSeq7 = new DNA("ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG");
        DNA emptySeq = new DNA("");
        DNA[] testDNA = new DNA[] { dnaSeq1, dnaSeq2, dnaSeq3, dnaSeq7, emptySeq };
        String[] expected = new String[] { "ATCGATCG", "A", "AAAA", "ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG",
                "" };
        for (int i = 0; i < testDNA.length; i++) {
            String actualString = testDNA[i].toString();
            int num = i + 1;
            if (num == 4) {
                num = 7; // consistent with other tests
            } else if (num == 5) {
                num = -1;
            }
            String testResult = compareStrings(actualString, expected[i], num);
            if (!testResult.equals("")) {
                logs += "  - " + testResult + "\n";
            }
        }
        return logs;
    }

    /**
     * Tests DNA size
     * - Should simply return the length of the sequence
     * - An empty DNA sequence has a size of 0
     * 
     * @return true iff all B.2b toString tests pass
     */
    public static String testB2size() {
        DNA dnaSeq1 = new DNA("ATCGatcg");
        // dnaSeq1.size() should give 8
        DNA dnaSeq2 = new DNA("a");
        DNA dnaSeq3 = new DNA("AaAa");
        DNA emptySeq = new DNA("");
        DNA dnaSeq7 = new DNA("ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG");
        // dnaSeq1.toString() should give "ATCGATCG"
        // dnaSeq1.size() should give 8
        String logs = "";
        DNA[] testDNA = new DNA[] { dnaSeq1, dnaSeq2, dnaSeq3, dnaSeq7, emptySeq };
        int[] expected = new int[] { 8, 1, 4, 45, 0 };
        for (int i = 0; i < testDNA.length; i++) {
            int actualSize = testDNA[i].size();
            int num = i + 1;
            if (num == 4) {
                num = 7; // consistent with other tests
            } else if (num == 5) {
                num = -1;
            }
            String testResult = compareSizes(actualSize, expected[i], num);
            if (!testResult.equals("")) {
                logs += "  - " + testResult + "\n";
            }
        }

        return logs;
    }

    /**
     * Tests DNA complement
     * - Should return a _String_ complement of the DNA sequence, in uppercase
     * - An empty DNA sequence has a complement of ""
     * 
     * @return true iff all B.3 complement tests pass
     */
    public static String testB3complement() {
        DNA dnaSeq1 = new DNA("ATCGatcg");
        DNA dnaSeq2 = new DNA("a");
        DNA dnaSeq3 = new DNA("AaAa");
        DNA dnaSeq4 = new DNA("ACCAGTGTAG");
        DNA emptySeq = new DNA("");
        String logs = "";
        DNA[] testDNA = new DNA[] { dnaSeq1, dnaSeq2, dnaSeq3, dnaSeq4, emptySeq };
        String[] expected = new String[] { "TAGCTAGC", "T", "TTTT", "TGGTCACATC", "" };
        for (int i = 0; i < testDNA.length; i++) {
            int num = i + 1;
            if (num == 4) {
                num = -1;
            }
            String actualComplement = testDNA[i].complement();
            String testResult = compareStrings(actualComplement, expected[i], num);
            if (!testResult.equals("")) {
                logs += "  - " + testResult + "\n";
            }
        }
        return logs;
    }

    /**
     * Tests DNA countOccurrences
     * - Should return a the number of times a certain character is found in
     * a DNA sequence
     * - Should ignore letter-casing when counting ('a' and 'A') both count 'A'
     * - An empty DNA sequence will always return 0 when given a valid base
     * - An IllegalArgumentException should be raised if given an invalid
     * base character, ignoring letter-casing
     * 
     * @return true iff all B.4 countOccurrences tests pass
     */
    public static String testB4countOccurrences() {
        DNA dnaSeq1 = new DNA("ATCGatcg");
        DNA dnaSeq2 = new DNA("a");
        DNA dnaSeq3 = new DNA("AaAa");
        DNA dnaSeq7 = new DNA("ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG");
        DNA emptySeq = new DNA("");

        String logs = "";

        int a1Count = dnaSeq1.countOccurrences('A');
        String testResult = compareCounts(a1Count, 2, 1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        int t1Count = dnaSeq1.countOccurrences('T');
        testResult = compareCounts(t1Count, 2, 1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Test ignoring letter-casing
        int a1LowercasedCount = dnaSeq1.countOccurrences('a');
        testResult = compareCounts(a1LowercasedCount, 2, 1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        int a2Count = dnaSeq2.countOccurrences('A');
        testResult = compareCounts(a2Count, 1, 2);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        int a3Count = dnaSeq3.countOccurrences('A');
        testResult = compareCounts(a3Count, 4, 3);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        int a7Count = dnaSeq7.countOccurrences('A');
        testResult = compareCounts(a7Count, 11, 7);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Testing 0 count case for non-empty sequence
        int t3Count = emptySeq.countOccurrences('T');
        testResult = compareCounts(t3Count, 0, 3);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Testing 0 count case for empty sequence
        int a4Count = emptySeq.countOccurrences('A');
        testResult = compareCounts(a4Count, 0, -1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        try {
            int d1Count = dnaSeq1.countOccurrences('D');
            logs += "  - Expected IllegalArgumentException for invalid base 'D' but none was thrown.\n";
        } catch (IllegalArgumentException e) {
            if (!e.getMessage().equals(EXPECTED_INVALID_BASE_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
        } catch (Exception e) {
            logs += "  - Unexpected exception thrown for invalid base 'D'.\n";
            logs += "  - " + e.toString();
        }

        try {
            // make sure they also throw IAE when lowercased invalid base is given.
            int d1LowercasedCount = dnaSeq1.countOccurrences('d');
            logs += "  - Expected IllegalArgumentException for invalid base 'd' but none was thrown.\n";
        } catch (IllegalArgumentException e) {
            // logs += " - Correctly throws IllegalArgumentException for invalid base
            // 'd'.\n";
            // logs += "Correctly throws IllegalArgumentException for invalid DNA
            // sequence.\n";
            if (!e.getMessage().equals(EXPECTED_INVALID_BASE_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
            return logs;
        } catch (Exception e) {
            logs += "  - Expected IllegalArgumentException for invalid base 'd' but a different exception was thrown.\n";
            logs += "  - " + e.toString();
        }
        return logs;
    }

    /**
     * Tests DNA percentageOf
     * - Should return a double between 0.0 and 1.0 based on the relative
     * percentage of a give character in a DNA sequence
     * - Should ignore letter-casing when counting ('a' and 'A') both count 'A'
     * - An empty DNA sequence will always return 0.0 when given a valid base
     * - An IllegalArgumentException should be raised if given an invalid
     * base character, ignoring letter-casing (this should be left to
     * countOccurrences to raise)
     * 
     * @return true iff all B.5 percentageOf tests pass
     */
    public static String testB5percentageOf() {
        DNA dnaSeq1 = new DNA("ATCGatcg");
        DNA dnaSeq2 = new DNA("a");
        DNA dnaSeq3 = new DNA("AaAa");
        DNA dnaSeq4 = new DNA("ACCAGTGTAG");
        DNA emptySeq = new DNA("");

        String logs = "";

        double t1Percent = dnaSeq1.percentageOf('T');
        String testResult = compareCounts(t1Percent, 0.25, 1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        double a2Percent = dnaSeq2.percentageOf('A');
        testResult = compareCounts(a2Percent, 1.0, 2);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Test ignoring letter-casing
        double t2LowercasedPercent = dnaSeq1.percentageOf('t');
        testResult = compareCounts(t2LowercasedPercent, 0.25, 1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        double a3percent = dnaSeq3.percentageOf('A');
        testResult = compareCounts(a3percent, 1.0, 3);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Testing different percentage for all bases (upper-cased)
        double a4percent = dnaSeq4.percentageOf('A');
        testResult = compareCounts(a4percent, 0.3, 5);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        double t4percent = dnaSeq4.percentageOf('T');
        testResult = compareCounts(t4percent, 0.2, 5);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        double c4percent = dnaSeq4.percentageOf('C');
        testResult = compareCounts(c4percent, 0.2, 5);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        double g4percent = dnaSeq4.percentageOf('G');
        testResult = compareCounts(g4percent, 0.3, 5);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        // Testing 0 count/0.0 percentage case for empty string
        double emptyAPercent = emptySeq.percentageOf('A');
        testResult = compareCounts(emptyAPercent, 0.0, -1);
        if (!testResult.equals("")) {
            logs += "  - " + testResult + "\n";
        }

        try {
            double d1Percent = dnaSeq1.percentageOf('D');
            logs += "  - Expected IllegalArgumentException for invalid base 'D' but none was thrown.\n";
        } catch (IllegalArgumentException e) {
            if (!e.getMessage().equals(EXPECTED_INVALID_BASE_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
        } catch (Exception e) {
            logs += "  - Expected IllegalArgumentException for invalid base 'D' but a different exception was thrown.\n";
            logs += "  - " + e.toString();
        }

        try {
            // make sure they also throw IAE when lowercased invalid base is given.
            double d1LowercasedPercent = dnaSeq1.percentageOf('d');
            logs += "  - Expected IllegalArgumentException for invalid base 'd' but none was thrown.\n";
        } catch (IllegalArgumentException e) {
            if (!e.getMessage().equals(EXPECTED_INVALID_BASE_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
        } catch (Exception e) {
            logs += "  - Expected IllegalArgumentException for invalid base 'd' but a different exception was thrown.\n";
            logs += "  - " + e.toString();
        }
        return logs;
    }

    /**
     * Helper functions for testing.
     */
    public static String compareStrings(String actual, String expected, int num) {
        String result = "";
        String testName = "dnaSeq" + num;
        if (num == -1) {
            testName = "emptyDNASeq";
        }
        if (!actual.equals(expected)) {
            result += testName + ": Expected string is " + expected + ", Actual: " + actual;
        }
        return result;
    }

    public static String compareSizes(int actual, int expected, int num) {
        String result = "";
        String testName = "dnaSeq" + num;
        if (num == -1) {
            testName = "emptySeq";
        }
        if (actual != expected) {
            result += testName + ": Expected size is " + expected + ", Actual: " + actual;
        }
        return result;
    }

    public static String compareCounts(int actual, int expected, int num) {
        String result = "";
        String testName = "dnaSeq" + num;
        if (num == -1) {
            testName = "emptySeq";
        }
        if (actual != expected) {
            result += testName + ": Expected count is " + expected + ", Actual: " + actual;
        }
        return result;
    }

    public static String compareCounts(double actual, double expected, double num) {
        String result = "";
        String testName = "dnaSeq" + num;
        if (num == -1) {
            testName = "emptySeq";
        }
        if (actual != expected) {
            result += testName + ": Expected percentage is " + expected + ", Actual: " + actual;
        }
        return result;
    }

    /**
     * Generates a '***...***' error row string for readable test results.
     * 
     * @return - single error row string
     */
    public static String generateErrorRow() {
        String row = "";
        for (int i = 0; i < 80; i++) {
            row += '*';
        }
        return row;
    }

}
