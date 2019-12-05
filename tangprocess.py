#Importing necessary libraries
import json
import pprint
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

counters = {"Original Size" : 0 , "Drop Duplicate Size" : 0, "Contains Link" : 0,
"Mention Paris" : 0, "Mention Tokyo" : 0, "Mention China": 0, 
"Mention 2020": 0, "Mention 2022": 0, 
"Mention League of Legends" : 0, "Mention Paris Olympic Games" : 0, "Mention Asian Games" : 0 , 
"Hashtags" : 0, "Hashtag Types" : 0, "Trump Factor" : 0,  
"Vader Positive": 0, "Vader Negative": 0, "Vader Neutral": 0,
"TextBlob Positive": 0, "TextBlob Negative": 0, "TextBlob Neutral": 0,
"Conflict Positives" : 0, "Conflict Neutrals": 0 ,"Conflict Negatives": 0, "Conflict Precentage" : 0.00
}

results = {"Contains Link" : [],
"Mention Paris" : [], "Mention Tokyo" : [], "Mention China": [], 
"Mention 2020": [], "Mention 2022": [], 
"Mention League of Legends" : [], "Mention Paris Olympic Games" : [], "Mention Asian Games" : [] , 
"Has Hashtags" : [], "Hashtags": set(), "Trump Factor" : [],
"Vader Positive": [], "Vader Negative": [], "Vader Neutral": [],
"TextBlob Positive": [], "TextBlob Negative": [], "TextBlob Neutral": [],
"Conflict Positives" : [], "Conflict Neutrals": [] ,"Conflict Negatives": []
}

with open("tang/tweetsR.json", "r") as read_file:
    data = json.load(read_file)

df = pd.DataFrame(data)
counters['Original Size'] =  len(df.index)

df = df.drop_duplicates(['text'], keep='first')
df = df.reset_index(drop=True)
counters['Drop Duplicate Size'] = len(df.index)

data_sentiment = SentimentIntensityAnalyzer()

for ind in df.index:
    if('http' in df['text'][ind]):
        results['Contains Link'].append(df['_id'][ind])
    if('Paris' in df['text'][ind] or 'paris' in df['text'][ind]):
        results['Mention Paris'].append(df['_id'][ind])
    if('Tokyo' in df['text'][ind] or 'tokyo' in df['text'][ind]):
        results['Mention Tokyo'].append(df['_id'][ind])
    if('China' in df['text'][ind] or 'china' in df['text'][ind]):
        results['Mention China'].append(df['_id'][ind])
    if('2020' in df['text'][ind]):
        results['Mention 2020'].append(df['_id'][ind])
    if('2022' in df['text'][ind]):
        results['Mention 2022'].append(df['_id'][ind])
    if('League' in df['text'][ind] or 'League of Legends' in df['text'][ind] or 'LoL' in df['text'][ind]):
        results['Mention League of Legends'].append(df['_id'][ind])
    if('Paris Olympic Games' in df['text'][ind] or 'paris olympic games' in df['text'][ind] or 'Paris Games' in df['text'][ind] or 'paris games' in df['text'][ind]):
        results['Mention Paris Olympic Games'].append(df['_id'][ind])
    if('Asian Games' in df['text'][ind] or 'Asia Games' in df['text'][ind] or 'asian games' in df['text'][ind] or 'asia games' in df['text'][ind]):
        results['Mention Asian Games'].append(df['_id'][ind])
    if('#' in df['text'][ind]):
        results['Has Hashtags'].append(df['_id'][ind])
        for tag in df['text'][ind].split():
            if tag.startswith("#"):
                results['Hashtags'].add(tag)
    if('Trump' in df['text'][ind] or 'Donald Trump' in df['text'][ind] or 'trump' in df['text'][ind]):
        results['Trump Factor'].append(df['_id'][ind])
    #Vader Sentiment
    sentiment = data_sentiment.polarity_scores(df['text'][ind])['compound']
    if sentiment > 0.05:
        results['Vader Positive'].append(df['_id'][ind])
    if sentiment <= 0.05 and sentiment >= -0.05:
        results['Vader Neutral'].append(df['_id'][ind])
    if sentiment < -0.05:
        results['Vader Negative'].append(df['_id'][ind])
    #Text Blob Sentiment
    a_sentiment = TextBlob(df['text'][ind])
    sentiment = a_sentiment.sentiment.polarity
    if sentiment > 0.05:
        results['TextBlob Positive'].append(df['_id'][ind])
    if sentiment <= 0.05 and sentiment >= -0.05:
        results['TextBlob Neutral'].append(df['_id'][ind])
    if sentiment < -0.05:
        results['TextBlob Negative'].append(df['_id'][ind])

# Postive in vader, but not in textblob
for t in results['Vader Positive']:
    if t not in results['TextBlob Positive']:
        results["Conflict Positives"].append(t)

# Neutral in vader, but not in textblob
for t in results['Vader Neutral']:
    if t not in results['TextBlob Neutral']:
        results["Conflict Neutrals"].append(t)

# Negative in vader, but not in textblob
for t in results['Vader Negative']:
    if t not in results['TextBlob Negative']:
        results["Conflict Negatives"].append(t)

counters['Contains Link'] = len(results['Contains Link'])
counters['Mention Paris'] = len(results['Mention Paris'])
counters['Mention Tokyo'] = len(results['Mention Tokyo'])
counters['Mention China'] = len(results['Mention China'])
counters['Mention 2020'] = len(results['Mention 2020'])
counters['Mention 2022'] = len(results['Mention 2022'])
counters['Mention League of Legends'] = len(results['Mention League of Legends'])
counters['Mention Paris Olympic Games'] = len(results['Mention Paris Olympic Games'])
counters['Mention Asian Games'] = len(results['Mention Asian Games'])
counters['Has Hashtags'] = len(results['Has Hashtags'])
counters['Hashtags'] = len(results['Hashtags'])
counters['Trump Factor'] = len(results['Trump Factor'])
counters['Vader Positive'] = len(results['Vader Positive'])
counters['Vader Neutral'] = len(results['Vader Neutral'])
counters['Vader Negative'] = len(results['Vader Negative'])
counters['TextBlob Positive'] = len(results['TextBlob Positive'])
counters['TextBlob Neutral'] = len(results['TextBlob Neutral'])
counters['TextBlob Negative'] = len(results['TextBlob Negative'])
counters['Conflict Positives'] = len(results['Conflict Positives'])
counters['Conflict Neutrals'] = len(results['Conflict Neutrals'])
counters['Conflict Negatives'] = len(results['Conflict Negatives'])
counters['Conflict Precentage'] = (counters['Conflict Positives'] + counters['Conflict Negatives'] + counters['Conflict Neutrals']) / counters['Drop Duplicate Size']

#pprint.pprint(results)
pprint.pprint(counters)
