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
3551 haikus

#### Best Haikus of All Time
http://www.thehypertexts.com/Best%20Haiku.htm
146 haikus

#### Haikus from Basho and Buson
246 haikus

### Reformatting to word-line pairs

#### Association score
There are two way to compute

1. Average similarity score between some words in 1st and 2nd, 2nd and 3rd lines.
2. Similarity score between the sum of some words in 1st and 2nd lines with some word in the 3rd line. (This can be only done in vector space.)

In vector space, the two method are comparable, thus we can find best association score over the words in the lines.

## To Run

`cd` to the root directory of this repo.

To run scrappers, first uncomment the website that you want to scrap in scrapers\scraper.py and run
```
python scrapers/scraper.py
```
This will overwrite the files in `/data`

To run converter (converting the scrapped haikus to word-line pairs), uncomment accordingly (see file converter/converter.py) and run,
```
python converter/converter.py
```

To run topic expansion, run
```
python converter/expand.py
```


### GloVe

Download repo from here: https://github.com/stanfordnlp/GloVe

In `/glove` there are files for converting scrapped haiku to lines and paired-lines. This is for training word embedding.