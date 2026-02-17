from crewai import Agent
from tools import tool


## Create senior blog content researcher

blog_researcher= Agent(
    role='Blog Researcher from arxiv',
    goal='Get the relevant paper from the arxiv for the topic {topic}',
    verbose = True,
    memory=True,
    backstory=(
        "Expert in understanding research papers in AI, GenAI models and the latest techniques used to solve an issue"
    ),
    tools=[],
    allow_delegation=True,
)

## Creating a writer agent with arxiv tool
blog_writer = Agent(
    role = 'Blog Writer',
    goal=(
            "Craft a compelling, technically accurate, and engaging narrative explaining "
    "the complete tech stack behind {topic}, breaking down architecture, tools, "
    "trade-offs, and real-world implementation insights in a way that is both "
    "educational and captivating."
    ),
    verbose = True,
    memory=True,
    backstory=(
            "A former senior engineer turned technical blogger who has built and scaled "
    "multiple AI-driven systems in production. You understand distributed systems, "
    "LLM pipelines, cloud infrastructure, and developer tooling deeply. You don't "
    "just explain what tools are used — you explain why they were chosen, what "
    "problems they solve, and what trade-offs they introduce. Your stories feel "
    "like behind-the-scenes engineering breakdowns from real-world systems."
    ),
    tools=[tool],
    allow_delegation=False
)
