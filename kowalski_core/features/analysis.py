import sys

from kowalski_core.config            import GROQ_API_KEY, MODEL_NAME
from kowalski_core.features.markdown import get_metadata, get_content

from groq import Groq
from importlib.resources import open_text

class Analysis():

    def __init__(self, source: str) -> None:
        with open(source) as f:
            note = f.read()
        metadata = get_metadata(note)
        self.intent = metadata['intent']
        self.intent_output = metadata['intent_output']
        self.content  = get_content(note)
        self.client = Groq(api_key=GROQ_API_KEY)

    def get_prompt(self) -> str:
        prompt = open_text('kowalski_core.templates', f'{self.intent}.md')
        return prompt.read()

    def run(self) -> None:
        with open(self.intent_output, 'w', encoding="utf-8") as f:  
            messages = [
                {'role': 'system', 'content': self.get_prompt()},
                {'role': 'user'  , 'content': self.content}
            ]
            response = self.client.chat.completions.create(messages=messages, model=MODEL_NAME)
            content = response.choices[0].message.content
            sys.stdout.write(content)
            f.write(content)