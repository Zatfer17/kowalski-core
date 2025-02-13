package model

import (
	"crypto/md5"
	"encoding/hex"
	"sort"
	"strings"
	"fmt"
	"os"
	"path/filepath"
)


var TEMPLATE = `---
created: %s
tags: %s
color: %s
---
%s`

type Note struct {
	Created string
	Tags    []string
	Color   string
	Content string
}

func generateColor(tags []string) string {
	hash := md5.Sum([]byte(tagsToString(tags)))
	return "#" + hex.EncodeToString(hash[:])[0:6]
}

func tagsToString(tags []string) string {
	return "||" + (string)(append([]byte(nil), []byte(tags[0])...))
}

func NewNote(created string, tags []string, content string) Note {
	sort.Strings(tags)
	return Note{
		Created: created,
		Tags:    tags,
		Color:   generateColor(tags),
		Content: content,
	}
}

func (note Note) GetName() string {
	return fmt.Sprintf("%s.md", note.Created)
}

func Colored(r, g, b int, text string) string {
	return fmt.Sprintf("\033[38;2;%d;%d;%dm%s\033[0m", r, g, b, text)
}

func Bold(text string) string {
	return fmt.Sprintf("\033[1m%s\033[0m", text)
}

func (note Note) String() string {
	
	name := note.GetName()
	name  = Colored(235, 171, 52, name)
	name  = Bold(name)
	
	content := note.Content
	content  = strings.ReplaceAll(content, "\n", " ")
	if len(content) > 27 {
		content = content[:27]
	}
	content = content + strings.Repeat(".", 30-len(content))
	content = Bold(content)

	tags := strings.Join(note.Tags, ", ")
	tags  = strings.ReplaceAll(tags, "[", "")
	tags  = strings.ReplaceAll(tags, "]", "")
	if len(tags) > 17 {
		tags = tags[:17]
	}
	tags = tags + strings.Repeat(".", 20-len(tags))
	tags = Colored(0, 168, 138, tags)

	return fmt.Sprintf("(%s): [🗞  %s] [🏷️  %s]", name, content, tags)
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