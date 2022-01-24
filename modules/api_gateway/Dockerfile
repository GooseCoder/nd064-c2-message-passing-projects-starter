FROM python:3.8

WORKDIR /opt/api_gateway

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENV PYTHONPATH /opt/api_gateway

# compile protobuf classes
RUN python -m grpc_tools.protoc -Iapp/api/proto --python_out=. --grpc_python_out=. app/api/proto/PersonMessage.proto
RUN python -m grpc_tools.protoc -Iapp/api/proto --python_out=. --grpc_python_out=. app/api/proto/ConnectionMessage.proto
CMD ["flask", "run", "--host", "0.0.0.0"]