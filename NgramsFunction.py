
def calculateNGrams(text, n):
    """ calculates the ngrams of a text of n items, and returns the most
    frequent n-gram in a complexity of O(n+n)"""
    nGrams=[]
    for i in range(len(text)-(n-1)):
        nGrams.append(text[i:i+n])
    mostFrequent = mostFrequencyItem(nGrams)
    return mostFrequent


def mostFrequencyItem(itemList):
    """receives a list of items and returns the most frequent item in a
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
    
