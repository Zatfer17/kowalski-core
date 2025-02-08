package cmd

import (
	"log"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/remove"
)

var removeCmd = &cobra.Command{
	Use:   "remove [name]",
	Short: "Remove a note.",
	Args:  cobra.MaximumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		err := remove.Remove(args[0])
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

	},
}

func init() {
}