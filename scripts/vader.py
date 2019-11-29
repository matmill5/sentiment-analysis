#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk 
from nltk.tokenize import word_tokenize
import emoji
from emoji.unicode_codes import UNICODE_EMOJI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def vaderGo(file):
    #loading the data into the dataframe
    data=pd.read_csv(file, encoding='utf-8')
    data['text']=data.astype(str).apply(' '.join, axis=1)
    data=pd.DataFrame(data['text'])
    

    #Removing the duplicate rows from text column and resetting index
    data=data.drop_duplicates(['text'],keep='first')
    data=data.reset_index(drop=True)
    data['Original Text']=data['text']


    #converting emoji into the text
    import emoji
    for i in range(len(data)):
        data.loc[i,'text'] = emoji.demojize(data.loc[i,'text'])



    #converting special character "’" to "'" for contraction
    for i in range(len(data)):
        data.loc[i,'text']=data.loc[i,'text'].replace("’","'")

    
    
    # sys.path.insert(0, 'path for contractions.py')

    from contractions_1 import CONTRACTION_MAP
    def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                          flags=re.IGNORECASE|re.DOTALL)
        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match)\
                                    if contraction_mapping.get(match)\
                                    else contraction_mapping.get(match.lower())                       
            expanded_contraction = first_char+expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, text)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text

    for i in range(len(data)):
        data.loc[i,'text'] = expand_contractions(str(data.loc[i,'text']))


    #data cleaning steps
    for i in range(len(data)):
        # Remove the word starting with @
        data.loc[i,'text'] = re.sub(r'@[A-Za-z0-9]+', ' ', str(data.loc[i,'text']))

        #Remove URL links
        data.loc[i,'text']  = re.sub('https?://[A-Za-z0-9./]+',' ',data.loc[i,'text'] ) 
        data.loc[i,'text']  = re.sub('http?://[A-Za-z0-9./]+',' ',data.loc[i,'text'] )


        # Converting to Lowercase
        data.loc[i,'text']  = data.loc[i,'text'] .lower()

        #Remove the new line characters
        data.loc[i,'text'] = re.sub(r"\t|\n|\r", " ", data.loc[i,'text'] , flags=re.I)

        #Remove punctuation
        data.loc[i,'text'] = re.sub(r"[,‘@\#-:'?\.$%_!()&;+”/…*•|“]", " ", data.loc[i,'text'] , flags=re.I)

        #Remove duble quotes
        data.loc[i,'text'] = re.sub(r'"', " ", data.loc[i,'text'] , flags=re.I)

        #Remove digits
        data.loc[i,'text'] = re.sub(r"\d", "", data.loc[i,'text'] )

        # remove all single characters
        data.loc[i,'text'] = re.sub(r'\s+[a-zA-Z]\s+', ' ', data.loc[i,'text'] )

        # Substituting multiple spaces with single space
        data.loc[i,'text']  = re.sub(r'\s+', ' ', data.loc[i,'text'] , flags=re.I)


    for i in range(len(data)):
        # removing rt from the data
        data.loc[i, 'text']=' '.join([x for x in data.loc[i,'text'].split() if x !='rt' and x !='nan'])  

         # remove all single characters
        data.loc[i,'text'] = re.sub(r'\s+[a-zA-Z]\s+', ' ', data.loc[i,'text'] )

        # Substituting multiple spaces with single space
        data.loc[i,'text']  = re.sub(r'\s+', ' ', data.loc[i,'text'] , flags=re.I)



    # remove remaining tokens that are not alphabetic
    for i in range(len(data)):
        data.loc[i, 'text']=' '.join([x for x in data.loc[i,'text'].split() if x.isalpha()])
    


    # remove stopwords
    stop_words = stopwords.words('english')
    stop_words.remove('no')
    stop_words.remove('not')
    for i in range(len(data)):
        data.loc[i,'text'] = ' '.join([word for word in data.loc[i,'text'].split() if not word in stop_words])


    # Lemmetization of words (it will change the word in the base form)
    lemmatizer = WordNetLemmatizer()
    for i in range(len(data)):
        data.loc[i,'text'] = ' '.join([lemmatizer.lemmatize(word,pos='a') for word in data.loc[i,'text'].split()])
        data.loc[i,'text'] = ' '.join([lemmatizer.lemmatize(word,pos='v') for word in data.loc[i,'text'].split()])
        data.loc[i,'text'] = ' '.join([lemmatizer.lemmatize(word,pos='n') for word in data.loc[i,'text'].split()])

   

    for i in range(len(data)):
        # remove all single characters
        data.loc[i,'text'] = re.sub(r'\s+[a-zA-Z]\s+', ' ', data.loc[i,'text'] )

        # Substituting multiple spaces with single space
        data.loc[i,'text']  = re.sub(r'\s+', ' ', data.loc[i,'text'] , flags=re.I)

    # Using VADER (Python Library) to find the sentiments of data
    for x in range(len(data)):
        data_sentiment = SentimentIntensityAnalyzer()
        data.loc[x,'Sentiment']=data_sentiment.polarity_scores(data.loc[x,'text'])['compound']


        
    data['Sentiment_rolled']= data['Sentiment'].apply(lambda x:  1 if x > 0.05 else (0 if (x <=0.05 and x>=-0.05)  else -1))
    data['Polarity'] = data['Sentiment_rolled'].apply(lambda x:  'Positive' if x ==1  else ('Neutral' if x == 0  else 'Negative'))
    
    # saving dataframe into json format
    data.to_csv('userResults/vaderSentiment.csv', index=False)

    df = pd.DataFrame(data, columns= ["Sentiment_rolled", "Polarity"])


    # saving dataframe into json format
    df.to_json(r'userResults/vaderSentiment.json')
    # data.to_json(r'userResults/vaderSentiment_table.json', orient='table')
    # data.to_json(r'userResults/vaderSentiment_split.json', orient='split')

    
    return "Success"





    