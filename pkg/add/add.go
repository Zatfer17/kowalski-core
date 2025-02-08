package add

import (
	"fmt"
	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func Add(created string, tags []string, content string) (model.Note, error) {

	config, err := config.InitConfig()
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading config file: %w", err)
	}

	n := model.Note{Created: created, Tags: tags, Content: content}
	
	if err := n.Write(config.NotesPath); err != nil {
		return model.Note{}, fmt.Errorf("error saving note: %w", err)
	}

	return n, nil
}