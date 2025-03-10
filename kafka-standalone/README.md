# Start Kafka

To start **kafka** execute `docker-compose up -d`

To stop **kafka** execute `docker-compose down -d`

You can connect to the kafka container with the following command: `docker exec -it broker /bin/bash`

## Create a Topic

`/opt/kafka/bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic first-kafka-topic --bootstrap-server localhost:9092`

## Create Events for the Topic

`/opt/kafka/bin/kafka-console-producer.sh --topic first-kafka-topic --bootstrap-server localhost:9092`

## Consume Events of a Topic

`/opt/kafka/bin/kafka-console-consumer.sh --topic first-kafka-topic --from-beginning --bootstrap-server localhost:9092`
