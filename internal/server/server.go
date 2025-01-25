package server

import (
	"context"
	"log"
	"fmt"
	"github.com/Zatfer17/kowalski-core/internal/service"
	"github.com/Zatfer17/kowalski-core/pkg/add"
	"github.com/Zatfer17/kowalski-core/pkg/list"
)

type Server struct {
	service.UnimplementedServiceServer
}

func (s *Server) Add(ctx context.Context, req *service.AddRequest) (*service.AddResponse, error) {

	note, err := add.Add(req.Content, req.Tags)
	if err != nil {
		message := fmt.Sprintf("Error adding the note: %v", err)
		log.Printf(message)
		return &service.AddResponse{
			Message: fmt.Sprintf(message),
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

func (s *Server) List(ctx context.Context, req *service.ListRequest) (*service.ListResponse, error) {

	limit := int(req.Limit)

	notes, err := list.List(limit)
	if err != nil {
		message := fmt.Sprintf("Error listing the notes: %v", err)
		log.Printf(message)
		return &service.ListResponse{
			Message: message,
			Notes: nil,
		}, err
	}

	var notes_payload []*service.Note
	for _, note := range notes {

		n := &service.Note{
			Name: note.Name,
			Created: note.Created,
			Updated: note.Updated,
			Tags: note.Tags,
			Content: note.Content,
		}

		notes_payload = append(notes_payload, n)
	}
	return &service.ListResponse{
		Message: "Note added successfully",
		Notes: notes_payload,
	}, nil
}
