package utils

import (
	"crypto/md5"
	"strconv"
	"fmt"
	"path/filepath"
	"os"
	"log"
	"encoding/csv"
	"strings"
)

var palette []string

func init() {
    csvPath := filepath.Join("internal", "utils", "palette.csv")
    file, err := os.Open(csvPath)
    if err != nil {
        log.Fatalf("Failed to open palette file: %v", err)
    }
    defer file.Close()

    reader := csv.NewReader(file)
    records, err := reader.ReadAll()
    if err != nil {
        log.Fatalf("Failed to read palette data: %v", err)
    }

    if len(records) == 0 {
        log.Fatalf("Palette file is empty")
    }

    palette = make([]string, 0, len(records))
    for i, record := range records {
        if len(record) == 0 || record[0] == "" {
            log.Fatalf("Empty color code at line %d", i+1)
        }
        color := strings.TrimPrefix(record[0], "#")
        color = strings.TrimSuffix(color, ",")
        
        if len(color) != 6 {
            log.Fatalf("Invalid color code at line %d: %s", i+1, record[0])
        }
        palette = append(palette, color)
    }
}

func GenerateColor(tags []string) string {
    if len(tags) == 0 {
        return "000000"
    }
    
    firstTag := tags[0]
    hash := md5.Sum([]byte(firstTag))
    index := int(hash[0]) % len(palette)
    return palette[index]
}

func ColoredSquare(color string) string {
	r, _ := strconv.ParseInt(color[0:2], 16, 64)
	g, _ := strconv.ParseInt(color[2:4], 16, 64)
	b, _ := strconv.ParseInt(color[4:6], 16, 64)
	return fmt.Sprintf("\033[48:2::%d:%d:%dm \033[49m", r, g, b)
}

func Colored(r, g, b int, text string) string {
	return fmt.Sprintf("\033[38;2;%d;%d;%dm%s\033[0m", r, g, b, text)
}

func Bold(text string) string {
	return fmt.Sprintf("\033[1m%s\033[0m", text)
}

