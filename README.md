<p align="center">
  <img src="https://static.wikia.nocookie.net/dreamworks-penguins/images/f/f9/Kowalski1New.png/revision/latest?cb=20211201210141"  width="150" align="center"/>
</p>

# kowalski-core

[![PyPI - Version](https://img.shields.io/pypi/v/kowalski-dev.svg)](https://pypi.org/project/kowalski-core)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kowalski-dev.svg)](https://pypi.org/project/kowalski-core)

kowalski-core is a simple cli for note taking, built with [Typer](https://github.com/fastapi/typer).

kowalski-core can capture strings, urls and youtube transcriptions, create `*.md` notes and easily process them locally with your LLM of choice via [Ollama](https://github.com/ollama/ollama)

-----

## Table of Contents

- [kowalski-core](#kowalski-core)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Collect](#collect)
    - [Transform](#transform)
    - [Bonus](#bonus)
  - [Rationale](#rationale)
  - [Setup](#setup)
  - [License](#license)

## Usage

```                                                  
 Usage: kowalski-core [OPTIONS] COMMAND [ARGS]...                                                                   
                                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                          │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.   │
│ --help                        Show this message and exit.                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ collect                                                                                                          │
│ transform                                                                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Collect

```
 Usage: kowalski-core collect [OPTIONS] [SOURCE]                                                                    
                                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   source      [SOURCE]  The piece of information you want to collect (note, url, youtube link)                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Transform

```
 Usage: kowalski-core transform [OPTIONS] [SOURCE]                                                                  
                                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   source      [SOURCE]  The note you want to transform (path)                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --intent        [POLISH|SUMMARIZE|ORGANIZE|ELABORATE|BRAINSTOR  What Kowalski should do with that piece of       │
│                 M]                                              information                                      │
│                                                                 [default: SUMMARIZE]                             │
│ --help                                                          Show this message and exit.                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Bonus

The two commands can be piped, ie you can do:
```
kowalski collect [SOURCE] | kowalski transform
```

In this way the transformation will be applied straight to the note collected. You can also pipe in the output from pbpaste:
```
pbpaste | kowalski collect | kowalski transform
```
And define a shortcut in your terminal for ease

## Rationale

At work I:
- consume a lot of webpages (mostly Sagemaker documentation xD)
- occasionally watch youtube tutorials
- write quick and bad notes
- code

All in all I end up reading and writing a lot of text.

According to [The New York Times](https://archive.nytimes.com/bits.blogs.nytimes.com/2009/12/09/the-american-diet-34-gigabytes-a-day/) we process 34 gigabytes of information every day. This is the equivalent of 100000 words or 174 newspapers. But a big chunk of this information goes wasted, unless you have a really good memory.

Partly inspired by what Daniel Miessler did with [Fabric](https://github.com/danielmiessler/fabric), I ended up developing `kowalski`, in its cli version for now. `kowalski` is my way of easily building a knowledge base with the help of LLMs. I can now paste any youtube link in the terminal and `kowalski` will handle it for me, retrieving its transcription and then summarize it for me. Or I can jot down a quick idea and `kowalski` will elaborate on it for me.

## Setup

1. **Clone this repo**

    ```
    git clone https://github.com/Zatfer17/kowalski-core.git
    cd kowalski-core
    ```

2. **Create a config**

    ```
    touch kowalski_core/config.py
    nano kowalski_core/config.py
    ```

    Your config must include:
    ```
    NOTES_PATH=<FILL_ME>
    MODEL_NAME=<FILL_ME>
    API_BASE=<FILL_ME>
    ```
    where:
    - `NOTES_PATH` can be any path, but make sure to have two subfolders in there, one called `collect` and one called `transform`.
    - `MODEL_NAME` is the name of your ollama model of choice.
    - `API_BASE` is the ollama base api, typically `http://localhost:11434`

    A sample config would be:
    ```
    NOTES_PATH = '/home/matteo/Documents/Github/notes'
    MODEL_NAME = 'ollama/llama3.2:1b'
    API_BASE   = 'http://localhost:11434'
    ```

3. **Start ollama**
    ```
    ollama serve
    ```

4. **Install kowalski-core**
    ```
    pipx install .
    ```

## License

`kowalski-core` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
