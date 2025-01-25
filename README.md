<p align="center">
  <img src="assets/kowalski.png" width="80" align="center"/>
</p>

# kowalski-core

`kowalski-core` is a hackable terminal-based [PKMS](https://www.reddit.com/r/PKMS/comments/1ae7spf/what_is_pkm/?tl=it) for the AI era. You can use it to take notes or save read-it-later content.

## Setup

`kowalski-core` expects a yaml config in `~/.config/kowalski`:
```
mkdir ~/config/kowalski
nano ~/.config/kowalski/core.yaml
```
The config should look like:
```
notesPath: "/home/zatfer/Documents/notes" # Your (existing) notes folder
editor: "nano" # Your editor of choice
```
**Please note**: the `notesPath` should a the full expanded path, no symbols (`~`) or env variables (`$HOME`) allowed. This is due to Go.

## License

`kowalski-core` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
