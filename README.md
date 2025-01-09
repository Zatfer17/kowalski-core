<p align="center">
  <img src="assets/pictures/kowalski.png"  width="100" align="center"/>
</p>

# kowalski

`kowalski` is a knowledge management system for the CLI. You can use it as a note-taking tool, a read-it-later app or a bookmarks system.

![kowalski-demo](assets/pictures/demo.gif)

## Setup

Create a config:
```bash
mkdir $HOME/.config/kowalski
nano $HOME/.config/kowalski/config.ini
```
and populate it:
```
[DEFAULT]
Path = /home/zatfer/Documents/kowalski
Editor = nano
```
---
Create the path you just specified in the config:
```bash
mkdir /home/zatfer/Documents/kowalski
```
---
Install:
```bash
git clone https://github.com/Zatfer17/kowalski
cd kowalski
uv tool install .
```
---
Enable autocompletion (optional but strongly advised):
```bash
uv tool install argcomplete
activate-global-python-argcomplete
eval "$(register-python-argcomplete ko)"
```

## Usage

- **add**
```bash
# Open an editor to write a note with:
ko add

# Or quickly jot down something with:
ko add --content "Your content goes here"
```
- **save**
```bash
# Transcribe a Youtube video with:
ko save https://youtu.be/dQw4w9WgXcQ?si=J9KKlOmNFz75b7Cf
# Note that this command might not work 100% of the times as it depends on the availability of the video transcription

# Retrieve the content of a website (if static) with:
ko save https://it.wikipedia.org/wiki/Stefano_Bandecchi
```
- **list**
```bash
# List all notes from latest to oldest with:
ko list

# Show only the last 10 notes:
ko list --limit 10
```
- **find**
```bash
# Find a note by content with:
ko find "Python is a language"

# This is also case insensitive:
ko find "python is a language"


# Note that file name is also part of the note content so you can also use that for the lookup:
ko find 250109 # Will return all notes written on 9th of Jan
```
- **show**
```bash
# Show the content of a note with:
ko show 193900-250109.md
```
- **edit**
```bash
# Open an editor to edit a note with:
ko edit 193900-250109.md

# Or quickly update the content of the note with:
ko edit 193900-250109.md --content "This is the new note content"
```
- **remove**
```bash
# Delete a note with:
ko remove 193900-250109.md
```

## Tricks

`kowalski` plays well with other CLI tools like [mods](https://github.com/charmbracelet/mods) and [glow](https://github.com/charmbracelet/glow).

For instance you can transcribe a Youtube video summarize it and put it in a note with:
```bash
ko save https://www.youtube.com/watch?v=sSxGEHakfuc&t=587s # Gets saved to 195456-250109.md
ko show 195456-250109.md | mods "Please summarize this" # Gets saved to f343930 conversation
mods -f f343930 | ko add # Creates a new note out of the AI generated summary

# Or in two shots:
ko save https://www.youtube.com/watch?v=sSxGEHakfuc&t=587s # Gets saved to 195456-250109.md
ko show 195456-250109.md | mods "Please summarize this" | ko add

# Or simply replace the original note for simplicity:
ko show 195456-250109.md | mods "Please summarize this" | ko edit 195456-250109.md
```

You can also pretty render a note in the terminal:
```bash
ko show 195456-250109.md | glow -
```


## License

`kowalski` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
