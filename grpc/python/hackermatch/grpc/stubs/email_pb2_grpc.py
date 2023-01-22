"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import email_pb2 as email__pb2

class EmailServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMatchAlert = channel.unary_unary('/EmailService/SendMatchAlert', request_serializer=email__pb2.SendMatchAlertRequest.SerializeToString, response_deserializer=email__pb2.SendMatchAlertResponse.FromString)

class EmailServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMatchAlert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EmailServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'SendMatchAlert': grpc.unary_unary_rpc_method_handler(servicer.SendMatchAlert, request_deserializer=email__pb2.SendMatchAlertRequest.FromString, response_serializer=email__pb2.SendMatchAlertResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('EmailService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class EmailService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMatchAlert(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EmailService/SendMatchAlert', email__pb2.SendMatchAlertRequest.SerializeToString, email__pb2.SendMatchAlertResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)