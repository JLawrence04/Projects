# Wikipedia Pages Sentiment Analyzer Utilzing MediaWiki API
I wanted to learn more about the applications of Natural Language Processing (NLP) and was particularly interested in creating something to do with sentiment analysis. With Wikipedia articles mainly being edited and wrtitten by random individuals (especially the non prominent pages) I was interested in seeing the polarity and subjectivity of any given Wikipedia article. So I created a python script where a user can provide a search for a wikipedia article title, then the script sends an API request for the search to Wikipedia's API, the script then cleans the text for NLP, and I then used Textblob to perform sentiment analysis and output the results. I also encode the words in the text into vectors to be able to cluster different sentences together based on vector similarity and see the different sentiment results of the different sentence groups.
Polarity scores range from -1 to 1 with -1 indicating a very negative sentiment, 0 being neutral, and 1 being very positive. Subjectivity scores range from 0 to 1 with 1 being the most subjective and 0 indicating a very objective text. From experimenting and playing around with the script, it appears a good average fro a wikipedia polarity score would be around .05 and subjectivity varying more but seems to have an average around .3 indicating most of these wikipedia articles keep a neutral and atleast somewhat objective sentiment.

## Key Steps Taken in Project
- Created functions to send API requests and retrieve plain article text.
- Preprocessed text and cleaned the text for it to be suitable and optimal for Textblob to perform a sentiment analysis.
- The script outputs the polarity and subjectivity scores of the text, a long with polarity scores of each clustered sentence group.
- Performed word encoding to be able to cluster sentences together based on vector similarity, used k-means clustering to achieve this.

## How To Run Script
In this folder for this project, there is a requirements.txt file with all the necessary libraries so in the command line you just need to run pip install -r (file path) to make sure the required python packages are installed then there shouldn't be an issues arising when running the python script.



