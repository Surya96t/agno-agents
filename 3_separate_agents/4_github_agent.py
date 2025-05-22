# Please install using `pip install pygithub`

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GITHUB_ACCESS_TOKEN"]=os.getenv("GITHUB_ACCESS_TOKEN")


from agno.agent import Agent
from agno.tools.github import GithubTools
from agno.models.openai import OpenAIChat

agent = Agent(
    # model=OpenAIChat(id="gpt-3.5-turbo"),
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "Use your tools to answer questions about the repo: Surya96t/official_project",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools()],
    show_tool_calls=True,
)

# agent.print_response("List open pull requests", markdown=True)

# Example: Directory listing
# agent.print_response(
#     "Create an issue for the repo Surya96t/rag-fastapi-project with the title List docs api not working and the body The docs api is not working",
#     markdown=True,
# )

agent.print_response(
    "List all the pull requests (open and closed) that are in the repo.",
    markdown=True,
)