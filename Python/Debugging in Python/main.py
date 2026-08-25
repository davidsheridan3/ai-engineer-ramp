# debugging

# linting
# num + 4 # ides like pycharm already have linting built in (underlines)

# use an ide/editor always
# they have all these built in tools for us to use, allowing us to detect errors before running code

# learn to read errors
# 4 + 'shdhsjja'
# e.g. Traceback (most recent call last):
#   File "/Users/david.sheridan/PycharmProjects/ai-engineer-ramp/Python/Debugging in Python/main.py", line 4, in <module>
#     num + 4 # ides like pycharm already have linting built in (underlines)
# NameError: name 'num' is not defined

# pdb (python debugger package)
import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 'hhkhads')

# use 'help' to explore it's capabilities in console, e.g. step, continue, a, w


