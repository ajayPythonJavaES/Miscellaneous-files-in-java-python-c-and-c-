class MyException(Exception):

    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


def checkWithdraw(amount):
    try:
        if(amount <= 5000):
            raise MyException("ERROR: Amount cannot be withdrew")
        else:
            print("Amount got withdraw")
    except MyException as exc:
        print exc
    else:
        print "Bon Voyage"
        
