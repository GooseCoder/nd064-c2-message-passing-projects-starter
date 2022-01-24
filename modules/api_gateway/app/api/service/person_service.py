import grpc
import PersonMessage_pb2 as person_pb2
import PersonMessage_pb2_grpc as person_pb2_grpc

person_channel = grpc.insecure_channel("person-service:6002")
person_stub = person_pb2_grpc.PersonServiceStub(person_channel)


def get_person_by_id(person_id):
    """
    Gets a single person by id
    This executes a gRRPC call
    """
    person_request_message = person_pb2.PersonRequestMessage(id=person_id)
    person = person_stub.Retrieve(person_request_message)
    return person


def get_all():
    """
    Get a list of all persons.
    This executes a gRRPC call
    """
    person_request_message = person_pb2.PersonRequestMessage()
    persons = person_stub.RetrieveAll(person_request_message)
    return persons


def create(person_data):
    """
    Creates a new person record
    This executes a gRRPC call
    """
    person_message = person_pb2.PersonMessage(
        first_name=person_data['first_name'],
        last_name=person_data['last_name'],
        company_name=person_data['company_name']
    )
    new_person_message = person_stub.Create(person_message)
    return new_person_message
