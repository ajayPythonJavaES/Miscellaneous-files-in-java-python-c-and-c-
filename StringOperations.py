import re

str = "aabaabaaaabaaabaabaa bbabab abababababaaabaabaaba"
list_of_ab = re.split(r'\a*',str)
print(list_of_ab)


def pattern():
    patstr = "(((()))"
