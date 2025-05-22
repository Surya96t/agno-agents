
from agno.agent import Agent
from agno.tools.email import EmailTools

receiver_email = "madichetti.srinivas@gmail.com"
sender_email = "surya96t@gmail.com"
sender_name = "Surya"
sender_passkey = "xldb gnfi qrfz uwdj"

agent = Agent(
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ]
)
agent.print_response("Send an email to <receiver_email> with content as This is a agent ai test email and a haiku on life.")