import re
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
def train(data):
    #Text Preprocessing
    df=pd.concat([pd.DataFrame([' '.join([i for i in word_tokenize(re.sub(r'[^a-zA-Z]+',' ',utter).lower()) if i not in stopwords.words('english')]) for utter in data['utterances']],columns=['utterances']),data['intents']],axis=1)
    df=df.drop_duplicates()
    df=df.dropna()
    df=pd.concat([df,pd.get_dummies(df['intents'])],axis=1)
    target_cols=len(df.columns[2:])
    col_labels=df.columns[2:]                             
    dataset_length=len(df)
    #Convert Text into Matrix
    vectorizer=TfidfVectorizer()
    tfidf=vectorizer.fit_transform(df.values[:,0])
    tfidf_cols=tfidf.shape[1]
    neurons=round((tfidf_cols+target_cols)/2)
    #Build a Deeplearning model using ANN
    classifier = Sequential()
    classifier.add(Dense(units = neurons, activation = 'relu', kernel_initializer = 'uniform', input_dim = tfidf_cols))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(units = neurons, activation = 'relu', kernel_initializer = 'uniform'))
    classifier.add(Dropout(rate = 0.1))
    classifier.add(Dense(units = target_cols, kernel_initializer = 'uniform', activation = 'softmax'))
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    #Train Model
    classifier.fit(tfidf, df.values[:,2:], batch_size = round(dataset_length/10), epochs = dataset_length)
    print('\nBot Trained Successfully!!\n')
    return classifier,vectorizer

def transform_utter(model,vectorizer,df,utter):
    #Intent
    pred=model.predict(vectorizer.transform([utter.lower()]))
    col_labels=pd.get_dummies(df['intents']).columns
    #Entity
    tagged_list=pos_tag([i for i in word_tokenize(re.sub(r'^a-zA-Z',' ',utter).lower()) if i not in stopwords.words('english')])
    entities=[word for word,pos in tagged_list if pos in ['NN','NNP','NNS','NNPS','JJ','JJR','JJS','VB','VBN','VBG','VBD','VBP']]
    #Sentiment
    sid = SentimentIntensityAnalyzer()
    scores=sid.polarity_scores(utter)
    #Output Dictionary
    Int_Ent_Sent={'Intent':col_labels[pred.argmax()],'Entity':entities,'Sentiment':scores['compound']*100,'Confidence':pred.max()*100}
    return Int_Ent_Sent
    

