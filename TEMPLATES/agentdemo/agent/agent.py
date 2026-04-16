import os
import random

from google.adk import Agent
from google.adk.tools.tool_context import ToolContext

os.environ.setdefault("OTEL_SERVICE_NAME", "agentdemo")

from google.adk.telemetry.setup import maybe_set_otel_providers  # noqa: E402

maybe_set_otel_providers()


def roll_die(sides: int, tool_context: ToolContext) -> int:
    """Roll a die and record the outcome for later reference."""
    result = random.randint(1, sides)
    if "rolls" not in tool_context.state:
        tool_context.state["rolls"] = []
    tool_context.state["rolls"] = tool_context.state["rolls"] + [result]
    return result


async def check_prime(nums: list[int]) -> str:
    """Check whether the provided numbers are prime."""
    primes = set()
    for number in nums:
        number = int(number)
        if number <= 1:
            continue
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(number)
    if not primes:
        return "No prime numbers found."
    return f"{', '.join(str(num) for num in primes)} are prime numbers."


root_agent = Agent(
    model="gemini-2.5-flash",
    name="agentdemo_agent",
    description="Dice-rolling demo agent.",
    instruction=(
        "You are a helpful assistant that can roll dice and answer questions "
        "about prime numbers. When asked to roll a die, use the roll_die tool. "
        "To check for primes, use the check_prime tool."
    ),
    tools=[roll_die, check_prime],
)
