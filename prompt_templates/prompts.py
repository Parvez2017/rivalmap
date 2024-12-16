competitor_identify_prompt = """
Act as a SaaS product analyst. Your first task is to identify the competitors of a given SaaS product. 
Perform an intensive internet search and explore the following criteria to identify relevant competitors:
Core Features and Use Cases:

Identify SaaS products offering similar functionalities or solving similar problems.
Include direct competitors (offering identical solutions) and indirect competitors (addressing the same audience but with slightly different approaches).
Market Niche and Target Audience:

Identify products targeting the same industries, customer segments, or niches.
Keyword and SEO Analysis:

Search for products ranking for similar keywords in search engines and ad campaigns.
Brand Presence and Product Mentions:

Check blogs, forums, and social media discussions for mentions of alternative products.
Search across:
Google Search
Product review platforms i.e. G2.
Blogs and news articles discussing SaaS solutions.
Reddit threads, forums, and Quora discussions.
Social media posts (LinkedIn, Twitter, etc.).
App marketplaces (Google App store, Shopify App Store, etc.).

Product Name: {}
Website: {}
Focus Area: {}\n
{}
"""

competitor_information_extractor_prompt = """ 
Act as a senior product manager. Gather comprehensive and detailed information about the competitors. 
You should consider atleast three competitors for the product.
Use reliable sources to collect insights across the following categories:

Features and Functionalities:

List the key features and unique selling points of each competitor.
Identify standout innovations and noteworthy integrations.
Pricing and Plans:

Detail their pricing models (e.g., monthly/yearly plans, freemium options, free trials).
Compare value propositions and pricing transparency.
Customer Feedback and Reviews:

Aggregate customer ratings and reviews from G2 and other platforms.
Extract patterns from customer complaints and praise.
Search Reddit threads, forums, and Quora for unfiltered user feedback.
Marketing and Social Media:

Analyze the company’s branding, messaging, and tone from their website and ads.
Evaluate social media engagement on LinkedIn, Twitter, and other platforms.
Examine their LinkedIn company page for insights like follower count, hiring trends, and updates.
Market Position and News:

Search for news articles and blogs mentioning the competitor’s growth, partnerships, or acquisitions.
Highlight any notable achievements or funding rounds.
Community Sentiment and Marketplaces:

Explore discussions and sentiment from Reddit threads and forums.
Review ratings and feedback from app marketplaces (e.g., Google appstore, Shopify).
Deliverable:
Organize the information in a detailed and structured format with clear categories for each competitor. Include sources for credibility.
Product Name: {}
Website: {}
Focus Area: {}\n
{}
"""

strategy_provider_prompt ="""
Act as a SaaS market research specialist. Using the collected data from competitor research, conduct a comprehensive SWOT analysis for the given SaaS product. 
Focus on leveraging insights from competitor findings to inform the strengths, weaknesses, opportunities, and threats. 
Include the following components:

SWOT Analysis for the Given Product:

Strengths: Identify features, benefits, or strategies where the product excels compared to competitors (e.g., unique features, pricing advantages, customer satisfaction).
Weaknesses: Highlight areas where competitors outperform the product or where it falls short (e.g., missing features, poor reviews, higher pricing).
Opportunities: Explore gaps in the market or competitors’ strategies that the product can exploit (e.g., underserved audiences, unmet customer needs).
Threats: Assess risks posed by competitors’ strengths, new entrants, or market trends that could impact the product.
Feature Comparison Table:

Compare the given product side-by-side with competitors in terms of features, pricing, customer reviews, and integrations.
Strategic Recommendations:

Provide actionable recommendations based on the findings.
Suggest strategies to improve the product’s market position by addressing weaknesses, leveraging opportunities, or countering threats.
Comprehensive Report:

Highlight key differentiators and unique selling points of the given product.
Include strategic recommendations for actionable next steps.
Deliverable:
Produce a ready-to-use report that includes the SWOT analysis, feature comparison, key insights, and clear recommendations for enhancing the product’s competitive positioning.
The report should be in markdown format.

Product Name: {}
Website: {}
Focus Area: {}\n
{}
"""