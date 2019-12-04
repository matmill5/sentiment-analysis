import json
import pprint

def getWordResults(filename):
    with open("user/userResults/{{ filename }}", "r") as read_file:
        data = json.load(read_file)

    outputDict = { "word": 0}

    for item in data["text"].values():
        words = item.split()
        for word in words:
            if word in outputDict:
                outputDict[word] = outputDict[word] + 1
            else:
                outputDict[word] = 1

    child = []
    node = {"word": "aName", "size" : 0}
    for item in outputDict:
        node["word"]=item
        node["size"]=outputDict[f'{item}']
        child.append(node.copy())
        #print(item)

    pprint.pprint(child)

    #print(json.dumps(outputDict, sort_keys=True, indent=4))
    f = open("user/userResults_d3/{{ file name }}", "w")
    f.write(json.dumps(child, sort_keys=True, indent=4))
    f.close()
    #pprint.pprint(outputDict)