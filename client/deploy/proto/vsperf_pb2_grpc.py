# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import vsperf_pb2 as vsperf__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HostConnect = channel.unary_unary(
        '/vsperf.Controller/HostConnect',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.VsperfInstall = channel.unary_unary(
        '/vsperf.Controller/VsperfInstall',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.TGenHostConnect = channel.unary_unary(
        '/vsperf.Controller/TGenHostConnect',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.TGenInstall = channel.unary_unary(
        '/vsperf.Controller/TGenInstall',
        request_serializer=vsperf__pb2.HostVerInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.TGenUploadConfigFile = channel.stream_unary(
        '/vsperf.Controller/TGenUploadConfigFile',
        request_serializer=vsperf__pb2.ConfFile.SerializeToString,
        response_deserializer=vsperf__pb2.UploadStatus.FromString,
        )
    self.CollectdInstall = channel.unary_unary(
        '/vsperf.Controller/CollectdInstall',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.CollectdUploadConfig = channel.stream_unary(
        '/vsperf.Controller/CollectdUploadConfig',
        request_serializer=vsperf__pb2.ConfFile.SerializeToString,
        response_deserializer=vsperf__pb2.UploadStatus.FromString,
        )
    self.DutHugepageConfig = channel.unary_unary(
        '/vsperf.Controller/DutHugepageConfig',
        request_serializer=vsperf__pb2.HugepConf.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )
    self.CheckDependecies = channel.unary_unary(
        '/vsperf.Controller/CheckDependecies',
        request_serializer=vsperf__pb2.HostInfo.SerializeToString,
        response_deserializer=vsperf__pb2.StatusReply.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HostConnect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VsperfInstall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TGenHostConnect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TGenInstall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TGenUploadConfigFile(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CollectdInstall(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CollectdUploadConfig(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DutHugepageConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckDependecies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HostConnect': grpc.unary_unary_rpc_method_handler(
          servicer.HostConnect,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'VsperfInstall': grpc.unary_unary_rpc_method_handler(
          servicer.VsperfInstall,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'TGenHostConnect': grpc.unary_unary_rpc_method_handler(
          servicer.TGenHostConnect,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'TGenInstall': grpc.unary_unary_rpc_method_handler(
          servicer.TGenInstall,
          request_deserializer=vsperf__pb2.HostVerInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'TGenUploadConfigFile': grpc.stream_unary_rpc_method_handler(
          servicer.TGenUploadConfigFile,
          request_deserializer=vsperf__pb2.ConfFile.FromString,
          response_serializer=vsperf__pb2.UploadStatus.SerializeToString,
      ),
      'CollectdInstall': grpc.unary_unary_rpc_method_handler(
          servicer.CollectdInstall,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'CollectdUploadConfig': grpc.stream_unary_rpc_method_handler(
          servicer.CollectdUploadConfig,
          request_deserializer=vsperf__pb2.ConfFile.FromString,
          response_serializer=vsperf__pb2.UploadStatus.SerializeToString,
      ),
      'DutHugepageConfig': grpc.unary_unary_rpc_method_handler(
          servicer.DutHugepageConfig,
          request_deserializer=vsperf__pb2.HugepConf.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
      'CheckDependecies': grpc.unary_unary_rpc_method_handler(
          servicer.CheckDependecies,
          request_deserializer=vsperf__pb2.HostInfo.FromString,
          response_serializer=vsperf__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'vsperf.Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
