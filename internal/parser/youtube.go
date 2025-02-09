package parser

import (
	"fmt"
	"encoding/json"
	"regexp"
	"strings"
	"html"

	"github.com/anaskhan96/soup"
)

var videoIDRegex = regexp.MustCompile(`(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})`)

func GetVideoID(url string) (string, error) {

	match := videoIDRegex.FindStringSubmatch(url)
	if len(match) > 1 {
		return match[1], nil
	}

	return "", fmt.Errorf("error extracting video ID")
}

func GetTranscript(videoID string) (string, error) {

	url := "https://www.youtube.com/watch?v=" + videoID

	resp, err := soup.Get(url)
	if err != nil {
		return "", err
	}

	doc := soup.HTMLParse(resp)
	scriptTags := doc.FindAll("script")

	for _, scriptTag := range scriptTags {

		if strings.Contains(scriptTag.Text(), "captionTracks") {

			regex := regexp.MustCompile(`"captionTracks":(\[.*?\])`)
			match := regex.FindStringSubmatch(scriptTag.Text())

			if len(match) > 1 {

				var captionTracks []struct {
					BaseURL string `json:"baseUrl"`
				}

				json.Unmarshal([]byte(match[1]), &captionTracks)

				if len(captionTracks) > 0 {

					transcriptURL := captionTracks[0].BaseURL
					transcriptResp, err := soup.Get(transcriptURL)
					if err != nil {
						return "", err
					}

					return transcriptResp, nil
				}
			}
		}
	}

	return "", fmt.Errorf("error fetching transcript")
}

func ParseTranscript(transcript string) (string, error) {

	doc := soup.HTMLParse(transcript)
	textTags := doc.FindAll("text")

	var textBuilder strings.Builder

	for _, textTag := range textTags {

		decodedText := html.UnescapeString(textTag.Text()) 
		textBuilder.WriteString(decodedText)
		textBuilder.WriteString(" ")

	}
	
	return textBuilder.String(), nil
}