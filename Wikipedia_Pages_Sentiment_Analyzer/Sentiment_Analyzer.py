#Importing Libraries
import requests
import json

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

print(find_page('basketball'))
