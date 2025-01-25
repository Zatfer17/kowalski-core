package parser

import (
	"strings"
	"fmt"
	"github.com/adrg/frontmatter"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func ParseNote(content string) (model.Note, error) {

	var matter struct {
		Name    string `yaml:"name"`
		Created string `yaml:"created"`
		Updated string `yaml:"updated"`
		Tags    []string `yaml:"tags"`
	}

	rest, err := frontmatter.MustParse(strings.NewReader(content), &matter)
	if err != nil {
		return model.Note{}, fmt.Errorf("invalid note format")
	}

	return model.Note{
		Name: matter.Name,
		Created: matter.Created,
		Updated: matter.Updated,
		Tags: matter.Tags,
		Content: string(rest),
	}, nil
}