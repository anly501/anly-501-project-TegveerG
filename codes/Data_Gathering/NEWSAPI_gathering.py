#pip install newsapi-python

import pandas as pd
from newsapi import NewsApiClient

# https://newsapi.org/docs/endpoints/everything

newsapi = NewsApiClient(api_key='188722aa04164b9aac4b7c781331350e')

# filling in parameters to our needs (AND (crime OR attack OR criminals OR rug pull OR honeypot or ransomware or scam))

news_data_raw=newsapi.get_everything(q="+crypto",
                            domains='news.google.com, reuters.com, theverge.com, wired.com, techcrunch.com,bbc.com,nbcnews.com,news.yahoo.com,businessinsider.com,foxnews.com',
                            page=1,page_size=100,
                            to='2022-09-10',
                            language='en',sort_by='relevancy')

#extracting relevant raw json data

articles_raw=news_data_raw['articles']

#converting and exporting json raw data to pandas df

df_raw=pd.DataFrame(articles_raw)
print("Dataframe shape is ", df_raw.shape)
df_raw.to_csv('NewsApi_raw.csv')