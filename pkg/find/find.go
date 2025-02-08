package find

import (
	"fmt"
	"os/exec"
	"strings"
	"sort"
	"os"
	"github.com/Zatfer17/kowalski-core/internal/config"
	"github.com/Zatfer17/kowalski-core/internal/model"
	"github.com/Zatfer17/kowalski-core/internal/parser"
)

func Find(content string, descending bool) ([]model.Note, error){

	config, err := config.InitConfig()
	if err != nil {
		return nil, fmt.Errorf("error reading config file: %w", err)
	}

	cmd := exec.Command("grep", "-ril", content, "--include=*.md", config.NotesPath)
	output, err := cmd.Output()
	if err != nil {
		if exitError, ok := err.(*exec.ExitError); ok && exitError.ExitCode() == 1 {
			output = []byte{}
		} else {
			return nil, fmt.Errorf("error finding notes: %w", err)
		}
	}

	files := strings.FieldsFunc(string(output), func(r rune) bool { return r == '\n' })

	if descending {
		sort.Sort(sort.Reverse(sort.StringSlice(files)))
	} else {
		sort.Strings(files)
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