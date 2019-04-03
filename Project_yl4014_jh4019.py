#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:41:17 2019

@author: yeli
"""
#1000~Champian-Fulton~Easy-to-Love.txt
import os
dir = '/Users/yeli/Documents/Columbia MS&E/Spring 2019/IEOR4501_Tools For Analytics/Project/Lyrics'
lyrics_dic = {}

for file in os.listdir(dir):
    path = dir + '/' + file
    lyrics = open(path,'r')
    lyrics_dic.update({file:lyrics.read()})
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

# score in absolute number is given based on the number of words/terms in a few categories mentioned
# words/terms deemed not kid safe are split into two levels
# if any level 2 word/terms are detected, the score will automatically be set to zero
def get_kid_safe(lyrics):
    lyrics_split = lyrics.split()
    level1_word = ['depress','depression','anxiety', 'sin','pain','suck','escort','shoot',
                   'shooting''freak','shot','pot','grave']
    level2_word = ['kill','violent','violence','blood','bloody','bomb','die','dead',
                  'suicide','shit','fuck','hell','ass','asshole','fucker','motherfucker',
                  'bitch','goddamn','damn','whore','pussy','nigga','bastard','douchebag',
                  'cock','slut','douche','crap','dick','fag','filthy','masturbate','cunt',
                  'masturbating','sex','fucked','horny',"fuckin'",'porn','pornstar','sugardaddy',
                  'sugarbaby','gun','alcoholic','alcohol','drug','weed','smoke','smoking',
                  'drugging','booty','porno'
                  ]
    count_listw1 = []
    count_listw2 = []
    for word in level1_word:
        count_listw1.append(lyrics_split.count(word))
    for word in level2_word:
        count_listw2.append(lyrics_split.count(word))
    
    level2_term = ['make love','making love',"makin' love"]
    count_listt2 = []
    for term in level2_term:
        count_listt2.append(lyrics.find(term))
    
    if sum(count_listw2) > 0 or sum(count_listt2) > 0:
        score = 0
    else: 
        score = sum(count_listw1)
    return score

# score in absolute number is given based on the number of love related words mentioned
# list of words include: love, loving, like, admire, adore
def get_love(lyrics):
    lyrics_split = lyrics.split()
    count_list = []
    love_word = ['love','loving','like','admire','adore', 'lover']
    for word in love_word:
        count_list.append(lyrics_split.count(word))
    return sum(count_list)

#char_dic = {}

!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def get_mood(lyrics):
    snt = analyser.polarity_scores(lyrics)
    print("{:-<40}{}".format(lyrics, str(snt)))

get_mood("""I'm watching TV a Saturday night """)



    

    
    


#file = open('/Users/yeli/Documents/Columbia MS&E/Spring 2019/IEOR4501_Tools For Analytics/Project/Lyrics/1000~Champian-Fulton~Easy-to-Love.txt', 'r')
#print(type(file.read()))
