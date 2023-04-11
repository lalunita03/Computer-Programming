/**
 * CS 1 22fa MP 7 Part A Starter Code
 * Intro to Java
 * Student name: Lea Grohmann
 * 
 * Reminder: Part A is strictly no-collaboration. If you run into questions,
 * ask on Discord/OH!
 * 
 * This is an executable "client" Java program (as opposed to the 
 * DNA class defined in DNA.java). Note that this client
 * program has a main method, which is called when the program
 * is ran from the terminal (or in an IDE), similar to the
 * code ran in an if __name__ == '__main__' branch in a .py program.
 * 
 * If running a .java program in the terminal (assuming you have 
 * java installed), you can run this as follows:
 * 
 * $ javac MP7A.java
 * $ java MP7A
 * 
 * Analogous to:
 * $ python3 mp7a.py
 * 
 * The first line compiles the Java program (javac stands for compile Java).
 * The second line runs the compiled Java program, assuming no
 * compiler errors were thrown when compiling (very common to get these
 * when you have errors in your first Java programs). 
 * 
 * Alternatively, you can use the Play -> Run Java button in VSCode,
 * though the first approach can be helpful to get a feel for 
 * the required "compile, then run" process in Java.
 * You can find a Java setup guide on the course website to get you started 
 * as well.
 */
public class MP7A {

    /**
     * Main method, invoked when this Java program is compiled/ran.
     * The method header syntax is very strict for every main method
     * in an executable Java program; do not change it. 
     * You don't have to worry too much about what it means for the 
     * purposes of this assignment (you'll learn more
     * in CS 2 if you take it and can ask El on Discord/OH).
     */
    public static void main(String[] args) {
        // You can test expressions/Java code here.
        // To print to the terminal, use System.out.println(<value>); 

        // Provided example from Part A.1.
        // int example = 1 + 2;
        // System.out.println(example);
        // Provided examples from Part A.2.
        // String result = "foo";
        
        // System.out.println(result);
        // String result = foo;
        // System.out.println(result);;

        // B.2.1.
        // B.2.2.
        // B.2.3.
        // B.2.4.

        // Some tests for Part A.3.c.
        String twoDashes = stringMultiplier("-", 2);
        String pythonWannabe = stringMultiplier("-", 70);
        String batmanDemo = stringMultiplier("na", 20);

        System.out.println(twoDashes);
        System.out.println(pythonWannabe);
        System.out.println(batmanDemo);
        // You can add more tests here
    }

    /**
     * Part A.1. Expressions
     * Write your answers for Part A.1. here. Make sure you are
     * actually testing these in Java (e.g. in the above
     * main method and re-compiling/running the program in the 
     * terminal).
     * -------------------------------------------------- 
     * Example format of expected answers:
     * #. <expression from spec> // evaluated value
     * 0. 1 + 2 // 3
     * -------------------------------------------------- 
     * 1. 8 - 5 // 3
     * 2. 6 * 2.5 // 15.0
     * 3. 51 / 2 // 25
     * 4. 51 / -2 // -25
     * 5. 51 % 2 // 1
     * 6. 51 % -2 // 1
     * 7. -51 % 2 // -1
     * 8. 51 / -2.0 // -25.5
     * 9. 1 + 4 * 5 // 21
     * 10. (1 + 4) * 5 // 25
     */

    /**
     * Part A.2. String Expressions
     * Write your answers for Part A.2. here.
     * Two examples of what we expect for your answers are provided below,
     * one with a valid assignment and the other with an error.
     * -------------------------------------------------- 
     * Example format of expected answers:
     * 0. String result = "foo";
     * a. "foo" 
     * b. No error
     * c. Aside from the type and ;, Python evaluates "foo" the same as Java.
     * 
     * 0. String result = foo;
     * a. Error 
     * b. MP7A.java:35: error: cannot find symbol
          String result = foo;
                        ^
          symbol:   variable foo
          location: class MP7A
     * c. Python and Java have similar errors in this case missing quotes
     * around characters that are expected to be treated as String/str values.
     * For example: (you don't have to go this in depth, but you are encouraged to
     *               to indicate you actually understand the error/difference between Java and Python)
     * >>> result = foo
     * gives an error for an undefined variable/symbol 
       Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       NameError: name 'foo' is not defined
     * however, this error occurs when the Java program is compiled, 
     * whereas Python (which we don't compile) raises the NameError only
     * when the statement is (unsuccessfully) executed in a ran .py program or interpreter. 
     * -------------------------------------------------- 
     * 1. String result = "foo" + 'bar';
     * a. error
     * b. MP7A.java:57: error: unclosed character literal
          String result = "foo" + 'bar';
                                  ^
          MP7A.java:57: error: unclosed character literal
          String result = "foo" + 'bar';
                                      ^
          MP7A.java:57: error: not a statement
          String result = "foo" + 'bar';
                                    ^
     * c. in java strings always have "", python allows
     *    both "" and '' for strings
     * -------------------------------------------------- 
     * 2. String result = "foo" + "bar";
     * a. "foobar"
     * b. no error
     * c. string concatination with + is possible in both
     *    languages
     * -------------------------------------------------- 
     * 3. String result = "foo"
          String b = "bar"
          String result += b;
     * a. error
     * b. MP7A.java:57: error: ';' expected
          String result = "foo"
                               ^
          MP7A.java:58: error: ';' expected
          String b = "bar"
                          ^
          MP7A.java:59: error: ';' expected
          String result += b;
                       ^
          MP7A.java:59: error: not a statement
          String result += b;
                           ^
     * c. in java every line needs to end with a semicolon
     *    python doesn't rely on semicolons 
     * -------------------------------------------------- 
     * 4. String month = "October";
          int days = 31;
          String result = days + " days hath " + month;
          System.out.println(result);
     * a. "31 days hath October"
     * b. no error
     * c. in java strings can be concatinated with ints
     *    this is not possible in python
     * -------------------------------------------------- 
     */

    /**
     * Part A.3. String Generation
     * Warm-up:
     * Write your answers for Part A.3.a. and B.3.b. here, 
     * indicating the evaluated result (or an error/what type 
     * if an error is thrown) **as well as whether the behavior
     * was different than what you expected**.
     * -------------------------------------------------- 
     * a. 3150 (I expected it to be a string of 70 '-')
     * 
     * b. MP7A.java:55: error: bad operand types for binary operator '*'
          System.out.println("-" * 70);
                                 ^
          first type:  String
          second type: int
          (this is also not what I expected)
     * 
     * -------------------------------------------------- 
     * c. Next, you'll write your first Java function to implement
     * the string multiplication behavior we get with * in Python.
     * We are providing the function stub and documentation to get
     * you started, which you are encouraged to use as reference for
     * the methods you write in Parts B/C (though note that Parts B-C.2.
     * will be written in a stateful class without an executable main method,
     * which is why you'll use "this." in those class methods, but not here).
     * 
     * The equivalent of a Python docstring in Java is called a javadoc 
     * comment. These use multiline comments in the format below (_above_
     * the function, not within). Javadoc comments clearly indicate parameters 
     * and any return value with @params and @return; because each method
     * includes types in its signature, these annotations do not need to
     * re-specify the types, which is different than Python docstrings.
     * 
     * The provided function/Javadoc template is commented out with //
     * so a compiler error isn't thrown due to placeholders:
     */
     
    /**
     * Function description
     * 
     * @param name - description of name parameter
     * @param name - description of name parameter
     * ...
     * @return - description of return value
     */
     // IMPORTANT: Functions (outside of classes) are defined with static.
     //            Methods (those you write in Parts B-C.2) should omit static.
     // public static <returnType> fnName(param1Type param1Name, param2Type, param2Name, ...) {
     //  
     // } 

    /**
     * Part A.3.c.
     * Generates a String result of s repeated n times.
     * Analogous to Python's str * int string-multiplication.
     * Requires n >= 0.
     *
     * @param s - String to multiply
     * @param n - Number of times to multiply s
     * @return - A generated String of n occurrences of s
     */
    public static String stringMultiplier(String s, int n) {
        String result = "";

        for (int i = 0; i < n; i++) {
            result += s;
        }

        return result;
    }
}
