# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_twofactor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_twofactor.proto',
  package='',
  serialized_pb=_b('\n\x1dsteammessages_twofactor.proto\",\n\x19\x43TwoFactor_Status_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"\xbc\x02\n\x1a\x43TwoFactor_Status_Response\x12\r\n\x05state\x18\x01 \x01(\r\x12\x1b\n\x13inactivation_reason\x18\x02 \x01(\r\x12\x1a\n\x12\x61uthenticator_type\x18\x03 \x01(\r\x12\x1d\n\x15\x61uthenticator_allowed\x18\x04 \x01(\x08\x12\x19\n\x11steamguard_scheme\x18\x05 \x01(\r\x12\x11\n\ttoken_gid\x18\x06 \x01(\t\x12\x17\n\x0f\x65mail_validated\x18\x07 \x01(\x08\x12\x19\n\x11\x64\x65vice_identifier\x18\x08 \x01(\t\x12\x14\n\x0ctime_created\x18\t \x01(\r\x12%\n\x1drevocation_attempts_remaining\x18\n \x01(\r\x12\x18\n\x10\x63lassified_agent\x18\x0b \x01(\t\"\xcc\x01\n#CTwoFactor_AddAuthenticator_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x1a\n\x12\x61uthenticator_time\x18\x02 \x01(\x04\x12\x15\n\rserial_number\x18\x03 \x01(\x06\x12\x1a\n\x12\x61uthenticator_type\x18\x04 \x01(\r\x12\x19\n\x11\x64\x65vice_identifier\x18\x05 \x01(\t\x12\x14\n\x0csms_phone_id\x18\x06 \x01(\t\x12\x14\n\x0chttp_headers\x18\x07 \x03(\t\"\xf3\x01\n$CTwoFactor_AddAuthenticator_Response\x12\x15\n\rshared_secret\x18\x01 \x01(\x0c\x12\x15\n\rserial_number\x18\x02 \x01(\x06\x12\x17\n\x0frevocation_code\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x13\n\x0bserver_time\x18\x05 \x01(\x04\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x06 \x01(\t\x12\x11\n\ttoken_gid\x18\x07 \x01(\t\x12\x17\n\x0fidentity_secret\x18\x08 \x01(\x0c\x12\x10\n\x08secret_1\x18\t \x01(\x0c\x12\x0e\n\x06status\x18\n \x01(\x05\"d\n\x1c\x43TwoFactor_SendEmail_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x12\n\nemail_type\x18\x02 \x01(\r\x12\x1f\n\x17include_activation_code\x18\x03 \x01(\x08\"\x1f\n\x1d\x43TwoFactor_SendEmail_Response\"\xa5\x01\n+CTwoFactor_FinalizeAddAuthenticator_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x1a\n\x12\x61uthenticator_code\x18\x02 \x01(\t\x12\x1a\n\x12\x61uthenticator_time\x18\x03 \x01(\x04\x12\x17\n\x0f\x61\x63tivation_code\x18\x04 \x01(\t\x12\x14\n\x0chttp_headers\x18\x05 \x03(\t\"w\n,CTwoFactor_FinalizeAddAuthenticator_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\twant_more\x18\x02 \x01(\x08\x12\x13\n\x0bserver_time\x18\x03 \x01(\x04\x12\x0e\n\x06status\x18\x04 \x01(\x05\"\x9e\x01\n&CTwoFactor_RemoveAuthenticator_Request\x12\x17\n\x0frevocation_code\x18\x02 \x01(\t\x12\x19\n\x11revocation_reason\x18\x05 \x01(\r\x12\x19\n\x11steamguard_scheme\x18\x06 \x01(\r\x12%\n\x1dremove_all_steamguard_cookies\x18\x07 \x01(\x08\"v\n\'CTwoFactor_RemoveAuthenticator_Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bserver_time\x18\x03 \x01(\x04\x12%\n\x1drevocation_attempts_remaining\x18\x05 \x01(\r\")\n\'CTwoFactor_CreateEmergencyCodes_Request\"9\n(CTwoFactor_CreateEmergencyCodes_Response\x12\r\n\x05\x63odes\x18\x01 \x03(\t\";\n(CTwoFactor_DestroyEmergencyCodes_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"+\n)CTwoFactor_DestroyEmergencyCodes_Response\"0\n CTwoFactor_ValidateToken_Request\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"2\n!CTwoFactor_ValidateToken_Response\x12\r\n\x05valid\x18\x01 \x01(\x08\x32\xa8\x06\n\tTwoFactor\x12H\n\x0bQueryStatus\x12\x1a.CTwoFactor_Status_Request\x1a\x1b.CTwoFactor_Status_Response\"\x00\x12\x61\n\x10\x41\x64\x64\x41uthenticator\x12$.CTwoFactor_AddAuthenticator_Request\x1a%.CTwoFactor_AddAuthenticator_Response\"\x00\x12L\n\tSendEmail\x12\x1d.CTwoFactor_SendEmail_Request\x1a\x1e.CTwoFactor_SendEmail_Response\"\x00\x12y\n\x18\x46inalizeAddAuthenticator\x12,.CTwoFactor_FinalizeAddAuthenticator_Request\x1a-.CTwoFactor_FinalizeAddAuthenticator_Response\"\x00\x12j\n\x13RemoveAuthenticator\x12\'.CTwoFactor_RemoveAuthenticator_Request\x1a(.CTwoFactor_RemoveAuthenticator_Response\"\x00\x12m\n\x14\x43reateEmergencyCodes\x12(.CTwoFactor_CreateEmergencyCodes_Request\x1a).CTwoFactor_CreateEmergencyCodes_Response\"\x00\x12p\n\x15\x44\x65stroyEmergencyCodes\x12).CTwoFactor_DestroyEmergencyCodes_Request\x1a*.CTwoFactor_DestroyEmergencyCodes_Response\"\x00\x12X\n\rValidateToken\x12!.CTwoFactor_ValidateToken_Request\x1a\".CTwoFactor_ValidateToken_Response\"\x00\x42\x03\x80\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CTWOFACTOR_STATUS_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_Status_Request',
  full_name='CTwoFactor_Status_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CTwoFactor_Status_Request.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=77,
)


_CTWOFACTOR_STATUS_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_Status_Response',
  full_name='CTwoFactor_Status_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='CTwoFactor_Status_Response.state', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inactivation_reason', full_name='CTwoFactor_Status_Response.inactivation_reason', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_type', full_name='CTwoFactor_Status_Response.authenticator_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_allowed', full_name='CTwoFactor_Status_Response.authenticator_allowed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steamguard_scheme', full_name='CTwoFactor_Status_Response.steamguard_scheme', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token_gid', full_name='CTwoFactor_Status_Response.token_gid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email_validated', full_name='CTwoFactor_Status_Response.email_validated', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_identifier', full_name='CTwoFactor_Status_Response.device_identifier', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_created', full_name='CTwoFactor_Status_Response.time_created', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revocation_attempts_remaining', full_name='CTwoFactor_Status_Response.revocation_attempts_remaining', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classified_agent', full_name='CTwoFactor_Status_Response.classified_agent', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=396,
)


_CTWOFACTOR_ADDAUTHENTICATOR_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_AddAuthenticator_Request',
  full_name='CTwoFactor_AddAuthenticator_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CTwoFactor_AddAuthenticator_Request.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_time', full_name='CTwoFactor_AddAuthenticator_Request.authenticator_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='CTwoFactor_AddAuthenticator_Request.serial_number', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_type', full_name='CTwoFactor_AddAuthenticator_Request.authenticator_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_identifier', full_name='CTwoFactor_AddAuthenticator_Request.device_identifier', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sms_phone_id', full_name='CTwoFactor_AddAuthenticator_Request.sms_phone_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_headers', full_name='CTwoFactor_AddAuthenticator_Request.http_headers', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=399,
  serialized_end=603,
)


_CTWOFACTOR_ADDAUTHENTICATOR_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_AddAuthenticator_Response',
  full_name='CTwoFactor_AddAuthenticator_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shared_secret', full_name='CTwoFactor_AddAuthenticator_Response.shared_secret', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='CTwoFactor_AddAuthenticator_Response.serial_number', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revocation_code', full_name='CTwoFactor_AddAuthenticator_Response.revocation_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='CTwoFactor_AddAuthenticator_Response.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='CTwoFactor_AddAuthenticator_Response.server_time', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_name', full_name='CTwoFactor_AddAuthenticator_Response.account_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token_gid', full_name='CTwoFactor_AddAuthenticator_Response.token_gid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identity_secret', full_name='CTwoFactor_AddAuthenticator_Response.identity_secret', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secret_1', full_name='CTwoFactor_AddAuthenticator_Response.secret_1', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='CTwoFactor_AddAuthenticator_Response.status', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=849,
)


_CTWOFACTOR_SENDEMAIL_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_SendEmail_Request',
  full_name='CTwoFactor_SendEmail_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CTwoFactor_SendEmail_Request.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email_type', full_name='CTwoFactor_SendEmail_Request.email_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_activation_code', full_name='CTwoFactor_SendEmail_Request.include_activation_code', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=951,
)


_CTWOFACTOR_SENDEMAIL_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_SendEmail_Response',
  full_name='CTwoFactor_SendEmail_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=984,
)


_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_FinalizeAddAuthenticator_Request',
  full_name='CTwoFactor_FinalizeAddAuthenticator_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CTwoFactor_FinalizeAddAuthenticator_Request.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_code', full_name='CTwoFactor_FinalizeAddAuthenticator_Request.authenticator_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticator_time', full_name='CTwoFactor_FinalizeAddAuthenticator_Request.authenticator_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='CTwoFactor_FinalizeAddAuthenticator_Request.activation_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_headers', full_name='CTwoFactor_FinalizeAddAuthenticator_Request.http_headers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=987,
  serialized_end=1152,
)


_CTWOFACTOR_FINALIZEADDAUTHENTICATOR_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_FinalizeAddAuthenticator_Response',
  full_name='CTwoFactor_FinalizeAddAuthenticator_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='CTwoFactor_FinalizeAddAuthenticator_Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='want_more', full_name='CTwoFactor_FinalizeAddAuthenticator_Response.want_more', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='CTwoFactor_FinalizeAddAuthenticator_Response.server_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='CTwoFactor_FinalizeAddAuthenticator_Response.status', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1154,
  serialized_end=1273,
)


_CTWOFACTOR_REMOVEAUTHENTICATOR_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_RemoveAuthenticator_Request',
  full_name='CTwoFactor_RemoveAuthenticator_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='revocation_code', full_name='CTwoFactor_RemoveAuthenticator_Request.revocation_code', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revocation_reason', full_name='CTwoFactor_RemoveAuthenticator_Request.revocation_reason', index=1,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steamguard_scheme', full_name='CTwoFactor_RemoveAuthenticator_Request.steamguard_scheme', index=2,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove_all_steamguard_cookies', full_name='CTwoFactor_RemoveAuthenticator_Request.remove_all_steamguard_cookies', index=3,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1276,
  serialized_end=1434,
)


_CTWOFACTOR_REMOVEAUTHENTICATOR_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_RemoveAuthenticator_Response',
  full_name='CTwoFactor_RemoveAuthenticator_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='CTwoFactor_RemoveAuthenticator_Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='CTwoFactor_RemoveAuthenticator_Response.server_time', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revocation_attempts_remaining', full_name='CTwoFactor_RemoveAuthenticator_Response.revocation_attempts_remaining', index=2,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1436,
  serialized_end=1554,
)


_CTWOFACTOR_CREATEEMERGENCYCODES_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_CreateEmergencyCodes_Request',
  full_name='CTwoFactor_CreateEmergencyCodes_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1556,
  serialized_end=1597,
)


_CTWOFACTOR_CREATEEMERGENCYCODES_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_CreateEmergencyCodes_Response',
  full_name='CTwoFactor_CreateEmergencyCodes_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codes', full_name='CTwoFactor_CreateEmergencyCodes_Response.codes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1599,
  serialized_end=1656,
)


_CTWOFACTOR_DESTROYEMERGENCYCODES_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_DestroyEmergencyCodes_Request',
  full_name='CTwoFactor_DestroyEmergencyCodes_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamid', full_name='CTwoFactor_DestroyEmergencyCodes_Request.steamid', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1658,
  serialized_end=1717,
)


_CTWOFACTOR_DESTROYEMERGENCYCODES_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_DestroyEmergencyCodes_Response',
  full_name='CTwoFactor_DestroyEmergencyCodes_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1719,
  serialized_end=1762,
)


_CTWOFACTOR_VALIDATETOKEN_REQUEST = _descriptor.Descriptor(
  name='CTwoFactor_ValidateToken_Request',
  full_name='CTwoFactor_ValidateToken_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='CTwoFactor_ValidateToken_Request.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1764,
  serialized_end=1812,
)


_CTWOFACTOR_VALIDATETOKEN_RESPONSE = _descriptor.Descriptor(
  name='CTwoFactor_ValidateToken_Response',
  full_name='CTwoFactor_ValidateToken_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='CTwoFactor_ValidateToken_Response.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1814,
  serialized_end=1864,
)

DESCRIPTOR.message_types_by_name['CTwoFactor_Status_Request'] = _CTWOFACTOR_STATUS_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_Status_Response'] = _CTWOFACTOR_STATUS_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_AddAuthenticator_Request'] = _CTWOFACTOR_ADDAUTHENTICATOR_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_AddAuthenticator_Response'] = _CTWOFACTOR_ADDAUTHENTICATOR_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_SendEmail_Request'] = _CTWOFACTOR_SENDEMAIL_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_SendEmail_Response'] = _CTWOFACTOR_SENDEMAIL_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_FinalizeAddAuthenticator_Request'] = _CTWOFACTOR_FINALIZEADDAUTHENTICATOR_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_FinalizeAddAuthenticator_Response'] = _CTWOFACTOR_FINALIZEADDAUTHENTICATOR_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_RemoveAuthenticator_Request'] = _CTWOFACTOR_REMOVEAUTHENTICATOR_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_RemoveAuthenticator_Response'] = _CTWOFACTOR_REMOVEAUTHENTICATOR_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_CreateEmergencyCodes_Request'] = _CTWOFACTOR_CREATEEMERGENCYCODES_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_CreateEmergencyCodes_Response'] = _CTWOFACTOR_CREATEEMERGENCYCODES_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_DestroyEmergencyCodes_Request'] = _CTWOFACTOR_DESTROYEMERGENCYCODES_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_DestroyEmergencyCodes_Response'] = _CTWOFACTOR_DESTROYEMERGENCYCODES_RESPONSE
DESCRIPTOR.message_types_by_name['CTwoFactor_ValidateToken_Request'] = _CTWOFACTOR_VALIDATETOKEN_REQUEST
DESCRIPTOR.message_types_by_name['CTwoFactor_ValidateToken_Response'] = _CTWOFACTOR_VALIDATETOKEN_RESPONSE

CTwoFactor_Status_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_Status_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_STATUS_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_Status_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_Status_Request)

CTwoFactor_Status_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_Status_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_STATUS_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_Status_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_Status_Response)

CTwoFactor_AddAuthenticator_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_AddAuthenticator_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_ADDAUTHENTICATOR_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_AddAuthenticator_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_AddAuthenticator_Request)

CTwoFactor_AddAuthenticator_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_AddAuthenticator_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_ADDAUTHENTICATOR_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_AddAuthenticator_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_AddAuthenticator_Response)

CTwoFactor_SendEmail_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_SendEmail_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_SENDEMAIL_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_SendEmail_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_SendEmail_Request)

CTwoFactor_SendEmail_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_SendEmail_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_SENDEMAIL_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_SendEmail_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_SendEmail_Response)

CTwoFactor_FinalizeAddAuthenticator_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_FinalizeAddAuthenticator_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_FINALIZEADDAUTHENTICATOR_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_FinalizeAddAuthenticator_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_FinalizeAddAuthenticator_Request)

CTwoFactor_FinalizeAddAuthenticator_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_FinalizeAddAuthenticator_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_FINALIZEADDAUTHENTICATOR_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_FinalizeAddAuthenticator_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_FinalizeAddAuthenticator_Response)

CTwoFactor_RemoveAuthenticator_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_RemoveAuthenticator_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_REMOVEAUTHENTICATOR_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_RemoveAuthenticator_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_RemoveAuthenticator_Request)

CTwoFactor_RemoveAuthenticator_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_RemoveAuthenticator_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_REMOVEAUTHENTICATOR_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_RemoveAuthenticator_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_RemoveAuthenticator_Response)

CTwoFactor_CreateEmergencyCodes_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_CreateEmergencyCodes_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_CREATEEMERGENCYCODES_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_CreateEmergencyCodes_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_CreateEmergencyCodes_Request)

CTwoFactor_CreateEmergencyCodes_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_CreateEmergencyCodes_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_CREATEEMERGENCYCODES_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_CreateEmergencyCodes_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_CreateEmergencyCodes_Response)

CTwoFactor_DestroyEmergencyCodes_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_DestroyEmergencyCodes_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_DESTROYEMERGENCYCODES_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_DestroyEmergencyCodes_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_DestroyEmergencyCodes_Request)

CTwoFactor_DestroyEmergencyCodes_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_DestroyEmergencyCodes_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_DESTROYEMERGENCYCODES_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_DestroyEmergencyCodes_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_DestroyEmergencyCodes_Response)

CTwoFactor_ValidateToken_Request = _reflection.GeneratedProtocolMessageType('CTwoFactor_ValidateToken_Request', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_VALIDATETOKEN_REQUEST,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_ValidateToken_Request)
  ))
_sym_db.RegisterMessage(CTwoFactor_ValidateToken_Request)

CTwoFactor_ValidateToken_Response = _reflection.GeneratedProtocolMessageType('CTwoFactor_ValidateToken_Response', (_message.Message,), dict(
  DESCRIPTOR = _CTWOFACTOR_VALIDATETOKEN_RESPONSE,
  __module__ = 'steammessages_twofactor_pb2'
  # @@protoc_insertion_point(class_scope:CTwoFactor_ValidateToken_Response)
  ))
_sym_db.RegisterMessage(CTwoFactor_ValidateToken_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001'))
# @@protoc_insertion_point(module_scope)
