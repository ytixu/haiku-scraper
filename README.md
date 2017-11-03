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

### Reformatting to word-line pairs

#### All word pairs
Find words present in a corpus as topic words and get all combination of word-line pairs (ignoring repeated words between lines). (150095 entries)


```
Converting all_words with wordnet
---
data/daily_haiku.csv
Average haiku expansion: 4.14171208721
Average word-to-topic ratio: 0.545537294038
Average word-to-topic ratio (stopwords removed): 0.744350017835
Average line length: [2.6617505610772683, 3.7733247835844823, 3.025008015389548]
---
data/herons_nest.csv
Average haiku expansion: 3.90958498024
Average word-to-topic ratio: 0.549963750688
Average word-to-topic ratio (stopwords removed): 0.766909317626
Average line length: [2.54883069828722, 3.7255434782608696, 3.0500658761528325]
---
data/mikhaemoji.csv
Average haiku expansion: 3.91130492019
Average word-to-topic ratio: 0.549882907014
Average word-to-topic ratio (stopwords removed): 0.766900890235
Average line length: [2.5497778509132796, 3.7268389007734077, 3.0504360704294884]
---
data/reddit_haiku.csv
Average haiku expansion: 5.28889498218
Average word-to-topic ratio: 0.519227588161
Average word-to-topic ratio (stopwords removed): 0.750037214205
Average line length: [3.0267617219632577, 4.2988209487249796, 3.4688785302988756]
---
data/temps_libres.csv
Average haiku expansion: 5.05130620985
Average word-to-topic ratio: 0.520680662941
Average word-to-topic ratio (stopwords removed): 0.747462315343
Average line length: [2.9995717344753747, 4.1934903640256955, 3.377002141327623]
---
data/twitter_haiku.csv
Average haiku expansion: 5.30585614258
Average word-to-topic ratio: 0.516480257195
Average word-to-topic ratio (stopwords removed): 0.743477578052
Average line length: [3.0661645095126953, 4.282127448900205, 3.4459650611783013]
