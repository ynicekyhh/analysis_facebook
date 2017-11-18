import json
import re
from konlpy.tag import Twitter
from collections import Counter


def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    jsondata = json.loads(jsonfile.read())

    data = ''
    for items in jsondata:
        value = items.get(key)
        if value is None:
            continue

        data += re.sub(r'[^\w]', '', value)

    return data


def count_wordfreq(data):
    twitter = Twitter()
    # nouns가 중복되어 있는 단어들의 리스트를 가지고 있음
    nouns = twitter.nouns(data)

    count = Counter(nouns)
    return count