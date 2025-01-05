<p align="center">
  <img src="https://static.wikia.nocookie.net/dreamworks-penguins/images/f/f9/Kowalski1New.png/revision/latest?cb=20211201210141"  width="150" align="center"/>
</p>

# kowalski-core

`kowalski-core`  is a simple think-it-later app for your CLI.

## Principles

- [x] Should be a cli for responsible note takers, no error handling to ensure speed 
- [x] Files should be in markdown format 
- [x] Default name should be timestamp
- [x] ID is filename
- [x] Filename should be timestamp
- [x] Files should all be in a single folder
- [x] No subfolders
- [ ] Just tags
- [ ] All commands must return also JSON print like nmcli
- [ ] Git based
- [ ] Use § as prefix for identifiers in interlinking

## Usage
- Clone an empty repo (no README) called `.kowalski` in your HOME folder
- Start using `kowalski-core`
- Install `gitJournal` on mobile
- Update settings on `gitJournal`:
  - `Storage & File Formats > New Note Filename` = `yyyymmddhhmmss`
  - `Storage & File Formats > Note Metadata Settings > Modified Field` = `updated`

## Ideas

- Use GitHub actions to:
  - run URL/YouTube parsing from mobile
  - run kaboom from mobile or defer from cli
- Implement:
  - Add with URL or Youtube link
  - Show with regular expression to search
  - Sync, to run as part of every command, triggers every half an hour or so
  - Kaboom, with ID or question. RAG capability could be implemented relying on tags for document similarity

## License

`kowalski-core` is distributed under the terms of the [GNU general public license](https://www.gnu.org/licenses/gpl-3.0.html).
