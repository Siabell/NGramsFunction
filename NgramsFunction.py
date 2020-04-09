
def calculateNGrams(text, n):
    """ calculates the n-grams of a text of "n" items, and returns a list
    of the n-grams, in a complexity of O(n)"""
    nGrams=[]
    if (len(text)<n or n<1 ):
        raise Exception('The "n" value is not compatible for the n-grams')
    elif (len(text)==0):
        raise Exception('The "text" value is not compatible for the n-grams')
    for i in range(len(text)-(n-1)):
        nGrams.append(text[i:i+n])
    return nGrams

def mostFrequentNGram(text, n):
    """ calculates the n-grams of a text of "n" items, and returns the most
    frequent n-gram, in a complexity of O(n+n)"""
    nGrams = calculateNGrams(text,n)
    mostFrequent = mostFrequencyItem(nGrams)
    return mostFrequent


def mostFrequencyItem(itemList):
    """receives a list of items and returns the most frequent item, in a
    complexity of O(n) """
    nGramsDict={}
    mostFrequentValue = 0
    mostFrequentItem = ''
    for item in itemList:
        if (nGramsDict.get(item)):
            nGramsDict[item]+=1
        else:
            nGramsDict[item]=1
        actualValue = nGramsDict.get(item)
        if (actualValue > mostFrequentValue):
            mostFrequentValue = actualValue
            mostFrequentItem = item 
    return  mostFrequentItem
    
