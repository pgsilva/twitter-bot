import time
import requests
import json
import oauth2
import urllib.parse

def read_status():
    try:
        post = open('post.txt', 'r')
        return post
    except Exception as erro:
        print('some error occurred: ', erro)  
        return False

def post_tweet(post):
    with open('auth.txt') as json_auth:  
        data = json.load(json_auth)
        for p in data['auth']:
            api_key = p['api_key']
            api_secret_key = p['api_secret_key']
            access_token_secret = p['access_token_secret']
            access_token = p['access_token']
    
    consumer = oauth2.Consumer(api_key, api_secret_key)
    token = oauth2.Token(access_token,access_token_secret)
    cliente = oauth2.Client(consumer, token)

    post_end = urllib.parse.quote(post, safe='')
    req = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status='+ post_end  , method='POST')
    print(req)
    

while not read_status():
    print('trying open a file for post...')
    time.sleep(5)

post = read_status()
post_tweet(post.read())


