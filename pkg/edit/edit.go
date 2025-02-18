package edit

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/parser"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func Open(name string) (error){

	config, err := config.InitConfig()
	if err != nil {
		return fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	if _, err := os.Stat(filePath); err != nil {
		return fmt.Errorf("error reading file: %w", err)
	}
	
	cmd := exec.Command(config.Editor, filePath)
	if _, err := cmd.Output(); err != nil {
		return fmt.Errorf("error executing command: %w", err)
	}

	return nil
}

func UpdateTags(name string, tags []string) (model.Note, error) {

	var err error

	config, err := config.InitConfig()
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(fileContent))
	if err != nil {
		return model.Note{}, fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	if tags != nil {
		note.Tags = tags
		err = note.Write(config.NotesPath)
		if err != nil {
			return model.Note{}, fmt.Errorf("error writing note %s: %w", filePath, err)
		}
	}

	return note, nil
}

func UpdateContent(name string, content string) (model.Note, error) {

	var err error

	config, err := config.InitConfig()
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(fileContent))
	if err != nil {
		return model.Note{}, fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	if content != "" {
		note.Content = content
		err = note.Write(config.NotesPath)
		if err != nil {
			return model.Note{}, fmt.Errorf("error writing note %s: %w", filePath, err)
		}
	}

	return note, nil
}