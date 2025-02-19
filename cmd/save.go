package cmd

import (
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"github.com/Zatfer17/kowalski-core/pkg/save"
)

var saveCmd = &cobra.Command{
	Use: "save [link]",
	Short: "Save a link.",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {

		tags, err := cmd.Flags().GetStringSlice("tag")
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		note, err := save.Save(tags, args[0])
		if err != nil {
			log.Fatalf("Error: %v", err)
		}

		fmt.Println(note)
	},
}

func init() {
	saveCmd.Flags().StringSlice("tag", []string{}, "tags (separated by comma)")
}