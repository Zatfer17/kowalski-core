package cmd

import (
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/add"
	"github.com/Zatfer17/kowalski-core/pkg/edit"
)

var addCmd = &cobra.Command{
	Use:   "add [content]",
	Short: "Add a new note. Skipping the content will open the editor of choice.",
	Args:  cobra.MaximumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		tags, err := cmd.Flags().GetStringArray("tag")
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		var content string;
		if len(args) > 0 {
			content = args[0]
		}
		
		note, err := add.Add(tags, content)
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		if len(args) == 0 {
			err := edit.Open(note.GetName())
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
		} else {
			fmt.Println(note)
		}
	},
}

func init() {
	addCmd.Flags().StringArray("tag", []string{}, "tags (separated by comma)")
}