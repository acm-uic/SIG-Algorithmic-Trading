'''
NEWS GETTER

Get the top 5 headlines for a specific company

For example get 5 headlines for NVDA
Use the Dow Jones API:
https://developer.dowjones.com/site/docs/newswires_apis/dow_jones_top_stories_api/index.gsp#overview-1

Output should be a container or strings (dictionary or array, whichever)
This output will later be fed to the sentiment analysis program

TO DO: Implement basic functionality for getting the top 5 headlines about DJT (Trump Media)
- Hint use requests library to send GET request to API endpoint url
'''
import requests
import xml.etree.ElementTree as ET

# r = requests.get('https://feeds.a.dj.com/rss/RSSMarketsMain.xml')
# if r.status_code == 200:
#     root = ET.fromstring(r.content) # Parse the XML response
#     children = root[0] # Get the first child of the root to iterate through

#     for child in children: # Iterate through the XML and print elements
#         print(f"Tag: {child.tag}, Attributes: {child.attrib}, Text: {child.text}")
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
    url = 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'
    news_getter = NewsGetter(url)
    top_headlines = NewsGetter.get_top_headlines()
    top_headlines_with_descriptions = NewsGetter.get_headlines_with_descriptions(url)
    print(top_headlines)
    print(top_headlines_with_descriptions)