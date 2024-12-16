import json
import os 
import requests
import streamlit as st
from langchain.tools import tool

from .summarizer_tools import summarize
from .apify_utils import g2_product_review

class G2ProdcutReviewTools():
    @tool("Scrape G2 Website for Reviews")
    def scrape_and_summarize_g2_reviews(product_name:str) ->str:
        """Scrape and find important user reviews about the product from G2. Insert the product name."""
        data = g2_product_review(product_name)
        summary = summarize(data)
        return summary 