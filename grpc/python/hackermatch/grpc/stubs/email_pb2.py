"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bemail.proto"5\n\x15SendMatchAlertRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0e\n\x06emails\x18\x02 \x03(\t":\n\x16SendMatchAlertResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2S\n\x0cEmailService\x12C\n\x0eSendMatchAlert\x12\x16.SendMatchAlertRequest\x1a\x17.SendMatchAlertResponse"\x00b\x06proto3')
_SENDMATCHALERTREQUEST = DESCRIPTOR.message_types_by_name['SendMatchAlertRequest']
_SENDMATCHALERTRESPONSE = DESCRIPTOR.message_types_by_name['SendMatchAlertResponse']
SendMatchAlertRequest = _reflection.GeneratedProtocolMessageType('SendMatchAlertRequest', (_message.Message,), {'DESCRIPTOR': _SENDMATCHALERTREQUEST, '__module__': 'email_pb2'})
_sym_db.RegisterMessage(SendMatchAlertRequest)
SendMatchAlertResponse = _reflection.GeneratedProtocolMessageType('SendMatchAlertResponse', (_message.Message,), {'DESCRIPTOR': _SENDMATCHALERTRESPONSE, '__module__': 'email_pb2'})
_sym_db.RegisterMessage(SendMatchAlertResponse)
_EMAILSERVICE = DESCRIPTOR.services_by_name['EmailService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SENDMATCHALERTREQUEST._serialized_start = 15
    _SENDMATCHALERTREQUEST._serialized_end = 68
    _SENDMATCHALERTRESPONSE._serialized_start = 70
    _SENDMATCHALERTRESPONSE._serialized_end = 128
    _EMAILSERVICE._serialized_start = 130
    _EMAILSERVICE._serialized_end = 213