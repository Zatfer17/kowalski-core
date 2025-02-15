package utils

import (
	"crypto/md5"
	"strconv"
	"fmt"
)

var palette = []string{
	"e6194B",
	"3cb44b",
	"ffe119",
	"4363d8",
	"f58231",
	"911eb4",
	"42d4f4",
	"f032e6",
	"bfef45",
	"fabed4",
	"469990",
	"dcbeff",
	"9A6324",
	"fffac8", 
	"800000",
	"aaffc3",
	"808000",
	"ffd8b1",
	"000075",
	"a9a9a9",
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

