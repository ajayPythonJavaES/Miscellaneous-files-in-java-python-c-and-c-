class MyCustomException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

def withdraw(amount):
    try:
        if(amount < 3000):
            #raise MyCustomException("Amount cannot be withdraw")
            print "Hello World"
        """else:
            print "Amount withdrew successful" """
    except(Exception):
        #print exc
        print "In except block"
    else:
        print "Better luck next time"
