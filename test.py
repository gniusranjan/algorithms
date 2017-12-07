from textblob import TextBlob as tb
import tweepy

customer_key='1v9QsJIxst7dDQvSmoAZ3uZGU'
customer_secret='svyasoW4q2EH4JEhj6KxfgC2Dl9hNwPjcSGou4IVBACCDCPRd6'
access_token='765095100712099840-ZMR78P8YiCwvklscEK3RmRObbS0MvfQ'
access_token_secret='8WU8hOt3TNqUV24BIYxJjMnpBlun2nrGkahINSibV1sA6'
authenticate =tweepy.OAuthHandler(customer_key,customer_secret)
authenticate.set_access_token(access_token,access_token_secret)
api=tweepy.API(authenticate)
public_tweets=api.search('ashish ')
for t in public_tweets:
    print(t.text)
    analysis= tb(t.text)
    print(analysis.sentiment)
