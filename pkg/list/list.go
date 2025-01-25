package list

import (
	"fmt"
	"path/filepath"
	"sort"
	"os"
	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/model"
	"github.com/Zatfer17/kowalski-core/internal/parser"
)

func List(limit int) ([]model.Note, error) {

	config, err := config.InitConfig()
	if err != nil {
		return nil, fmt.Errorf("error reading config file: %w", err)
	}

	pattern := filepath.Join(config.NotesPath, "*.md")
	files, err := filepath.Glob(pattern)
	if err != nil {
		return nil, fmt.Errorf("error listing notes: %w", err)
	}

	sort.Strings(files)

	if limit > 0 && limit < len(files) {
		files = files[len(files)-limit:]
	}

	var notes []model.Note
	for _, file := range files {
		content, err := os.ReadFile(file)
		if err != nil {
			return nil, fmt.Errorf("error reading file %s: %w", file, err)
		}

		note, err := parser.ParseNote(string(content))
		if err != nil {
			return nil, fmt.Errorf("error parsing note %s: %w", file, err)
		}

		notes = append(notes, note)
	}

	return notes, nil

}