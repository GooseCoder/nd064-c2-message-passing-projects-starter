import json
import logging
import sys
import time
from kafka import KafkaConsumer
from app.service.location_service import create_location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location-service")
BOOTSTRAP_SERVERS = ['kafka-service:9092']


def get_kafka_conn_object(timeout=3000):
    i = 0
    while True:
        time.sleep(5)
        if i > timeout:
            logger.info("[Connection Timed Out]")
            sys.exit()
        try:
            return KafkaConsumer('location',
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m:
                                 json.loads(m.decode('utf-8')),
                                 bootstrap_servers=BOOTSTRAP_SERVERS)
        except Exception:
            logger.info("Listening for Kafka connection ...")
            i += 1


def serve():
    logger.log(logging.INFO, 'Starting server...')
    consumer = get_kafka_conn_object()
    for message in consumer:
        logger.log(logging.INFO, 'Location Received={}.'.format(message.value))
        create_location(message.value)
    logger.log(logging.INFO, 'Consumer listening...')


if __name__ == "__main__":
    serve()
