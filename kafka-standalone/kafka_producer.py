import random
from kafka import KafkaProducer
from kafka.errors import KafkaError

## Kafka broker has to be running on localhost:9092

kafka_broker_address = 'localhost:9092'
topic = 'kappa-topic'
producer = KafkaProducer(bootstrap_servers=[kafka_broker_address])


# produce asynchronously
animals = ["Snake", "Ape", "Lion", "Spider", "Whale" ]
for _ in range(100):
    animal = random.choice(animals)
    producer.send(topic, value=animal.encode('utf-8'))

# block until all async messages are sent
producer.flush()
