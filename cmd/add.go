package cmd

import (
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski/pkg/add"
	//"github.com/Zatfer17/kowalski/pkg/edit"
)

var addCmd = &cobra.Command{
	Use:   "add [content]",
	Short: "Add a new note. Skipping the content will open the editor of choice.",
	Args:  cobra.MaximumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		tags, _ := cmd.Flags().GetStringArray("tag")

		content := ""
		if len(args) > 0 {
			content = args[0]
		}
		
		note, err := add.Add(content, tags)
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		//if len(args) == 0 {
			//Edit(note.Name)
		//}
		
		fmt.Println(note)
	},
}

func init() {
	addCmd.Flags().StringArray("tag", []string{}, "tags (separated by comma)")
}