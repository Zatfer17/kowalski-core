package model

import (
	"strings"
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

	name := note.Name

	content := note.Content
	content =  strings.ReplaceAll(content, "\n", " ")

	tags := note.Tags

	return fmt.Sprintf("(%s): [%s] [%s]", name, content, tags)
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