import collection
import analyze
import visualize

pagename = 'jtbcnews'
since = '2017-08-01'
until = '2017-10-12'

if __name__ == '__main__':
    items = [
        # 아래는 tuple이니까 immutable, 따라서 dictionary로 변경해 주면 collection과 analysis에서 resultfile을 수정해서 할 수 있다.
        # ('jtbcnews', '2017-10-15', '2017-10-17'),
        {'pagename': 'jtbcnews', 'since': '2017-10-15', 'until': '2017-10-17'},
        {'pagename': 'chosun', 'since': '2017-10-15', 'until': '2017-10-17'},
        {'pagename': 'hankyoreh', 'since': '2017-10-15', 'until': '2017-10-17'},
        ]

    # HTTP Error 500: Internal Server Error : 2017-10-13 09:56:13.431524
    # 위와 같은 에러가 발생하면, 500 에러니까 내가 만든 쿼리가 잘못된 것임을 파악, 서버에서 데이터를 가져오지 못하여 에러발생

    # collection
    # for pagename, since, until in items:
        # resultfile = collection.crawling(pagename, since, until)
    for item in items:
        resultfile = collection.crawling(**item, fetch=True)
        item['resultfile'] = resultfile

    # analysis
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count'] = analyze.count_wordfreq(data)

    # visualization
    for item in items:
        count = item['count']
        count_t50 = dict(count.most_common(50))
        filename = '%s_%s_%s' % (item['pagename'], item['since'], item['until'])

        visualize.wordcloud(count_t50, filename)
        """
        visualize.graph_bar(
            values=list(count_t50.values()),
            ticks = list(count_t50.keys()),
            showgrid=True,
            filename=filename,
            showgraph=False
        )
        """