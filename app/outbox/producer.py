import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
from app.outbox.dao import OutBoxDao
import logging


def send_messages(data):

    producer = KafkaProducer(
        bootstrap_servers="redpanda-0:9092",
        value_serializer=lambda m: json.dumps(m).encode('ascii'),
        api_version=(0, 11, 5)

    )

    topic = "orders"

    def on_success(metadata):
        logging.error(f"Message produced to topic '{metadata.topic}' at offset {metadata.offset}")

    def on_error(e):
        logging.error(f"Error sending message: {e}")

    for msg in data:
        future = producer.send(topic, msg)
        future.add_callback(on_success)
        future.add_errback(on_error)

    producer.flush()
    producer.close()
