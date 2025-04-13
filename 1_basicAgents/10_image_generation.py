from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools



# Create an agent that generates images based on text prompts
image_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DalleTools()],
    description=dedent("""\
        You are an experienced AI artist with expertise in various artistic styles,
        from photorealism to abstract art. You have a deep understanding of composition,
        color theory, and visual storytelling.\
    """),
    instructions=dedent("""\
        As an AI artist, follow these guidelines:
        1. Analyze the user's request carefully to understand the desired style and mood
        2. Before generating, enhance the prompt with artistic details like lighting, perspective, and atmosphere
        3. Use the `create_image` tool with detailed, well-crafted prompts
        4. Provide a brief explanation of the artistic choices made
        5. If the request is unclear, ask for clarification about style preferences

        Always aim to create visually striking and meaningful images that capture the user's vision!\
    """),
    markdown=True,
    show_tool_calls=True,
)

# Example usage
# image_agent.print_response(
#     "Create a magical library with floating books and glowing crystals", stream=True
# )
# # Retrieve and display generated images
# images = image_agent.get_images()
# if images and isinstance(images, list):
#     for image_response in images:
#         image_url = image_response.url
#         print(f"Generated image URL: {image_url}")


# Example 2: Generate an image with custom settings
custom_dalle = DalleTools(model="dall-e-3", size="1792x1024", quality="hd", style="natural")

agent_custom = Agent(
    tools=[custom_dalle],
    name="Custom DALL-E Generator",
    show_tool_calls=True,
)

agent_custom.print_response("Create a panoramic nature scene showing a peaceful mountain lake at sunset", markdown=True)