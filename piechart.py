import json

with open("userResults/vaderSentiment.json", "r") as read_file:
    data = json.load(read_file)

print(data["Polarity"])

posCount = 0
negCount = 0
neuCount = 0

for item in data["Polarity"].values():
    if item == "Positive":
        posCount = posCount + 1
    if item == "Negative":
        negCount = negCount + 1
    if item == "Neutral":
        neuCount = neuCount + 1

print(posCount)
print(negCount)
print(neuCount)

# Return this list of results
#resultList = [posCount, negCount, neuCount]