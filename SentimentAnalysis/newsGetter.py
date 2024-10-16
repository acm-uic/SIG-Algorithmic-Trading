'''
NEWS GETTER
This class is responsible for getting news from a given RSS Feed URL

Used the feedparser library to parse the XML response from RSS feeds for news data. 

This output will later be fed to the sentiment analysis program

TO DO: 
- Think about how to refactor Newsgetter class to work for larger inputs (e.g. dictionary of links)
'''

import feedparser

def parse_rss_feed(url):
    feed = feedparser.parse(url)
    return feed

def get_headlines(feed):
    headlines = []
    for entry in feed.entries:
        headlines.append(entry.title)
    return headlines

def get_headlines_with_descriptions(feed):
    headlines_with_descriptions = []
    for entry in feed.entries:
        headlines_with_descriptions.append({'title': entry.title, 'description': entry.summary})
    return headlines_with_descriptions

if __name__ == '__main__':
    wsj_url = 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'
    feed = parse_rss_feed(wsj_url)
    headlines = get_headlines(feed)
    headlines_with_descriptions = get_headlines_with_descriptions(feed)
    print(headlines)
    print(headlines_with_descriptions)