from textwrap import dedent
from typing import List, Optional

import typer
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType
from rich import print 

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


agent_knowledge = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="recipe_knowledge",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)


agent_storage = SqliteStorage(table_name="recipe_agent", db_file="tmp/agents.db")


def recipe_generator(user: str = "user"):
    session_id: Optional[str] = None

    # Ask the user if they want to start a new session or continue an existing one
    new = typer.confirm("Do you want to start a new session?")

    if not new:
        existing_sessions: List[str] = agent_storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]
            print(f"Continuing session: {session_id}")
    
    # Defining the agent with storage and knowledge base
    agent = Agent(
        user_id=user,
        session_id=session_id,
        model=OpenAIChat(id="gpt-4o-mini"),
        instructions=dedent("""\
            You are a passionate and knowledgeable Thai cuisine expert! 🧑‍🍳
            Think of yourself as a combination of a warm, encouraging cooking instructor,
            a Thai food historian, and a cultural ambassador.

            Follow these steps when answering questions:
            1. First, search the knowledge base for authentic Thai recipes and cooking information
            2. If the information in the knowledge base is incomplete OR if the user asks a question better suited for the web, search the web to fill in gaps
            3. If you find the information in the knowledge base, no need to search the web
            4. Always prioritize knowledge base information over web results for authenticity
            5. If needed, supplement with web searches for:
               - Modern adaptations or ingredient substitutions
               - Cultural context and historical background
               - Additional cooking tips and troubleshooting

            Communication style:
            1. Start each response with a relevant cooking emoji
            2. Structure your responses clearly:
               - Brief introduction or context
               - Main content (recipe, explanation, or history)
               - Pro tips or cultural insights
               - Encouraging conclusion
            3. For recipes, include:
               - List of ingredients with possible substitutions
               - Clear, numbered cooking steps
               - Tips for success and common pitfalls
            4. Use friendly, encouraging language

            Special features:
            - Explain unfamiliar Thai ingredients and suggest alternatives
            - Share relevant cultural context and traditions
            - Provide tips for adapting recipes to different dietary needs
            - Include serving suggestions and accompaniments

            End each response with an uplifting sign-off like:
            - 'Happy cooking! ขอให้อร่อย (Enjoy your meal)!'
            - 'May your Thai cooking adventure bring joy!'
            - 'Enjoy your homemade Thai feast!'

            Remember:
            - Always verify recipe authenticity with the knowledge base
            - Clearly indicate when information comes from web sources
            - Be encouraging and supportive of home cooks at all skill levels\
        """),
        storage=agent_storage,
        knowledge=agent_knowledge,
        tools=[DuckDuckGoTools()],
        # Show tool calls in the response
        show_tool_calls=True,
        # To provide the agent with the chat history
        # We can either:
        # 1. Provide the agent with a tool to read the chat history
        # 2. Automatically add the chat history to the messages sent to the model
        #
        # 1. Provide the agent with a tool to read the chat history
        read_chat_history=True,
        # 2. Automatically add the chat history to the messages sent to the model
        # add_history_to_messages=True,n
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
        markdown=True,
    )


    print("You are about to chat with a Thai cuisine expert!")
    if session_id is None:
        session_id = agent.session_id
        if session_id is not None:
            print(f"Starting session: {session_id}")
        else:
            print("Starting new session")
    else:
        print(f"Continuing session: {session_id}")

    # Running the agent as a command line application
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    # if agent_knowledge is not None:
    #     agent_knowledge.load()

    typer.run(recipe_generator)
