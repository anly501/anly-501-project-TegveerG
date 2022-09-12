# https://github.com/defiyield-app/api-docs/blob/main/README_Rekt_Database.md

# No Oauth required to GET data from this API

# filling in parameters to our needs (AND (crime OR attack OR criminals OR rug pull OR honeypot or ransomware or scam))

REKTcrypto_data_raw=newsapi.get_everything(q="+crypto",
                            domains='news.google.com, reuters.com, theverge.com, wired.com, techcrunch.com,bbc.com,nbcnews.com,news.yahoo.com,businessinsider.com,foxnews.com',
                            page=1,page_size=100,
                            to='2022-09-10',
                            language='en',sort_by='relevancy')

#extracting raw json data

scams_raw=['articles']

#converting and exporting json raw data to pandas df

df_raw=pd.DataFrame(articles_raw)
print("Dataframe shape is ", df_raw.shape)
df_raw.to_csv('NewsApi_raw.csv')