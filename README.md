<p align="center">
  <img src="assets/kowalski.png" width="80" align="center"/>
</p>

# kowalski-core

`kowalski-core` is a hackable terminal-based [PKMS](https://www.reddit.com/r/PKMS/comments/1ae7spf/what_is_pkm/?tl=it) for the AI era. You can use it to take notes or save read-it-later content.

## Setup

`kowalski-core` expects a yaml config in `~/.config/kowalski`:
```
mkdir ~/.config/kowalski
nano ~/.config/kowalski/core.yaml
```

`core.yaml` should look like:
```
notesPath: "/home/zatfer/Documents/notes" # Your (existing) notes folder
editor: "nano" # Your editor of choice
```

**Please note**: the `notesPath` should be the full expanded path, no symbols (`~`) or env variables (`$HOME`) allowed. This is due to how Go works.

Install running:
```
go build -o release/ko
sudo mv release/ko /usr/local/bin/
```

## Usage

```
Usage:
  ko [command]

Available Commands:
  add         Add a new note. Skipping the content will open the editor of choice.
  completion  Generate the autocompletion script for the specified shell
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
