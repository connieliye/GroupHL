#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:41:17 2019

@author: yeli
"""

def lyrics_analysis(path):
    import os
    import numpy as np
    from profanity_check import predict_prob
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    from lexicalrichness import LexicalRichness
    
    dir = path
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
        lyrics_split_lower = [item.lower() for item in lyrics_split]
        count_list = []
        love_word = ['love','loving','loved','like','admire','adore', 'lover', 'dear', 
                 'darlin', 'darling', 'sweet','kiss','boy','girl','baby','lovely',
                 'sweetheart','hug','good','best','hot','pretty','loves']
        for word in love_word:
            count_list.append(lyrics_split_lower.count(word))
            return sum(count_list)
    
    #return absolute score, need to be normalized
    def get_length(lyrics):
        return len(lyrics.split())
    
    
    def get_mood(lyrics):
        analyzer = SentimentIntensityAnalyzer()
        snt = analyzer.polarity_scores(lyrics)
        return (snt['compound'] + 2) / 2
    
    #lexicalrichness
    #pip install lexicalrichness
    #pip install textblob
    
    def get_complexity(lyrics):
        score = LexicalRichness(lyrics)
        return 1-score.ttr
    
    
    love_list = []
    for val in lyrics_dic.values():
        love_list.append(get_love(val))
    max_love = max(love_list)
    
    length_list = []
    for val in lyrics_dic.values():
        length_list.append(get_length(val))
    max_length = max(length_list)
        
    import json 
    result = dict()
    result_list = []
    for key, val in lyrics_dic.items():
        temp_dict = dict()
        #get value by key
        temp_dict['id'] = get_id(key)
        temp_dict['artist'] = get_artist(key)
        temp_dict['title'] = get_title(key)
        temp_dict['kid_safe'] = np.asscalar(np.around(get_kid_safe(val),3))
        temp_dict['love'] = np.around((get_love(val)/max_love),3)
        temp_dict['length'] = np.around((get_length(val)/max_length),3)
        temp_dict['mood'] = np.around(get_mood(val),3)
        temp_dict['complexity'] = np.around(get_complexity(val),3)
        result_list.append(temp_dict)
        
    result['characterization'] = result_list
    #print(result_list)
        
    #convert to json file
    json_string = json.dumps(result_list)
    return json_string


if __name__ == '__main__':  

    import argparse

    parser = argparse.ArgumentParser('Analyze given lyrics in a path')
    parser.add_argument('path', help='a path that stores all the lyrics file')
    args = parser.parse_args()

    lyrics_analysis(args.path)

    
    
    
    