import json
from datetime import datetime, timedelta
from .api import api
import os

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_post(post):
    # 공유수
    if 'shares' not in post:
        post['count_shares'] = 0
    else:
        # 이런식으로 가공해서 접근하게 쉽게 데이터 정규화를 한다
        post['count_shares'] = post['shares']['count']
        del post['shares']

    # 전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']
        del post['reactions']

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']
        del post['comments']

    # KST = UTC+9
    # post['created_time']의 값을 변경한 것이니까 여기선 지우면 안됨
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling(pagename, since, until, fetch=True):
    # list는 '+=' 연산이 됨
    results = []
    # save results to file
    filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since, until)

    if fetch:
        for posts in api.fb_fetch_posts(pagename, since, until):
            for post in posts:
                # facebook에서 가져온 post들의 정보가 너무 많으니까 preprocess_post에서 전처리로 필요없는 데이터들을 일부 쳐 낸 후 results에 다시 담게함
                # posts가 list형이고, post는 dictionary type이니까 call by reference로 접근됨. (mutable이니까)
                # 따라서 post = preprocess_post(post)와 같이 하지 않아도 post가 수정되면서 posts까지 수정됨
                preprocess_post(post)
            results += posts

        # with를 썼으니 자동으로 close됨
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename


# 해당 path에 디렉토리가 존재하지 않으면 만들어줌
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
