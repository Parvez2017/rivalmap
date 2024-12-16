from crewai import Task
from prompt_templates.prompts import competitor_identify_prompt,\
                                    competitor_information_extractor_prompt,\
                                    strategy_provider_prompt

class AnalystTasks():

    def identify_task(self, agent, product_name, website, focus_area):
        return Task(description=competitor_identify_prompt.format(product_name, website, focus_area, self.__tip_section()),
            expected_output="Provide a list of the top competitors, with a brief description of each product and why it qualifies as a competitor.",
            agent=agent)

    def gather_task(self, agent, product_name, website, focus_area):
        return Task(description=competitor_information_extractor_prompt.format(product_name, website, focus_area, self.__tip_section()),
            expected_output="Insightful and credible information in a detailed and structured format with clear categories for each competitors",
            agent=agent)

    def plan_task(self, agent, product_name, website, focus_area):
        return Task(description=strategy_provider_prompt.format(product_name, website, focus_area, self.__tip_section()),
            expected_output="A comprehensive report that includes the SWOT analysis, feature comparison, key insights, and clear recommendations for enhancing the product’s competitive positioning.",
            agent=agent)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $1000 and grant you any wish you want!"
