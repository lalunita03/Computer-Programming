# Demo on "Your First Python Program" slide
# 1. Show the editor, terminal, and directory
# 2. Can create new file with File > Create New File

# Steps:
# 1. Write program
# 2. Save
# 3. Run in terminal

# python --version
# Expressions

1 + 1
2.2 * 3.4
1 + 2 * 3
(1 + 2) * 3

# Operator Precedence
1 + 2 * 3   # 7
1 + (2 * 3) # 7
(1 + 2) * 3 # 9

2 * 3 ** 4 # 162
(2 * 3) ** 4 # 1296

# Variables and Assignment
salary = 18.5
salary * 20 # 370
salary = 30
a = 10
b1 = 20
this_is_a_name = 30
# &*%$2foo? = 40

x = 15 # x = 15
y = x * 5 # ...
y 
z = x + y 
z 
z = z + 10 
z

print('Hello world!')
print('Hello Lorem!')
age = int(input('Age: '))
print('Your age is: ' + str(age))

# U.S. dollars per hour
salary = 18.5
# Salary for 20 hours/week
weekly_salary = salary * 20
print(weekly_salary)

# Strings and Formatting
print('{} is the instructor for {}!'.format('El', 'CS1'))
salary = 30
weekly_salary = 18.5 * 20
print('If your hourly salary is ${}, you earn ${}'\
      'for working 20 hours a week.'.format(salary, weekly_salary))

print('an integer: {:d}'.format(42))
print('a float: {:f}'.format(42.156700))
print('a float: {:.2f}'.format(42.156700))
