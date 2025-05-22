"""
This requires `pip install crawl4ai`
"""

from agno.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools
from agno.models.groq import Groq

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[Crawl4aiTools(max_length=None)],
    show_tool_calls=True
    )
agent.print_response("Lis the projects from the website: https://surya96t.github.io/.")