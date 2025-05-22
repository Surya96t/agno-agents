"""
This is a simple Grok agent that uses the Grok API to get a response from the model. 
"""

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

from agno.agent import Agent, RunResponse
from agno.models.groq import Groq

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    markdown=True,
)


agent.print_response("Write a haiku about soccer.")