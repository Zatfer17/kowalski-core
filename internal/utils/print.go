package utils

import (
	"crypto/md5"
	"encoding/hex"
	"strings"
	"strconv"
	"fmt"
)

func GenerateColor(tags []string) string {
    hash := md5.Sum([]byte(tagsToString(tags)))
    return hex.EncodeToString(hash[:])[:6]
}

func tagsToString(tags []string) string {
    return "||" + strings.Join(tags, "||")
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

