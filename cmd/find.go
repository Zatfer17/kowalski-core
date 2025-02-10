package cmd

import (
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/find"
)

var findCmd = &cobra.Command{
	Use: "find [content]",
	Short: "Find a note.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		descending, err := cmd.Flags().GetBool("descending")
		if err != nil {
			log.Fatalf("Parse error: %v", err)
		}

		notes, err := find.Find(args[0], descending)
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		for _, note := range notes {
			fmt.Println(note)
		}

	},
}

func init() {
	findCmd.Flags().Bool("descending", false, "Sort the notes in descending order.")
}