from langchain.llms import OpenAIChat
from swarms.swarms import GroupChat, GroupChatManager
from swarms.workers import Worker

llm = OpenAIChat(
    model_name='gpt-4', 
    openai_api_key="api-key", 
    temperature=0.5
)

node = Worker(
    llm=llm,
    ai_name="Optimus Prime",
    ai_role="Worker in a swarm",
    external_tools = None,
    human_in_the_loop = False,
    temperature = 0.5,
)

node2 = Worker(
    llm=llm,
    ai_name="Optimus Prime",
    ai_role="Worker in a swarm",
    external_tools = None,
    human_in_the_loop = False,
    temperature = 0.5,
)

node3 = Worker(
    llm=llm,
    ai_name="Optimus Prime",
    ai_role="Worker in a swarm",
    external_tools = None,
    human_in_the_loop = False,
    temperature = 0.5,
)

nodes = [
    node,
    node2,
    node3
]

messages = [
    {
        "role": "system",
        "context": f"Create an a small feedforward in pytorch",
    }
]

group = GroupChat(
    workers=nodes,
    messages=messages
    max_rounds=3,
)


manager = GroupChatManager(
    groupchat=group,
    name="chat_manager",
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    system_message="Group chat manager",
)

output = group.run(
    messages,
    sender=node,
    config=group,
)

print(output)
