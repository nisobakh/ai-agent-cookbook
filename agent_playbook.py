# AI Agent Cookbook
# Example of a multi-agent workflow with simple prompt routing

import random

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def respond(self, message):
        responses = [
            f"{self.name} ({self.role}) processed: {message}",
            f"{self.name} handled request: {message}",
            f"{self.name} completed task: {message}"
        ]
        return random.choice(responses)

class Router:
    def __init__(self, agents):
        self.agents = agents

    def route(self, query):
        if "finance" in query.lower():
            return self.agents["Finance"].respond(query)
        elif "sales" in query.lower():
            return self.agents["Sales"].respond(query)
        elif "support" in query.lower():
            return self.agents["Support"].respond(query)
        else:
            return "No suitable agent found for query."

# Example setup
agents = {
    "Finance": Agent("FinBot", "Finance Automation"),
    "Sales": Agent("SellBot", "Sales Outreach"),
    "Support": Agent("HelpBot", "Customer Support")
}

router = Router(agents)

# Sample queries
print(router.route("Generate finance report for Q3"))
print(router.route("Send sales follow-up email"))
print(router.route("Handle support ticket #145"))
