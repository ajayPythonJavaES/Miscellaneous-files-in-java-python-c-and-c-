import os

class OSUtil:
    def __init__(self):
        print "***Welcome to the OS Util API"

    def dirname(self):
        directory = os.getcwd()
        print directory


osObj = OSUtil()
osObj.dirname()
