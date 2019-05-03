#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:41:17 2019

@author: yeli
"""

import os
from profanity_check import predict_prob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lexicalrichness import LexicalRichness

dir = '/Users/yeli/Documents/Columbia MS&E/Spring 2019/IEOR4501_Tools For Analytics/Project/Lyrics'
lyrics_dic = {}

for file in os.listdir(dir):
    path = dir + '/' + file
    lyrics = open(path,'r')
    lyrics_dic.update({file : lyrics.read()})
    lyrics.close()

def get_id(file):
    return file[0:file.find('~')]

def get_artist(file):
    end = file.find('~', file.find('~') + 1)
    artist = file[file.find('~') + 1 : end]
    return artist.replace('-' , ' ')

def get_title(file):
    start = file.find('~', file.find('~') + 1) + 1
    end = file.find('.')
    title = file[start : end]
    return title.replace('-' , ' ')

# utilize profanity_check package to get a score for each song
def get_kid_safe(lyrics):
    return 1 - predict_prob([lyrics])[0]


# return absolute score, need to be normalized
def get_love(lyrics):
    lyrics_split = lyrics.split()
    count_list = []
    love_word = ['love','loving','loved','like','admire','adore', 'lover', 'dear', 
                 'darlin', 'darling', 'sweet','kiss','boy','girl','baby','lovely',
                 'sweetheart','hug','good','best','hot','pretty','loves']
    for word in love_word:
        count_list.append(lyrics_split.count(word))
    return sum(count_list)

#return absolute score, need to be normalized
def get_length(lyrics):
    return len(lyrics.split())


def get_mood(lyrics):
    analyzer = SentimentIntensityAnalyzer()
    snt = analyzer.polarity_scores(lyrics)
    return snt['compound']

#lexicalrichness
#pip install lexicalrichness
#pip install textblob

def get_complexity(lyrics):
    score = LexicalRichness(lyrics)
    return 1-score.ttr


kid_safe_dic = {}
for key, val in lyrics_dic.items():
    kid_safe_dic.update({key: np.around(get_kid_safe(val),3)})
  

love_list = []
for val in lyrics_dic.values():
    love_list.append(get_love(val))
max_love = max(love_list)
love_dic = {}
for key, val in lyrics_dic.items():
    love_dic.update({key: np.around((get_love(val)/max_love),3)})
        
length_list = []
for val in lyrics_dic.values():
    length_list.append(get_length(val))
max_length = max(length_list)
length_dic = {}
for key, val in lyrics_dic.items():
    length_dic.update({key: np.around((get_length(val)/max_length),3)})

mood_dic = {}
for key, val in lyrics_dic.items():
    mood_dic.update({key: np.around(get_mood(val),3)}) 
    
complexity_dic = {}
for key, val in lyrics_dic.items():
    complexity_dic.update({key: np.around(get_complexity(val),3)}) 
id_dic ={}
for key, val in lyrics_dic.items():
    id_dic.update({key:get_id(key)})

artist_dic ={}
for key, val in lyrics_dic.items():
    artist_dic.update({key:get_artist(key)})

title_dic ={}
for key, val in lyrics_dic.items():
    title_dic.update({key:get_title(key)})
print(title_dic)
    
    
    
