import requests

class NewsGetter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.dowjones.com/v2/news"

    def get_top_headlines(self, company_name, count=5):
        """
        Get top headlines for a specific company.

        Args:
        - company_name (str): The name of the company to search for.
        - count (int): Number of headlines to retrieve (default is 5).

        Returns:
        - headlines (dict): A dictionary containing the top headlines and their sources.
        """
        params = {
            'query': company_name,
            'count': count,
        }
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }

        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            headlines = {article['headline']: article['source'] for article in articles[:count]}
            return headlines
        else:
            print(f"Error fetching news: {response.status_code} - {response.json().get('title')}")
            return {}

if __name__ == "__main__":
    #dowjones apikey
    news_getter = NewsGetter(api_key='your_api_key')
    company_name = "Tesla"
    headlines = news_getter.get_top_headlines(company_name)
    print(f"Top 5 headlines for {company_name}:")
    for headline, source in headlines.items():
        print(f"- {headline} (Source: {source})")