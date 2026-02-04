from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
## Kafka broker has to be running on localhost:9092

kafka_broker_address = 'localhost:9092'
topic = 'kappa-topic'
producer = KafkaProducer(bootstrap_servers=[kafka_broker_address])
#print(producer.config['api_version'])
# Asynchronous by default
future = producer.send(topic, value="Hello, World!".encode("utf-8"))

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')


# produce asynchronously
for _ in range(100):
    producer.send('my-topic', b'msg')

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send('my-topic', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)