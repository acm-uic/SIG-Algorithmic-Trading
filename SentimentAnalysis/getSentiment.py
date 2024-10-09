'''
Program to conduct sentiment analysis on strings and return an attitude value

Output should either be a string like "Postive" or an integer like 1 representing positive attitude

Use whatever dummy inputs you want for now. We will worry about input later.

Use this resource as a starting point to see how to perform sentiment analysis on language
https://blog.quantinsti.com/sentiment-analysis-trading/

TO DO: Implement basic functionality for determining if a string input is positive, neutral, or negative
Example: "I love dogs! They're great" should probably return "Positive" or 1.

'''

# Getting dataset
import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats

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
    return sentiment

# Test the sentiment analysis
positive_count = 0
negative_count = 0

# Ignore this for now, I was testing some stuff

# for tweet in test_data:
#     text = tweet[0]
#     print(tweet[0])
#     actual_sentiment = tweet[1]
#     predicted_sentiment = sentiment_analysis("$AAPL is my BEST investment so far. But it had some downsides.")
#     print("Text:", text)
#     print("Actual Sentiment:", actual_sentiment)
#     print("Predicted Sentiment:", predicted_sentiment)
#     print("---------------------------------------------\n\n\n")
        
#     if predicted_sentiment == 'Positive':
#         positive_count += 1
#     elif predicted_sentiment == 'Negative':
#         negative_count += 1
    
# print("Positive Count:", positive_count)
# print("Negative Count:", negative_count)

# accuracy = (positive_count + negative_count) / len(test_data)
# print("Accuracy:", accuracy*100, "%")

test_text = "I love dogs! They're great"
print(sentiment_analysis(test_text))