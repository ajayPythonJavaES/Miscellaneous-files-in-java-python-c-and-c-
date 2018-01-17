mylist = [1,23,2]

def listUtil():
    usr_choice = int(input("Please enter your choice:\n1.Enter the elements dynamically\n2.Specify your list\n:"))
    if(usr_choice == 1):
        print(getElementsFromTheUser())
    elif(usr_choice == 2):
        print(getListFromTheUser())
    else:
        print("Please enter a valid choice")
    

def getElementsFromTheUser():
    len_of_list = int(input("Please enter the length of the list:"))
    for i in range(0,len_of_list):
        element = input("Please enter element ")
        mylist.append(int(element))
    return mylist


def getListFromTheUser():
    templist = list(input("Please enter your list"))
    for i in templist:
        mylist.append(int(i))
    return mylist


"""def removeDups():
    list_def = [1,2,3,1,3,4,3]
    temp_list = list_def
    print(list_def)
    element_to_remove = int(input("Please enter the element to be removed"))
    for i in range(0, len(list_def) - 2):
        #print(i)
        if(element_to_remove == temp_list[i]):
            temp_list.remove(element_to_remove)
    print(temp_list)
    print(list_def) """


#Using linear search
def addElementToHashSet(element):
    if(len(mylist) == 0):
        mylist.append(element)
    else:
        count = 0
        for i in mylist:
            if(i == element):
                count += 1
        if(count == 0):
            mylist.append(element)
    print(mylist)


def factorial(fact):
    for i in range(1,fact ):
        fact *= i
    print(fact)
        
    
#Using binary search
def __addElementToHashSet(element):
    if(len(mylist) == 0):
        mylist.append(element)
    else:
        boolVal = binarysearch(element)
        if(boolVal == False):
            mylist.append(element)
        print(mylist)
    
    
def binarysearch(element):
    a = mylist
    a.sort()
    low = 0
    high = len(mylist) - 1
    mid = (low + high)//2
    count = 0
    while(True):
        if(element == a[low] or element == a[mid] or element == a[high]):
            count += 1
            break
        elif(a[low] < element and a[mid] > element):
            high = mid
            mid = (low + mid)//2            
        elif(a[mid] < element and a[high] > element):
            low = mid
            mid = (mid + high)//2
        if(element != a[low] or element != a[mid] or element != a[high]):
            count = -1
            break
    if(count > 0):
        print("True")
        retVal = True
    elif(count == -1):
        print("False")
        retVal = False
    return retVal
