package cmd

import (
	"log"

	"github.com/Zatfer17/kowalski-core/pkg/edit"
	"github.com/spf13/cobra"
)

var editCmd = &cobra.Command{
	Use: "edit [name]",
	Short: "Edit a note. Skipping the content will open the editor of choice.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		contentFlag := cmd.Flags().Lookup("content")
		if contentFlag != nil && contentFlag.Changed {

			content, err := cmd.Flags().GetString("content")
			if err != nil {
				log.Fatalf("Error: %v", err)
			}

			_, err = edit.UpdateContent(args[0], content)
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
			
		}

		tagFlag := cmd.Flags().Lookup("tag")
		if tagFlag != nil && tagFlag.Changed {
		
			tags, err := cmd.Flags().GetStringSlice("tag")
			if err != nil {
				log.Fatalf("Error: %v", err)
			}

			_, err = edit.UpdateTags(args[0], tags)
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
		}

		if !(contentFlag != nil && contentFlag.Changed) && !(tagFlag != nil && tagFlag.Changed) {
			err := edit.Open(args[0])
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
		}

	},
}

func init() {
	editCmd.Flags().String("content", "", "new content")
	editCmd.Flags().StringSlice("tag", []string{}, "new tags (separated by comma)")
}