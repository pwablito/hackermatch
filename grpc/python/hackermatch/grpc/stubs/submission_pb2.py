"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10submission.proto"3\n\x14AddSubmissionRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t"9\n\x15AddSubmissionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t"!\n\x11GetMatchesRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t"F\n\x12GetMatchesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06emails\x18\x03 \x03(\t2\x8e\x01\n\x11SubmissionService\x12@\n\rAddSubmission\x12\x15.AddSubmissionRequest\x1a\x16.AddSubmissionResponse"\x00\x127\n\nGetMatches\x12\x12.GetMatchesRequest\x1a\x13.GetMatchesResponse"\x00b\x06proto3')
_ADDSUBMISSIONREQUEST = DESCRIPTOR.message_types_by_name['AddSubmissionRequest']
_ADDSUBMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['AddSubmissionResponse']
_GETMATCHESREQUEST = DESCRIPTOR.message_types_by_name['GetMatchesRequest']
_GETMATCHESRESPONSE = DESCRIPTOR.message_types_by_name['GetMatchesResponse']
AddSubmissionRequest = _reflection.GeneratedProtocolMessageType('AddSubmissionRequest', (_message.Message,), {'DESCRIPTOR': _ADDSUBMISSIONREQUEST, '__module__': 'submission_pb2'})
_sym_db.RegisterMessage(AddSubmissionRequest)
AddSubmissionResponse = _reflection.GeneratedProtocolMessageType('AddSubmissionResponse', (_message.Message,), {'DESCRIPTOR': _ADDSUBMISSIONRESPONSE, '__module__': 'submission_pb2'})
_sym_db.RegisterMessage(AddSubmissionResponse)
GetMatchesRequest = _reflection.GeneratedProtocolMessageType('GetMatchesRequest', (_message.Message,), {'DESCRIPTOR': _GETMATCHESREQUEST, '__module__': 'submission_pb2'})
_sym_db.RegisterMessage(GetMatchesRequest)
GetMatchesResponse = _reflection.GeneratedProtocolMessageType('GetMatchesResponse', (_message.Message,), {'DESCRIPTOR': _GETMATCHESRESPONSE, '__module__': 'submission_pb2'})
_sym_db.RegisterMessage(GetMatchesResponse)
_SUBMISSIONSERVICE = DESCRIPTOR.services_by_name['SubmissionService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ADDSUBMISSIONREQUEST._serialized_start = 20
    _ADDSUBMISSIONREQUEST._serialized_end = 71
    _ADDSUBMISSIONRESPONSE._serialized_start = 73
    _ADDSUBMISSIONRESPONSE._serialized_end = 130
    _GETMATCHESREQUEST._serialized_start = 132
    _GETMATCHESREQUEST._serialized_end = 165
    _GETMATCHESRESPONSE._serialized_start = 167
    _GETMATCHESRESPONSE._serialized_end = 237
    _SUBMISSIONSERVICE._serialized_start = 240
    _SUBMISSIONSERVICE._serialized_end = 382