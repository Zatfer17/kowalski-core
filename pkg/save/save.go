package save

import (
	"fmt"
	"github.com/Zatfer17/kowalski-core/internal/model"
	"github.com/Zatfer17/kowalski-core/internal/parser"
	"github.com/Zatfer17/kowalski-core/pkg/add"
)

func Save(tags []string, content string) (model.Note, error) {

	content, err := parser.ParseLink(content)
	if err != nil {
		return model.Note{}, fmt.Errorf("error parsing link: %w", err)
	}

	note, err := add.Add(tags, content)
	if err != nil {
		return model.Note{}, fmt.Errorf("error saving note: %w", err)
	}

	return note, nil
}