import requests
import json
import uuid

index_name = "yelp_reviews_3"
headers = {"Content-Type": "application/json"}

# Create Index Template Using The Example Below

create_template_url = "http://localhost:9200/_index_template/yelp_adv_template"
with open(r".\\reveiws_template.json", "r") as tmpl_buf:
    template_data = json.load(tmpl_buf)
    tr = requests.put(url=create_template_url, json=template_data, headers=headers)
print(tr.status_code, tr.text)

# add data to and create an index for yelp 
responses = []
with open(r"..\\..\\stream_file.json", "r") as sf:
    for line in sf:
        doc_id = str(uuid.uuid4())
        opensearch_url = f"http://localhost:9200/{index_name}/_doc/{doc_id}"
        r = requests.put(url=opensearch_url, headers=headers, json=json.loads(line))
        responses.append(r)

# search the data as a test
search = {'query': {'match': {'text': 'service'}}}
search_url = "http://localhost:9200/yelp_reviews/_search"
search_response = requests.get(search_url, headers=headers, json=search)

