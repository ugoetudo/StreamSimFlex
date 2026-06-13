# Kafka Guide

Some useful material for setting up the Yelp review stream as a producer in Kafka using Kafka Connect

## Starting Up Kafka

```sh
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
bin/kafka-server-start.sh config/server.properties &
bin/kafka-topics.sh --create --topic yelp-review-events --bootstrap-server localhost:9092
echo "$(bin/kafka-topics --describe --topic yelp-review-events --bootstrap-server localhost:9092)"
echo "plugin.path=libs/connect-file-4.3.0.jar" >> config/connect-standalone.properties
```

## Kafka Connect Properties for Running in Standalone Mode

This is what my connect-file-source.properties configuration file looks like:
```
name=local-file-source
connector.class=FileStreamSource
tasks.max=1
file=/mnt/c/Users/ugoet/ugo-dev/yelp-reviews-producer/StreamSimFlex/stream_file.json
topic=yelp-review-events
```

## Start Kafka Connect in Standalone Mode

```sh
bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties
```

## Consume Messages via Stdout

```sh
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic yelp-review-events --from-beginning
```