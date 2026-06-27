# Installation & Configuration Guide for OpenSearch, OpenSearch Dashboards and Data Prepper

## Prerequisites
Before attempting this practicum, ensure that you have installed Docker Desktop. Because We are spooling up several OpenSearch services (three different services per the title of this readme) I have decided to bundle the setup and configuration procedure into a docker compose YAML file. With a single, platform independent, command you will be able to get started with this exercise.

You need to have connected the simulated yelp reviews producer to kafka, configuring a Kafka topic (as well as kafka itself) to that end. 

## OpenSearch Documentation
I won't reproduce OpenSearch documentation here. Instead, learn all about it by following this link [Open Search Docs]('https://docs.opensearch.org/latest/about/') 

## Create an OpenSearch Index
Open search organizes data into indexes. So we'll need to create an index into which we'll progressively stream Yelp reviews produced by our simulation.

See [Managing Indexes]('https://docs.opensearch.org/latest/im-plugin/') in the OpenSearch Docs

## Add Some Data to the Index

Using Python (because it is easier than cURL) "requests" library, we will send requests to OpenSearch. 

First some preliminaries:

```py
import requests
import json
import uuid

index_name = "yelp_reviews_3"
headers = {"Content-Type": "application/json"}
```

Now, lets create an index template. This is basically a schema for the index, defining processing options and data types for incoming data: 

```py
create_template_url = "http://localhost:9200/_index_template/yelp_adv_template"
with open(r".\\reveiws_template.json", "r") as tmpl_buf:
    template_data = json.load(tmpl_buf)
    tr = requests.put(url=create_template_url, json=template_data, headers=headers)
print(tr.status_code, tr.text)
```
The file `reviews_template.json` is included in this repo `./scripts/reviews_template.json`. Be sure to take a look at it.

Now, we can add data to the index:

```py
with open(r"..\\..\\stream_file.json", "r") as sf:
    for line in sf:
        doc_id = str(uuid.uuid4())
        opensearch_url = f"http://localhost:9200/{index_name}/_doc/{doc_id}"
        r = requests.put(url=opensearch_url, headers=headers, json=json.loads(line))
        responses.append(r)
```

Notice that I am using the stream_file.json file - this is file into which our stream simulation appends data. In our final class, we will learn how to bring this all together for real-time dashboards

### Note
Before launching the docker composition, you'll need to run the commands below in windows from the terminal (CMD):

```sh
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```