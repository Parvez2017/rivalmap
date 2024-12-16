from crewai import Agent, LLM
import re
import os 
import streamlit as st

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from tools.linkedin_tools import LinkedInTools
from tools.g2_product_review_tools import G2ProdcutReviewTools
from tools.reddit_tools import RedditTools

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

llm = LLM(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=2500,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

class AnalystAgents():

    def product_selection_agent(self):
        return Agent(
            role='Product Research Expert',
            goal='Select the direct and inderect competitors of the given SaaS product',
            backstory='An expert in analyzing SaaS products to identify competiting SaaS product',
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=llm,
            max_rpm=200,
            allow_delegation=False
        )

    def saas_expert_agent(self):
        return Agent(
            role='Senior Product Manager',
            goal='Provide the BEST insights about the selected SaaS product',
            backstory="""An exceptional senior SaaS product manager with extensive experience
                    about product, its features, GTM, sales and growth strategy""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                LinkedInTools.scrape_and_summarize_linkedin,
                G2ProdcutReviewTools.scrape_and_summarize_g2_reviews,
                RedditTools.scrape_and_summarize_reddit_comment
            ],
            llm=llm,
            verbose=True,
            max_rpm=200,
            allow_delegation=False
        )

    def competitor_analyst_agent(self):
        return Agent(
            role='SaaS Market Research Specialist',
            goal="""Prepare a ready-to-use competitor analysis report highlighting key differentiators,
                feature comparisons, and strategic recommendations.""",
            backstory="""Specialist in product competitor analysis with 
                 decades of experience""",
            llm=llm,
            verbose=True,
            max_rpm=200,
            allow_delegation=False
        )

###########################################################################################
# Print agent process to Streamlit app container                                          #
# This portion of the code is adapted from @AbubakrChan; thank you!                       #
# https://github.com/AbubakrChan/crewai-UI-business-product-launch/blob/main/main.py#L210 #
###########################################################################################
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Senior Product Manager" in cleaned_data:
            # Apply different color 
            cleaned_data = cleaned_data.replace("Senior Product Manager", f":{self.colors[self.color_index]}[Senior Product Manager]")
        if "Product Research Expert" in cleaned_data:
            cleaned_data = cleaned_data.replace("Product Research Expert", f":{self.colors[self.color_index]}[Product Research Expert]")
        if "SaaS Market Research Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("SaaS Market Research Specialist", f":{self.colors[self.color_index]}[SaaS Market Research Specialist]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
