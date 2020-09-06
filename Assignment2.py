# Assignment2 python code
# Ian Brinkerhoff
# CS 3620

# Part1: BMI Calculator
# Gather Weight(kg) and Height(m) from user
def bmi(h, w):
    try:
        b = (w / (h**2))
        return b
    except ZeroDivisionError:
        return 'Improper height entered'
# End Part1 Function


# Part2: Function to divide two numbers
# Gather two numbers from user
def twoNum(one, two):
    try:
        return one/two
    except ZeroDivisionError:
        return 'Cannot divide by zero!'
# End Part2 Function


# Part4: Prompt user for name of product
# return respective price related to product
def products(p):
    prods = {
        "soda": "$2.50",
        "candy": "$1.75",
        "popcorn": "$4.60",
        "ice cream": "$3.20",
        "burger": "$5.00"
    }
    if p in prods:
        return 'Price: {0}'.format(prods[p])
    else:
        return 'Error: Product does not exist!'
# End Part4 Function


# Main of program
# Part1:
print('Part1: Body Mass Index Calculator:')
h = float(input('Please enter height(m): '))
w = float(input('Please enter weight(kg): '))
print('BMI: {0}'.format(str(bmi(h, w))))
# End Part1

print()

# Part2:
print('Part2: Enter two numbers to divide:')
one = int(input('Enter number one: '))
two = int(input('Enter number two: '))
print('{0} / {1} = {2}'.format(str(one), str(two), str(twoNum(one, two))))
# End Part2

print()

# Part3: Open file named demo.txt
# Read content of file
# Write random data into it
print('Part3: Read, Write, Append')
# Write
file = open('demo.txt', 'w')
file.write('This is random data for part 3, Assignment 2. ')
file.close()

# Read
print('Before Append:')
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

# Append
file = open('demo.txt', 'a')
file.write('This is additional information being added to end of file.')
file.close()

# Read again to check that append worked
print('After Append:')
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()
# End Part3

print()

# Part4
print('Part4: Products and Prices (soda, candy, popcorn, ice cream, burger)')
p = input('Enter a product to see the price: ')
print(products(p))
# End Part4

print()

# Part5
print('Part5: Odd List, 1 to 100')
nums = [x for x in range(100) if x % 2 != 0]
print(list(nums))
# End Part5
