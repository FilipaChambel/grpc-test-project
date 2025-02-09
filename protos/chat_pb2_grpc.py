# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import chat_pb2 as chat__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in chat_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/chat.ChatService/Login',
                request_serializer=chat__pb2.LoginRequest.SerializeToString,
                response_deserializer=chat__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.Logout = channel.unary_unary(
                '/chat.ChatService/Logout',
                request_serializer=chat__pb2.LogoutRequest.SerializeToString,
                response_deserializer=chat__pb2.LogoutResponse.FromString,
                _registered_method=True)
        self.SendPrivateMessage = channel.unary_unary(
                '/chat.ChatService/SendPrivateMessage',
                request_serializer=chat__pb2.PrivateMessageRequest.SerializeToString,
                response_deserializer=chat__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.SendGroupMessage = channel.unary_unary(
                '/chat.ChatService/SendGroupMessage',
                request_serializer=chat__pb2.GroupMessageRequest.SerializeToString,
                response_deserializer=chat__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.StreamMessages = channel.unary_stream(
                '/chat.ChatService/StreamMessages',
                request_serializer=chat__pb2.StreamRequest.SerializeToString,
                response_deserializer=chat__pb2.ChatMessage.FromString,
                _registered_method=True)
        self.GetOnlineUsers = channel.unary_unary(
                '/chat.ChatService/GetOnlineUsers',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.OnlineUsersResponse.FromString,
                _registered_method=True)
        self.UpdatePresence = channel.unary_unary(
                '/chat.ChatService/UpdatePresence',
                request_serializer=chat__pb2.PresenceRequest.SerializeToString,
                response_deserializer=chat__pb2.PresenceResponse.FromString,
                _registered_method=True)


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """User authentication
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPrivateMessage(self, request, context):
        """Send a private message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendGroupMessage(self, request, context):
        """Send a group message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMessages(self, request, context):
        """Stream messages in real-time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnlineUsers(self, request, context):
        """Get online users
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePresence(self, request, context):
        """Update presence status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=chat__pb2.LoginRequest.FromString,
                    response_serializer=chat__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=chat__pb2.LogoutRequest.FromString,
                    response_serializer=chat__pb2.LogoutResponse.SerializeToString,
            ),
            'SendPrivateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPrivateMessage,
                    request_deserializer=chat__pb2.PrivateMessageRequest.FromString,
                    response_serializer=chat__pb2.MessageResponse.SerializeToString,
            ),
            'SendGroupMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendGroupMessage,
                    request_deserializer=chat__pb2.GroupMessageRequest.FromString,
                    response_serializer=chat__pb2.MessageResponse.SerializeToString,
            ),
            'StreamMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMessages,
                    request_deserializer=chat__pb2.StreamRequest.FromString,
                    response_serializer=chat__pb2.ChatMessage.SerializeToString,
            ),
            'GetOnlineUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOnlineUsers,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.OnlineUsersResponse.SerializeToString,
            ),
            'UpdatePresence': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePresence,
                    request_deserializer=chat__pb2.PresenceRequest.FromString,
                    response_serializer=chat__pb2.PresenceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('chat.ChatService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/Login',
            chat__pb2.LoginRequest.SerializeToString,
            chat__pb2.LoginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/Logout',
            chat__pb2.LogoutRequest.SerializeToString,
            chat__pb2.LogoutResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendPrivateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/SendPrivateMessage',
            chat__pb2.PrivateMessageRequest.SerializeToString,
            chat__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendGroupMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/SendGroupMessage',
            chat__pb2.GroupMessageRequest.SerializeToString,
            chat__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/chat.ChatService/StreamMessages',
            chat__pb2.StreamRequest.SerializeToString,
            chat__pb2.ChatMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOnlineUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/GetOnlineUsers',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.OnlineUsersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdatePresence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/chat.ChatService/UpdatePresence',
            chat__pb2.PresenceRequest.SerializeToString,
            chat__pb2.PresenceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
