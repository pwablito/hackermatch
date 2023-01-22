"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import submission_pb2 as submission__pb2

class SubmissionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSubmission = channel.unary_unary('/SubmissionService/AddSubmission', request_serializer=submission__pb2.AddSubmissionRequest.SerializeToString, response_deserializer=submission__pb2.AddSubmissionResponse.FromString)
        self.GetMatches = channel.unary_unary('/SubmissionService/GetMatches', request_serializer=submission__pb2.GetMatchesRequest.SerializeToString, response_deserializer=submission__pb2.GetMatchesResponse.FromString)

class SubmissionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddSubmission(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMatches(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SubmissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddSubmission': grpc.unary_unary_rpc_method_handler(servicer.AddSubmission, request_deserializer=submission__pb2.AddSubmissionRequest.FromString, response_serializer=submission__pb2.AddSubmissionResponse.SerializeToString), 'GetMatches': grpc.unary_unary_rpc_method_handler(servicer.GetMatches, request_deserializer=submission__pb2.GetMatchesRequest.FromString, response_serializer=submission__pb2.GetMatchesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('SubmissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SubmissionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddSubmission(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubmissionService/AddSubmission', submission__pb2.AddSubmissionRequest.SerializeToString, submission__pb2.AddSubmissionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMatches(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SubmissionService/GetMatches', submission__pb2.GetMatchesRequest.SerializeToString, submission__pb2.GetMatchesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)