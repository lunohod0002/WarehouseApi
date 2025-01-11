import json
from kafka import KafkaConsumer
import logging
def get_messages():
    consumer = KafkaConsumer(
      bootstrap_servers=["redpanda-0:9092"],
      group_id="demo-group",
      auto_offset_reset="latest",
      enable_auto_commit=False,
      consumer_timeout_ms=1000,
      value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )

    consumer.subscribe("orders")

    try:
        for message in consumer:
            topic_info = f"topic: {message.partition}|{message.offset})"
            message_info = f"key: {message.key}, {message.value}"
            logging.error(f"{topic_info}, {message_info}")
    except Exception as e:
        logging.error(f"Error occurred while consuming messages: {e}")
    finally:
        consumer.close()