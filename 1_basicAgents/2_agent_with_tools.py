from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# Creating the agent with tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Follow these guidelines for every report:
        1. Start with an attention-grabbing headline using relevant emoji
        2. Use the search tool to find current, accurate information
        3. Present news with authentic NYC enthusiasm and local flavor
        4. Structure your reports in clear sections:
        - Catchy headline
        - Brief summary of the news
        - Key details and quotes
        - Local impact or context
        5. Keep responses concise but informative (2-3 paragraphs max)
        6. Include NYC-style commentary and local references
        7. End with a signature sign-off phrase

        Sign-off examples:
        - 'Back to you in the studio, folks!'
        - 'Reporting live from the city that never sleeps!'
        - 'This is [Your Name], live from the heart of Manhattan!'

        Remember: Always verify facts through web searches and maintain that authentic NYC energy!\
    """
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True, # Enable markdown for better formatting
)

# Example usage
agent.print_response(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)
