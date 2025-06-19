import json
import time
import logging
import uuid
import faker
import random
from datetime import datetime
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)

#create kafka topic
ORDER_KAFKA_TOPIC  = "order-details"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers='kafka-local.orders-microservice.svc.cluster.local:9092')

def create_orders():
    f = faker.Faker()
    orders = dict(
        order_id = str(uuid.uuid4()),
        username = f.user_name(),
        first_name = f.first_name(),
        last_name = f.last_name(),
        email = f.email(),
        quantity = round(float(random.uniform(10.5, 100.99)), 2),
        date_created = str(datetime.utcnow())
    )
    return orders
if __name__ == '__main__':
    logging.info("Generating orders...")
    for order in range(ORDER_LIMIT):
        data = create_orders()
        #send orders to kafka topic
        producer.send(ORDER_KAFKA_TOPIC, json.bumps(data).encode("utf-8"))
        logging.info(f"Done creating order...{order} - {data} ")
        time.sleep(1 )
