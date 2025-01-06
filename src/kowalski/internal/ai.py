from litellm import completion


class Client():

    def __init__(self, model: str):
        self.model = model

    def completion(self, note: str, prompt: str) -> str:
        response = completion(
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user"  , "content": note}
            ],
            model=self.model
        )
        return "".join(choice.message.content for choice in response.choices)