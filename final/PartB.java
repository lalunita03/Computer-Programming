/**
 * CS 1 22fa Final Exam Part B
 * Student Name: Lea Grohmann
 */
public class PartB {
    
    /**
     * Main function of PartB.java, testing an implemented toSnakeCase
     * function for Part B.1 of the Final Exam.
     * 
     * DO NOT MODIFY.
     */
    public static void main(String[] args) {
        String s = toSnakeCase("snek_case");
        int failedCount = assertEquals("snek_case", s);
        int testCount = 7;
        s = toSnakeCase("snakeCase");
        failedCount += assertEquals("snake_case", s);
        s = toSnakeCase("camelCase");
        failedCount += assertEquals("camel_case", s);
        s = toSnakeCase("PascalCase");
        failedCount += assertEquals("pascal_case", s);
        s = toSnakeCase("removeAll3");
        failedCount += assertEquals("remove_all3", s);
        s = toSnakeCase("cAtTeRpIlLaRcAse");
        failedCount += assertEquals("c_at_te_rp_il_la_rc_ase", s);
        s = toSnakeCase("");
        failedCount += assertEquals("", s);

        if (failedCount == 0) {
            System.out.println("[PASSED] All B.1. toSnakeCase tests pass.");
        } else {
            System.out.println("[FAILED] " + failedCount + "/" + testCount + 
                               " B.1 toSnakeCase tests failed.");
        }
    }

    /**
     * A helper function to compare an expected String value with an actual
     * String value. Returns 1 if the assertion failed, otherwise 0.
     * @param expected - Expected String value
     * @param actual - Actual String value
     * @return - 1 if assertion failed (representing 1 failed test, otherwise 0)
     * 
     * DO NOT MODIFY.
     */
    public static int assertEquals(String expected, String actual) {
        int failedCount = 0;
        if (!expected.equals(actual)) {
            failedCount++;
        }
        return failedCount;
    }

    /**
     * Converts a string to snake case
     * example: "randomString" --> "random_string"
     * @param s - string to be converted to snake case
     * @return - `s` in snake case
     */
    public static String toSnakeCase(String s) {

        String newS = "";
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && i < s.length() && Character.isUpperCase(s.charAt(i))) {
                newS += "_";
            }
            newS += s.charAt(i);
        }
        return newS.toLowerCase();
    }
}
