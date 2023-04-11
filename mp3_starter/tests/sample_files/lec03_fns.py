# Lecture 3
# Examples of custom functions; in lecture, El showed how to use the VSCode debugger
# to watch the flow of program execution when writing/calling functions. 
# We will continue to use functions in programs, and soon we won't have any
# variables outside of functions/main (best practice)

# At this line, no executable statements in this program has yet been run
# (Python runs the program top-down (unless jumping _into_ function calls))
# The Python interpreter "only knows" basic built-in things, like types,
# syntax and operators, and built-in functions like print(), int(), min(), etc.

# Let's say that the interpreter knows N built-in functions
name = 'Lorem'
other_name = 'Ipsum'

# Example 1: 1 parameter, print output
def say_hello(name):
  print('Hello ' + name + '!')

# On this line, we add our own function to the "environment"; the interpreter
# know nows N + 1 functions (it does not yet know f(x, y) though)
# say_hello(1)
say_hello('World')

# A Function Call "Underneath the Hood"
# 1. Evaluate other_name -> 'Ipsum'
# 2. the evaluation ('Ipsum') as the single argument to say_hello
# say_hello(other_name) -> say_hello('Ipsum')

# 3. The program jumps to say_hello's definition, with its parameter 
#    which happens to be called `name`` (irrelevant to the variable on Line 9) 
#    replaced by the value 'Ipsum' 
# Experiment with the VSCode debugger shown in class!
say_hello(other_name)

# f(1, 2) # error, f isn't defined yet

# Example 2: 2 parameters, return int
def f(x, y):
	return x + 2 * y

# On this line, we add a second function to the "environment"; the interpreter
# know nows N + 2 functions 

f(1, 2) # no error