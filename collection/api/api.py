# json.parser.online.fr 사이트를 참고할 것!
# facebook api 참고할 것!
# python ppt 3-1 참고할 것!

from urllib.parse import urlencode
from .json_request import json_request


ACCESS_TOKEN = '%s|%s' % ("862784310559106", "48278256b2a4a40c34d9cb153432fe99")
BASE_URL_FB_API = 'https://graph.facebook.com/v2.8'
LIMIT_REQUEST = 50


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    # urlencode는 parameter들을 알아서 파싱한 후 '&'로 묶어줌
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_name_to_id(pagename):
    url = fb_gen_url(
        node=pagename,
        access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    return json_result.get('id')


def fb_fetch_posts(pagename, since, until):
    # 최초 facebook URL 만들기
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields = 'id,message,link,name,type,shares,\
    created_time,reactions.limit(0).summary(true),\
    comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=LIMIT_REQUEST,
        access_token=ACCESS_TOKEN)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        # C 스타일의 json_result == None ? json_result : json_result.get('paging') 과 같음
        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')
        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts

        # url = paging.get('next')
        # if url is None:
        #     break
