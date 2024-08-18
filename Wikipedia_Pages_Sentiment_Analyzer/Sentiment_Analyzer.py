#Importing Libraries
import requests
import json
import re
from textblob import TextBlob
import contractions
from gensim.models import Word2Vec
import numpy as np
from sklearn.cluster import KMeans
from kneed import KneeLocator
def find_page(input):
    url = 'https://en.wikipedia.org/w/rest.php/v1/search/title' #API endpoints needed were found on Wikipedia's MediaWiki REST API
    info = requests.get(url, params= {'q': input, 'limit':1})
    info = json.loads(info.text)
    
    if info['pages'] == []: #While testing random search cases, sometimes the search would result in no similar page being found
        return 'MediaWiki API call could not find a similar wiki page to search input, try another search'
    
    else:
        wiki_page = info['pages']
        page_info = wiki_page[0]
        title = page_info['title'] 
        web_link = 'https://en.wikipedia.org/wiki/' + page_info['key']
        
        #Retreiving the text of queried wiki article through API request
        url1 = "https://en.wikipedia.org/w/api.php"
        text_params = {"action": "query", "titles": title, "prop": "extracts", "explaintext": True, "format": "json"}

        text_response = requests.get(url1, text_params)
        text_json = json.loads(text_response.text)

        #Retrieving only the text and filtering out other keys in the dictionary
        text = text_json['query']['pages']
        id = page_info['id']

        lst = [title,web_link,text[str(id)]['extract']]
        return lst

def clean_text(text):
    text = text.lower() #Making all text lowercase so textblob doesn't weigh words differently because of capitalization
    
    text = contractions.fix(text)

    text = re.sub("\n", " ", text) #\n indicates a line break and isn't needed for the sentiment analysis

    sentences = TextBlob(text).sentences
    
    lst = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        sentence = re.sub(r'[^a-zA-Z\s]', '', str(sentence)) #Removing special characters, punctuation, and numbers that will just add noise to sentiment analysis

        sentence = re.sub('\t', "", sentence)

        sentence = re.sub(r"\s{2,}", " ", sentence)
        lst.append(sentence)
    return lst

def encode(sentences):
    #Splitting sentences into words for encoding but still listed with words in same sentence
    words = [sentence.split() for sentence in sentences]

    encode_model = Word2Vec(words,window=5, min_count=1)

    vectors = []
    for sentence in words:
        word_vectors = []
        for word in sentence:
            if word in encode_model.wv:
                word_vectors.append(encode_model.wv[word])
        vectors.append(np.mean(word_vectors, axis = 0)) #Averaging the word vectors to create vector for the entire sentence
    
    return vectors

def clusters(vectors):

# Calculate WCSS for different numbers of clusters and automatically detect the elbow point
    wcss = []
    count = 0
    for i in range(1, 11):
        if i <= len(vectors):
            kmeans = KMeans(n_clusters=i, random_state=0)
            kmeans.fit(vectors)
            wcss.append(kmeans.inertia_)
            count += 1


    kneedle = KneeLocator(range(1, count+1), wcss, curve='convex', direction='decreasing')
    optimal_clusters = kneedle.elbow
    return optimal_clusters

def sentiment(sentences,text):
    if len(sentences) >= 2 and (clusters(sentences) != None):
        clusters_num = clusters(sentences)
        kmeans = KMeans(n_clusters=clusters_num, random_state=0)
        kmeans.fit(sentences)

        labels = kmeans.labels_
        clusters_dict = {i: [] for i in range(clusters_num)}

        #Storing sentences vectors in dictionary under the cluster they were labeled
        for i,sentence in enumerate(text):
            clusters_dict[labels[i]].append(sentence)
        
        #Finding polarity scores of each cluster, can show how much weight each cluster has in the overall polarity score
        cluster_polarity = {}
        for i in range(clusters_num):
            polarity = TextBlob(" ".join(clusters_dict[i])).sentiment.polarity
            cluster_polarity[i] = polarity
            

        return [TextBlob(" ".join(text)).sentiment.polarity,TextBlob(" ".join(text)).sentiment.subjectivity,cluster_polarity]
    else:
        return [TextBlob(" ".join(text)).sentiment.polarity,TextBlob(" ".join(text)).sentiment.subjectivity]

x = [find_page('basketball')[2]]

x = clean_text(x[0])

print('===================================')
y = encode(x)

print(sentiment(y,x))
