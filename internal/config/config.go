package config

import (
	"os"
	"path/filepath"
	"fmt"
	"github.com/spf13/viper"
)

type Config struct {
	Editor    string
	NotesPath string
}

func InitConfig() (*Config, error) {

	homePath := os.Getenv("HOME")
	configPath := filepath.Join(homePath, ".config/kowalski/config.yaml")
	viper.SetConfigFile(configPath)

	if err := viper.ReadInConfig(); err != nil {
		return nil, err
	}

	if !viper.IsSet("notesPath") {
		return nil, fmt.Errorf("config key 'notesPath' is not set in the configuration file")
	}

	if !viper.IsSet("editor") {
		return nil, fmt.Errorf("config key 'editor' is not set in the configuration file")
	}

	config := &Config{
		Editor:    viper.GetString("editor"),
		NotesPath: viper.GetString("notesPath"),
	}

	return config, nil
}
