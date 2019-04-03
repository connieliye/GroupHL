#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:41:17 2019

@author: yeli
"""
#1000~Champian-Fulton~Easy-to-Love.txt
import os
from profanity_check import predict, predict_prob
from googletrans import Translator

dir = '/Users/yeli/Documents/Columbia MS&E/Spring 2019/IEOR4501_Tools For Analytics/Project/Lyrics'
lyrics_dic = {}

for file in os.listdir(dir):
    path = dir + '/' + file
    lyrics = open(path,'r')
    translated_lyrics = Translator().translate(lyrics.read()).text
    lyrics_dic.update({file : translated_lyrics})
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
    return 1 - predict_prob([lyrics])


# score in absolute number is given based on the number of love related words mentioned
# list of words include: love, loving, like, admire, adore
def get_love(lyrics):
    lyrics_split = lyrics.split()
    count_list = []
    love_word = ['love','loving','like','admire','adore', 'lover']
    for word in love_word:
        count_list.append(lyrics_split.count(word))
    return sum(count_list)

def get_length(lyrics):
    return 1

#char_dic = {}


    

    
    


#file = open('/Users/yeli/Documents/Columbia MS&E/Spring 2019/IEOR4501_Tools For Analytics/Project/Lyrics/1000~Champian-Fulton~Easy-to-Love.txt', 'r')
#print(type(file.read()))