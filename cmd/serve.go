package cmd

import (
	"fmt"
	"log"
	"net"

	"github.com/spf13/cobra"
	"google.golang.org/grpc"
	pb "github.com/Zatfer17/kowalski-core/internal/proto"
	"github.com/Zatfer17/kowalski-core/internal/server"
)

var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Start kowalski in server mode.",
	Run: func(cmd *cobra.Command, args []string) {
		lis, err := net.Listen("tcp", "0.0.0.0:50051")
		if err != nil {
			log.Fatalf("Failed to listen: %v", err)
		}

		s := grpc.NewServer()
		pb.RegisterKowalskiServer(s, &service.Server{})

		fmt.Println("gRPC server listening on port 50051...")
		if err := s.Serve(lis); err != nil {
			log.Fatalf("Failed to serve: %v", err)
		}
	},
}

func init() {
}