package add

import (
	"fmt"
	"time"
	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func Add(content string, tags []string) (model.Note, error) {

	config, err := config.InitConfig()
	if err != nil {
		return model.Note{}, fmt.Errorf("error reading config file: %w", err)
	}

	created := time.Now().Local().Truncate(time.Second).Format(time.RFC3339)
	name := fmt.Sprintf("%s.md", created)
	var updated string

	n := model.Note{Name: name, Created: created, Updated: updated, Tags: tags, Content: content}

	if err := n.Write(config.NotesPath); err != nil {
		return model.Note{}, fmt.Errorf("error saving note: %w", err)
	}

	return n, nil
}