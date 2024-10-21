import sys


from kowalski_core.config                    import MODEL_NAME, API_BASE
from kowalski_core.features.transform.intent import Intent

from importlib.resources import open_text
from litellm             import completion


class Analysis():

    def __init__(self, note: str) -> None:
        self.note = note

    def get_prompt(self, intent: Intent) -> str:
        prompt = open_text('kowalski_core.features.transform.templates', f'{intent}.md')
        return prompt.read()

    def run(self, intent: Intent) -> None:
        with open(self.note.transform_path, 'w', encoding="utf-8") as f:  
            messages = [
                {'role': 'system', 'content': self.get_prompt(intent)},
                {'role': 'user'  , 'content': self.note.content}
            ]
            if API_BASE is None:
                response = completion(
                    model    = MODEL_NAME,
                    messages = messages
                )
            else:
                response = completion(
                    model    = MODEL_NAME,
                    messages = messages,
                    api_base = API_BASE
                )
            content = response.choices[0].message.content
            #sys.stdout.write(content)
            return content