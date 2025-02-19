<p align="center">
  <img src="assets/kowalski.png" width="80" align="center"/>
</p>

# `kowalski-core`


![GitHub top language](https://img.shields.io/github/languages/top/Zatfer17/kowalski-core)
![GitHub last commit](https://img.shields.io/github/last-commit/Zatfer17/kowalski-core)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL-orange.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

`kowalski-core` is an AI-powered terminal-based [PKMS](https://www.reddit.com/r/PKMS/comments/1ae7spf/what_is_pkm/?tl=it). You can use it to take notes or save read-it-later content.

## Install

- [Install go](https://go.dev/doc/install)
- Sign up at [OpenRouter](https://openrouter.ai/)
- Run `make all`
- Update the yaml config. Note that:
  - `notesPath` is the full **expanded** path where you will save your notes
  - `editor` is the default editor `kowalski-core` will use
  - `model` is the OpenRouter model id you get from [here](https://openrouter.ai/models)
  - `apiKey` is your OpenRouter api key

## Usage

```
Usage:
  ko [command]

Available Commands:
  add         Add a new note. Skipping the content will open the editor of choice.
  completion  Generate the autocompletion script for the specified shell
  cook        Cook a note with AI.
  edit        Edit a note. Skipping the content will open the editor of choice.
  find        Find a note.
  help        Help about any command
  list        List the notes. Skipping the limit will list all the notes.
  remove      Remove a note.
  save        Save a link.
  serve       Start kowalski in server mode.
  show        Show a note.

Flags:
  -h, --help   help for ko

Use "ko [command] --help" for more information about a command.
```

## License

`kowalski-core` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
