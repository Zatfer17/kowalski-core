package service

import (
	"context"
	"fmt"

	pb "github.com/Zatfer17/kowalski-core/internal/proto"
	"github.com/Zatfer17/kowalski-core/pkg/add"
	"github.com/Zatfer17/kowalski-core/pkg/edit"
	"github.com/Zatfer17/kowalski-core/pkg/list"
	"github.com/Zatfer17/kowalski-core/pkg/save"
)

type Server struct {
	pb.UnimplementedKowalskiServer
}

func (s *Server) Add(ctx context.Context, req *pb.AddRequest) (*pb.AddResponse, error) {

	fmt.Printf("AddRequest received: tags=%v, content=%s\n", req.Tags, req.Content)

	_, err := add.Add(req.Tags, req.Content)
	if err != nil {
		return &pb.AddResponse{}, err
	}

	return &pb.AddResponse{}, nil
}

func (s *Server) Edit(ctx context.Context, req *pb.EditRequest) (*pb.EditResponse, error) {

	fmt.Printf("EditRequest received: name=%s, tags=%v, content=%s\n", req.Name, req.Tags, req.Content)

	if req.Tags != nil {
		err := edit.UpdateTags(req.Name, req.Tags)
		if err != nil {
			return &pb.EditResponse{}, err
		}
	}

	if req.Content != "" {
		err := edit.UpdateContent(req.Name, req.Content)
		if err != nil {
			return &pb.EditResponse{}, err
		}
	}

	return &pb.EditResponse{}, nil
}

func (s *Server) List(ctx context.Context, req *pb.ListRequest) (*pb.ListResponse, error) {

	fmt.Printf("ListRequest received: limit=%d, descending=%v\n", req.Limit, req.Descending)

	notes, err := list.List(int(req.Limit), req.Descending)
	if err != nil {
		return &pb.ListResponse{}, err
	}

	var pbNotes []*pb.Note
	for _, n := range notes {
		pbNotes = append(pbNotes, &pb.Note{
			Created: n.Created,
			Tags:    n.Tags,
			Content: n.Content,
		})
	}

	return &pb.ListResponse{Notes: pbNotes}, nil
}

func (s *Server) Save(ctx context.Context, req *pb.SaveRequest) (*pb.SaveResponse, error) {

	fmt.Printf("SaveRequest received: tags=%v, content=%s\n", req.Tags, req.Content)

	_, err := save.Save(req.Tags, req.Content)
	if err != nil {
		return &pb.SaveResponse{}, err
	}

	return &pb.SaveResponse{}, nil
}