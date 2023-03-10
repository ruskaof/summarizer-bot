import json
import codecs
from pprint import pprint

with codecs.open('../messages.json', 'r', 'utf-8') as f:
    d = json.load(f)
    for i in range(5):
        pprint(d[i]['date'])
        pprint(d[i]['from_user']['first_name']+' '+d[i]['from_user']['last_name'])
        pprint(d[i]['text'])
    print(type(d))
