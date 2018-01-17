print "Hello World"


def power_bill():
    print "Power Bill Generator"
    for i in range(0,5):
        units_consumed = int(input("Please enter the units consumed by user " + str(i+1) + ": "))
        if(units_consumed > 0 and units_consumed <= 50):
            print(0.5 * units_consumed)
        elif(units_consumed > 50 and units_consumed <= 100):
            print(0.75 * units_consumed)
        elif(units_consumed > 100 and units_consumed <= 150):
            print(1.25 * units_consumed)
        elif(units_consumed > 150 and units_consumed <= 200):
            print(2 * units_consumed)
        else:
            print(5 * units_consumed)
        

def totalUnitsOfAnArea():
    units_consumed = 0
    for i in range(0,5):
        add = int(input("Please enter the units consumed by user " + str(i+1) + ": "))
        units_consumed += add
    return units_consumed



"""

a = [1,2,3,"abc",'a',True,2.0,190.34]
>>> print a
[1, 2, 3, 'abc', 'a', True, 2.0, 190.34]
>>> a.index("abc")
3
>>> a.append("appended")
>>> print a
[1, 2, 3, 'abc', 'a', True, 2.0, 190.34, 'appended']
>>> a.insert(6,"value addedd at 6")
>>> print a
[1, 2, 3, 'abc', 'a', True, 'value addedd at 6', 2.0, 190.34, 'appended']
>>> a.insert(0,"sunil")
>>> print a
['sunil', 1, 2, 3, 'abc', 'a', True, 'value addedd at 6', 2.0, 190.34, 'appended']
>>> a2 = ['this','is','new','list']
>>> print a2
['this', 'is', 'new', 'list']
>>> print a + a2
['sunil', 1, 2, 3, 'abc', 'a', True, 'value addedd at 6', 2.0, 190.34, 'appended', 'this', 'is', 'new', 'list']
>>> a.extend(a2)
>>> print a
['sunil', 1, 2, 3, 'abc', 'a', True, 'value addedd at 6', 2.0, 190.34, 'appended', 'this', 'is', 'new', 'list']
>>> a.remove('a')
>>> print a
['sunil', 1, 2, 3, 'abc', True, 'value addedd at 6', 2.0, 190.34, 'appended', 'this', 'is', 'new', 'list']

"""
print "END OF FILE"

