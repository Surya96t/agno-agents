# pip install -U google-auth-oauthlib google-auth-httplib2 google-api-python-client openai agno
# pip install mistralai

try:
    from tzlocal import get_localzone_name
except (ModuleNotFoundError, ImportError):
    raise ImportError("`tzlocal not found` install using `pip install tzlocal`")

import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.googlecalendar import GoogleCalendarTools


cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("google_client/client_secret.json")
print(tmp)

load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")


agent = Agent(
    tools=[GoogleCalendarTools(credentials_path=tmp)],
    show_tool_calls=True,
    instructions=[
        f"""
You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
You should help users to perform these actions in their Google calendar :
    - get their scheduled events from a certain date and time
    - create events based on provided details
"""
    ],
    model=MistralChat(api_key=os.getenv("MISTRAL_API_KEY")),
    add_datetime_to_instructions=True,
)

#agent.print_response("Create an event tomorrow called langchain certifications from 2pm to 5pm.", markdown=True)

# agent.print_response("What do I have scheduled for only tomorrow?", markdown=True)

agent.print_response("Can you create a new calendar called test?", markdown=True)