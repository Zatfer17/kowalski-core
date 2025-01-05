<p align="center">
  <img src="https://static.wikia.nocookie.net/dreamworks-penguins/images/f/f9/Kowalski1New.png/revision/latest?cb=20211201210141"  width="150" align="center"/>
</p>

# kowalski-core

`kowalski-core` it's an AI powered CLI for knowledge management. You can use it as:
- a note-taking tool
- a read-it-later app
- a bookmarks system

## Principles

- [x] Should be a cli for responsible note takers, no error handling to ensure speed 
- [x] Files should be in markdown format 
- [x] Default name should be timestamp
- [x] ID is filename
- [x] Filename should be timestamp
- [x] Files should all be in a single folder
- [x] No subfolders
- [x] Git based
- [ ] Just tags
- [ ] All commands must return also JSON print like nmcli
- [ ] Use § as prefix for identifiers in interlinking

## Setup

### SSH

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

## Suggested setup
- Clone an empty repo (no README) called `.kowalski` in your HOME folder
- Start using `kowalski-core`
- Install `gitJournal` on mobile
- Update settings on `gitJournal`:
  - `Storage & File Formats > New Note Filename` = `yyyymmddhhmmss`
  - `Storage & File Formats > Note Metadata Settings > Modified Field` = `updated`

## Roadmap
- [ ] Implement Save with URL or Youtube link
- [ ] Implement Kaboom, with ID or question. RAG capability could be implemented relying on tags for document similarity
- [ ] Make website
- [ ] (Implement Init with gitPython to clone .kowalski repo)
- [ ] (Implement Show with regular expression or keyword to search)
- [ ] Use GitHub actions to run URL/YouTube parsing from mobile
- [ ] Use GitHub actions to run kaboom from mobile or defer from cli
- [ ] Implement script for Obsidian migration

## Issues
- Notes created on gitJournal can't be deleted from CLI, as they are restored on first gitJournal push

## License

`kowalski-core` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
