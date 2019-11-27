import json
import pprint

with open("userResults/vaderSentiment.json", "r") as read_file:
    data = json.load(read_file)

outputDict = { "word": 0}

for item in data["text"].values():
    words = item.split()
    for word in words:
        if word in outputDict:
            outputDict[word] = outputDict[word] + 1
        else:
            outputDict[word] = 1

#print(json.dumps(outputDict, sort_keys=True, indent=4))
f = open("d3Results/testD3Result.json", "w")
f.write(json.dumps(outputDict, sort_keys=True, indent=4))
f.close()
#pprint.pprint(outputDict)