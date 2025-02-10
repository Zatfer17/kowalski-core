package cmd

import (
	"log"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/show"
)

var showCmd = &cobra.Command{
	Use: "show [name]",
	Short: "Show a note.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		err := show.Show(args[0])
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

	},
}

func init() {
}