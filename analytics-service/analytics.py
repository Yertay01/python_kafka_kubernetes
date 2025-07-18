import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.info)


ORDER_PROCESSED_KAFKA_TOPIC = "order-processed"
BOOT_STRAP_SERVER = "kafka_local.orders-microservice.svc.cluster.local:9092"

# consumer 
consumer = KafkaConsumer(
    ORDER_PROCESSED_KAFKA_TOPIC,
    bootstrap_servers = BOOT_STRAP_SERVER
)

if __name__ == "__main__":
    total_orders_count = 0
    total_revenue = 0.0
    logging.info("Started order analytics...")
    while True:
        for message in consumer:
            logging.info("Updating analytics service...")
            consumed_message = json.loads(message.value.decode("utf-8"))
            total_cost = float(consumed_message["total_cost"])
            total_order_count += 1
            total_revenue += total_cost

            logging.info(f"Total orders count for today: {total_orders_count}")
            logging.info(f"Total revenue collected for today: {round(total_revenue, 2)}")        