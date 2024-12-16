# RivalMap: Streamlit-Integrated AI Crew for Competitor Research and Strategy Creation for Your SaaS tool

_Forked and enhanced from the_ [_crewAI examples repository_](https://github.com/joaomdmoura/crewAI-examples/tree/main/trip_planner)

## Introduction
Meet RivalMap – your AI-powered competitor analysis tool designed to keep you ahead in the SaaS game. With RivalMap, you can effortlessly discover your competitors, analyze their strategies, and gain actionable insights to refine your own.

Powered by cutting-edge AI, Google Search, LinkedIn scrapers, and web crawlers, RivalMap takes the hassle out of competitor research and delivers a ready-to-use strategic plan in no time.

**Check out the video below for the tool walkthrough** 👇
https://drive.google.com/file/d/1-zwCH658q8i0mGQxa8hbsYh0hX_hNAeQ/view?usp=sharing

## CrewAI Framework

CrewAI simplifies the orchestration of role-playing AI agents. In VacAIgent, these agents collaboratively decide on cities and craft a complete itinerary for your trip based on specified preferences, all accessible via a streamlined Streamlit user interface.

## Streamlit Interface

The introduction of [Streamlit](https://streamlit.io/) transforms this application into an interactive web app, allowing users to easily input their preferences and receive tailored strategic plans.

## Running the Application

To run the RivalMap app:

- **Configure Environment**: Set up the environment variables for [Browserless](https://www.browserless.io/), [Serper](https://serper.dev/), [OpenAI](https://openai.com/) and [Apify](https://apify.com/). Use the `env.example` as a guide to add your the file (`.env`)

- **Install Dependencies**: Execute `pip install -r requirements.txt` in your terminal.
- **Launch the App**: Run `streamlit run streamlit_app.py` to start the Streamlit interface.

★ **Disclaimer**: The application uses GPT-4 by default. Ensure you have access to OpenAI's API and be aware of the associated costs.

## Details & Explanation

- **Streamlit UI**: The Streamlit interface is implemented in `streamlit_app.py`, where users can input their SaaS product details.
- **Components**:
  - `./analyst_tasks.py`: Contains task prompts for the agents.
  - `./analyst_agents.py`: Manages the creation of agents.
  - `./tools directory`: Houses tool classes used by agents.
  - `./prompt_templates`: All the prompts for the agents
  - `./streamlit_app.py`: The heart of the Streamlit app.


## Using Local Models with Ollama

For enhanced privacy and customization, you can integrate local models like Ollama:

### Setting Up Ollama

- **Installation**: Follow Ollama's guide for installation.
- **Configuration**: Customize the model as per your requirements.

### Integrating Ollama with CrewAI

Pass the Ollama model to agents in the CrewAI framework:

```python
from langchain.llms import Ollama

ollama_model = Ollama(model="model")

class AnalystAgents:
    # ... existing methods

    def market_expert(self):
        return Agent(
            role='SaaS Market Expert',
            tools=[SearchTools.search_internet, BrowserTools.scrape_and_summarize_website],
            llm=ollama_model,
            verbose=True
        )

```

## Benefits of Local Models

- **Privacy**: Process sensitive data in-house.
- **Customization**: Tailor models to fit specific needs.
- **Performance**: Potentially faster responses with on-premises models.

## To Know More
- Email: hasanparvez2017@gmail.com
- LinkedIn: https://www.linkedin.com/in/parvej2017

## License

RivalMap is open-sourced under the MIT License.
