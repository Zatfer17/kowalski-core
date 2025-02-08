package parser

import (
	"strings"
	"fmt"
	"github.com/adrg/frontmatter"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func ParseNote(content string) (model.Note, error) {

	var matter struct {
		Created string `yaml:"created"`
		Tags    []string `yaml:"tags"`
	}

	rest, err := frontmatter.MustParse(strings.NewReader(content), &matter)
	if err != nil {
		return model.Note{}, fmt.Errorf("invalid note format")
	}

	return model.Note{
		Created: matter.Created,
		Tags: matter.Tags,
		Content: string(rest),
	}, nil
}