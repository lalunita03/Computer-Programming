"""
Student name: Lea Grohmann
Date: 10/02/2022

HW1
"""
# Exercise A: Course Policies
# A.1: not allowed

# A.2: not allowed

# A.3: allowed

# A.4: not allowed

# A.5: allowed (except for MP's)

# A.6: not allowed

# A.7: allowed (as long as they don't write the code for you)

# A.8: allowed (except for MP's)

# A.9: not allowed

# Exercise B.1: Expressions
# B.1.1: 8 - 5 --> 3

# B.1.2: 6 * 2.5 --> 15.0

# B.1.3: 51 / 2 --> 25.5

# B.1.4: 51 / -2 --> -25.5

# B.1.5: 51 % 2 --> 1

# B.1.6: 51 % -2 --> -1

# B.1.7: -51 % 2 --> 1

# B.1.8: 51 / -2.0 --> -25.5

# B.1.9: 1 + 4 * 5 --> 21

# B.1.10: (1 + 4) * 5 --> 25

# Exercise B.2: Shortcut Expressions
# B.2.1: x = 120 --> x = 120

# B.2.2: x = x + 10 --> x = 130

# B.2.3: x += 20 --> x = 150

# B.2.4: x = x - 30 --> x = 120

# B.2.5: x -= 70 --> x = 50

# B.2.6: x *= 3 --> x = 150

# B.2.7: x /= 5 --> x = 30.0

# B.2.8: x %= 5 --> x = 0.0

# Exercise B.3: Evaluation Walkthrough
# B.3: 
# rewrite:
# x += x - x --> x = x + x - x
# RHS Evaluation:
# 1. Look up the variable x to get its value: x --> 3
# 2. replace all instances of x on RHS with its value 3
#   x = x + (x - x)
#   x = 3 + (3 - 3)
# 2. Evaluate substraction (-) on (3 - 3) first (order of operations) --> 0
# then x = 3 + (0)
# 3. Evaluate substraction (-) on 3 - 0 --> 3
# LHS Update:
# Re-assign x to 3
# after the statement has been evaluated x = 3

# Exercise B.4: Complex Numbers
# B.4.1: 1j + 2.4j --> 3.4j

# B.4.2: 4j * 4j --> (-16+0j)

# B.4.3: (1+2j) / (3+4j) --> (0.44+0.08j)

# B.4.4: (1+2j) * (1+2j) --> (-3+4j)

# B.4.5: 1+2j * 1+2j --> (1+4j)

# B.4.6: because of the order of operation () have precedence over * and * has precedence of +. This tells us that python handles complex numbers like two seperate numbers (one imaginary number and one real number) when written without parantheses and only handles the complex number as one number when it's with parantheses.

# Excercise B.5: Functions on complex numbers
# B.5.1: cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)

# B.5.2: cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)

# B.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)

# B.5.4: the first option is better because the functions in math and cmath have similar names which can lead to confusion or an error

# Exercise B.6: String expressions
# B.6.1: "foo" + 'bar' --> 'foobar'

# B.6.2: "foo" 'bar' --> 'foobar'

# B.6.3: a = 'foo' \n b = "bar" \ a + b --> 'foobar'

# B.6.4: a = 'foo' \n b = "bar" \ a b --> SyntaxError

# B.6.5: month = "October" \n days = 31 \n days + " days hath " + month --> TypeError

# Excercise B.7: Fun with quotes
# B.7: 'A\nB\nC'

# Excercise B.8: String generation
# B.8: '-' * 70

# Excercise B.9: A string puzzle
# B.9: 'Line 1\nLine 2\nLine 3'

# Excercise B.10: String formatting
x = 9
y = 4.25

# B.10.1:
print('Lorem is {}.'.format(x))

# B.10.2:
print('Lorem is {} months old.'.format(x))

# B.10.3:
print('A puppuccino is ${}.'.format(y))

# B.10.4:
print('{} * {}'.format(y, x))

# B.10.5:
print('{} * {} is {}.'.format(y, x, x * y))

# Excercise B.11: Terminal input
# B.11:
num = float(input("Enter a number: "))
print(num)

# Excercise B.12: Quadratic expressions
# B.12:
def quadratic(a, b, c, x):
    """Computes the value of the quardratic expression a x^2 + b x + c
    
    Arguments:
        a: number
        b: number
        c: number
        x: number
    
    Returns:
        value of the quadratic expression a x^2 + b x + c"""
    return a * x * x + b * x + c

# Excercise B.13: DNA
# B.13:
def GC_content(dna):
    """"Computes the portion of the DNA bases which are either G or C (case insensitive)
    
    Arguments:
        'dna' (string): string that represents a DNA sequence
    
    Returns:
        (float): portion of bases that are either G or C
        """
    dna = dna.upper()
    gc = dna.count('G') + dna.count('C')
    return gc / len(dna)