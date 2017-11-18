from analysis_fb.collection.api import api

# url = api.fb_gen_url(pagename='jtbcnews', a=1, b=2, no=3, token='asdf')
# print(url)

# id = api.fb_name_to_id('jtbcnews')
# print(id)


datas = []

for posts in api.fb_fetch_posts('jtbcnews', '2017-08-01', '2017-10-12'):
    # datas.append(posts)
    print(posts)


# api.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-10-12')
# api.fb_fetch_posts('chosun', '2017-01-01', '2017-10-12')


