package model

import (
	"fmt"
	"os"
	"path/filepath"
)


var TEMPLATE = `---
name: %s
created: %s
updated: %s
tags: %s
---

%s
`

type Note struct {
	Name    string
	Created string
	Updated string
	Tags    []string
	Content string
}

func (note Note) String() string {
	return fmt.Sprintf("(%s): [🗞  %s] [🏷️  %s]", note.Name, note.Content, note.Tags)
}

func (note Note) Format() string {
	return fmt.Sprintf(TEMPLATE, note.Name, note.Created, note.Updated, note.Tags, note.Content)
}

func (note Note) Write(directory string) error {

	filePath := filepath.Join(directory, note.Name)

	f, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer f.Close()

	_, err = f.WriteString(note.Format())
	return err
}