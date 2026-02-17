from crewai import Task
from tools import tool
from agents import blog_researcher,blog_writer

## Research Task
research_task = Task(
    description=(
        "Conduct deep technical research on the topic: {topic}. "
        "Identify relevant research papers (preferably from arXiv), "
        "industry blogs, official documentation, and production case studies. "
        "Extract key insights about architecture, core algorithms, frameworks, "
        "tools used, performance trade-offs, and real-world challenges."
    ),
    expected_output=(
        "A structured research report containing:\n"
        "1. Overview of the topic\n"
        "2. Key research papers with summaries\n"
        "3. Core technologies and frameworks involved\n"
        "4. Architecture patterns commonly used\n"
        "5. Technical challenges and trade-offs\n"
        "6. Emerging trends or recent advancements\n"
        "7. References with links"
    ),
    tools=[tool],
    agent=blog_researcher,
)




## Writing task
writing_task = Task(
    description=(
        "Using the research findings provided, craft a compelling and technically "
        "accurate long-form article on {topic}. Transform the structured research "
        "into an engaging narrative that explains the tech stack, architecture, "
        "design decisions, trade-offs, and real-world applications."
    ),
    expected_output=(
        "A well-structured technical article in Markdown including:\n"
        "1. Attention-grabbing introduction\n"
        "2. Clear explanation of the problem space\n"
        "3. Breakdown of the system architecture\n"
        "4. Explanation of core technologies and why they were chosen\n"
        "5. Trade-offs and engineering decisions\n"
        "6. Real-world implementation insights\n"
        "7. Strong conclusion summarizing key takeaways\n"
        "The article should be engaging, technically deep, and written in a "
        "professional engineering blog tone."
    ),
    tools=[tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
