# Task 5
# Word Count: Create a program that takes a 
# sentence as input from the user and counts 
# the number of words in it.

import os
from functions import *
os.system('clear && neofetch')

text = getText()
wordCount = getWordCount(text)
print('Word Count: ', wordCount)