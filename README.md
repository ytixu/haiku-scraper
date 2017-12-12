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
Find words present in embedded word vector space and get first n best combination of word-line pairs according to the association score. (92040 entires)

Mean and variance of the association score
```
glove_poem_pair_50 data/daily_haiku.csv 0.426720520313 0.0308187132536
glove_poem_pair_50 data/haiku_foundation.csv 0.430753140632 0.0301892363038
glove_poem_pair_50 data/herons_nest.csv 0.415355115674 0.027218049136
glove_poem_pair_50 data/modern_haiku.csv 0.367671944758 0.0308155489674
glove_poem_pair_50 data/reddit_haiku.csv 0.500054891507 0.0335015490394
glove_poem_pair_50 data/temps_libres.csv 0.439545564794 0.0293613901322
glove_poem_pair_50 data/twitter_haiku.csv 0.473346197345 0.0392785278992
glove_poem_pair_50 data/basho-buson.txt 0.466559954747 0.0310958709744
glove_poem_pair_50 data/best_haikus.txt 0.443525686815 0.0325005803886
glove_poem_pair_50 data/hsa_haiku.txt 0.412536348356 0.032246705612
glove_poem_pair_50 data/mikhaemoji.txt 0.563596556276 0.0187410765112
glove_poem_pair_50 data/write_a_haiku.txt 0.596324130905 0.0385583520554

```
