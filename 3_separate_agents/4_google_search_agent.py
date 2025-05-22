"""
Please install using `pip install googlesearch-python`
Please install using `pip install pycountry`
`google-api-python-client`
"""

from textwrap import dedent
from pathlib import Path

from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.models.groq import Groq

cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tool_tmp")

google_search_agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[GoogleSearchTools()],
    # Sytem Message
    description=dedent("""\
        You are a Google Search agent. Your task is to perform searches and provide relevant information to the user.
    """),
    show_tool_calls=True,
    markdown=True,
    save_response_to_file=str(tmp.joinpath("{message}.md")),
    debug_mode=True
)


google_search_agent.print_response("List the starting positions for Bahrain 2025 Grand Prix")

# google_search_agent.print_response("What are the latest developments in AI?")