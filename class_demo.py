class Parent:
    default_dict = {}
    
    def __init__(self):
        print("Constructor called")        
        printHelloWorld()

    def printHi(self):
        print("Hi")


def printHelloWorld():
    print("Hello World")


p = Parent()
p.printHi()
#p.__init__()
