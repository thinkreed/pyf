#!/usr/bin/env python
# Simple debugger
# See instructions around line 34
import sys
import readline


# Our buggy program
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out


# main program that runs the buggy program
def main():
    print(remove_html_markup('xyz'))

    print(remove_html_markup('"<b>foo</b>"'))

    print(remove_html_markup("'<b>foo</b>'"))


# globals
breakpoints = {9: True}
stepping = False

""" *** INSTRUCTIONS ***
Improve and expand this function to accept 
a print command 'p <arg>'.
If the print command has no argument,
print out the dictionary that holds all variables.
Print the value of the supplied variable
in a form 'var = repr(value)', if
the 'p' is followed by an argument,
or print 'No such variable:', arg
if no such variable exists.
"""


def debug(command, my_locals):
    global stepping
    global breakpoints

    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'):  # step
        stepping = True
        return True
    elif command.startswith('c'):  # continue
        stepping = False
        return True
    elif command.startswith('p'):  # print
        if not arg:
            print(my_locals)
            return True

        if arg in my_locals:
            print('%s = %s' % (arg, repr(my_locals[arg])))
        else:
            print('No such variable: %s' % arg)

    elif command.startswith('q'):  # quit
        sys.exit(0)
    else:
        print("No such command", repr(command))

    return False


commands = ["p", "s", "p tag", "p foo", "q"]


def input_command():
    # command = raw_input("(my-spyder) ")
    global commands
    command = commands.pop(0)
    return command


def traceit(frame, event, trace_arg):
    global stepping

    if event == 'line':
        if stepping or frame.f_lineno in breakpoints:
            resume = False
            while not resume:
                print(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
                command = input_command()
                resume = debug(command, frame.f_locals)
    return traceit


# Using the tracer
sys.settrace(traceit)
main()
sys.settrace(None)
print(debug('p out', {'quote': True, 's': '"foo"', 'tag': False, 'c': 'b', 'out': '<'}))
