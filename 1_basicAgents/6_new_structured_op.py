import asyncio
from typing import List

from agno.agent import Agent, RunResponse  # noqa
from agno.models.openai import OpenAIChat
from pydantic import BaseModel, Field
from rich.pretty import pprint  # noqa


class MovieScript(BaseModel):
    setting: str = Field(
        ..., description="Provide a nice setting for a blockbuster movie."
    )
    ending: str = Field(
        ...,
        description="Ending of the movie. If not available, provide a happy ending.",
    )
    genre: str = Field(
        ...,
        description="Genre of the movie. If not available, select action, thriller or romantic comedy.",
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )


# Agent that uses JSON mode
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You write movie scripts.",
    response_model=MovieScript,
)

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini", response_format=None),
    description="You write movie scripts.",
    response_model=MovieScript,
)


asyncio.run(json_mode_agent.aprint_response("New York"))
asyncio.run(structured_output_agent.aprint_response("Japan"))

print(json_mode_agent.model.__dict__)
print(structured_output_agent.model.__dict__)

