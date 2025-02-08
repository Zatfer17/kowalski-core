package show

import (
	"fmt"
	"path/filepath"
	"os"
	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/parser"
)

func Show(name string) error {
	
	config, err := config.InitConfig()
	if err != nil {
		return fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	if _, err := os.Stat(filePath); err != nil {
		return fmt.Errorf("error reading file: %w", err)
	}

	content, err := os.ReadFile(filePath)
	if err != nil {
		return fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	note, err := parser.ParseNote(string(content))
	if err != nil {
		return fmt.Errorf("error parsing note %s: %w", filePath, err)
	}

	fmt.Println(note.Format())

	return nil
}