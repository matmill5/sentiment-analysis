from wordCloud import getWordResults
from bubbleCloud import getBubbleResults
from piechart import getPiResults

def createD3Results(file):
    getWordResults(file)
    getBubbleResults(file)
    getPiResults(file)

    return "success"