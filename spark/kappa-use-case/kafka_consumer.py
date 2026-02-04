from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         group_id='my_group_id',
                         api_version=(3, 9, 0),
                         bootstrap_servers=['localhost:9092'])

# Subscribe to a specific topic
consumer.subscribe(topics=['kappa-topic'])

# Poll for new messages
while True:
    msgs = consumer.poll(timeout_ms=1000)
    if msgs:
        for tp, messages in msgs.items():
            for msg in messages:
                print("Topic: {} | Partition: {} | Offset: {} | Key: {} | Value: {}".format(
                    msg.topic, msg.partition, msg.offset, msg.key, msg.value.decode("utf-8")
                ))
    else:
        print("No new messages")
