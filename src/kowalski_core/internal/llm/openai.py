from .client import Client
from openai  import OpenAI as OpenAiClient


class OpenAI(Client):

    def __init__(self):
        super().__init__()
        self.client = OpenAiClient()

    def completion(self, prompt: str, content: str, model: str) -> str:

        response = self.client.chat.completions.create(
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user"  , "content": content}
            ],
            model=model,
        )

        return "".join(choice.message.content for choice in response.choices)