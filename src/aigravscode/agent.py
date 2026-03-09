"""
Agent logic for Aigravscode.
"""

class Agent:
    def __init__(self, name: str = "Assistant"):
        self.name = name

    def run(self, task: str):
        return f"Agent {self.name} is working on: {task}"
