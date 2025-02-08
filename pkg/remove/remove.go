package remove

import (
	"fmt"
	"path/filepath"
	"os"
	"github.com/Zatfer17/kowalski-core/internal/config"
)

func Remove(name string) error {
	
	config, err := config.InitConfig()
	if err != nil {
		return fmt.Errorf("error reading config file: %w", err)
	}

	filePath := filepath.Join(config.NotesPath, name)
	if _, err := os.Stat(filePath); err != nil {
		return fmt.Errorf("error reading file: %w", err)
	}

	if err := os.Remove(filePath); err != nil {
		return fmt.Errorf("error removing file: %w", err)
	}

	return nil
}