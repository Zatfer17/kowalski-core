package model

import (
	"strings"
	"fmt"
	"os"
	"path/filepath"
)


var TEMPLATE = `---
created: %s
tags: %s
---
%s`

type Note struct {
	Created string
	Tags    []string
	Content string
}

func (note Note) GetName() string {
	return fmt.Sprintf("%s.md", note.Created)
}

func (note Note) String() string {
	
	name := note.GetName()
	
	content := note.Content
	content =  strings.ReplaceAll(content, "\n", " ")

	tags := note.Tags

	return fmt.Sprintf("(%s): [%s] %s", name, content, tags)
}

func (note Note) Format() string {
	return fmt.Sprintf(TEMPLATE, note.Created, note.Tags, note.Content)
}

func (note Note) Write(directory string) error {

	filePath := filepath.Join(directory, note.GetName())

	f, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer f.Close()

	_, err = f.WriteString(note.Format())
	return err
}