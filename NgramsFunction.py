
def calculateNGrams(text, n):
    """ calculates the ngrams of a text of n items """
    ngrams=[]
    for i in range(len(text)-(n-1)):
        ngrams.append(text[i:i+n])
    return ngrams

