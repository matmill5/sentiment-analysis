import os
#from aiModel import sentimentLSTM
from textBlob import textBlobGo
from vader import vaderGo
#from aiModel import sentimentLSTM

path = '/home/capstone/sites/SentimentAnalysis/user/userUploads'

def processUploads():
    for filename in os.listdir('user/userUploads'):
        if(filename[0:3] == "up_"):
            #and sentimentLSTM("user/userUploads/" + filename)
            if(vaderGo("user/userUploads/" + filename) and textBlobGo("user/userUploads/" + filename)):
                os.rename("user/userUploads/" + filename, "user/userUploads/" + filename.replace("up_", "p_"))
                return "Success"
            else:
                return "Failure"


    return "Success"