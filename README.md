# **Project：Analyze lyrics of 1000 songs using Python**

Group Section: 7
Group Members: 
- Connie Ye Li(yl4014)
- Jiannuo Hu (jh4019)

## **Intro** 

The objective of this project is to test music lyrics of 1000 songs that are stored in a folder called "Lyrics". 
The team analyzed all lyrics and assigned scores to those lyrics based on 5 metrics: 

- kid_safe: If the song is safe for kids to listen to? 0: not kid safe; 1: very kid safe

- love: Whether the song is related to love or not? 0: not a love song; 1: a love song

- mood: Whether the song is in positive mood or sad mood? 0: a dark song; 1: a happy song 

- length: This metric indicates how long the song's lyrics is compared with other songs. 0: very short; 1: very long 

- complexity: What's the lexical richness of this song? 0: very simple song; 1: very complex song 

## Data Processing

First thing first, import all packages required for this text analysis as followings:

```
import os
from profanity_check import predict_prob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from lexicalrichness import LexicalRichness
import numpy as np 

```

###### Loading the data
All lyrics data was given and downloaded from coursework in a folder called "lyrics". The folder contains
1000 songs and each file's title is in the format of 

> id-singer name-song title.txt.

To load the data from the folder, use 

```
for file in os.listdir(dir):
    path = dir + '/' + file
    lyrics = open(path,'r')
    lyrics_dic.update({file : lyrics.read()})
    lyrics.close()
    
```
    
To extract each song's information, use three functions we created
1. `get_id`: to extract id from the file's title
2. `get_artist`: to extract singer's name 
3. `get_title`: to extract song's title

###### Defining dimensions

In order to get those 5 dimensions to measure those lyrics, we created 5 functions, which are:

1. `get_kid_safe`: we utilized 'profanity_check' package to get a score for each song.
2. `get_love`: we compile a list of `love` key words (e.g. 'love','loving','loved','like','admire','adore') and count how many                  love key words that the song has.
3. `get_length`: we use `len(lyrics.split())` to count the word number of the song.
4. `get_mood`: we use `vaderSentiment.vaderSentiment` package to check the mood of the song.
5: `get_complexity`: we use `lexicalrichness` package to check the vocabulary level of the song. 

###### Assign Scores

Since socore for all metrics ranging from 0 to 1. We need to normalize scores we return at the end after using those functions. 

- For kid_safe, profanity_check automatically returns scores in [0,1]. 
- For love, we find the maximum number of "love" key word and use the number of "love" key words of each song / max(love key word) to normalize the score. 
- For length, we find the longest song and return `max_length` which is the word number of the longest song. Then we use word number of each song / max(length) to normal the socore of length metric.
- For mood & complexity, python packages automatically return scores in [0,1].

In the last step, we combine all results in a list named `result_list` and convert it into json file.

## Contact us
If you have any questions, please reach out to us by the following contact information: 

Connie Ye Li: yl4014@columbia.edu
Jiannuo Hu: jh4019@columbia.edu 








