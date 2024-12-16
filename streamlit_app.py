from crewai import Crew
from crewai.process import Process
from analyst_agents import AnalystAgents, StreamToExpander
from analyst_tasks import AnalystTasks
import streamlit as st
import sys

st.set_page_config(layout="wide")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

class AnalystCrew:

    def __init__(self, product_name, website, focus_area):
        self.product_name = product_name
        self.website = website
        self.focus_area = focus_area
        self.output_placeholder = st.empty()

    def run(self):
        agents = AnalystAgents()
        tasks = AnalystTasks()

        product_selector_agent = agents.product_selection_agent()
        saas_expert_agent = agents.saas_expert_agent()
        competitor_analyst_agent = agents.competitor_analyst_agent()

        identify_task = tasks.identify_task(
            product_selector_agent,
            self.product_name,
            self.website,
            self.focus_area,
    
        )

        gather_task = tasks.gather_task(
            saas_expert_agent,
            self.product_name,
            self.website,
            self.focus_area,
    
        )

        plan_task = tasks.plan_task(
            competitor_analyst_agent,
            self.product_name,
            self.website,
            self.focus_area,
        )

        crew = Crew(
            agents=[
                product_selector_agent, saas_expert_agent, competitor_analyst_agent
            ],
            tasks=[identify_task, gather_task, plan_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("RivalMap")

    st.subheader("AI agents to take your SaaS product ahead of your competitors",
                 divider="rainbow", anchor=False)

    with st.sidebar:
        st.header("👇 Enter your SaaS product details")
        with st.form("my_form"):
            product_name = st.text_input(
                "What is the name of your SaaS product?", placeholder="Airtable")
            website = st.text_input(
                "What is the Website of your SaaS product?", placeholder="https://www.airtable.com")
            focus_area = st.text_area("Your focus area of the competitors",
                                     placeholder="I want to know their growth strategy") 

            submitted = st.form_submit_button("Run Agents")

        st.divider()

if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            trip_crew = AnalystCrew(product_name, website, focus_area)
            result = trip_crew.run()
        status.update(label="✅ Strategic Plan Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Strategic Plan", anchor=False, divider="rainbow")
    st.markdown(result)
