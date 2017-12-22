#!/bin/bash
cat haikus | python convert.py > poem
./demo.sh
cp vectors.txt <YOUR_ROOT_NAME>/haiku-scraper/corpora/glove.haikus.50.txt
echo 'Done haiku'

cat limericks.txt | python convert.py >> poem
./demo.sh
cp vectors.txt <YOUR_ROOT_NAME>/haiku-scraper/corpora/glove.poems.50.txt
echo 'Done poem'

cat haikus | python convert.py --paired > poem
./demo.sh
cp vectors.txt <YOUR_ROOT_NAME>/haiku-scraper/corpora/glove.haiku_pair.50.txt
echo 'Done haiku_lower'

cat limericks.txt | python convert.py --paired >> poem
./demo.sh
cp vectors.txt <YOUR_ROOT_NAME>/haiku-scraper/corpora/glove.poem_pair.50.txt
echo 'Done poem_lower'



