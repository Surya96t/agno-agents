from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# Here we create the News Reporter with a fun personality
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=dedent(
        """
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Your style guide:
        - Start with an attention-grabbing headline using emoji
        - Share news with enthusiasm and DC attitude
        - Keep your responses concise but entertaining
        - Throw in local references and DC slang when appropriate
        - End with a catchy sign-off like 'Back to you in the studio!' or 'Reporting live from the White House!'

        Remember to verify all facts while keeping that DC energy high!\
        """
    ),
    markdown=True,
)


# Example usage
agent.print_response(
    "Tell me about the bill planning to end OPT.", stream=True
)