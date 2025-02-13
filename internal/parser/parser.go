package parser

import (
	"strings"
	"fmt"
	"regexp"
	"github.com/adrg/frontmatter"
	"github.com/go-shiori/go-readability"
	"net/http"
	"net/url"
	"github.com/Zatfer17/kowalski-core/internal/model"
)

func ParseNote(content string) (model.Note, error) {

	var matter struct {
		Created string `yaml:"created"`
		Tags    []string `yaml:"tags"`
	}

	rest, err := frontmatter.MustParse(strings.NewReader(content), &matter)
	if err != nil {
		return model.Note{}, fmt.Errorf("invalid note format")
	}

	return model.NewNote(matter.Created, matter.Tags, string(rest)), nil
}

var (
	ytRegex  = regexp.MustCompile(`^(?:https?:)?(?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\_-]{7,15})(?:[\?&][a-zA-Z0-9\_-]+=[a-zA-Z0-9\_-]+)*(?:[&\/\#].*)?$`)
	httpRegex = regexp.MustCompile(`^(?:https?:\/\/)?[\w.-]+\.[a-zA-Z]{2,}`)
)

func ParseLink(link string) (string, error) {

	if !strings.HasPrefix(link, "http://") && !strings.HasPrefix(link, "https://") {
		link = "https://" + link
	}

	if ytRegex.MatchString(link) {

		videoId, err := GetVideoID(link)
		if err != nil {
			fmt.Println("Error getting video id")
			return "", err
		}

		transcript, err := GetTranscript(videoId)
		if err != nil {
			fmt.Println("Error fetching transcript")
			return "", err
		}

		transcript, err = ParseTranscript(transcript)
		if err != nil {
			fmt.Println("Error parsing transcript")
			return "", err
		}

		return transcript, nil

	} else if httpRegex.MatchString(link) {

		resp, err := http.Get(link)
		if err != nil {
			return "", err
		}
		defer resp.Body.Close()

		parsedURL, err := url.Parse(link)
		if err != nil {
			return "", fmt.Errorf("error parsing url: %w", err)
		}

		doc, err := readability.FromReader(resp.Body, parsedURL)
		if err != nil {
			return "", err
		}
		return doc.TextContent, nil
	}

	return "", fmt.Errorf("link not supported")
}