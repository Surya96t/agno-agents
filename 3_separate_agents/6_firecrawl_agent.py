# Please install using `pip install firecrawl-py` 

from agno.agent import Agent
from agno.tools.firecrawl import FirecrawlTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

agent = Agent(
    tools=[FirecrawlTools(scrape=False, crawl=True)],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Summarize the code from this repo https://github.com/Surya96t/bikeshare-app")