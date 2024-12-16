import os
import json 
from apify_client import ApifyClient
from . import APIFY_KEY

# Initialize the ApifyClient with your API token
client = ApifyClient(APIFY_KEY)

def linkedin_scraper(linkedin_url:str) ->str:
    run_input = {
    "urls": [
        linkedin_url
    ],
    "proxy": { "useApifyProxy": True },
    }

    # Run the Actor and wait for it to finish
    run = client.actor("sanjeta/linkedin-company-profile-scraper").call(run_input=run_input)
    items = [json.dumps(item) for item in client.dataset(run["defaultDatasetId"]).iterate_items()]
    return "\n".join(items)

def g2_product_review(product_name: str) ->str:
    run_input = {
    "query": product_name.lower(),
    "mode": "review",
    "limit": 5,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("jupri/g2-explorer").call(run_input=run_input)
    items = [json.dumps(item) for item in client.dataset(run["defaultDatasetId"]).iterate_items()]
    return "\n".join(items)

def reddit_comment_scraper(reddit_comment_url: str) ->str:
    run_input = { "startUrls": [{ "url": reddit_comment_url}] }

    # Run the Actor and wait for it to finish
    run = client.actor("creative_tablecloth/reddit-scraper-for-posts").call(run_input=run_input)
    items = [json.dumps(item["body"]) for item in client.dataset(run["defaultDatasetId"]).iterate_items()]
    return "\n".join(items)
