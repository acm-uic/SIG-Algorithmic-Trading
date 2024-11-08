'''
Program to conduct sentiment analysis on strings and return an attitude value

Output should either be a string like "Postive" or an integer like 1 representing positive attitude

Resource:
https://blog.quantinsti.com/sentiment-analysis-trading/

TO DO: 
- Implement functiality for neutral sentiment
- Connect output from newsGetter.py to this file and run sentiment analysis on the news articles

'''
# Import packages
import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats
import newsGetter
#import wallStreetBetsScraper


# Download NLTK resources
nltk.download('twitter_samples')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load positive and negative tweets from the NLTK Twitter corpus
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')

# Preprocess tweets
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_tweet(tweet):
    # Tokenize the tweet
    tokens = word_tokenize(tweet.lower())
    # Remove stopwords and stem the remaining words
    stemmed_tokens = [ps.stem(token) for token in tokens if token not in stop_words and token.isalpha()]
    # Create a dictionary of word features
    features = {}
    for token in stemmed_tokens:
        features[token] = True
    return features
    
# Generate feature sets for positive and negative tweets
positive_features = [(preprocess_tweet(tweet), 'Positive') for tweet in positive_tweets]
negative_features = [(preprocess_tweet(tweet), 'Negative') for tweet in negative_tweets]

# Split the data into training and testing sets
train_data = positive_features[:800] + negative_features[:800]
test_data = positive_features + negative_features

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_data)

# Perform sentiment analysis on new data
def sentiment_analysis(text):
    features = preprocess_tweet(text)
    sentiment = classifier.classify(features)

    # This doesn't work as intended, classifier defaults to positive
    # pos_tokens = 0
    # neg_tokens = 0
    # for token in features:
    #     if token:
    #         pos_tokens += 1
    #     else:
    #         neg_tokens += 1
    # if pos_tokens == neg_tokens or pos_tokens == neg_tokens + 1:
    #     sentiment = 'Neutral'
    return sentiment

# Test the sentiment analysis
# test_text = "I love dogs! They're great"
# print(sentiment_analysis(test_text))
# test_text2 = "I hate cats! They're terrible"
# print(sentiment_analysis(test_text2))
# test_text3 = "I am neutral"
# print(sentiment_analysis(test_text3))
# test_text4 = "A variety of factors, encompassing both internal and external influences, contribute to the development of diverse perspectives and behaviors in individuals across different environments. These elements, while subject to variation depending on situational context, can include but are not limited to, cultural background, socioeconomic conditions, personal experiences, and the interplay between individual psychology and societal norms. By considering a wide range of influences and acknowledging the multifaceted nature of human decision-making processes, one can gain a more comprehensive understanding of the complexities that shape actions, thoughts, and attitudes."
# print(sentiment_analysis(test_text4))
if __name__ == '__main__':
    # Perform sentiment analysis on headlines from the Wall Street Journal
    url = 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'
    feed = newsGetter.parse_rss_feed(url)
    headlines = newsGetter.get_headlines(feed)
    headlines_with_descriptions = newsGetter.get_headlines_with_descriptions(feed)

    print("Headlines:")
    positive_count = 0
    negative_count = 0

    for headline in headlines:
        print(headline)
        sentiment = sentiment_analysis(headline)
        print(sentiment)
        if (sentiment == 'Positive'):
            positive_count += 1
        elif (sentiment == 'Negative'):
            negative_count += 1
        print("\n")
    print("Positive Count:", positive_count)
    print("Negative Count:", negative_count)
    print("Total Headlines:", len(headlines))

    wsj_market_sentiment_assessment = "WSJ Markets feed is positive" if positive_count > negative_count else "WSJ Markets feed is negative"
    print(wsj_market_sentiment_assessment)

    # Perform sentiment analysis on posts from the WallStreetBets subreddit
    # hot_posts = wallStreetBetsScraper.read_hot_posts()
    # print("Posts:")
    # for post in hot_posts['data']['children']:
    #     title = post['data']['title']
    #     title_sentiment = sentiment_analysis(title)
    #     print(title_sentiment)
    #     if (title_sentiment == 'Positive'):
    #         positive_count += 1
    #     elif (title_sentiment == 'Negative'):
    #         negative_count += 1
    #     print("\n")
    # positive_count = 0
    # negative_count = 0