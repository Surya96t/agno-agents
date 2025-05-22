"""🎥 YouTube Agent - Your Video Content Expert!

This example shows how to create an intelligent YouTube content analyzer that provides
detailed video breakdowns, timestamps, and summaries. Perfect for content creators,
researchers, and viewers who want to efficiently navigate video content.

Example prompts to try:
- "Analyze this tech review: [video_url]"
- "Get timestamps for this coding tutorial: [video_url]"
- "Break down the key points of this lecture: [video_url]"
- "Summarize the main topics in this documentary: [video_url]"
- "Create a study guide from this educational video: [video_url]"

Run: `pip install openai youtube_transcript_api agno` to install the dependencies
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.youtube import YouTubeTools


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")



youtube_agent = Agent(
    name="YouTube Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YouTubeTools()],
    instructions=dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        Your analysis style:
        - Begin with a video overview
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
    """),
    add_datetime_to_instructions=True,
    markdown=True,
)


# Example usage with different types of videos
youtube_agent.print_response(
    "Analyze this video: https://www.youtube.com/watch?v=SaDzIVkYqyY&list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&index=9",
    stream=True,
)

