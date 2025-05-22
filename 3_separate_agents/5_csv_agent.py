# Please install using `pip install duckdb`

import httpx
from pathlib import Path
from agno.agent import Agent
from agno.tools.csv_toolkit import CsvTools

url = "https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
response = httpx.get(url)

imdb_csv = Path(__file__).parent.joinpath("wip").joinpath("imdb.csv")
imdb_csv.parent.mkdir(parents=True, exist_ok=True)
imdb_csv.write_bytes(response.content)

agent = Agent(
    tools=[CsvTools(csvs=[imdb_csv])],
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "First always get the list of files",
        "Then check the columns in the file",
        "Then run the query to answer the question",
        "Always wrap column names with double quotes if they contain spaces or special characters",
        "Remember to escape the quotes in the JSON string (use \")",
        "Use single quotes for string values"
    ],
)

agent.cli_app(stream=False)