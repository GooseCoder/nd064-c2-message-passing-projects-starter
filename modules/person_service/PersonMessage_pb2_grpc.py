# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import PersonMessage_pb2 as PersonMessage__pb2


class PersonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/PersonService/Create',
                request_serializer=PersonMessage__pb2.PersonMessage.SerializeToString,
                response_deserializer=PersonMessage__pb2.PersonMessage.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/PersonService/Retrieve',
                request_serializer=PersonMessage__pb2.PersonRequestMessage.SerializeToString,
                response_deserializer=PersonMessage__pb2.PersonMessage.FromString,
                )
        self.RetrieveAll = channel.unary_unary(
                '/PersonService/RetrieveAll',
                request_serializer=PersonMessage__pb2.PersonRequestMessage.SerializeToString,
                response_deserializer=PersonMessage__pb2.PersonListMessage.FromString,
                )


class PersonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=PersonMessage__pb2.PersonMessage.FromString,
                    response_serializer=PersonMessage__pb2.PersonMessage.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=PersonMessage__pb2.PersonRequestMessage.FromString,
                    response_serializer=PersonMessage__pb2.PersonMessage.SerializeToString,
            ),
            'RetrieveAll': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveAll,
                    request_deserializer=PersonMessage__pb2.PersonRequestMessage.FromString,
                    response_serializer=PersonMessage__pb2.PersonListMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/Create',
            PersonMessage__pb2.PersonMessage.SerializeToString,
            PersonMessage__pb2.PersonMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/Retrieve',
            PersonMessage__pb2.PersonRequestMessage.SerializeToString,
            PersonMessage__pb2.PersonMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/RetrieveAll',
            PersonMessage__pb2.PersonRequestMessage.SerializeToString,
            PersonMessage__pb2.PersonListMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
