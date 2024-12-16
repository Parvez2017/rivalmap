import json
import os 
import requests
import streamlit as st
from langchain.tools import tool

from .summarizer_tools import summarize
from .apify_utils import linkedin_scraper

class LinkedInTools():
    @tool("Scrape LinkedIn Page")
    def scrape_and_summarize_linkedin(linkedin_page_url:str) ->str:
        """Scrape and find important information about the company from LinkedIn.
        Provide a valid linkedin url for the company. 
        The url structure should look like this: 'https://www.linkedin.com/company/{company name}'"""
        data = linkedin_scraper(linkedin_page_url)
        summary = summarize(data)
        return summary 
