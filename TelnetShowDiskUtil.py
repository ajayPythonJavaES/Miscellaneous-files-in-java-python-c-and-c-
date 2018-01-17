tableToDictionary = {}

def constructDictionary():
    headersList = []
    with open('F:/Python/TestCaseProject/show disks.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    splitTheHeaders = content[1].split(' ')    
    [headersList.append(listElement) for listElement in splitTheHeaders]
    newList = []
    [newList.append(element) for element in headersList]
    newList = list(filter(None,newList))
    for lineNum in range(3,len(content)-4):
        splitFields = []
        [splitFields.append(element) for element in content[lineNum].split(' ')]
        splitFields = list(filter(None,splitFields))
        for key,value in newList,splitFields:
            #tableToDictionary.update({key:list.append(value)})
            valuesList = []
            if(tableToDictionary.get(key) is not None):
                valuesList = tableToDictionary.get(key)
                valuesList.append(value)
                temp = {key:valuesList}
            else:
                temp = {key:list(value)}
            tableToDictionary.update(temp)            
    print(tableToDictionary)







##        for key,value in zip(convertToSet,splitFields):
##            temp = {key:value}
##            tableToDictionary.update(temp)
##    print(tableToDictionary.values())
    
                
        
        
    
