package cmd

import (
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/list"
)

var listCmd = &cobra.Command{
	Use: "list [limit]",
	Short: "List the notes. Skipping the limit will list all the notes.",
	Run: func(cmd *cobra.Command, args []string) {

		limit, err := cmd.Flags().GetInt("limit")
		if err != nil {
			log.Fatalf("Parse error: %v", err)
		}

		descending, err := cmd.Flags().GetBool("descending")
		if err != nil {
			log.Fatalf("Parse error: %v", err)
		}

		notes, err := list.List(limit, descending)
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		for _, note := range notes {
			fmt.Println(note)
		}
	},
}

func init() {
	listCmd.Flags().Int("limit", 0, "The number of notes to list.")
	listCmd.Flags().Bool("descending", false, "Sort the notes in descending order.")
}