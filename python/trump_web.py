#!/usr/bin/env python3

import hashlib

from sys import path
path.append( '/home/ubuntu/char-rnn/src/trumptweeter/' )
from trumptweeter import fetch_tweet
from twitter_bot import push_tweet_to_twitter

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods = [ 'GET', 'POST' ] )
def show_website():
    if request.method == 'GET':
        return render_template( 'index.html' )
    else:
        dna = request.form[ 'dna' ]
        return render_template(
            'minimal.html',
            tweet = fetch_tweet( dna ),
            hashed_tweet = hashlib.md5(dna.encode()).hexdigest(),     
        )


@app.route('/retweet', methods = [ 'GET' ] )
def retweet():
    hashed_tweet = request.args.get( 'hashed_tweet' )
    if hashed_tweet is None:
        return 'You did not supply the tweet hash'
    if not is_md5( hashed_tweet ):
        return 'bad input'
    tweet = fetch_tweet( '', seed = hashed_tweet )
    push_tweet_to_twitter( tweet ) # TODO enable and test
    return redirect( 'https://twitter.com/bestDonaldTrum2' )


def is_md5( md5_hash ):
    try:
        int( md5_hash, 16 )
    except ValueError:
        return False
    return len( md5_hash ) == 32
