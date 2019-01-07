#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:14:24 2019

@author: john
"""

import os
from flask import Flask, render_template
from flask import request
from jinja2 import Template
import tweepy
import json
import datetime
from datetime import datetime

t_consumerkey = 'MWQadaodeKZ02JKLfkJA8OhF9'  # Customer Key here
t_secretkey = 'hVGVTiEtAEFwzLZLB6gpa8IaI2xrdv9l4G7S61AbcI3lrPwcU3'  # Customer secret here
access_tokenkey = '2942702198-rybhZK6kteq3c1KyIoXXLtV3C49Q8LlW2VkQcz5'  # Access Token here
access_tokensecret = 'ErFaebAlbAfL1e4yh2NjEx1VBCFQq8En6OurUbHYyUKKY'  # Access Token Secret here

app = Flask(__name__, template_folder="mytemplate")

cf_port = os.getenv("PORT")


@app.route('/',  methods=['GET','POST'])
def Search():    
    all_tweets_text = []    
    
    if request.method == 'GET':
        return render_template('TweetPage.html')
    else:            
        name = request.form['name']
        sdate = datetime.strptime(request.form['sdate'], '%Y-%m-%d')
        edate = datetime.strptime(request.form['edate'], '%Y-%m-%d')
      
        auth = tweepy.OAuthHandler(t_consumerkey, t_secretkey)
        auth.set_access_token(access_tokenkey, access_tokensecret)

        api = tweepy.API(auth)

        public_tweets = api.user_timeline(screen_name=name, tweet_mode='extended')
            
        for tweet_info in public_tweets:
            if tweet_info.created_at < edate and tweet_info.created_at > sdate:
               all_tweets_text.append(tweet_info.full_text)  
            
        return render_template('TweetPage.html', _anchor="Search", result=all_tweets_text)

if __name__ == '__main__':
   if cf_port is None:
       app.run(host='0.0.0.0', port=5000, debug=True)
   else:
       app.run(host='0.0.0.0', port=int(cf_port), debug=True)
