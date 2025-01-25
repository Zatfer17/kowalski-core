package server

import (
	"context"
	"log"
	"fmt"
	"github.com/Zatfer17/kowalski-core/internal/service"
	"github.com/Zatfer17/kowalski-core/pkg/add"
)

type Server struct {
	service.UnimplementedServiceServer
}

func (s *Server) Add(ctx context.Context, req *service.AddRequest) (*service.AddResponse, error) {

	note, err := add.Add(req.Content, req.Tags)
	if err != nil {
		log.Printf("Error adding the note: %v", err)
		return &service.AddResponse{
			Message: fmt.Sprintf("Error adding the note: %v", err),
			Note: &service.Note{},
		}, err
	}

	return &service.AddResponse{
		Message: "Note added successfully",
		Note: &service.Note{
			Name: note.Name,
			Created: note.Created,
			Updated: note.Updated,
			Tags: note.Tags,
			Content: note.Content,
		},
	}, nil
}
