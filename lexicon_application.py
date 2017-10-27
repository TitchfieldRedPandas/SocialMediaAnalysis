# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:40:21 2017

@author: cmorris
"""
import pandas as pd

lexicon = pd.read_csv('C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\lexicon.csv',header=None, sep=',')

lexicon = lexicon.rename(columns = {0:'word'})
lexicon = lexicon.rename(columns = {1:'anger'})
lexicon = lexicon.rename(columns = {2:'anticipation'})
lexicon = lexicon.rename(columns = {3:'disgust'})
lexicon = lexicon.rename(columns = {4:'fear'})
lexicon = lexicon.rename(columns = {5:'joy'})
lexicon = lexicon.rename(columns = {6:'negative'})
lexicon = lexicon.rename(columns = {7:'positive'})
lexicon = lexicon.rename(columns = {8:'sadness'})
lexicon = lexicon.rename(columns = {9:'suprise'})
lexicon = lexicon.rename(columns = {10:'trust'})
lexicon = lexicon.drop(lexicon.index[0])

lexicon.positive = lexicon.positive.astype(int)
lexicon.negative = lexicon.negative.astype(int)


paragraph = ''

def get_Score(paragraph):
    paragraph=paragraph.lower()
    split_paragraph = paragraph.split()
    score = 0
    for word in split_paragraph:
        
        word_positivity=0
        if word in lexicon.word.values:
            row = lexicon.loc[lexicon.word == word].copy()
            word_positivity=row.positive.values[0]-row.negative.values[0]
        score=score + word_positivity
        #print(word, word_positivity)
        
    return score

print(get_Score(paragraph))
#print(split_paragraph)

#split_paragraph=pd.DataFrame(split_paragraph)

#split_paragraph=split_paragraph.rename(columns = {0:'word'})

#for split_paragraph['word'] is in lexicon[']


































#anger=0
#anticipation=0
#disgust=0
#fear=0
#joy=0
#negative=0
#positive=0
#sadness=0
#suprise=0
#trust=0


#for lexicon['0'] in split_paragraph:
    #anger = anger + lexicon[1]
    #anticipation = anticipation + lexicon[2]
    #disgust = disgust + lexicon[3]
    #fear = fear + lexicon[4]
    #joy = joy + lexicon[5]
    #negative = negative + lexicon[6]
    #positive = positive + lexicon[7]
    #sadness = sadness + lexicon[8]
    #suprise = suprise + lexicon[9]
    #trust = trust + lexicon[10]
#print(anger)
#print(anticipation)
#print(disgust)
#print(fear)
#print(joy)
#print(negative)
#print(positive)
#print(sadness)
#print(suprise)
#print(trust)



























#with open('C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\lexicon.csv', 'r') as f:
    #lex = csv.reader(f)

#lex=pd.DataFrame(list(lex))

#lexicon = row
    
#lexicon = open('C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\lexicon.csv', 'r')

#lex = csv.reader(f)

#lexicon = pd.DataFrame(list(lexicon))


#lexicon['anger'] = lexicon[].apply(lambda x : x[','])
#lexicon['anticipation'] = lexicon[]].apply(lambda x : x[','])
#lexicon['disgust'] = lexicon[].apply(lambda x : x[','])
#lexicon['fear'] = lexicon[].apply(lambda x : x[','])
#lexicon['joy'] = lexicon[].apply(lambda x : x[','])
#lexicon['negative'] = lexicon[].apply(lambda x : x[','])
#lexicon['positive'] = lexicon[].apply(lambda x : x[','])
#lexicon['sadness'] = lexicon[].apply(lambda x : x[','])
#lexicon['suprise'] = lexicon[].apply(lambda x : x[','])
#lexicon['trust'] = lexicon[].apply(lambda x : x[','])




#print(lexicon)