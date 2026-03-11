from agentlens.monitor import monitor
from agentlens.cost_analyzer import daily_cost

# simulate agent action

monitor.action("api_call", "openai.chat.completions")

monitor.tokens(
    model="gpt-4o",
    tokens=1200,
    cost=0.03
)

monitor.action("file_access", "/data/customer.csv")

print("Today's cost:", daily_cost())
