/**
 * CS 1 22fa 
 * Provided testing program for MP8 Part B: PokeLife class
 * 
 * Important: These tests should only be used after making sure all of the
 * Part A tests pass (see PartAPokePixelTests.java).
 * 
 * @author El Hovik
 * 
 * Instructions:
 * Add any test code in the studentTestArea function; we recommend using the 
 * examples from the spec to iteratively check each exercise if one of the
 * provided tests are failing.
 * 
 * javac PokePixel.java
 * javac PokeLife.java
 * javac PartBPokeLifeTests.java 
 *     - (can also use javac *.java to compile all java files, assuming no 
 *        compile errors in any of them)
 * java PartBPokeLifeTests
 * 
 * This program provides tests for B.1-B.7 (PokeLife.java) and requires that
 * Part A tests pass (see PartAPokePixelTests.java).
 * 
 * If something is failing, make sure to read the test results and line
 * number corresponding to the PartBPokeLifeTests.java test method line,
 * and the PokeLife.java and/or PokePixel.java method line (if something is 
 * thrown from one of these unexpectedly).
 * 
 * Just like in MP7, we **strongly** recommend you use the Run -> Debug to step 
 * through each statement and compare with the expected results. This is 
 * similar to setting breakpoints and running in the VSCode Python debugger, 
 * and El demo'd this in Lectures 24-26.
 */
import java.util.Arrays;

public class PartBPokeLifeTests {
    // This is one of the few cases where a global field is ok, since we're
    // keeping track of passed tests (almost always only makes sense for testing)
    public static int passed = 0;
    public static final String EXPECTED_CONSTRUCTOR_ERR = "width and height must be > 0";
    public static final String EXPECTED_INVALID_GET_POKE_ERR = "Invalid x and/or y coordinate.";

    // Colors for improved test results                                          
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RESET = "\u001B[0m";

    public static final String[] TYPES = {"Fire", "Water", "Grass", 
                                          "Electric", "Ground"};
    private static final String[] WEAKNESSES = {"Water,Ground", "Grass,Electric", "Fire", 
                                                "Ground", "Water,Grass"};


    public static void main(String[] args) {
        // Some examples of using split, which returns a String[] as described
        // in the spec
        String type = "Water";
        int typeIndex = 1; // find the index of TYPES "Water" (hard-coded
        // here, but shouldn't be in PokeLife.java)
        String weaknessStr = WEAKNESSES[1]; // "Grass,Electric"
        String[] parts = weaknessStr.split(",");
        // String[] result = {"Grass", "Electric"};
        // If a weaknessStr has no ",", then the split result will be a
        // 1-item array, such as {"Ground"} for the weakness of "Electric"

        // Note to students: To test your code with your own smaller test 
        // cases, uncomment the following and add example calls in 
        // the provided studentTestArea function, then use the VSCode debugger 
        // to step through those calls to help debug any problems that come up. 
        // studentTestArea();

        // i is a counter for number of tests ran in case the tests abort
        // (used in the catch statement)
        int i = 1;
        int testCount = 9;
        String[] testLabels = {"B.1 PokeLife constructor and B.2 getters (_valid_ arguments)",
                               "B.1 PokeLife constructor and B.2 getters (_invalid_ arguments)",
                               "B.3 PokeLife getPoke(x, y) (_valid_ arguments)",
                               "B.3 PokeLife getPoke(x, y) (_invalid_ arguments)",
                               "B.4 getWeaknesses",
                               "B.5 isSurroundedBy",
                               "B.6 updateType",
                               "B.7 getWinningType (3x3 spec example)",
                               "B.7 getWinningType (5x4 non-random test board)"};

        try {
            // To debug, refer to correspond test function
            String testB1aResults = testB12ConstructorValidArguments();
            printResults(testB1aResults, testLabels[i - 1]);
            i++;

            // Abort tests if constructor is incorrect for valid arguments
            if (!testB1aResults.isEmpty()) {
                String details = "Cannot continue tests without valid constructor implementation.";
                details += testB1aResults;
                abortTests(i, testCount, details);
                return;
            }
            // Otherwise, continue rest of tests
            String testB1bResults = testB1ConstructorInvalidArguments();
            printResults(testB1bResults, testLabels[i - 1]);
            i++;

            String testB3ValidResults = testB3getPokeValid();
            printResults(testB3ValidResults, testLabels[i - 1]);
            i++;

            String testB3InvalidResults = testB3getPokeInvalid();
            printResults(testB3InvalidResults, testLabels[i - 1]);
            i++;

            String testB4Results = testB4getWeaknesses();
            if (!testB4Results.isEmpty()) {
                String details = "Cannot continue B.4-B.7 tests without valid getWeaknesses.\n";
                details += testB4Results;
                abortTests(i, testCount, details);
                return;
            }
            printResults(testB4Results, testLabels[i - 1]);
            i++;

            String testB5Results = testB5isSurroundedBy();
            printResults(testB5Results, testLabels[i - 1]);
            i++;

            String testB6Results = testB6updateType();
            printResults(testB6Results, testLabels[i - 1]);
            i++;

            String testB7SpecResults = testB7getWinningTypeSpecExample();
            printResults(testB7SpecResults, testLabels[i - 1]);
            i++;

            String testB7TestBoardResults = testB7getWinningTypeTestBoard();
            printResults(testB7TestBoardResults, testLabels[i - 1]);
            i++;
            System.out.println();
            System.out.println("Total tests passed: " + passed + "/" + testCount);
        } catch (Exception e) {
            String row = generateErrorRow();
            String logs = row + "\n";
            logs += ANSI_RED + "[TESTS ABORTING] " + ANSI_RESET;
            logs += "Unexpected exception thrown for the following test:\n";
            logs += testLabels[i - 1] + "\n";
            // logs += row + "\n";
            logs += "  - " + e.toString() + "\n";
            logs += "  - (Please debug your code for this test before re-testing other cases).\n";
            logs += row + "\n";
            logs += "  - Total tests ran before unexpected exception: " + (i - 1) + "/" + testCount + "\n";
            System.out.println(logs);
        }
    }

    public static void studentTestArea() {
        // Students can add test their own testing code here
        // see example calls of assertEquals if you'd like to use them.
        // testMode == 1 Game.java test board
        PokeLife life = new PokeLife(5, 4, false);
        System.out.println("5x4 non-random small test board (initial state):");
        System.out.println(life);

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
     * Tests B.1. constructor and B.2. getters for valid arguments.
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB12ConstructorValidArguments() {
        String logs = "";
        try {
            PokeLife life1 = new PokeLife(5, 4, false);
            PokeLife life2 = new PokeLife(5, 4, true);
            PokeLife life3 = new PokeLife(60, 60, false);
            logs += assertEquals(5, life1.getWidth(), "5x4 width (isRandom=false)");
            logs += assertEquals(4, life1.getHeight(), "5x4 height");

            logs += assertEquals(5, life2.getWidth(), "5x4 width (isRandom=true)");
            logs += assertEquals(4, life2.getHeight(), "5x4 height");

            logs += assertEquals(60, life3.getWidth(), "60x60 width");
            logs += assertEquals(60, life3.getHeight(), "60x60 height");

        } catch (Exception e) {
            logs += "  - \nUnexpected exceptions thrown for _valid_ PokeLife arguments.\n";
            logs += "  - " + e.toString();
        }

        return logs;
    }

    /**
     * Tests B.1. constructor for correct IllegalArgumentException thrown when 
     * width or height arguments are < 0.
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB1ConstructorInvalidArguments() {
        String logs = "";
        try {
            PokeLife invalidNegativeWidth = new PokeLife(-1, 4, false);
            PokeLife invalid0Width = new PokeLife(0, 4, false);
            PokeLife invalidNegativeHeight = new PokeLife(5, -1, false);
            PokeLife invalid0Height = new PokeLife(5, 0, true);
            PokeLife invalid00 = new PokeLife(0, 0, false);
            PokeLife invalidBothNegative = new PokeLife(-1, -1, false);
        } catch (IllegalArgumentException e) {
            if (!e.getMessage().equals(EXPECTED_CONSTRUCTOR_ERR)) {
                logs += "  - IllegalArgumentException thrown, but the " + 
                        "following incorrect error message was given:\n";
                logs += "  - \"" + e.getMessage() + "\"\n";
            }
        } catch (Exception e) {
            logs += "  - Unexpected exceptions thrown for _invalid_ PokeLife arguments.\n";
            logs += "  - " + e.toString() + "\n";
        }
        return logs;
    }

    /**
     * Tests B.3 getPoke for non-random PokePixels
     * (requires everything so far to be correctly implemented)
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB3getPokeValid() {
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);

        PokePixel px00 = life.getPoke(0, 0);
        PokePixel px01 = life.getPoke(0, 1);
        PokePixel px10 = life.getPoke(1, 0);
        logs += assertEquals("Fire", px00.getType());
        logs += assertEquals("Fire", px01.getType());
        logs += assertEquals("Electric", px10.getType());

        // some corner cases for this board
        PokePixel px03 = life.getPoke(0, 3); // top right
        PokePixel px40 = life.getPoke(4, 0); // bottom left
        PokePixel px43 = life.getPoke(4, 3); // bottom right

        logs += assertEquals("Grass", px03.getType());
        logs += assertEquals("Grass", px40.getType());
        logs += assertEquals("Electric", px43.getType());
        return logs;
    }

    /**
     * Tests B.3 getPoke for _invalid_ (x, y) arguments which should
     * throw an IllegalArgumentException if either x or y is negative,
     * x >= board width, or y >= board height. 
     * (requires everything so far to be correctly implemented)
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB3getPokeInvalid() {
        // coordinates for tested invalid positions
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);
        // life.getPoke(-1, 0);  // invalid negative x case
        // life.getPoke(0, -1);  // invalid negative y case
        // life.getPoke(-1, -1); // invalid negative x and y case
        // life.getPoke(5, 0);   // invalid x upper-bounds case (5 rows, 0-based indexing)
        // life.getPoke(6, 0);   // one more test 
        // life.getPoke(0, 4);   // invalid y upper-bounds case
        // life.getPoke(0, 5);   // one more test 
        // life.getPoke(5, 4);   // invalid x and y upper-bounds case
        // life.getPoke(6, 5);   // invalid x and y upper-bounds case
        int[] xs = {-1, 0, -1, 5, 6, 0, 0, 5, 6};
        int[] ys = {0, -1, -1, 0, 0, 4, 5, 4, 5};
        boolean foundInvalidMessage = false;
        // Only print invalid message test case once.
        String[] labels = {"negative x", "negative y", "negative x and y",
                           "x == width", "x > width", "y == height", "y > height",
                           "x == width and y == height", "x > width and y > height"};
        for (int i = 0; i < xs.length; i++) {
            int x = xs[i];
            int y = ys[i];
            String label = labels[i];
            try {
                life.getPoke(x, y);
            } catch (IllegalArgumentException e) {
                if (!foundInvalidMessage) {
                    String testMessage = assertEquals(EXPECTED_INVALID_GET_POKE_ERR, e.getMessage(), "IllegalArgumentException thrown but with incorrect message)");
                    if (!testMessage.isEmpty()) {
                        foundInvalidMessage = true;
                        logs += testMessage;
                    }
                }
            } catch (Exception e) {
                logs += "  - Unexpected exception thrown for _invalid_ PokeLife arguments (" + 
                        label + " test):\n";
                logs += "    - " + e.toString() + "\n\n";
            }
        }
        return logs;
    }

    /**
     * Tests B.4 getWeaknesses (requires everything so far to be 
     * correctly implemented)
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB4getWeaknesses() {
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);
        String[] fireWeaknesses = life.getWeaknesses("Fire");
        String[] waterWeaknesses = life.getWeaknesses("Water");
        String[] grassWeaknesses = life.getWeaknesses("Grass");
        String[] electricWeaknesses = life.getWeaknesses("Electric");
        String[] groundWeaknesses = life.getWeaknesses("Ground");
        logs += assertEquals(new String[]{"Water", "Ground"}, fireWeaknesses, "getWeaknesses(\"Fire\")");
        logs += assertEquals(new String[]{"Grass", "Electric"}, waterWeaknesses, "getWeaknesses(\"Water\")");
        logs += assertEquals(new String[]{"Fire"}, grassWeaknesses, "getWeaknesses(\"Grass\")");
        logs += assertEquals(new String[]{"Ground"}, electricWeaknesses, "getWeaknesses(\"Electric\")");
        logs += assertEquals(new String[]{"Water", "Grass"}, groundWeaknesses, "getWeaknesses(\"Ground\")");
        return logs;
    }

    /**
     * Tests B.5 isSurroundedBy for non-random 5x4 test board
     * (requires getType/changeType to be correctly implemented)
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB5isSurroundedBy() {
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);
        // Fir Fir Wat Gra 
        // Ele Gro Wat Gro 
        // Ele Ele Gro Gra 
        // Gro Fir Gro Gra 
        // Gra Gra Ele Ele

        // Tests from B.5 spec examples
        PokePixel px = life.getPoke(1, 1); // "Ele", surrounded by 4 "Gro"
        logs += assertEquals("Ground", px.getType());
        // The board's [1][1] pixel is "Gro", surrounded by 2 "Fir", 3 "Ele", 2 "Wat", and 1 "Gro
        boolean test1 = life.isSurroundedBy(1, 1, "Fire", 1);
        logs += assertEquals(true, test1, "isSurroundedBy test1");
        boolean test2 = life.isSurroundedBy(1, 1, "Fire", 2);
        logs += assertEquals(true, test2, "isSurroundedBy test2");
        boolean test3 = life.isSurroundedBy(1, 1, "Fire", 3);
        logs += assertEquals(false, test3, "isSurroundedBy test3");
        boolean test4 = life.isSurroundedBy(1, 1, "Water", 3);
        logs += assertEquals(false, test4, "isSurroundedBy test4");
        boolean test5 = life.isSurroundedBy(1, 1, "Grass", 1);
        logs += assertEquals(false, test5, "isSurroundedBy test5");
        boolean test6 = life.isSurroundedBy(1, 1, "Ground", 1);
        logs += assertEquals(true, test6, "isSurroundedBy test6");
        boolean test7 = life.isSurroundedBy(1, 1, "Ground", 2);
        logs += assertEquals(false, test7, "isSurroundedBy test7");
        // The board's [1][3] pixel is the right-most "Gro", surrounded by 2 "Wat", 2 "Gra", and 1 "Gro"

        boolean test8 = life.isSurroundedBy(1, 3, "Grass", 1);
        logs += assertEquals(true, test8, "isSurroundedBy test8");
        boolean test9 = life.isSurroundedBy(1, 3, "Water", 2);
        logs += assertEquals(true, test9, "isSurroundedBy test9");
        boolean test10 = life.isSurroundedBy(1, 3, "Water", 3);
        logs += assertEquals(false, test10, "isSurroundedBy test10");

        return logs;
    }

    /**
     * Tests B.6 updateType for non-random 5x4 test board
     * (requires everything so far to be correctly implemented).
     * Since updateType is a private method that this client testing
     * program doesn't have access to, it is tested using the provided
     * public lifeCycle method.
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB6updateType() {
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);
        // Fir Fir Wat Gra 
        // Ele Gro Wat Gro 
        // Ele Ele Gro Gra 
        // Gro Fir Gro Gra 
        // Gra Gra Ele Ele

        // Tests from B.6 spec examples
        // updateType is private, so we test with lifeCycle, which uses it
        String cycle0Expected = "\nFir Fir Wat Gra \nEle Gro Wat Gro \nEle Ele Gro Gra \nGro Fir Gro Gra \nGra Gra Ele Ele \n";
        String cycle1Expected = "\nFir Fir Wat Gra \nEle Gro Wat Gro \nGro Gro Gro Gra \nGra Gro Gra Gra \nGra Gra Ele Ele \n";
        String cycle2Expected = "\nFir Fir Wat Gra \nGro Gro Wat Gro \nGra Gra Gra Gra \nGra Gra Gra Gra \nGra Gra Ele Ele \n";
        String cycle3Expected = "\nGro Gro Wat Gra \nGra Gra Gra Gra \nGra Gra Gra Gra \nGra Gra Gra Gra \nGra Gra Ele Ele \n";
        String cycle0 = life.toString();
        logs += assertEquals(cycle0Expected, "\n" + cycle0, "Initial board string (0 lifeCycle() calls)");

        life.lifeCycle();
        String cycle1 = life.toString();
        logs += assertEquals(cycle1Expected, "\n" + cycle1, "updateType across board after 1 lifeCycle() call");

        life.lifeCycle();
        String cycle2 = life.toString();
        logs += assertEquals(cycle2Expected, "\n" + cycle2, "updateType across board after 2 lifeCycle() calls");

        life.lifeCycle();
        String cycle3 = life.toString();
        logs += assertEquals(cycle3Expected, "\n" + cycle3, "updateType across board after 3 lifeCycle() calls");

        return logs;
    }

    /**
     * Tests getWinningType for non-random PokePixels from B.7 spec
     * example (3x3 board).
     * (requires everything so far to be correctly implemented)
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB7getWinningTypeSpecExample() {
        String logs = "";
        // Tests from B.7 spec examples
        // Populate test board from B.7 spec example
        PokeLife life = new PokeLife(3, 3, false);
        life.getPoke(0, 0).changeType("Fire");
        life.getPoke(0, 1).changeType("Water");
        life.getPoke(0, 2).changeType("Electric");
        life.getPoke(1, 0).changeType("Electric");
        life.getPoke(1, 1).changeType("Grass");
        life.getPoke(1, 2).changeType("Fire");
        life.getPoke(2, 0).changeType("Fire");
        life.getPoke(2, 1).changeType("Ground");
        life.getPoke(2, 2).changeType("Water");

        String firstWinningType = life.getWinningType();
        logs += assertEquals("Fire", firstWinningType, "spec example for winningType (no ties)");

        PokePixel px = life.getPoke(1, 2);  // Fire
        PokePixel px2 = life.getPoke(0, 0); // Fire
        px.changeType("Grass");
        px2.changeType("Ground");
        String secondWinningType = life.getWinningType();
        // Ground
        logs += assertEquals("Ground", secondWinningType, "spec example for winningType, tie-breaking with last type");

        return logs;
    }

    /**
     * Tests for B.7 getWinningType with the small non-random 5x4 test board
     * over a few cycles.
     * 
     * @return descriptive test error message if a test fails, 
     * otherwise "" to indicate these tests pass.
     */
    public static String testB7getWinningTypeTestBoard() {
        String logs = "";
        PokeLife life = new PokeLife(5, 4, false);
        // Fir Fir Wat Gra 
        // Ele Gro Wat Gro 
        // Ele Ele Gro Gra 
        // Gro Fir Gro Gra 
        // Gra Gra Ele Ele

        // Tests from B.7 spec examples
        // updateType is private, so we test with lifeCycle, which uses it
        String cycle0Winner = life.getWinningType(); 
        logs += assertEquals("Ground", cycle0Winner, "Initial board string (0 lifeCycle() calls)");

        life.lifeCycle();
        String cycle1Winner = life.getWinningType(); 
        logs += assertEquals("Grass", cycle1Winner, "updateType across board after 2 lifeCycle() calls");

        life.lifeCycle();
        String cycle2Winner = life.getWinningType(); 
        logs += assertEquals("Grass", cycle2Winner, "updateType across board after 3 lifeCycle() calls");

        life.lifeCycle();
        String cycle3Winner = life.getWinningType(); 
        logs += assertEquals("Grass", cycle3Winner, "updateType across board after 3 lifeCycle() calls");

        return logs;
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

    public static void abortTests(int testsRan, int testCount, String details) {
        String row = generateErrorRow();
        String logs = row + "\n";
        logs += ANSI_RED + "[TESTS ABORTING] " + ANSI_RESET;
        logs += details + "\n";
        logs += "  - (Please debug your code for this test before re-testing other cases).\n";
        logs += row + "\n";
        logs += "  - Total tests ran before aborting: " + (testsRan - 1) + "/" + testCount + "\n";
        System.out.println(logs);
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
            result = "\nExpected: " + expected + "\nActual: " + actual;
        }
        return result;
    }

    public static String assertEquals(int expected, int actual, String testDesc) {
        String result = "";
        if (expected != actual) {
            result = "Assertion error when testing " + testDesc + "\n";
            result += "\n  - Expected: " + expected + "\n  - Actual: " + actual + "\n";
        }
        return result;
    }

    public static String assertEquals(double expected, double actual) {
        String result = "";
        if (expected != actual) {
            result = "\n  - Expected: " + expected + "\n  - Actual: " + actual + "\n";
        }
        return result;
    }

    public static String assertEquals(boolean expected, boolean actual, String testDesc) {
        String result = "";
        if (expected != actual) {
            result = "Assertion error when testing " + testDesc + "\n";
            result += "\n  - Expected: " + expected + "\n  - Actual  : " + actual + "\n";
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

    public static String assertEquals(String[] expected, String[] actual, String testDesc) {
        String result = "";
        if (!Arrays.equals(expected, actual)) {
            String expString = Arrays.toString(expected);
            String actString = Arrays.toString(actual);
            result = "Assertion error when testing " + testDesc + "\n";
            result += "  - Expected: " + expString + "\n  - Actual  : " + actString + "\n";
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
