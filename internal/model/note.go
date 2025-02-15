package model

import (
	"strings"
	"fmt"
	"os"
	"path/filepath"
	"github.com/Zatfer17/kowalski-core/internal/utils"
)


var TEMPLATE = `---
created: %s
tags: [%s]
---
%s`

type Note struct {
	Created string
	Tags    []string
	Color   string
	Content string
}

func NewNote(created string, tags []string, content string) Note {
	return Note{
		Created: created,
		Tags:    tags,
		Color:   utils.GenerateColor(tags),
		Content: content,
	}
}

func (note Note) GetName() string {
	return fmt.Sprintf("%s.md", note.Created)
}

func (note Note) String() string {

	color := utils.ColoredSquare(note.Color)

	name := note.GetName()
	name  = utils.Colored(235, 171, 52, name)
	name  = utils.Bold(name)
	
	content := note.Content
	content  = strings.ReplaceAll(content, "\n", " ")
	if len(content) > 27 {
		content = content[:27]
	}
	content = content + strings.Repeat(".", 30-len(content))
	content = utils.Bold(content)

	tags := strings.Join(note.Tags, ",")
	if len(tags) > 17 {
		tags = tags[:17]
	}
	tags = tags + strings.Repeat(".", 20-len(tags))
	tags = utils.Colored(0, 168, 138, tags)

	return fmt.Sprintf("%s (%s): [🗞  %s] [🏷️  %s]", color, name, content, tags)
}

func (note Note) Format() string {
	return fmt.Sprintf(TEMPLATE, note.Created, strings.Join(note.Tags, ","), note.Content)
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