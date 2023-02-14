print("Welcome to my Quiz Show")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok!  Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct! ')
else:
    print('Incorrect!')

answer = input(
    "What is the result of the following Python expression: 3 + 4 * 2? ")
if answer == "11":
    print('Correct! ')
else:
    print('Incorrect!')

answer = input(
    "What is the name of the built-in function in Python that returns the absolute value of a number? ")
if answer == "abs()":
    print('Correct! ')
else:
    print('Incorrect!')

answer = input("What is symbol used for floor division in Python? ")
if answer == "//":
    print('Correct! ')
else:
    print('Incorrect!')

answer = input(
    "What is the keyword in Python that is used to define a function? ")
if answer == "def":
    print('Correct! ')
else:
    print('Incorrect!')
