package cmd

import (
	"net"
	"log"
	"fmt"
	"github.com/spf13/cobra"
	"google.golang.org/grpc"
	"github.com/Zatfer17/kowalski/internal/service"
	"github.com/Zatfer17/kowalski/internal/server"
)

var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Start kowalski in server mode.",
	Run: func(cmd *cobra.Command, args []string) {

		lis, err := net.Listen("tcp", ":50051")
		if err != nil {
			log.Fatalf("Failed to listen: %v", err)
		}

		s := grpc.NewServer()
		service.RegisterServiceServer(s, &server.Server{})

		fmt.Println("gRPC server listening on port 50051...")
		if err := s.Serve(lis); err != nil {
			log.Fatalf("Failed to serve: %v", err)
		}
	},
}

func init() {
}