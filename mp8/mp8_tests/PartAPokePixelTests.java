/**
 * CS 1 22fa 
 * Provided testing program for MP8 Part A: PokePixel class
 * 
 * @author El Hovik
 * 
 * Instructions:
 * Add any test code in the studentTestArea function; we recommend using the 
 * examples from the spec to iteratively check each exercise if one of the
 * provided tests are failing.
 * 
 * javac PokePixel.java
 * javac PartAPokePixelTests.java 
 *     - (can also use javac *.java to compile all java files, assuming no 
 *        compile errors in any of them)
 * java PartAPokePixelTests
 * 
 * This program provides tests for A.1-A.4 (PokePixel.java only).
 * Note that some test functions test multiple methods since
 * we need access to the private state for each PokePixel (e.g.
 * we need getType() to get the private type field).
 * 
 * If something is failing, make sure to read the test results and line
 * number corresponding to the PartAPokePixelTests.java test method line,
 * and PokePixel.java method line (if something is thrown from PokePixel
 * unexpectedly, which shouldn't happen for correct implementations).
 * 
 * Just like in MP7, we **strongly** recommend you use the Run -> Debug to step 
 * through each statement and compare with the expected results. This is 
 * similar to setting breakpoints and running in the VSCode Python debugger, 
 * and El demo'd this in Lectures 24-26.
 */
import java.util.Arrays;

public class PartAPokePixelTests {
    // This is one of the few cases where a global field is ok, since we're
    // keeping track of passed tests (almost always only makes sense for testing)
    public static int passed = 0;

    // Colors for improved test results                                          
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RESET = "\u001B[0m";

    public static final String[] TYPES = {"Fire", "Water", "Grass", 
                                          "Electric", "Ground"};

    public static void main(String[] args) {
        // Note to students: To test your code with your own smaller test 
        // cases, uncomment the following and add example calls in 
        // the provided studentTestArea function, then use the VSCode debugger 
        // to step through those calls to help debug any problems that come up. 
        // studentTestArea();

        // i is a counter for number of tests ran in case the tests abort
        // (used in the catch statement)
        int i = 1;
        int testCount = 3;
        try {
            // To debug, refer to correspond test function
            // Tests A.1, A.2, A.4 for random pixels
            String testA124Results = testRandomPokePixelsA124();
            printResults(testA124Results, "A.1, A.2, A.4 PokePixel() random");
            i++;

            String testA123Results = testNonRandom123();
            printResults(testA123Results, "A.1-A.3 PokePixel() non-random");
            i++;

            String testToStringResults = testToStringNonRandom();
            printResults(testToStringResults, "A.1-A.4 PokePixel() non-random with toString()");
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

    public static void studentTestArea() {
        // Students can add test their own testing code here
        // see example calls of assertEquals if you'd like to use them.
        // Example (A.3 Spec Example):
        PokePixel originallyFire = new PokePixel();
        // Set a debugger point on the above line if you want to check this,
        // which is preferred over just using System.out.println debugging
        String checkType = originallyFire.getType(); 
        // In the spec, we assume it was fire, but it may not actually be
        System.out.println("New PokePixel random type: " + checkType);
        originallyFire.changeType("Fire"); 
        checkType = originallyFire.getType(); 
        System.out.println("After changing to Fire type: " + checkType);
        originallyFire.changeType("Grass");
        System.out.println("After changing to Grass type: " + checkType);
        checkType = originallyFire.getType(); 
        System.out.println(checkType);
        // Feel free to add more examples below if you're debugging
        // failed test results

    }

    /**
     * Helper method to get type index given a type String.
     * @param type
     * @return index of given type in TYPES, or -1 if not found.
     */
    public static int getTypeIndex(String type) {
        for (int i = 0; i < TYPES.length; i++) {
            if (TYPES[i].equals(type)) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Tests A.1., A.2., and A.4 for randomly-constructed PokePixels
     * - A.1 PokePixel() constructor
     * - A.2 getType() method in PokePixel
     * - A.4 toString() method in PokePixel
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testRandomPokePixelsA124() {
        String result = "";
        // Testing randomness
        int[] tallies = {0, 0, 0, 0, 0};
        // Random object for assigning a random type upon initialization 
        int testCount = 1000;
        int errorMargin = 75; // 200 +- 75 margin window
        // 20% of 1000 = 200 for a perfect average
        int averageCount = testCount / tallies.length;
        // [125, 275] margin window for expected 200/1000 per count
        int minMargin = averageCount - errorMargin;
        int maxMargin = averageCount + errorMargin;
        // each type should occur roughly 20% (200) of 1000 times
        for (int i = 0; i < testCount; i++) {
            PokePixel ex = new PokePixel();
            String exType = ex.getType();
            int index = getTypeIndex(exType);
            if (index == -1) {
                String log = "Unexpected type found when calling getType()\n" +
                             "  - Should be one of the Strings in TYPES class constant " +
                             "but found " + exType + " (aborting rest of tests)\n";
                return log;
            }
            // While we're creating random PokePixels, we'll test toString for 
            // random types
            String pokeStr = ex.toString();
            String checkToString = assertEquals(pokeStr, exType.substring(0, 3));
            if (!checkToString.isEmpty()) {
                return "toString() test failed on a randomly-constructed PokePixel.\n" +
                        checkToString + "\n**Aborting** rest of tests (fix " + 
                        "PokePixel's toString and re-run tests).\n";
            }

            // type should be a valid type
            tallies[index]++;
        }
        String tallyString = Arrays.toString(tallies);
        for (int i = 0; i < tallies.length; i++) {
            int typeCount = tallies[i];
            if (typeCount <= minMargin || typeCount >= maxMargin) {
                result = "Randomness type-assignment for PokePixel constructor " + 
                         "tests failed:\n- Expected each type count to be between " + 
                         "[" + minMargin + ", " + maxMargin + "] for " + testCount + 
                         " PokePixel() instances,\n  but found " + typeCount + " " + 
                         TYPES[i] + " PokePixels.\n";
                result += "- Type tallies computed for random tests: " + tallyString + "\n";
                result += "  (if all are non-zero, try re-running the tests, otherwise " + 
                          "check your constructor!)\n";
            }
        }
        // If we reach here, everything checks out
        return result;
    }

    /*
     * Tests for getType and changeType for non-random PokePixels
     * (uses changeType to assign each type).
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testNonRandom123() {
        String logs = "";
        for (int i = 0; i < TYPES.length; i++) {
            String type = TYPES[i];
            String nextType = TYPES[(i + 1) % TYPES.length];
            // quick test to ensure they can change types
            PokePixel px = new PokePixel();
            px.changeType(type);
            String checkFirstCall = assertEquals(type, px.getType(), "px.changeType(\"" + type + "\");");
            if (!checkFirstCall.isEmpty()) { // incorrect for first call
                logs += checkFirstCall;
            } else { // now check that we can call it again
                px.changeType(nextType);
                String checkNewType = assertEquals(nextType, px.getType());
                if (!checkNewType.isEmpty()) {
                    logs += "Testing changeType with a second new type; expected " + 
                              "type to change again, but did not.";
                    logs += checkNewType;
                }
            }
        }
        return logs;
    }

    /*
     * Tests A.4 toString for non-random PokePixels
     * (requires getType/changeType to be correctly implemented)
     */
    public static String testToStringNonRandom() {
        String result = "";
        // Test toString() for each type String
        for (String type : TYPES) {
            PokePixel px = new PokePixel();
            px.changeType(type);
            String pxString = px.toString();
            // toString() of PokePixel should return first three characters
            // of its assigned type String
            result += assertEquals(type.substring(0, 3), pxString, 
                                   "toString() for " + type + "-type PokePixel");
        }
        return result;
    }

    /**
     * Helper function to print test results out
     * 
     * @param logs     - logs collected during a test function
     * @param testName - name of test to print results out
     */
    public static void printResults(String logs, String testName) {
        String result = logs.isEmpty() ? ANSI_GREEN + "PASSED" : ANSI_RED + "FAILED";
        result += ANSI_RESET;
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
     * Some helper assertion functions for comparing different types.
     * (note to students curious: in Java, you can redefine a method with
     * the same name if you define a different signature, as defined by the
     * types and number of parameters supported; Java is smart enough to
     * call the right one based on the arguments passed to the method call).
     */
    public static String assertEquals(int expected, int actual) {
        String result = "";
        if (expected != actual) {
            result = "\nExpected: " + expected + "\nActual: " + actual + "\n";
        }
        return result;
    }

    public static String assertEquals(int expected, int actual, String testDesc) {
        String result = "";
        if (expected != actual) {
            result = "Assertion error when testing " + testDesc + "\n";
            result = "  \n  - Expected: " + expected + "\n  - Actual: " + actual;
        }
        return result;
    }

    public static String assertEquals(String expected, String actual) {
        String result = "";
        if (!expected.equals(actual)){ 
            result = "\n  - Expected: " + expected + "\n  - Actual  : " + actual + "\n";
        }
        return result;
    }

    public static String assertEquals(String expected, String actual, String testDesc) {
        String result = "";
        if (!expected.equals(actual)) {
            result = "Assertion error when testing " + testDesc + "\n";
            result += "  - Expected: " + expected + "\n  - Actual  : " + actual + "\n";
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
