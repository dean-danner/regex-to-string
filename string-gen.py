"""
All '+' or '*' options must have a '()' to choose from.
The goal is to accept and generate regular expressions and strings like we saw in class.
Example input: ab(aa+bb)*b(a+b)ab(a)*
"""

import random


def parseRegex(regex):
    strings = []

    for x in range(5):  # Change this range to generate more or less strings.
        stack = []
        cur = ""
        write = True  # Assures that non-option chars are not automatically written.
        for i in range(len(regex)):  # Runs through the input regex.
            if regex[i] == '(':
                stack.append(i)  # Appends the position of the beginning of the options to a stack.
                write = False
            elif regex[i] == ')':
                start = stack.pop()
                opt = regex[start + 1: i].split('+')  # Exports the options contained within the '()'.
                choice = random.choice(opt)  # Chooses a random option.
                if i < len(regex)-1 and regex[i+1] == '*':
                    for j in range(random.randint(0, 10)):  # Determines how many times a '*' will run.
                        choice = random.choice(opt)
                        cur += choice
                else:
                    cur += choice
                write = True
            elif write and regex[i] != '*':  # Writes non-option chars to the string.
                cur += regex[i]
        strings.append(cur)

    return strings


def main():  # Takes input and runs the calculation on it.
    regex = input("Enter a valid regular expression: ")
    print("Generated strings:")
    [print(i) for i in parseRegex(regex)]


main()
