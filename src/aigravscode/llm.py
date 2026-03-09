"""
LLM provider integration for Aigravscode.
"""

class LLMProvider:
    def __init__(self, provider: str = "openai"):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return f"Response from {self.provider} for: {prompt}"
