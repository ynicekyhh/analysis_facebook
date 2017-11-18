import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def ex1():
    plt.plot([1, 3, 1, 3], [10, 20, 30, 40])
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(1, 1, 1)
    sp1.plot([1, 3, 5, 1], [10, 20, 30, 40])

    sp2 = fig.add_subplot(1, 2, 2)
    sp2.plot([1, 2, 3, 4], [10, 30, 20, 40])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(100), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 4)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


def ex4():
    fig, subplots = plt.subplots(2, 2)

    subplots[0, 0].plot(randn(50).cumsum(), 'k--')
    subplots[0, 1].hist(randn(100), bins=20, color='k', alpha=0.3)
    subplots[1, 0].scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


# ex1보다는 ex5 방식이 figure 한개에다가 여러 개를 쓸 수 있으니 추천한다.
def ex5():
    fig, subplots = plt.subplots(1, 1)
    subplots.scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


def ex6():
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha=0.3)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


def ex7():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--')

    plt.show()


# ex7()과 동일한 옵션, 03-01.데이터_수집_분석과 시각화.ppt p.39 참고
def ex8():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color='g', linestyle='--', marker='o')

    plt.show()


def ex9():
    fig, subplots = plt.subplots(1, 1)
    # subplots.plot(randn(50).cumsum(), 'ko--')
    subplots.plot(randn(50).cumsum(), color='g', linestyle='--', marker='o')
    plt.show()


def ex10():
    data = randn(50).cumsum()

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(data, color='#aaaaaa', linestyle='--', label='Default')
    subplots.plot(data, 'k-', drawstyle='steps-mid', label='steps-mid')

    plt.legend(loc='best')
    plt.show()


def ex11():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum())

    subplots.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6','pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('Positions')
    subplots.set_title('My First Matplotlib Plot')

    plt.show()


def ex12():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum(), 'k', label='one')
    subplots.plot(randn(100).cumsum(), 'k--', label='two')
    subplots.plot(randn(100).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()

# 03-01.데이터 수집_분석과 시각화.ptt p.46 참고
def ex13():
    # 영어만 처리됨
    # font_options = {'family': 'monospace', 'weight': 'bold', 'size': 'small'}

    # 한글적용 1번 방법
    # font_options = {'family': 'Malgun Gothic'}

    # plt.rc('font', **font_options)

    # 한글적용 2번 방법
    plt.rc('font', family='Malgun Gothic')
    # y축의 '-'들이 안깨지고 나오게 함
    plt.rc('axes', unicode_minus=False)

    # 한글적용 3번 방법
    # D:\Python\Python36\Lib\site-packages\matplotlib\mpl-data\matplotlibrc 에서
    # line 330 번째 줄 axes.unicode_minus:False 로 변경
    # line 199 번째 쭐 font.family:Malgun Gothic 로 변경

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum())

    subplots.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6','pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제13 한글처리')

    # 현재 프로젝트 경로에 메모리에 있는 plt를 ex13-plot.png로 저장함
    plt.savefig('ex13-plot.png', dpi=400, bbox_inches='tight')
    plt.savefig('ex13-plot.pdf', dpi=400, bbox_inches='tight')

    plt.show()


def ex14():
    # 파이썬은 리눅스에서도 돌기 때문에 경로 표시 시 '/'나 '\' 둘 다 사용가능
    fontfile = 'c:/windows/fonts/malgun.ttf'
    fontname = font_manager.FontProperties(fname=fontfile).get_name()
    print(fontname)


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    ex13()
    # ex14()