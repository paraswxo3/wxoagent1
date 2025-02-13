from crewai import Crew, Task, Agent
from crewai import LLM
from langchain_community.tools.tavily_search import TavilySearchResults
import os

os.environ["WATSONX_APIKEY"] = "jDAsTH4sneg9mAHK5tCjc6UULaIncdHEvRxwRm-VsOap"
os.environ["TAVILY_API_KEY"] = "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"
os.environ["WATSONX_PROJECT_ID"] = "273897d8-8d34-4b72-b2d0-c94de5c6b75e"
os.environ["WATSONX_URL"] = "https://us-south.ml.cloud.ibm.com"

llm = LLM(
    model="watsonx/mistralai/mistral-large",
    max_tokens=500,
    temperature=0
)

# Tools
search = TavilySearchResults(max_results=5)

# Create the agent
researcher = Agent(
    llm=llm,
    role="Senior AI Researcher",
    goal="Find promising research in the field of quantum computing.",
    backstory="You are a veteran quantum computing researcher with a background in modern physics.",
    allow_delegation=False,
    tools=[search],
    verbose=1,
)

# Create a task
task1 = Task(
    description="Search the internet and find 5 examples of promising AI research.",
    expected_output="A detailed bullet point summary on each of the topics. Each bullet point should cover the topic, background and why the innovation is useful.",
    output_file="task1output.txt",
    agent=researcher,
)

# Create the second agent
writer = Agent(
    llm=llm,
    role="Senior Speech Writer",
    goal="Write engaging and witty keynote speeches from provided research.",
    backstory="You are a veteran quantum computing writer with a background in modern physics.",
    allow_delegation=False,
    verbose=1,
)

# Create a task
task2 = Task(
    description="Write an engaging keynote speech on quantum computing.",
    expected_output="A detailed keynote speech with an intro, body and conclusion.",
    output_file="task2output.txt",
    agent=writer,
)

# Put all together with the crew
crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=1)
print(crew.kickoff())