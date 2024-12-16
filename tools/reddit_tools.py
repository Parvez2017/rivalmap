import json
import os 
import requests
import streamlit as st
from langchain.tools import tool

from .summarizer_tools import summarize
from .apify_utils import reddit_comment_scraper

class RedditTools():
    @tool("Scrape Reddit Page")
    def scrape_and_summarize_reddit_comment(reddit_comment_url:str) ->str:
        """Scrape and extract reddit comments from a subreddit thread.
        Provide a valid url for the Reddit comment. 
        The url structure should contain this url: 'https://www.reddit.com/r/{subreddit}/comments/{comment id}/{comment}/'"""
        data = reddit_comment_scraper(reddit_comment_url)
        summary = summarize(data)
        return summary 
