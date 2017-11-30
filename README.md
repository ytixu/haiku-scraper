# haiku-scraper

### Dependencies:

##### langdetect: Language detection
https://pypi.python.org/pypi/langdetect?

##### PRAW: Reddit API wrapper
http://praw.readthedocs.io/en/latest/index.html

##### python-twitter: Twitter API wrapper
https://github.com/bear/python-twitter

### DATA

#### Daily Haiku
http://www.dailyhaiku.org/
3172 haikus

#### The Heron's Nest
http://www.theheronsnest.com/
9267 haikus

#### Temps Libres
http://www.tempslibres.org/tl/tlphp/dblang.php?lg=e
5182 haikus

#### Reddit haiku
https://www.reddit.com/r/haiku/
6151 haikus

#### Twitter \#haikus
https://twitter.com/search?q=%23haiku&src=typd&lang=en
5027 haikus

#### Mikhaemoji
https://mikhaemoji.wordpress.com/2016/06/08/haiku-corpus-1/
12 haikus

#### Write a Haiku
http://writeahaiku.com/
37 haikus

#### Modern Haiku
http://www.modernhaiku.org/previousissue.html
399 haikus

#### Haiku Society of America
http://www.hsa-haiku.org/haikucollections.htm
1064 haikus

#### Haiku Foundation
https://www.thehaikufoundation.org/haiku-registry
35551 haikus

### Reformatting to word-line pairs

#### Association score
There are two way to compute

1. Average similarity score between some words in 1st and 2nd, 2nd and 3rd lines.
2. Similarity score between the sum of some words in 1st and 2nd lines with some word in the 3rd line. (This can be only done in vector space.)

In vector space, the two method are comparable, thus we can find best association score over the words in the lines.

#### Embedded vector space
`corpora/glove.haiku.50d.txt` is trained using GloVe on the scraped haikus.

Paramters:
- window size: 7
- minimum word frequency: 5
- vector dimension: 50

Output space has 5764 vectors.

#### All word pairs
Find words present in a corpus as topic words and get all combination of word-line pairs (ignoring repeated words between lines). (150095 entries)

#### Best association score pairs
Find words present in embedded word vector space and get first n best combination of word-line pairs according to the association score. (67855 entires)

Mean and variance of the association score
```
glove_haiku_50 data/daily_haiku.csv 0.357280552368 0.0464979427598
glove_haiku_50 data/herons_nest.csv 0.357637144935 0.0438426424914
glove_haiku_50 data/hsa_haiku.csv 0.356566539173 0.0441245800523
glove_haiku_50 data/mikhaemoji.csv 0.3566718037 0.0441249742062
glove_haiku_50 data/modern_haiku.csv 0.355237483642 0.0443131611342
glove_haiku_50 data/reddit_haiku.csv 0.383749767841 0.046844620716
glove_haiku_50 data/temps_libres.csv 0.380035201266 0.046402419614
glove_haiku_50 data/twitter_haiku.csv 0.39109512994 0.0488310002762
glove_haiku_50 data/write_a_haiku.csv 0.39109512994 0.0488310002762
```
