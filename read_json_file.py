def readJson():
    jsonFile = open("F:\\json.json","r")
    data = jsonFile.read()
    print("%s"%data)
