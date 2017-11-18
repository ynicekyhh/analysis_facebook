import collections
import matplotlib.pyplot as plt
import os

import pytagcloud

# RESULT_DIRECTORY = '__results__/graph'
RESULT_DIRECTORY = '__results__/visualization'


# 사용자들에게 그래프보다는 tagcloud 라이브러리를 활용하여 비쥬얼하게 보여줌
def wordcloud(wordsfreq, filename):
    taglist = pytagcloud.make_tags(wordsfreq.items(), maxsize=80)

    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(800, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0)
    )


def graph_bar(
        title=None,
        xlabel=None,
        ylabel=None,
        showgrid=False,
        values=None,
        ticks=None,
        filename=None,
        showgraph=True):

    fig, subplots = plt.subplots(1, 1)
    # 전체 bar가 몇 개 있냐를 지정 후 values를 넣음
    subplots.bar(range(len(values)), values, align='center')

    # ticks
    # 사용자가 ticks에 str같은 타입을 넣을 수도 있으니 ticks가 collections.Sequence인지 검증
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=60, fontsize='small')

    # title
    if title is not None and isinstance(title, str):
        pass

    # xlabel
    if xlabel is not None and isinstance(xlabel, str):
        pass

    # ylabel
    if ylabel is not None and isinstance(ylabel, str):
        pass

    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    # show grid - grid가 False면 안나오고, True면 나옴
    subplots.grid(showgraph)

    if showgraph:
        plt.show()

# visualizer.py를 import하면서 디렉토리가 없으면 만들어 주도록 하기 위해 전역에다 코딩
# 해당 path에 디렉토리가 존재하지 않으면 만들어줌
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)