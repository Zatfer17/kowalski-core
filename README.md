![OS support](https://img.shields.io/badge/OS-macOS%20Linux%20Windows-red)
![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)

<p align="center">
  <img src="assets/pictures/kowalski.png"  width="150" align="center"/>
</p>

# kowalski

`kowalski` is an AI powered knowledge management system for the CLI. You can use it as a note-taking tool, a read-it-later app or a bookmarks system, using your AI model of choice (Ollama, OpenAI, Anthropic, ...).

![kowalski-demo](assets/pictures/demo.gif)

## Tutorial

TODO

## Rationale

TODO

## Guiding principles
- Taking notes should be fast
- Notes should be in markdown format
- Notes are identified by their name
- Notes default name should be the creation timestamp
- Folders are forbidden
- Tags are used for categorisation

## Install

TODO

### Create the Kowalski folder

```bash
mkdir ~/.kowalski
```

### Update the config

Update the [config](src/kowalski/internal/config.py). Note that you will have to `uv tool install . --reinstall` any time you make changes to the config.

### Setup LLM of choice

- If using any OPENAI model:

```bash
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

- If using Ollama:
  - [install](https://ollama.com/download)
  - [pull a model](https://ollama.com/search)
  - `ollama serve`

### Install (with [uv](https://docs.astral.sh/uv/getting-started/installation/))

```bash
git clone https://github.com/Zatfer17/kowalski
cd kowalski
uv tool install .
```

### Setup SSH (only if syncing is needed)

Generate one using the following command:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Copy your public SSH key:

```bash
cat ~/.ssh/id_rsa.pub
```
Add the key to GitHub:

Run the following command to test your SSH connection:

```bash
ssh -T git@github.com
```

## My suggested setup
- Create an empty repo (no README) called `.kowalski`
- Clone it inside HOME
- Install gitJournal on mobile
- Hook gitJournal to the repo
- Update settings on gitJournal:
  - `Storage & File Formats > New Note Filename` = `yyyymmddhhmmss`
  - `Storage & File Formats > Note Metadata Settings > Modified Field` = `updated`
- Seamlessly sync notes across devices

## Roadmap
- [ ] Make website
- [ ] Use GitHub actions to run URL/YouTube parsing from mobile
- [ ] Use GitHub actions to run kaboom from mobile or defer from cli
- [ ] Implement Kaboom, with question. RAG capability could be implemented relying on tags for document similarity
- [ ] Implement Init with gitPython to clone .kowalski repo
- [ ] Implement Show with regular expression or keyword to search
- [ ] Implement script for Obsidian migration

## Known issues

- Notes created on gitJournal won't be deleted with `kowalski`, as they are restored on first gitJournal push

## License

`kowalski` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
