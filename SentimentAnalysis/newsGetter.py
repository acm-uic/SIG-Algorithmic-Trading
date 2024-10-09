'''
NEWS GETTER
This class is responsible for getting news from a given RSS Feed URL

Uses the requests library to get the XML response from the URL
Uses the xml.etree.ElementTree library to parse the XML response

This output will later be fed to the sentiment analysis program

TO DO: 
- Think about how to refactor Newsgetter class to work for larger inputs (e.g. dictionary of links)
'''
import requests
import xml.etree.ElementTree as ET

class NewsGetter:
    def __init__(self, link):
        self.url = link
    def get_top_headlines():
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            headlines = []
            for item in root.findall('.//item'):
                title = item.find('title').text
                headlines.append(title)
            return headlines
        else:
            return []
    def get_headlines_with_descriptions(url):
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            headlines_with_descriptions = []
            for item in root.findall('.//item'):
                title = item.find('title').text
                description = item.find('description').text
                headlines_with_descriptions.append({'title': title, 'description': description})
            return headlines_with_descriptions
        else:
            return

# Example usage
if __name__ == '__main__':
    

    url = 'https://abcnews.go.com/abcnews/usheadlines'
    news_getter = NewsGetter(url)
    top_headlines = NewsGetter.get_top_headlines()
    top_headlines_with_descriptions = NewsGetter.get_headlines_with_descriptions(url)
    print(top_headlines)
    #print(top_headlines_with_descriptions)