// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.21.12
// source: internal/proto/service.proto

package proto

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	Kowalski_Add_FullMethodName    = "/service.Kowalski/Add"
	Kowalski_Cook_FullMethodName   = "/service.Kowalski/Cook"
	Kowalski_Edit_FullMethodName   = "/service.Kowalski/Edit"
	Kowalski_Find_FullMethodName   = "/service.Kowalski/Find"
	Kowalski_List_FullMethodName   = "/service.Kowalski/List"
	Kowalski_Remove_FullMethodName = "/service.Kowalski/Remove"
	Kowalski_Save_FullMethodName   = "/service.Kowalski/Save"
)

// KowalskiClient is the client API for Kowalski service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type KowalskiClient interface {
	Add(ctx context.Context, in *AddRequest, opts ...grpc.CallOption) (*AddResponse, error)
	Cook(ctx context.Context, in *CookRequest, opts ...grpc.CallOption) (*CookResponse, error)
	Edit(ctx context.Context, in *EditRequest, opts ...grpc.CallOption) (*EditResponse, error)
	Find(ctx context.Context, in *FindRequest, opts ...grpc.CallOption) (*FindResponse, error)
	List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListResponse, error)
	Remove(ctx context.Context, in *RemoveRequest, opts ...grpc.CallOption) (*RemoveResponse, error)
	Save(ctx context.Context, in *SaveRequest, opts ...grpc.CallOption) (*SaveResponse, error)
}

type kowalskiClient struct {
	cc grpc.ClientConnInterface
}

func NewKowalskiClient(cc grpc.ClientConnInterface) KowalskiClient {
	return &kowalskiClient{cc}
}

func (c *kowalskiClient) Add(ctx context.Context, in *AddRequest, opts ...grpc.CallOption) (*AddResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(AddResponse)
	err := c.cc.Invoke(ctx, Kowalski_Add_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) Cook(ctx context.Context, in *CookRequest, opts ...grpc.CallOption) (*CookResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(CookResponse)
	err := c.cc.Invoke(ctx, Kowalski_Cook_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) Edit(ctx context.Context, in *EditRequest, opts ...grpc.CallOption) (*EditResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EditResponse)
	err := c.cc.Invoke(ctx, Kowalski_Edit_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) Find(ctx context.Context, in *FindRequest, opts ...grpc.CallOption) (*FindResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(FindResponse)
	err := c.cc.Invoke(ctx, Kowalski_Find_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListResponse)
	err := c.cc.Invoke(ctx, Kowalski_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) Remove(ctx context.Context, in *RemoveRequest, opts ...grpc.CallOption) (*RemoveResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(RemoveResponse)
	err := c.cc.Invoke(ctx, Kowalski_Remove_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *kowalskiClient) Save(ctx context.Context, in *SaveRequest, opts ...grpc.CallOption) (*SaveResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SaveResponse)
	err := c.cc.Invoke(ctx, Kowalski_Save_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// KowalskiServer is the server API for Kowalski service.
// All implementations must embed UnimplementedKowalskiServer
// for forward compatibility.
type KowalskiServer interface {
	Add(context.Context, *AddRequest) (*AddResponse, error)
	Cook(context.Context, *CookRequest) (*CookResponse, error)
	Edit(context.Context, *EditRequest) (*EditResponse, error)
	Find(context.Context, *FindRequest) (*FindResponse, error)
	List(context.Context, *ListRequest) (*ListResponse, error)
	Remove(context.Context, *RemoveRequest) (*RemoveResponse, error)
	Save(context.Context, *SaveRequest) (*SaveResponse, error)
	mustEmbedUnimplementedKowalskiServer()
}

// UnimplementedKowalskiServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedKowalskiServer struct{}

func (UnimplementedKowalskiServer) Add(context.Context, *AddRequest) (*AddResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Add not implemented")
}
func (UnimplementedKowalskiServer) Cook(context.Context, *CookRequest) (*CookResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Cook not implemented")
}
func (UnimplementedKowalskiServer) Edit(context.Context, *EditRequest) (*EditResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Edit not implemented")
}
func (UnimplementedKowalskiServer) Find(context.Context, *FindRequest) (*FindResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Find not implemented")
}
func (UnimplementedKowalskiServer) List(context.Context, *ListRequest) (*ListResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedKowalskiServer) Remove(context.Context, *RemoveRequest) (*RemoveResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Remove not implemented")
}
func (UnimplementedKowalskiServer) Save(context.Context, *SaveRequest) (*SaveResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Save not implemented")
}
func (UnimplementedKowalskiServer) mustEmbedUnimplementedKowalskiServer() {}
func (UnimplementedKowalskiServer) testEmbeddedByValue()                  {}

// UnsafeKowalskiServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to KowalskiServer will
// result in compilation errors.
type UnsafeKowalskiServer interface {
	mustEmbedUnimplementedKowalskiServer()
}

func RegisterKowalskiServer(s grpc.ServiceRegistrar, srv KowalskiServer) {
	// If the following call pancis, it indicates UnimplementedKowalskiServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Kowalski_ServiceDesc, srv)
}

func _Kowalski_Add_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Add(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Add_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Add(ctx, req.(*AddRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_Cook_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CookRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Cook(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Cook_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Cook(ctx, req.(*CookRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_Edit_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EditRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Edit(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Edit_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Edit(ctx, req.(*EditRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_Find_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FindRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Find(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Find_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Find(ctx, req.(*FindRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).List(ctx, req.(*ListRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_Remove_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemoveRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Remove(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Remove_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Remove(ctx, req.(*RemoveRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Kowalski_Save_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SaveRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KowalskiServer).Save(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Kowalski_Save_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KowalskiServer).Save(ctx, req.(*SaveRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Kowalski_ServiceDesc is the grpc.ServiceDesc for Kowalski service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Kowalski_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "service.Kowalski",
	HandlerType: (*KowalskiServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Add",
			Handler:    _Kowalski_Add_Handler,
		},
		{
			MethodName: "Cook",
			Handler:    _Kowalski_Cook_Handler,
		},
		{
			MethodName: "Edit",
			Handler:    _Kowalski_Edit_Handler,
		},
		{
			MethodName: "Find",
			Handler:    _Kowalski_Find_Handler,
		},
		{
			MethodName: "List",
			Handler:    _Kowalski_List_Handler,
		},
		{
			MethodName: "Remove",
			Handler:    _Kowalski_Remove_Handler,
		},
		{
			MethodName: "Save",
			Handler:    _Kowalski_Save_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "internal/proto/service.proto",
}
