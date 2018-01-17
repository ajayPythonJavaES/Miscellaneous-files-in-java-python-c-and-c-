def exc():
    myList = [1,2,3,4]
    print myList[5] 


def withExc():
    #myList = [1,2,3,4]
    try:
        #print myList[5]
        amount = 4000000
        if(amount < 3000):
            print "Hello World"
    except(IndexError):
        print "Sorry, index out of range, last index is: ",(len(myList) - 1)
        #print myList[len(myList) - 1]
    else:
        print "Happy Holi, blue, green, yellow, pink"

