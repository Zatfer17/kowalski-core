package cmd

import (
	"log"
	"fmt"

	"github.com/Zatfer17/kowalski-core/pkg/cook"
	"github.com/spf13/cobra"
)

var cookCmd = &cobra.Command{
	Use: "cook [name]",
	Short: "Cook a note with AI.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		prompt, err := cmd.Flags().GetString("prompt")
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		if prompt == "" {
			log.Fatalf("Error: prompt is required")
		}

		note, err := cook.Cook(args[0], prompt)
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		fmt.Println(note)

	},
}

func init() {
	cookCmd.Flags().String("prompt", "", "prompt for the completion")
}