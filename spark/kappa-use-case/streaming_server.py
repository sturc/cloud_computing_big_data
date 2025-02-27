import time

from kafka import KafkaProducer

## Kafka broker has to be running on localhost:9092

file_path = "data/nasa_http_log_1995.csv"
kafka_broker_address = 'localhost:9092'
topic = 'kappa-topic'

def start_server ():
    filetosend = open(file_path, "r")
    filetosend.readline() # skip header
    producer = KafkaProducer(bootstrap_servers=[kafka_broker_address])
    for line in filetosend:
       producer.send(topic, value=line.encode("utf-8"))
       print(line)
       time.sleep(0.1)
    producer.flush()
    filetosend.close()


if __name__ == "__main__":
    start_server()
