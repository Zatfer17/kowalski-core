package edit

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/parser"
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

func UpdateTags(name string, tags []string) (error) {

	var err error

	config, err := config.InitConfig()
	if err != nil {
		return fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(fileContent))
	if err != nil {
		return fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	if tags != nil {
		note.Tags = tags
		note.Write(config.NotesPath)
	}

	return nil
}

func UpdateContent(name string, content string) (error) {

	var err error

	config, err := config.InitConfig()
	if err != nil {
		return fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(fileContent))
	if err != nil {
		return fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	if content != "" {
		note.Content = content
		note.Write(config.NotesPath)
	}

	return nil
}