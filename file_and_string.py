#File reading and string manipulations

path = 'F://55.txt'

def readFile():
    filecontent = open(path,'rb')
    data_read = filecontent.read()
    print("==========File Information==========")
    print('File name: %s' %path[path.index('//')+2:])
    print('File size: %d'%len(data_read))
    #print('
    
