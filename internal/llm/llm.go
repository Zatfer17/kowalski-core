package llm

import (
    "bytes"
    "context"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
)

type Client struct {
    apiKey   string
    baseURL  string
    model    string
}

type Message struct {
    Role    string `json:"role"`
    Content string `json:"content"`
}

type CompletionRequest struct {
    Model    string    `json:"model"`
    Messages []Message `json:"messages"`
}

type Choice struct {
    Message struct {
        Content string `json:"content"`
    } `json:"message"`
}

type CompletionResponse struct {
    Choices []Choice `json:"choices"`
}

func NewClient(model string, apiKey string) *Client {
    return &Client{
        apiKey:   apiKey,
        baseURL:  "https://openrouter.ai/api/v1",
        model:    model,
    }
}

func (c *Client) Completion(ctx context.Context, prompt string, content string) (string, error) {
    reqBody := CompletionRequest{
        Model: c.model,
        Messages: []Message{
			{
				Role:    "system",
				Content: prompt,
			},
            {
                Role:    "user",
                Content: content,
            },
        },
    }

    jsonData, err := json.Marshal(reqBody)
    if err != nil {
        return "", fmt.Errorf("error marshaling request: %w", err)
    }

    req, err := http.NewRequestWithContext(ctx, "POST", c.baseURL+"/chat/completions", bytes.NewBuffer(jsonData))
    if err != nil {
        return "", fmt.Errorf("error creating request: %w", err)
    }

    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("Authorization", "Bearer "+c.apiKey)

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return "", fmt.Errorf("error making request: %w", err)
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return "", fmt.Errorf("error reading response: %w", err)
    }

    if resp.StatusCode != http.StatusOK {
        return "", fmt.Errorf("API request failed with status %d: %s", resp.StatusCode, string(body))
    }

    var completion CompletionResponse
    if err := json.Unmarshal(body, &completion); err != nil {
        return "", fmt.Errorf("error unmarshaling response: %w", err)
    }

    if len(completion.Choices) == 0 {
        return "", fmt.Errorf("no completion choices returned")
    }

    return completion.Choices[0].Message.Content, nil
}