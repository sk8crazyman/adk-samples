from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompts import BUSINESS_ANALYST_PROMPT, PRODUCT_MANAGER_PROMPT

MODEL = "gemini-2.5-pro"

product_manager_agent = LlmAgent(
    name="product_manager_agent",
    model=MODEL,
    instruction=PRODUCT_MANAGER_PROMPT,
)

business_analyst_agent = LlmAgent(
    name="business_analyst_agent",
    model=MODEL,
    instruction=BUSINESS_ANALYST_PROMPT,
    tools=[AgentTool(agent=product_manager_agent)],
)

root_agent = business_analyst_agent
