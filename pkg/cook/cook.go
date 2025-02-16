package cook

import (
	"context"
	"fmt"
	"os"
	"path/filepath"

	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/model"
	"github.com/Zatfer17/kowalski-core/internal/llm"
	"github.com/Zatfer17/kowalski-core/internal/parser"
)

func Cook(name string, prompt string) (model.Note, error) {
	
	var err error

	config, err := config.InitConfig()
	if err != nil {
		return model.Note{},fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return model.Note{},fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(fileContent))
	if err != nil {
		return model.Note{},fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	client := llm.NewClient(config.Model, config.ApiKey)

	ctx := context.Background()
	completion, err := client.Completion(ctx, note.Content, prompt)
	if err != nil {
		return model.Note{},fmt.Errorf("error transforming: %w", err)
	}

	note.Content = completion
	err = note.Write(config.NotesPath)
	if err != nil {
		return model.Note{},fmt.Errorf("error writing note %s: %w", filePath, err)
	}

	return note, nil

}