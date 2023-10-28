def getLoginAndPasswordFromFile(filePath):
    dataDict = {}

    with open(filePath, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            dataDict[key] = value

    return dataDict